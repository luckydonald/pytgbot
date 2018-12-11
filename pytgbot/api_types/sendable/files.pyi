from typing import Union, Tuple, Type, Dict, Optional, MutableMapping, Text, IO, BinaryIO
from luckydonaldUtils.encoding import binary_type


class InputFile(...):
    ...
    def __new__(
        cls
    ) -> Union[
        'InputFileFromBlob', 'InputFileFromDisk', 'InputFileFromURL',
        str,
    ]: ...
    # end def


    def __init__(
            self,  # : InputFile,
            file_id: Optional[str] = ...,
            path: Optional[str] = ...,
            url: Optional[str] = ...,
            blob: Optional[binary_type] = ...,
            mime: Optional[str] = ...,
            prefer_local_download: bool = ...,
            prefer_str: bool = ...,
            create_instance: bool = ...,
    ):
        super(InputFile, self).__init__()
        ...
    # end def


    def get_request_files(
        self,  # : InputFile,
        var_name: str
    ) -> Dict[str, Optional[Tuple[str, IO, str]]]: ...
    # end def

    def get_input_media_referenced_files(
        self,  # : InputFile,
        var_name: str
        # `('attach://{var_name}', {var_name: ('foo.png', open('foo.png', 'rb'), 'image/png')})`
    ) -> Tuple[str, Optional[Dict[str, Optional[Tuple[str, IO, str]]]]]: ...
    # end def

    def _calculate_size(self) -> int: ... # self: InputFile
    # end def

    @property
    def size(self) -> int: # self: InputFile
        return self._size
    # end def

    @classmethod
    def factory(
            cls: Type[InputFile],
            file_id: Optional[str] = ...,
            path: Optional[str] = ...,
            url: Optional[str] = ...,
            blob: Optional[binary_type] = ...,
            mime: Optional[str] = ...,
            prefer_local_download: bool = ...,
            prefer_str: bool = ...,
            create_instance: bool = ...,
    ) -> \
    Union[
        InputFile, 'InputFileFromBlob', 'InputFileFromDisk', 'InputFileFromURL', str,
        Tuple[
            Union[Type['InputFileFromBlob'], Type['InputFileFromDisk'], Type['InputFileFromURL'], Type[str]],
            Tuple,
            Dict,
        ]
    ]:
        ...
    # end def
# end class



class BaseInputFileUse(InputFile):
    def get_request_files(
        self,  # : BaseInputFileUse,
        var_name: str
    ) -> Dict:
        ...
    # end def
# end def


class InputFileUseFileId(BaseInputFileUse):
    def __init__(
        self,  # : InputFileUseFileID,
        file_id: str
    ) -> None:
        super().__init__()
        ...

    def get_input_media_referenced_files(
        self,  # : InputFileUseFileID,
        var_name: str
    ) -> Tuple[str, None]: ...
    # end def
# end class


class InputFileUseUrl(BaseInputFileUse):
    def __init__(
        self,
        url: str
    ):
        super(InputFileUseUrl, self).__init__()
        ...
    # end def

    def get_input_media_referenced_files(
        self,  # : InputFileUseUrl,
        var_name: str
    ) -> Tuple[str, None]: ...
    # end def
# end class


class InputFileFromBlob(InputFile):
    def __init__(
        self: Type[InputFileFromBlob],  #
        blob: binary_type,
        name: str = "file.unknown",
        mime: Optional[str] = None
    ) -> None:
        super(InputFileFromBlob, self).__init__(name=name, mime=mime)
        ...
    # end def

    @staticmethod
    def mime_from_blob(
        blob: binary_type
    ) -> str: ...
    # end def

    def get_request_files(
        self,
        var_name: str
    ) -> Dict[str, Tuple[str, binary_type, str]]: ...
    # end def

    def _calculate_size(self) -> int: ...
    # end def
# end class


class InputFileFromDisk(InputFile):
    def __init__(
        self,
        path: str,
        name: Optional[str] = None,
        mime: Optional[str] = None,
        **kwargs,
    ) -> None:
        super(InputFileFromDisk, self).__init__(name=name, mime=mime)
        ...
    # end def __init__

    @staticmethod
    def mime_from_file(
        path: str
    ) -> str: ...
    # end def

    def get_request_files(
        self,
        var_name: str
    ) -> Dict[str, Tuple[str, BinaryIO, str]]: ...
    # end def

    def _calculate_size(self) -> int: ...
# end class


class InputFileFromURL(InputFile):
    def __init__(
        self,
        url: str,
        name: Optional[str] = None,
        mime: Optional[str] = None,
    ) -> None:
        super(InputFileFromURL, self).__init__(name=name, mime=mime)
        ...
    # end def

    def __str__(self) -> str: ...
    # end def __str__

    @staticmethod
    def name_from_url(
        url: str
    ) -> str: ...
    # end def

    def get_request_files(
        self,
        var_name: str
    ) -> Dict[str, Tuple[str, binary_type, str]]: ...
    # end def

    def _calculate_size(self) -> int: ...
    # end def
# end class InputFileFromURL

