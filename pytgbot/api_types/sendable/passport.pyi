# -*- coding: utf-8 -*-
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from typing import Any, Union, List
from pytgbot.api_types.sendable import Sendable
from pytgbot.api_types.sendable.passport import PassportElementError

__author__ = 'luckydonald'


class PassportElementError(Sendable):
    """
    This object represents an error in the Telegram Passport element which was submitted that should be resolved by the user.

    https://core.telegram.org/bots/api#inputmedia

    Optional keyword parameters:
    """
# end class PassportElementError

class PassportElementErrorDataField(PassportElementError):
    """
    Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.

    https://core.telegram.org/bots/api#passportelementerrordatafield
    

    Parameters:
    
    :param source: Error source, must be data
    :type  source: str|unicode
    
    :param type: The section of the user's Telegram Passport which has the error, one of "personal_details", "passport", "driver_license", "identity_card", "internal_passport", "address"
    :type  type: str|unicode
    
    :param field_name: Name of the data field which has the error
    :type  field_name: str|unicode
    
    :param data_hash: Base64-encoded data hash
    :type  data_hash: str|unicode
    
    :param message: Error message
    :type  message: str|unicode
    

    Optional keyword parameters:
    """
    source: str
    type: str
    field_name: str
    data_hash: str
    message: str
# end class PassportElementErrorDataField

class PassportElementErrorFrontSide(PassportElementError):
    """
    Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes.

    https://core.telegram.org/bots/api#passportelementerrorfrontside
    

    Parameters:
    
    :param source: Error source, must be front_side
    :type  source: str|unicode
    
    :param type: The section of the user's Telegram Passport which has the issue, one of "passport", "driver_license", "identity_card", "internal_passport"
    :type  type: str|unicode
    
    :param file_hash: Base64-encoded hash of the file with the front side of the document
    :type  file_hash: str|unicode
    
    :param message: Error message
    :type  message: str|unicode
    

    Optional keyword parameters:
    """
    source: str
    type: str
    file_hash: str
    message: str
# end class PassportElementErrorFrontSide

class PassportElementErrorReverseSide(PassportElementError):
    """
    Represents an issue with the reverse side of a document. The error is considered resolved when the file with reverse side of the document changes.

    https://core.telegram.org/bots/api#passportelementerrorreverseside
    

    Parameters:
    
    :param source: Error source, must be reverse_side
    :type  source: str|unicode
    
    :param type: The section of the user's Telegram Passport which has the issue, one of "driver_license", "identity_card"
    :type  type: str|unicode
    
    :param file_hash: Base64-encoded hash of the file with the reverse side of the document
    :type  file_hash: str|unicode
    
    :param message: Error message
    :type  message: str|unicode
    

    Optional keyword parameters:
    """
    source: str
    type: str
    file_hash: str
    message: str
# end class PassportElementErrorReverseSide

class PassportElementErrorSelfie(PassportElementError):
    """
    Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.

    https://core.telegram.org/bots/api#passportelementerrorselfie
    

    Parameters:
    
    :param source: Error source, must be selfie
    :type  source: str|unicode
    
    :param type: The section of the user's Telegram Passport which has the issue, one of "passport", "driver_license", "identity_card", "internal_passport"
    :type  type: str|unicode
    
    :param file_hash: Base64-encoded hash of the file with the selfie
    :type  file_hash: str|unicode
    
    :param message: Error message
    :type  message: str|unicode
    

    Optional keyword parameters:
    """
    source: str
    type: str
    file_hash: str
    message: str
# end class PassportElementErrorSelfie

class PassportElementErrorFile(PassportElementError):
    """
    Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes.

    https://core.telegram.org/bots/api#passportelementerrorfile
    

    Parameters:
    
    :param source: Error source, must be file
    :type  source: str|unicode
    
    :param type: The section of the user's Telegram Passport which has the issue, one of "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration"
    :type  type: str|unicode
    
    :param file_hash: Base64-encoded file hash
    :type  file_hash: str|unicode
    
    :param message: Error message
    :type  message: str|unicode
    

    Optional keyword parameters:
    """
    source: str
    type: str
    file_hash: str
    message: str
# end class PassportElementErrorFile

class PassportElementErrorFiles(PassportElementError):
    """
    Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.

    https://core.telegram.org/bots/api#passportelementerrorfiles
    

    Parameters:
    
    :param source: Error source, must be files
    :type  source: str|unicode
    
    :param type: The section of the user's Telegram Passport which has the issue, one of "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration"
    :type  type: str|unicode
    
    :param file_hashes: List of base64-encoded file hashes
    :type  file_hashes: list of str|unicode
    
    :param message: Error message
    :type  message: str|unicode
    

    Optional keyword parameters:
    """
    source: str
    type: str
    file_hashes: List[str]
    message: str
# end class PassportElementErrorFiles

class PassportElementErrorTranslationFile(PassportElementError):
    """
    Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes.

    https://core.telegram.org/bots/api#passportelementerrortranslationfile
    

    Parameters:
    
    :param source: Error source, must be translation_file
    :type  source: str|unicode
    
    :param type: Type of element of the user's Telegram Passport which has the issue, one of "passport", "driver_license", "identity_card", "internal_passport", "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration"
    :type  type: str|unicode
    
    :param file_hash: Base64-encoded file hash
    :type  file_hash: str|unicode
    
    :param message: Error message
    :type  message: str|unicode
    

    Optional keyword parameters:
    """
    source: str
    type: str
    file_hash: str
    message: str
# end class PassportElementErrorTranslationFile

class PassportElementErrorTranslationFiles(PassportElementError):
    """
    Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change.

    https://core.telegram.org/bots/api#passportelementerrortranslationfiles
    

    Parameters:
    
    :param source: Error source, must be translation_files
    :type  source: str|unicode
    
    :param type: Type of element of the user's Telegram Passport which has the issue, one of "passport", "driver_license", "identity_card", "internal_passport", "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration"
    :type  type: str|unicode
    
    :param file_hashes: List of base64-encoded file hashes
    :type  file_hashes: list of str|unicode
    
    :param message: Error message
    :type  message: str|unicode
    

    Optional keyword parameters:
    """
    source: str
    type: str
    file_hashes: List[str]
    message: str
# end class PassportElementErrorTranslationFiles

class PassportElementErrorUnspecified(PassportElementError):
    """
    Represents an issue in an unspecified place. The error is considered resolved when new data is added.

    https://core.telegram.org/bots/api#passportelementerrorunspecified
    

    Parameters:
    
    :param source: Error source, must be unspecified
    :type  source: str|unicode
    
    :param type: Type of element of the user's Telegram Passport which has the issue
    :type  type: str|unicode
    
    :param element_hash: Base64-encoded element hash
    :type  element_hash: str|unicode
    
    :param message: Error message
    :type  message: str|unicode
    

    Optional keyword parameters:
    """
    source: str
    type: str
    element_hash: str
    message: str
# end class PassportElementErrorUnspecified
