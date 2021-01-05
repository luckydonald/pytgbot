# -*- coding: utf-8 -*-
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from typing import Any, Union, List
from pytgbot.api_types.receivable import Result

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
    data: List[EncryptedPassportElement]
    credentials: EncryptedCredentials
# end class PassportData

class PassportFile(Result):
    """
    This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB.

    https://core.telegram.org/bots/api#passportfile


    Parameters:

    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :type  file_id: str|unicode

    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :type  file_unique_id: str|unicode

    :param file_size: File size
    :type  file_size: int

    :param file_date: Unix time when the file was uploaded
    :type  file_date: int


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    file_id: str
    file_unique_id: str
    file_size: int
    file_date: int
# end class PassportFile

class EncryptedPassportElement(Result):
    """
    Contains information about documents or other Telegram Passport elements shared with the bot by the user.

    https://core.telegram.org/bots/api#encryptedpassportelement


    Parameters:

    :param type: Element type. One of "personal_details", "passport", "driver_license", "identity_card", "internal_passport", "address", "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration", "phone_number", "email".
    :type  type: str|unicode

    :param hash: Base64-encoded element hash for using in PassportElementErrorUnspecified
    :type  hash: str|unicode


    Optional keyword parameters:

    :param data: Optional. Base64-encoded encrypted Telegram Passport element data provided by the user, available for "personal_details", "passport", "driver_license", "identity_card", "internal_passport" and "address" types. Can be decrypted and verified using the accompanying EncryptedCredentials.
    :type  data: str|unicode

    :param phone_number: Optional. User's verified phone number, available only for "phone_number" type
    :type  phone_number: str|unicode

    :param email: Optional. User's verified email address, available only for "email" type
    :type  email: str|unicode

    :param files: Optional. Array of encrypted files with documents provided by the user, available for "utility_bill", "bank_statement", "rental_agreement", "passport_registration" and "temporary_registration" types. Files can be decrypted and verified using the accompanying EncryptedCredentials.
    :type  files: list of pytgbot.api_types.receivable.passport.PassportFile

    :param front_side: Optional. Encrypted file with the front side of the document, provided by the user. Available for "passport", "driver_license", "identity_card" and "internal_passport". The file can be decrypted and verified using the accompanying EncryptedCredentials.
    :type  front_side: pytgbot.api_types.receivable.passport.PassportFile

    :param reverse_side: Optional. Encrypted file with the reverse side of the document, provided by the user. Available for "driver_license" and "identity_card". The file can be decrypted and verified using the accompanying EncryptedCredentials.
    :type  reverse_side: pytgbot.api_types.receivable.passport.PassportFile

    :param selfie: Optional. Encrypted file with the selfie of the user holding a document, provided by the user; available for "passport", "driver_license", "identity_card" and "internal_passport". The file can be decrypted and verified using the accompanying EncryptedCredentials.
    :type  selfie: pytgbot.api_types.receivable.passport.PassportFile

    :param translation: Optional. Array of encrypted files with translated versions of documents provided by the user. Available if requested for "passport", "driver_license", "identity_card", "internal_passport", "utility_bill", "bank_statement", "rental_agreement", "passport_registration" and "temporary_registration" types. Files can be decrypted and verified using the accompanying EncryptedCredentials.
    :type  translation: list of pytgbot.api_types.receivable.passport.PassportFile

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    type: str
    hash: str
    data: str
    phone_number: str
    email: str
    files: List[PassportFile]
    front_side: PassportFile
    reverse_side: PassportFile
    selfie: PassportFile
    translation: List[PassportFile]
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
    data: str
    hash: str
    secret: str
# end class EncryptedCredentials
