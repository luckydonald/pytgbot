# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
from . import Result

__all__ = ['PassportData', 'PassportFile', 'EncryptedPassportElement', 'EncryptedCredentials']
__author__ = 'luckydonald'


class PassportData(Result):
    """
    Contains information about Telegram Passport data shared with the bot by the user.

    https://core.telegram.org/bots/api#passportdata


    Parameters:

    :param data: Array with information about documents and other Telegram Passport elements that was shared with the bot
    :type  data: list of pytgbot.api_types.receivable.passport.EncryptedPassportElement

    :param credentials: Encrypted credentials required to decrypt the data
    :type  credentials: pytgbot.api_types.receivable.passport.EncryptedCredentials


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, data, credentials, _raw=None):
        """
        Contains information about Telegram Passport data shared with the bot by the user.

        https://core.telegram.org/bots/api#passportdata


        Parameters:

        :param data: Array with information about documents and other Telegram Passport elements that was shared with the bot
        :type  data: list of pytgbot.api_types.receivable.passport.EncryptedPassportElement

        :param credentials: Encrypted credentials required to decrypt the data
        :type  credentials: pytgbot.api_types.receivable.passport.EncryptedCredentials


        Optional keyword parameters:

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(PassportData, self).__init__()
        assert_type_or_raise(data, list, parameter_name="data")
        self.data = data

        assert_type_or_raise(credentials, EncryptedCredentials, parameter_name="credentials")
        self.credentials = credentials

        self._raw = _raw
    # end def __init__

    def to_array(self):
        """
        Serializes this PassportData to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(PassportData, self).to_array()
        array['data'] = self._as_array(self.data)  # type list of EncryptedPassportElement
        array['credentials'] = self.credentials.to_array()  # type EncryptedCredentials
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new PassportData from a given dictionary.

        :return: new PassportData instance.
        :rtype: PassportData
        """
        if array is None or not array:
            return None
        # end if
        assert_type_or_raise(array, dict, parameter_name="array")


        data = {}
        data['data'] = EncryptedPassportElement.from_array_list(array.get('data'), list_level=1)
        data['credentials'] = EncryptedCredentials.from_array(array.get('credentials'))
        data['_raw'] = array
        return PassportData(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(passportdata_instance)`
        """
        return "PassportData(data={self.data!r}, credentials={self.credentials!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(passportdata_instance)`
        """
        if self._raw:
            return "PassportData.from_array({self._raw})".format(self=self)
        # end if
        return "PassportData(data={self.data!r}, credentials={self.credentials!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in passportdata_instance`
        """
        return key in ["data", "credentials"] and hasattr(self, key) and bool(getattr(self, key, None))
    # end def __contains__
# end class PassportData



class PassportFile(Result):
    """
    This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB.

    https://core.telegram.org/bots/api#passportfile


    Parameters:

    :param file_id: Unique identifier for this file
    :type  file_id: str|unicode

    :param file_size: File size
    :type  file_size: int

    :param file_date: Unix time when the file was uploaded
    :type  file_date: int


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, file_id, file_size, file_date, _raw=None):
        """
        This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB.

        https://core.telegram.org/bots/api#passportfile


        Parameters:

        :param file_id: Unique identifier for this file
        :type  file_id: str|unicode

        :param file_size: File size
        :type  file_size: int

        :param file_date: Unix time when the file was uploaded
        :type  file_date: int


        Optional keyword parameters:

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(PassportFile, self).__init__()
        assert_type_or_raise(file_id, unicode_type, parameter_name="file_id")
        self.file_id = file_id

        assert_type_or_raise(file_size, int, parameter_name="file_size")
        self.file_size = file_size

        assert_type_or_raise(file_date, int, parameter_name="file_date")
        self.file_date = file_date

        self._raw = _raw
    # end def __init__

    def to_array(self):
        """
        Serializes this PassportFile to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(PassportFile, self).to_array()
        array['file_id'] = u(self.file_id)  # py2: type unicode, py3: type str
        array['file_size'] = int(self.file_size)  # type int
        array['file_date'] = int(self.file_date)  # type int
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new PassportFile from a given dictionary.

        :return: new PassportFile instance.
        :rtype: PassportFile
        """
        if array is None or not array:
            return None
        # end if
        assert_type_or_raise(array, dict, parameter_name="array")

        data = {}
        data['file_id'] = u(array.get('file_id'))
        data['file_size'] = int(array.get('file_size'))
        data['file_date'] = int(array.get('file_date'))
        data['_raw'] = array
        return PassportFile(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(passportfile_instance)`
        """
        return "PassportFile(file_id={self.file_id!r}, file_size={self.file_size!r}, file_date={self.file_date!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(passportfile_instance)`
        """
        if self._raw:
            return "PassportFile.from_array({self._raw})".format(self=self)
        # end if
        return "PassportFile(file_id={self.file_id!r}, file_size={self.file_size!r}, file_date={self.file_date!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in passportfile_instance`
        """
        return key in ["file_id", "file_size", "file_date"] and hasattr(self, key) and bool(getattr(self, key, None))
    # end def __contains__
# end class PassportFile



class EncryptedPassportElement(Result):
    """
    Contains information about documents or other Telegram Passport elements shared with the bot by the user.

    https://core.telegram.org/bots/api#encryptedpassportelement


    Parameters:

    :param type: Element type. One of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”, “phone_number”, “email”.
    :type  type: str|unicode

    :param hash: Base64-encoded element hash for using in PassportElementErrorUnspecified
    :type  hash: str|unicode

    Optional keyword parameters:

    :param data: Optional. Base64-encoded encrypted Telegram Passport element data provided by the user, available for “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport” and “address” types. Can be decrypted and verified using the accompanying EncryptedCredentials.
    :type  data: str|unicode

    :param phone_number: Optional. User's verified phone number, available only for “phone_number” type
    :type  phone_number: str|unicode

    :param email: Optional. User's verified email address, available only for “email” type
    :type  email: str|unicode

    :param files: Optional. Array of encrypted files with documents provided by the user, available for “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be decrypted and verified using the accompanying EncryptedCredentials.
    :type  files: list of pytgbot.api_types.receivable.passport.PassportFile

    :param front_side: Optional. Encrypted file with the front side of the document, provided by the user. Available for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and verified using the accompanying EncryptedCredentials.
    :type  front_side: pytgbot.api_types.receivable.passport.PassportFile

    :param reverse_side: Optional. Encrypted file with the reverse side of the document, provided by the user. Available for “driver_license” and “identity_card”. The file can be decrypted and verified using the accompanying EncryptedCredentials.
    :type  reverse_side: pytgbot.api_types.receivable.passport.PassportFile

    :param selfie: Optional. Encrypted file with the selfie of the user holding a document, provided by the user; available for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and verified using the accompanying EncryptedCredentials.
    :type  selfie: pytgbot.api_types.receivable.passport.PassportFile

    :param translation: Optional. Array of encrypted files with translated versions of documents provided by the user. Available if requested for “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be decrypted and verified using the accompanying EncryptedCredentials.
    :type  translation: list of pytgbot.api_types.receivable.passport.PassportFile

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, type, hash, data=None, phone_number=None, email=None, files=None, front_side=None, reverse_side=None, selfie=None, translation=None, _raw=None):
        """
        Contains information about documents or other Telegram Passport elements shared with the bot by the user.

        https://core.telegram.org/bots/api#encryptedpassportelement


        Parameters:

        :param type: Element type. One of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”, “phone_number”, “email”.
        :type  type: str|unicode

        :param hash: Base64-encoded element hash for using in PassportElementErrorUnspecified
        :type  hash: str|unicode


        Optional keyword parameters:

        :param data: Optional. Base64-encoded encrypted Telegram Passport element data provided by the user, available for “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport” and “address” types. Can be decrypted and verified using the accompanying EncryptedCredentials.
        :type  data: str|unicode

        :param phone_number: Optional. User's verified phone number, available only for “phone_number” type
        :type  phone_number: str|unicode

        :param email: Optional. User's verified email address, available only for “email” type
        :type  email: str|unicode

        :param files: Optional. Array of encrypted files with documents provided by the user, available for “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be decrypted and verified using the accompanying EncryptedCredentials.
        :type  files: list of pytgbot.api_types.receivable.passport.PassportFile

        :param front_side: Optional. Encrypted file with the front side of the document, provided by the user. Available for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and verified using the accompanying EncryptedCredentials.
        :type  front_side: pytgbot.api_types.receivable.passport.PassportFile

        :param reverse_side: Optional. Encrypted file with the reverse side of the document, provided by the user. Available for “driver_license” and “identity_card”. The file can be decrypted and verified using the accompanying EncryptedCredentials.
        :type  reverse_side: pytgbot.api_types.receivable.passport.PassportFile

        :param selfie: Optional. Encrypted file with the selfie of the user holding a document, provided by the user; available for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and verified using the accompanying EncryptedCredentials.
        :type  selfie: pytgbot.api_types.receivable.passport.PassportFile

        :param translation: Optional. Array of encrypted files with translated versions of documents provided by the user. Available if requested for “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be decrypted and verified using the accompanying EncryptedCredentials.
        :type  translation: list of pytgbot.api_types.receivable.passport.PassportFile

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(EncryptedPassportElement, self).__init__()

        assert_type_or_raise(type, unicode_type, parameter_name="type")
        self.type = type

        assert_type_or_raise(hash, unicode_type, parameter_name="hash")
        self.hash = hash

        assert_type_or_raise(data, None, unicode_type, parameter_name="data")
        self.data = data

        assert_type_or_raise(phone_number, None, unicode_type, parameter_name="phone_number")
        self.phone_number = phone_number

        assert_type_or_raise(email, None, unicode_type, parameter_name="email")
        self.email = email

        assert_type_or_raise(files, None, list, parameter_name="files")
        self.files = files

        assert_type_or_raise(front_side, None, PassportFile, parameter_name="front_side")
        self.front_side = front_side

        assert_type_or_raise(reverse_side, None, PassportFile, parameter_name="reverse_side")
        self.reverse_side = reverse_side

        assert_type_or_raise(selfie, None, PassportFile, parameter_name="selfie")
        self.selfie = selfie

        assert_type_or_raise(translation, None, list, parameter_name="translation")
        self.translation = translation

        self._raw = _raw
    # end def __init__

    def to_array(self):
        """
        Serializes this EncryptedPassportElement to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(EncryptedPassportElement, self).to_array()
        array['type'] = u(self.type)  # py2: type unicode, py3: type str

        array['hash'] = u(self.hash)  # py2: type unicode, py3: type str

        if self.data is not None:
            array['data'] = u(self.data)  # py2: type unicode, py3: type str
        if self.phone_number is not None:
            array['phone_number'] = u(self.phone_number)  # py2: type unicode, py3: type str
        if self.email is not None:
            array['email'] = u(self.email)  # py2: type unicode, py3: type str
        if self.files is not None:
            array['files'] = self._as_array(self.files)  # type list of PassportFile
        if self.front_side is not None:
            array['front_side'] = self.front_side.to_array()  # type PassportFile
        if self.reverse_side is not None:
            array['reverse_side'] = self.reverse_side.to_array()  # type PassportFile
        if self.selfie is not None:
            array['selfie'] = self.selfie.to_array()  # type PassportFile
        if self.translation is not None:
            array['translation'] = self._as_array(self.translation)  # type list of PassportFile
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new EncryptedPassportElement from a given dictionary.

        :return: new EncryptedPassportElement instance.
        :rtype: EncryptedPassportElement
        """
        if array is None or not array:
            return None
        # end if
        assert_type_or_raise(array, dict, parameter_name="array")


        data = {}
        data['type'] = u(array.get('type'))
        data['hash'] = u(array.get('hash'))
        data['data'] = u(array.get('data')) if array.get('data') is not None else None
        data['phone_number'] = u(array.get('phone_number')) if array.get('phone_number') is not None else None
        data['email'] = u(array.get('email')) if array.get('email') is not None else None
        data['files'] = PassportFile.from_array_list(array.get('files'), list_level=1) if array.get('files') is not None else None
        data['front_side'] = PassportFile.from_array(array.get('front_side')) if array.get('front_side') is not None else None
        data['reverse_side'] = PassportFile.from_array(array.get('reverse_side')) if array.get('reverse_side') is not None else None
        data['selfie'] = PassportFile.from_array(array.get('selfie')) if array.get('selfie') is not None else None
        data['translation'] = PassportFile.from_array_list(array.get('translation'), list_level=1) if array.get('translation') is not None else None
        data['_raw'] = array
        return EncryptedPassportElement(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(encryptedpassportelement_instance)`
        """
        return "EncryptedPassportElement(type={self.type!r}, hash={self.hash!r}, data={self.data!r}, phone_number={self.phone_number!r}, email={self.email!r}, files={self.files!r}, front_side={self.front_side!r}, reverse_side={self.reverse_side!r}, selfie={self.selfie!r}, translation={self.translation!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(encryptedpassportelement_instance)`
        """
        if self._raw:
            return "EncryptedPassportElement.from_array({self._raw})".format(self=self)
        # end if
        return "EncryptedPassportElement(type={self.type!r}, hash={self.hash!r}, data={self.data!r}, phone_number={self.phone_number!r}, email={self.email!r}, files={self.files!r}, front_side={self.front_side!r}, reverse_side={self.reverse_side!r}, selfie={self.selfie!r}, translation={self.translation!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in encryptedpassportelement_instance`
        """
        return key in ["type", "hash", "data", "phone_number", "email", "files", "front_side", "reverse_side", "selfie", "translation"] and hasattr(self, key) and bool(getattr(self, key, None))
    # end def __contains__
# end class EncryptedPassportElement



class EncryptedCredentials(Result):
    """
    Contains data required for decrypting and authenticating EncryptedPassportElement. See the Telegram Passport Documentation for a complete description of the data decryption and authentication processes.

    https://core.telegram.org/bots/api#encryptedcredentials


    Parameters:

    :param data: Base64-encoded encrypted JSON-serialized data with unique user's payload, data hashes and secrets required for EncryptedPassportElement decryption and authentication
    :type  data: str|unicode

    :param hash: Base64-encoded data hash for data authentication
    :type  hash: str|unicode

    :param secret: Base64-encoded secret, encrypted with the bot's public RSA key, required for data decryption
    :type  secret: str|unicode


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, data, hash, secret, _raw=None):
        """
        Contains data required for decrypting and authenticating EncryptedPassportElement. See the Telegram Passport Documentation for a complete description of the data decryption and authentication processes.

        https://core.telegram.org/bots/api#encryptedcredentials


        Parameters:

        :param data: Base64-encoded encrypted JSON-serialized data with unique user's payload, data hashes and secrets required for EncryptedPassportElement decryption and authentication
        :type  data: str|unicode

        :param hash: Base64-encoded data hash for data authentication
        :type  hash: str|unicode

        :param secret: Base64-encoded secret, encrypted with the bot's public RSA key, required for data decryption
        :type  secret: str|unicode


        Optional keyword parameters:

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(EncryptedCredentials, self).__init__()
        assert_type_or_raise(data, unicode_type, parameter_name="data")
        self.data = data

        assert_type_or_raise(hash, unicode_type, parameter_name="hash")
        self.hash = hash

        assert_type_or_raise(secret, unicode_type, parameter_name="secret")
        self.secret = secret

        self._raw = _raw
    # end def __init__

    def to_array(self):
        """
        Serializes this EncryptedCredentials to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(EncryptedCredentials, self).to_array()
        array['data'] = u(self.data)  # py2: type unicode, py3: type str
        array['hash'] = u(self.hash)  # py2: type unicode, py3: type str
        array['secret'] = u(self.secret)  # py2: type unicode, py3: type str
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new EncryptedCredentials from a given dictionary.

        :return: new EncryptedCredentials instance.
        :rtype: EncryptedCredentials
        """
        if array is None or not array:
            return None
        # end if
        assert_type_or_raise(array, dict, parameter_name="array")

        data = {}
        data['data'] = u(array.get('data'))
        data['hash'] = u(array.get('hash'))
        data['secret'] = u(array.get('secret'))
        data['_raw'] = array
        return EncryptedCredentials(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(encryptedcredentials_instance)`
        """
        return "EncryptedCredentials(data={self.data!r}, hash={self.hash!r}, secret={self.secret!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(encryptedcredentials_instance)`
        """
        if self._raw:
            return "EncryptedCredentials.from_array({self._raw})".format(self=self)
        # end if
        return "EncryptedCredentials(data={self.data!r}, hash={self.hash!r}, secret={self.secret!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in encryptedcredentials_instance`
        """
        return key in ["data", "hash", "secret"] and hasattr(self, key) and bool(getattr(self, key, None))
    # end def __contains__
# end class EncryptedCredentials

