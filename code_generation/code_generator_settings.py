CLASS_TYPE_PATHS__IMPORT = 0
CLASS_TYPE_PATHS__PARENT = 1
CLASS_TYPE_PATHS__DESCRIPTION = 2

CLASS_TYPE_PATHS = {  # class: import, master_class, descr
    # "to_unicode": ("luckydonaldUtils.encoding.", "object", None), # https://github.com/luckydonald/pytgbot/issues/5
    "TgBotApiObject": ("pytgbot.api_types.", "object", None),

    # pytgbot.api_types.receivable.__init__.*
    "Receivable":           ("pytgbot.api_types.receivable.", "TgBotApiObject", None),
    "Result":               ("pytgbot.api_types.receivable.", "Receivable", None),

    # pytgbot.api_types.receivable.media.*
    "MessageEntity":        ("pytgbot.api_types.receivable.media.", "Result", None),
    "PhotoSize":            ("pytgbot.api_types.receivable.media.", "Result", None),
    "UserProfilePhotos":    ("pytgbot.api_types.receivable.media.", "Result", None),
    "ChatPhoto":            ("pytgbot.api_types.receivable.media.", "Result", None),
    "Media":                ("pytgbot.api_types.receivable.media.", "Receivable", None),
    "File":                 ("pytgbot.api_types.receivable.media.", "Receivable", None),
    "Voice":                ("pytgbot.api_types.receivable.media.", "Media", None),
    "VideoNote":            ("pytgbot.api_types.receivable.media.", "Media", None),  # May 18, 2017
    "Contact":              ("pytgbot.api_types.receivable.media.", "Media", None),
    "Location":             ("pytgbot.api_types.receivable.media.", "Media", None),
    "Venue":                ("pytgbot.api_types.receivable.media.", "Media", None),
    "Audio":                ("pytgbot.api_types.receivable.media.", "Media", None),
    "Document":             ("pytgbot.api_types.receivable.media.", "Media", None),
    "Sticker":              ("pytgbot.api_types.receivable.media.", "Media", None),  # Moved July 21, 2017
    "Video":                ("pytgbot.api_types.receivable.media.", "Media", None),
    "Game":                 ("pytgbot.api_types.receivable.media.", "Media", None),
    "Animation":            ("pytgbot.api_types.receivable.media.", "Media", None),
    "Poll":                 ("pytgbot.api_types.receivable.media.", "Media", None),  # April 14, 2019
    "PollOption":           ("pytgbot.api_types.receivable.media.", "Receivable", None),  # April 14, 2019
    "PollAnswer":           ("pytgbot.api_types.receivable.media.", "Receivable", None),  # January 23, 2020
    "Dice":                 ("pytgbot.api_types.receivable.media.", "Media", None),  # March 30, 2020

    # pytgbot.api_types.receivable.responses.*

    # pytgbot.api_types.receivable.peer.*
    "ChatPermissions": ("pytgbot.api_types.receivable.peer.", "Result", None),  # July 29, 2019
    "ChatMember":      ("pytgbot.api_types.receivable.peer.", "Result", None),
    "Peer":            ("pytgbot.api_types.receivable.peer.", "Result", None),
    "User":            ("pytgbot.api_types.receivable.peer.", "Peer", None),
    "Chat":            ("pytgbot.api_types.receivable.peer.", "Peer", None),

    # pytgbot.api_types.receivable.command.*
    "BotCommand":            ("pytgbot.api_types.sendable.command.", "Sendable", None),

    # pytgbot.api_types.receivable.updates.*
    "Update":               ("pytgbot.api_types.receivable.updates.", "Receivable", None),
    "UpdateType":           ("pytgbot.api_types.receivable.updates.", "Receivable", None),
    "Message":              ("pytgbot.api_types.receivable.updates.", "UpdateType", None),
    "CallbackQuery":        ("pytgbot.api_types.receivable.updates.", "UpdateType", None),
    "CallbackGame":         ("pytgbot.api_types.receivable.updates.", "UpdateType", None),  # October 3, 2016
    "ResponseParameters":   ("pytgbot.api_types.receivable.updates.", "Receivable", None),  # October 3, 2016
    "WebhookInfo":          ("pytgbot.api_types.receivable.updates.", "Receivable", None),  # October 3, 2016

    # pytgbot.api_types.receivable.inline.*
    "InlineQuery":                  ("pytgbot.api_types.receivable.inline.", "Result", None),
    "ChosenInlineResult":           ("pytgbot.api_types.receivable.inline.", "UpdateType", None),

    # pytgbot.api_types.receivable.game.*
    "GameHighScore": ("pytgbot.api_types.receivable.game.", "Result", None),  # October 3, 2016

    # pytgbot.api_types.receivable.payments.*
    "Invoice":              ("pytgbot.api_types.receivable.payments.", "Result", None),  # May 18, 2017
    "OrderInfo":            ("pytgbot.api_types.receivable.payments.", "Result", None),  # May 18, 2017
    "ShippingAddress":      ("pytgbot.api_types.receivable.payments.", "Result", None),  # May 18, 2017
    "SuccessfulPayment":    ("pytgbot.api_types.receivable.payments.", "Result", None),  # May 18, 2017
    "ShippingQuery":        ("pytgbot.api_types.receivable.payments.", "UpdateType", None),  # May 18, 2017
    "PreCheckoutQuery":     ("pytgbot.api_types.receivable.payments.", "UpdateType", None),  # May 18, 2017

    # pytgbot.api_types.receivable.stickers.*
    # "Sticker":      ("pytgbot.api_types.receivable.stickers.", "Media", None),  # July 21, 2017
    "StickerSet":   ("pytgbot.api_types.receivable.stickers.", "Result", None),  # July 21, 2017
    "MaskPosition": ("pytgbot.api_types.receivable.stickers.", "Result", None),  # July 21, 2017

    # pytgbot.api_types.receivable.passport.*
    "PassportData":               ("pytgbot.api_types.receivable.passport.", "Result", None),  # July 26, 2018
    "EncryptedPassportElement":   ("pytgbot.api_types.receivable.passport.", "Result", None),  # July 26, 2018
    "EncryptedCredentials":       ("pytgbot.api_types.receivable.passport.", "Result", None),  # July 26, 2018
    "PassportFile":               ("pytgbot.api_types.receivable.passport.", "Result", None),  # July 26, 2018

    # pytgbot.api_types.sendable.*
    "Sendable":                     ("pytgbot.api_types.sendable.", "TgBotApiObject", None),

    # pytgbot.api_types.sendable.files.*
    "InputFile":                    ("pytgbot.api_types.sendable.files.", "TgBotApiObject", None),
    "InputFileFromDisk":            ("pytgbot.api_types.sendable.files.", "InputFile", None),
    "InputFileFromURL":             ("pytgbot.api_types.sendable.files.", "InputFile", None),

    # pytgbot.api_types.sendable.inline.*
    "InputMessageContent":          ("pytgbot.api_types.sendable.inline.", "Sendable", None),
    "InputTextMessageContent":      ("pytgbot.api_types.sendable.inline.", "InputMessageContent", None),
    "InputLocationMessageContent":  ("pytgbot.api_types.sendable.inline.", "InputMessageContent", None),
    "InputVenueMessageContent":     ("pytgbot.api_types.sendable.inline.", "InputMessageContent", None),
    "InputContactMessageContent":   ("pytgbot.api_types.sendable.inline.", "InputMessageContent", None),
    "InlineQueryResult":            ("pytgbot.api_types.sendable.inline.", "Sendable", None),
    "InlineQueryResultArticle":     ("pytgbot.api_types.sendable.inline.", "InlineQueryResult", None),
    "InlineQueryResultPhoto":       ("pytgbot.api_types.sendable.inline.", "InlineQueryResult", None),
    "InlineQueryResultGif":         ("pytgbot.api_types.sendable.inline.", "InlineQueryResult", None),
    "InlineQueryResultMpeg4Gif":    ("pytgbot.api_types.sendable.inline.", "InlineQueryResult", None),
    "InlineQueryResultVideo":       ("pytgbot.api_types.sendable.inline.", "InlineQueryResult", None),
    "InlineQueryResultAudio":       ("pytgbot.api_types.sendable.inline.", "InlineQueryResult", None),
    "InlineQueryResultVoice":       ("pytgbot.api_types.sendable.inline.", "InlineQueryResult", None),
    "InlineQueryResultDocument":    ("pytgbot.api_types.sendable.inline.", "InlineQueryResult", None),
    "InlineQueryResultLocation":    ("pytgbot.api_types.sendable.inline.", "InlineQueryResult", None),
    "InlineQueryResultVenue":       ("pytgbot.api_types.sendable.inline.", "InlineQueryResult", None),
    "InlineQueryResultContact":     ("pytgbot.api_types.sendable.inline.", "InlineQueryResult", None),
    "InlineQueryResultGame":        ("pytgbot.api_types.sendable.inline.", "InlineQueryResult", None),  # October 3, 2016
    # "InlineQueryResultCached":      ("pytgbot.api_types.sendable.inline.", "Sendable", None),
    "InlineQueryCachedResult":      ("pytgbot.api_types.sendable.inline.", "InlineQueryResult", None),
    "InlineQueryResultCachedArticle":     ("pytgbot.api_types.sendable.inline.", "InlineQueryCachedResult", None),
    "InlineQueryResultCachedPhoto":       ("pytgbot.api_types.sendable.inline.", "InlineQueryCachedResult", None),
    "InlineQueryResultCachedGif":         ("pytgbot.api_types.sendable.inline.", "InlineQueryCachedResult", None),
    "InlineQueryResultCachedMpeg4Gif":    ("pytgbot.api_types.sendable.inline.", "InlineQueryCachedResult", None),
    "InlineQueryResultCachedSticker":     ("pytgbot.api_types.sendable.inline.", "InlineQueryCachedResult", None),
    "InlineQueryResultCachedVideo":       ("pytgbot.api_types.sendable.inline.", "InlineQueryCachedResult", None),
    "InlineQueryResultCachedAudio":       ("pytgbot.api_types.sendable.inline.", "InlineQueryCachedResult", None),
    "InlineQueryResultCachedVoice":       ("pytgbot.api_types.sendable.inline.", "InlineQueryCachedResult", None),
    "InlineQueryResultCachedDocument":    ("pytgbot.api_types.sendable.inline.", "InlineQueryCachedResult", None),
    "InlineQueryResultCachedLocation":    ("pytgbot.api_types.sendable.inline.", "InlineQueryCachedResult", None),
    "InlineQueryResultCachedVenue":       ("pytgbot.api_types.sendable.inline.", "InlineQueryCachedResult", None),
    "InlineQueryResultCachedContact":     ("pytgbot.api_types.sendable.inline.", "InlineQueryCachedResult", None),

    # pytgbot.api_types.sendable.input_media.*
    "InputMedia":                   ("pytgbot.api_types.sendable.input_media.", "Sendable", None),
    "InputMediaPhoto":              ("pytgbot.api_types.sendable.input_media.", "InputMedia", None),
    "InputMediaWithThumb":          ("pytgbot.api_types.sendable.input_media.", "InputMedia", None),
    "InputMediaVideo":              ("pytgbot.api_types.sendable.input_media.", "InputMediaWithThumb", None),
    "InputMediaAnimation":          ("pytgbot.api_types.sendable.input_media.", "InputMediaWithThumb", None),
    "InputMediaAudio":              ("pytgbot.api_types.sendable.input_media.", "InputMediaWithThumb", None),
    "InputMediaDocument":           ("pytgbot.api_types.sendable.input_media.", "InputMediaWithThumb", None),

    # pytgbot.api_types.sendable.reply_markup.*
    "Button":                 ("pytgbot.api_types.sendable.reply_markup.", "Sendable", None),
    "ReplyMarkup":            ("pytgbot.api_types.sendable.reply_markup.", "Sendable", None),
    "ReplyKeyboardMarkup":    ("pytgbot.api_types.sendable.reply_markup.", "ReplyMarkup", None),
    "ReplyKeyboardRemove":    ("pytgbot.api_types.sendable.reply_markup.", "ReplyMarkup", None),
    "ForceReply":             ("pytgbot.api_types.sendable.reply_markup.", "ReplyMarkup", None),
    "InlineKeyboardMarkup":   ("pytgbot.api_types.sendable.reply_markup.", "ReplyMarkup", None),
    "KeyboardButton":         ("pytgbot.api_types.sendable.reply_markup.", "Button", None),
    "KeyboardButtonPollType": ("pytgbot.api_types.sendable.reply_markup.", "Button", None),  # January 23, 2020
    "InlineKeyboardButton":   ("pytgbot.api_types.sendable.reply_markup.", "Button", None),
    "LoginUrl":               ("pytgbot.api_types.sendable.reply_markup.", "Sendable", None),  # May 31, 2019

    # pytgbot.api_types.sendable.payments.*
    "LabeledPrice":     ("pytgbot.api_types.sendable.payments.", "Sendable", None),  # May 18, 2017
    "ShippingOption":   ("pytgbot.api_types.sendable.payments.", "Sendable", None),  # May 18, 2017


    # pytgbot.api_types.sendable.passport.*
    "PassportElementError":                 ("pytgbot.api_types.sendable.passport.", "Sendable", None),  # July 26, 2018
    "PassportElementErrorDataField":        ("pytgbot.api_types.sendable.passport.", "PassportElementError", None),  # July 26, 2018
    "PassportElementErrorFrontSide":        ("pytgbot.api_types.sendable.passport.", "PassportElementError", None),  # July 26, 2018
    "PassportElementErrorReverseSide":      ("pytgbot.api_types.sendable.passport.", "PassportElementError", None),  # July 26, 2018
    "PassportElementErrorSelfie":           ("pytgbot.api_types.sendable.passport.", "PassportElementError", None),  # July 26, 2018
    "PassportElementErrorFile":             ("pytgbot.api_types.sendable.passport.", "PassportElementError", None),  # July 26, 2018
    "PassportElementErrorFiles":            ("pytgbot.api_types.sendable.passport.", "PassportElementError", None),  # July 26, 2018
    "PassportElementErrorTranslationFile":  ("pytgbot.api_types.sendable.passport.", "PassportElementError", None),  # August 27, 2018
    "PassportElementErrorTranslationFiles": ("pytgbot.api_types.sendable.passport.", "PassportElementError", None),  # August 27, 2018
    "PassportElementErrorUnspecified":      ("pytgbot.api_types.sendable.passport.", "PassportElementError", None),  # August 27, 2018
}
"""
class: import, master_class, descr
"""

WHITELISTED_FUNCS = {  # Array with names of functions which have no parameters table and thus wouldn't be detected, or default replacements of stuff which just won't get parsed correctly.
    # "func": {'return': {'expected': '', 'replace': ''}, 'r_type': {'expected': '', 'replace': ''}},
    "getMe":                  {'return': {'expected': '', 'replace': 'Returns basic information about the bot in form of a User object'}, 'r_type': {'expected': '', 'replace': 'User'}},
    "deleteWebhook":          {'return': {'expected': '', 'replace': 'Returns True on success'}, 'r_type': {'expected': '', 'replace': 'True'}},
    "getWebhookInfo":         {'return': {'expected': 'On success, returns a WebhookInfo object. If the bot is using getUpdates, will return an object with the url field empty', 'replace': 'On success, returns a WebhookInfo object'}, 'r_type': {'expected': 'WebhookInfo or getUpdates or url', 'replace': 'WebhookInfo'}},
    "kickChatMember":         {'return': {'expected': 'In the case of supergroups and channels, the user will not be able to return to the group on their own using invite links, etc. Returns True on success', 'replace': 'Returns True on success'}, 'r_type': {'expected': 'True', 'replace': 'True'}},
    "unbanChatMember":        {'return': {'expected': 'The user will not return to the group or channel automatically, but will be able to join via link, etc. Returns True on success', 'replace': 'Returns True on success'}, 'r_type': {'expected': 'True', 'replace': 'True'}},
    "getChatAdministrators":  {'return': {'expected': 'On success, returns an Array of ChatMember objects that contains information about all chat administrators except other bots. If the chat is a group or a supergroup and no administrators were appointed, only the creator will be returned', 'replace': 'On success, returns an Array of ChatMember objects that contains information about all chat administrators except other bots'}, 'r_type': {'expected': 'list of ChatMember', 'replace': 'list of ChatMember'}},
    "setChatStickerSet":      {'return': {'expected': 'Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success', 'replace': 'Returns True on success'}, 'r_type': {'expected': 'can_set_sticker_set or getChat or True', 'replace': 'True'}},
    "deleteChatStickerSet":   {'return': {'expected': 'Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success', 'replace': 'Returns True on success'}, 'r_type': {'expected': 'can_set_sticker_set or getChat or True', 'replace': 'True'}},
    "setGameScore":           {'return': {'expected': "On success, if the message was sent by the bot, returns the edited Message, otherwise returns True. Returns an error, if the new score is not greater than the user's current score in the chat and force is False", 'replace': 'On success, if the message was sent by the bot, returns the edited Message, otherwise returns True'}, 'r_type': {'expected': 'Message or True or force or False', 'replace': 'Message or True'}},
    "getGameHighScores":      {'return': {'expected': 'This method will currently return scores for the target user, plus two of their closest neighbors on each side. Will also return the top three users if the user and his neighbors are not among them. Please note that this behavior is subject to change.','replace': 'On success, returns an Array of GameHighScore objects'}, 'r_type': {'expected': '', 'replace': 'list of GameHighScore'}},
    "setPassportDataErrors":  {'return': {'expected': 'The user will not be able to re-submit their Passport to you until the errors are fixed (the contents of the field for which you returned the error must change). Returns True on success', 'replace': 'Returns True on success'}, 'r_type': {'expected': 'True', 'replace': 'True'}},
    "sendMediaGroup":         {'return': {'expected': 'On success, an array of the sent Messages is returned', 'replace': 'On success, an array of the sent Messages is returned'}, 'r_type': {'expected': 'Messages', 'replace': 'list of Message'}},
    "answerShippingQuery":    {'return': {'expected': 'On success, True is returned', 'replace': 'On success, True is returned'}, 'r_type': {'expected': '', 'replace': 'True'}},
    "answerPreCheckoutQuery": {'return': {'expected': 'On success, True is returned', 'replace': 'On success, True is returned'}, 'r_type': {'expected': '', 'replace': 'True'}},
}
"""
Array with names of functions which have no parameters table and thus wouldn't be detected, or default replacements of stuff which just won't get parsed correctly.
"""

WHITELISTED_CLASSES = [  # Array with names of classes which have no parameters table and thus wouldn't be detected.
    "CallbackGame",
    "InlineQueryResult",
    "InputMedia",
    "PassportElementError",
    "InputMediaWithThumb",
]
""" Array with names of classes which have no parameters table and thus wouldn't be detected."""


MESSAGE_CLASS_OVERRIDES = {  # Overrides of send function classification for teleflask. More docstring below.
    "MessageMessage": "TextMessage",  # sendMessage, for text
}
"""
Overrides of send function classification for teleflask.
Function "sendMessage" => "Message" will be replaced with "TextMessage".
"""


TYPE_STRING_OVERRIDES = {  # Overrides function types
    "Array of InputMediaPhoto and InputMediaVideo": "list of InputMediaPhoto | list of InputMediaVideo",  # sendMediaGroup
    "Messages": "list of Message",  # sendMediaGroup
}
"""
Overrides of send function classification for teleflask.
Function "sendMessage" => "Message" will be replaced with "TextMessage".
"""

class CustomClass(object):
    def __init__(self, text, imports):
        """

        :param text: str[]
        :param imports: str[]
        """
        self.text = text
        self.imports = imports
    # end def
# end class


CUSTOM_CLASSES = {
    "pytgbot.api_types.receivable.media.Media": CustomClass(
        text=[
            'class Media(Receivable):',
            '    """ parent class for all receivable media. """',
            '    pass',
            '# end class Media',
        ],
        imports=[
            "pytgbot.api_types.receivable.Receivable",
        ],
    ),
    "pytgbot.api_types.receivable.peer.Peer": CustomClass(
        text=[
            "class Peer(Result):",
            '    """ parent class for both users and chats """',
            "    pass",
            "# end class Peer",
        ],
        imports=[
            "pytgbot.api_types.receivable.Result",
        ],
    ),
    "pytgbot.api_types.receivable.updates.UpdateType": CustomClass(
        text=[
            "class UpdateType(Receivable):",
            '    """',
            '    All extending classes are an property of the Update type.',
            '    Like Message: Update.message',
            '    """',
            '   pass',
            '# end class UpdateType',
        ],
        imports=[
            "pytgbot.api_types.receivable.Receivable",
        ],
    ),
    "pytgbot.api_types.receivable.updates.CallbackGame": CustomClass(
        text=[
            'class CallbackGame(UpdateType):',
            '    """',
            '    A placeholder, currently holds no information. Use BotFather to set up your game.',
            '',
            '    https://core.telegram.org/bots/api#callbackgame',
            '    """',
            '    def to_array(self):',
            '        return {}',
            '    # end def',
            '',
            '    @staticmethod',
            '    def validate_array(array):',
            '        return {}',
            '    # end def',
            '# end class',
        ],
        imports=[
            "pytgbot.api_types.receivable.updates.UpdateType",
        ],
    ),
    "pytgbot.api_types.receivable.sendable.inline.InlineQueryResult": CustomClass(
        text=[
            'class InlineQueryResult(Sendable):',
            '    """',
            '    This object represents one result of an inline query.',
            '',
            '    https://core.telegram.org/bots/api#inlinequeryresult',
            '',
            '    Telegram clients currently support results of 20 types',
            '    """',
            '    def __init__(self, id, type):',
            '        assert_type_or_raise(id, unicode_type, int, parameter_name="id")',
            '        if not isinstance(id, unicode_type):',
            '            id = u(id)',
            '        assert(isinstance(id, unicode_type))',
            '        self.id = id',
            '',
            '        self.type = type',
            '        super(InlineQueryResult, self).__init__()',
            '    # end def',
            '',
            '    def to_array(self):',
            '        return {',
            '            "type": u(self.type),',
            '            "id": u(self.id),',
            '        }',
            '    # end def to_array',
            '# end class InlineQueryResult',
        ],
        imports=[
            "pytgbot.api_types.receivable.sendable.Sendable",
        ],
    ),
    "pytgbot.api_types.receivable.sendable.inline.InlineQueryCachedResult": CustomClass(
        text=[
            'class InlineQueryCachedResult(InlineQueryResult):',
            '    pass',
            '# end class InlineQueryCachedResult',
        ],
        imports=[
            "pytgbot.api_types.receivable.sendable.inline.InlineQueryResult",
        ],
    ),
    "pytgbot.api_types.receivable.sendable.inline.InputMessageContent": CustomClass(
        text=[
            'class InputMessageContent(Sendable):',
            '    pass',
            '# end class InputMessageContent',
        ],
        imports=[
            "pytgbot.api_types.receivable.sendable.Sendable",
        ],
    ),
    "pytgbot.api_types.receivable.sendable.input_media.InputMedia": CustomClass(
        text=[
            'class InputMedia(Sendable):',
            '    """',
            '    This object represents the content of a media message to be sent.',
            '',
            '    https://core.telegram.org/bots/api#inputmedia',
            '',
            '',
            '    Parameters:',
            '',
            '    :param type: Type of the result',
            '    :type  type: str|unicode',
            '',
            '    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »',
            '    :type  media: str|unicode',
            '',
            '    Optional keyword parameters:',
            '',
            '    :param parse_mode: Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in the media caption.',
            '    :type  parse_mode: str|unicode',
            '    """',
            '',
            '    def __init__(self, type, media, caption=None, parse_mode=None):',
            '        """',
            '        This object represents the content of a media message to be sent.',
            '',
            '        https://core.telegram.org/bots/api#inputmedia',
            '',
            '',
            '        Parameters:',
            '',
            '        :param type: Type of the result',
            '        :type  type: str|unicode',
            '',
            '        :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »',
            '        :type  media: str|unicode',
            '',
            '',
            '        Optional keyword parameters:',
            '',
            '        :param caption: Optional. Caption of the media to be sent, 0-1024 characters',
            '        :type  caption: str|unicode',
            '',
            '        :param parse_mode: Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in the media caption.',
            '        :type  parse_mode: str|unicode',
            '        """',
            '        super(InputMedia, self).__init__()',
            '',
            '        assert_type_or_raise(type, unicode_type, parameter_name="type")',
            '        self.type = type',
            '',
            '        assert_type_or_raise(media, unicode_type, InputFile, parameter_name="media")',
            '        self.media = media',
            '',
            '        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")',
            '        self.caption = caption',
            '',
            '        assert_type_or_raise(parse_mode, None, unicode_type, parameter_name="parse_mode")',
            '        self.parse_mode = parse_mode',
            '    # end def __init__',
            '',
            '    def to_array(self):',
            '        """',
            '        Serializes this InputMediaPhoto to a dictionary.',
            '',
            '        :return: dictionary representation of this object.',
            '        :rtype: dict',
            '        """',
            '        array = {',
            '            "type": u(self.type),',
            '            #"media": u(self.media),',
            '        }',
            '        if self.caption is not None:',
            '            array[\'caption\'] = u(self.caption)  # py2: type unicode, py3: type str',
            '        # end if',
            '        if self.parse_mode is not None:',
            '            array[\'parse_mode\'] = u(self.parse_mode)  # py2: type unicode, py3: type str',
            '        # end if',
            '        return array',
            '    # end def to_array',
            '',
            '    @staticmethod',
            '    def validate_array(array):',
            '        """',
            '        Builds a new array with valid values for the InputMedia constructor.',
            '',
            '        :return: new array with valid values',
            '        :rtype: dict',
            '        """',
            '        assert_type_or_raise(array, dict, parameter_name="array")',
            '        data = InputMedia.validate_array(array)',
            '        data[\'type\'] = u(array.get(\'type\'))',
            '        data[\'media\'] = u(array.get(\'media\'))',
            '        data[\'caption\'] = u(array.get(\'caption\')) if array.get(\'caption\') is not None else None',
            '        data[\'parse_mode\'] = u(array.get(\'parse_mode\')) if array.get(\'parse_mode\') is not None else None',
            '        return data',
            '    # end def validate_array',
            '',
            '    @staticmethod',
            '    def from_array(array):',
            '        """',
            '        Deserialize a new InputMedia from a given dictionary.',
            '',
            '        :return: new InputMedia instance.',
            '        :rtype: InputMedia',
            '        """',
            '        if not array:  # None or {}',
            '            return None',
            '        # end if',
            '',
            '        data = InputMedia.validate_array(array)',
            '        instance = InputMedia(**data)',
            '        instance._raw = array',
            '        return instance',
            '    # end def from_array',
            '',
            '    def __str__(self):',
            '        """',
            '        Implements `str(inputmediaphoto_instance)`',
            '        """',
            '        return "InputMedia(type={self.type!r}, media={self.media!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r})".format(self=self)',
            '    # end def __str__',
            '',
            '    def __repr__(self):',
            '        """',
            '        Implements `repr(inputmedia_instance)`',
            '        """',
            '        if self._raw:',
            '            return "InputMedia.from_array({self._raw})".format(self=self)',
            '        # end if',
            '        return "InputMedia(type={self.type!r}, media={self.media!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r})".format(self=self)',
            '    # end def __repr__',
            '',
            '    def __contains__(self, key):',
            '        """',
            '        Implements `"key" in inputmedia_instance`',
            '        """',
            '        return (',
            '            key in ["type", "media", "caption", "parse_mode"]',
            '            and hasattr(self, key)',
            '            and bool(getattr(self, key, None))',
            '        )',
            '    # end def __contains__',
            '',
            '    def get_request_data(self, var_name, full_data=False):',
            '        """',
            '        :param var_name:',
            '        :param full_data: If you want `.to_array()` with this data, ready to be sent.',
            '        :return: A tuple of `to_array()` dict and the files (:py:func:`InputFile.get_request_files()`).',
            '                 Files can be None, if no file was given, but an url or existing `file_id`.',
            '                 If `media` is :py:class:`InputFile` however, the first tuple element,',
            '                 media, will have [\'media\'] set to `attach://{var_name}_media` automatically.',
            '        """',
            '        if full_data:',
            '            data = self.to_array()',
            '            data[\'media\'], file = self.get_inputfile_data(self.media, var_name, suffix=\'_media\')',
            '            return data, file',
            '        # end if',
            '        return self.get_inputfile_data(self.media, var_name, suffix=\'_media\')',
            '    # end def get_request_data',
            '',
            '    @staticmethod',
            '    def get_inputfile_data(media, var_name, suffix=\'_media\'):',
            '        name = "{var_name}{suffix}".format(var_name=var_name, suffix=suffix)',
            '        if isinstance(media, InputFile):',
            '            # is file to be uploaded',
            '            string = \'attach://{name}\'.format(name=name)',
            '            return string, media.get_request_files(name)',
            '        else:',
            '            # is no upload',
            '            return media, None',
            '        # end if',
            '    # end def get_inputfile_data',
            '# end class InputMedia',
        ],
        imports=[
            "pytgbot.api_types.receivable.sendable.Sendable",
        ],
    ),
    "pytgbot.api_types.receivable.sendable.input_media.InputMediaWithThumb": CustomClass(
        text=[
            'class InputMediaWithThumb(InputMedia):',
            '    """',
            '    Represents a media with thumb field to be sent.',
            '',
            '',
            '    Parameters:',
            '',
            '    :param type: Type of the result, must be photo',
            '    :type  type: str|unicode',
            '',
            '    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »',
            '    :type  media: str|unicode',
            '',
            '    :param thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file',
            '    :type  thumb: InputFile | str|unicode',
            '',
            '',
            '    Optional keyword parameters:',
            '',
            '    :param caption: Optional. Caption of the photo to be sent, 0-1024 characters',
            '    :type  caption: str|unicode',
            '',
            '    :param parse_mode: Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in the media caption.',
            '    :type  parse_mode: str|unicode',
            '    """',
            '',
            '    def __init__(self, type, media, thumb, caption=None, parse_mode=None):',
            '        """',
            '        Represents a media with thumb field to be sent.',
            '',
            '',
            '        Parameters:',
            '',
            '        :param type: Type of the result, must be photo',
            '        :type  type: str|unicode',
            '',
            '        :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »',
            '        :type  media: str|unicode',
            '',
            '        :param thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file',
            '        :type  thumb: InputFile | str|unicode',
            '',
            '',
            '        Optional keyword parameters:',
            '',
            '        :param caption: Optional. Caption of the photo to be sent, 0-1024 characters',
            '        :type  caption: str|unicode',
            '',
            '        :param parse_mode: Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in the media caption.',
            '        :type  parse_mode: str|unicode',
            '        """',
            '        super(InputMediaWithThumb, self).__init__(type, media, caption, parse_mode)',
            '        assert_type_or_raise(thumb, None, InputFile, unicode_type, parameter_name="thumb")',
            '        self.thumb = thumb',
            '    # end def',
            '',
            '    def get_request_data(self, var_name, full_data=False):',
            '        """',
            '        :param var_name:',
            '        :param full_data: If you want `.to_array()` with this data, ready to be sent.',
            '        :return: A tuple of `to_array()` dict and the files (:py:func:`InputFile.get_request_files()`).',
            '                 Files can be None, if no file was given, but an url or existing `file_id`.',
            '',
            '                 If `self.media` is an `InputFile` however,',
            '                 the first tuple element (either the string, or the dict\'s `[\'media\']` if `full_data=True`),',
            '                 will be set to `attach://{var_name}_media` automatically.',
            '                 If `self.thumb` is an `InputFile` however, the first tuple element\'s `[\'thumb\']`, will be set to `attach://{var_name}_thumb` automatically.',
            '        """',
            '        if not full_data:',
            '            raise ArithmeticError(\'we have a thumbnail, please use `full_data=True`.\')',
            '        # end if',
            '        file = {}',
            '        data, file_to_add = super(InputMediaWithThumb, self).get_request_data(var_name, full_data=True)',
            '        if file_to_add:',
            '            file.update(file_to_add)',
            '        # end if',
            '        data[\'thumb\'], file_to_add = self.get_inputfile_data(self.thumb, var_name, suffix=\'_thumb\')',
            '        if data[\'thumb\'] is None:',
            '            del data[\'thumb\']  # having `\'thumb\': null` in the json produces errors.',
            '        # end if',
            '        if file_to_add:',
            '            file.update(file_to_add)',
            '        # end if',
            '        return data, (file or None)',
            '        # end if',
            '    # end def',
            '',
            '    def to_array(self):',
            '        """',
            '        Serializes this InputMediaPhoto to a dictionary.',
            '',
            '        :return: dictionary representation of this object.',
            '        :rtype: dict',
            '        """',
            '        array = super(InputMediaWithThumb, self).to_array()',
            '        # \'type\' is handled by superclass',
            '        array[\'media\'] = u(self.media)  # py2: type unicode, py3: type str',
            '        if self.caption is not None:',
            '            array[\'caption\'] = u(self.caption)  # py2: type unicode, py3: type str',
            '        if self.parse_mode is not None:',
            '            array[\'parse_mode\'] = u(self.parse_mode)  # py2: type unicode, py3: type str',
            '        return array',
            '    # end def to_array',
            '',
            '    @staticmethod',
            '    def validate_array(array):',
            '        """',
            '        Builds a new array with valid values for the InputMediaPhoto constructor.',
            '',
            '        :return: new array with valid values',
            '        :rtype: dict',
            '        """',
            '        assert_type_or_raise(array, dict, parameter_name="array")',
            '        data = InputMedia.validate_array(array)',
            '        # \'type\' is handled by the superclass.',
            '        data[\'media\'] = u(array.get(\'media\'))',
            '        data[\'caption\'] = u(array.get(\'caption\')) if array.get(\'caption\') is not None else None',
            '        data[\'parse_mode\'] = u(array.get(\'parse_mode\')) if array.get(\'parse_mode\') is not None else None',
            '        return data',
            '    # end def validate_array',
            '',
            '    @staticmethod',
            '    def from_array(array):',
            '        """',
            '        Deserialize a new InputMediaWithThumb from a given dictionary.',
            '',
            '        :return: new InputMediaWithThumb instance.',
            '        :rtype: InputMediaWithThumb',
            '        """',
            '        if not array:  # None or {}',
            '            return None',
            '        # end if',
            '',
            '        data = InputMediaWithThumb.validate_array(array)',
            '        instance = InputMediaWithThumb(**data)',
            '        instance._raw = array',
            '        return instance',
            '    # end def from_array',
            '',
            '    def __str__(self):',
            '        """',
            '        Implements `str(inputmediawiththumb_instance)`',
            '        """',
            '        return "InputMediaWithThumb(type={self.type!r}, media={self.media!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r})".format(self=self)',
            '    # end def __str__',
            '',
            '    def __repr__(self):',
            '        """',
            '        Implements `repr(inputmediawiththumb_instance)`',
            '        """',
            '        if self._raw:',
            '            return "InputMediaWithThumb.from_array({self._raw})".format(self=self)',
            '        # end if',
            '        return "InputMediaWithThumb(type={self.type!r}, media={self.media!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r})".format(self=self)',
            '    # end def __repr__',
            '',
            '    def __contains__(self, key):',
            '        """',
            '        Implements `"key" in inputmediawiththumb_instance`',
            '        """',
            '        return (',
            '            key in ["type", "media", "caption", "parse_mode"]',
            '            and hasattr(self, key)',
            '            and bool(getattr(self, key, None))',
            '        )',
            '    # end def __contains__',
            '# end class InputMediaWithThumb',
       ],
        imports=[
            "pytgbot.api_types.receivable.sendable.input_media.InputMedia",
        ],
    ),
    "pytgbot.api_types.receivable.sendable.passport.PassportElementError": CustomClass(
        text=[
            'class PassportElementError(Sendable):',
            '    """',
            '    This object represents an error in the Telegram Passport element',
            '    which was submitted that should be resolved by the user.',
            '    """',
            '    pass',
            '# end class PassportElementError',
       ],
        imports=[
            "pytgbot.api_types.receivable.sendable.Sendable",
        ],
    ),
    "pytgbot.api_types.receivable.sendable.reply_markup.Button": CustomClass(
        text=[
            'class Button(Sendable):',
            '    def __init__(self):',
            '        super(Button, self).__init__()',
            '    # end def __init__',
            '# end class Button',
       ],
        imports=[
            "pytgbot.api_types.receivable.sendable.Sendable",
        ],
    ),
    "pytgbot.api_types.receivable.sendable.reply_markup.ReplyMarkup": CustomClass(
        text=[
            'class ReplyMarkup(Sendable):',
            '    def __init__(self):',
            '        super(ReplyMarkup, self).__init__()',
            '    # end def __init__',
            '# end class ReplyMarkup',
       ],
        imports=[
            "pytgbot.api_types.receivable.sendable.Sendable",
        ],
    ),
    "pytgbot.api_types.TgBotApiObject": CustomClass(
        text=[
            'class Receivable(TgBotApiObject):',
            '    pass',
            '# end class Receivable',
       ],
        imports=[
            "pytgbot.api_types.TgBotApiObject",
        ],
    ),
    "pytgbot.api_types.receivable.Result": CustomClass(
        text=[
            'class Result(Receivable):',
            '    def to_array(self):',
            '        return {}',
            '    pass',
            '# end class Result',
       ],
        imports=[
            "pytgbot.api_types.receivable.Receivable",
        ],
    ),
}
