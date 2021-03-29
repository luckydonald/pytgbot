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
    "MessageEntity":            ("pytgbot.api_types.receivable.media.", "Result", None),
    "PhotoSize":                ("pytgbot.api_types.receivable.media.", "Result", None),
    "UserProfilePhotos":        ("pytgbot.api_types.receivable.media.", "Result", None),
    "ChatPhoto":                ("pytgbot.api_types.receivable.media.", "Result", None),
    "Media":                    ("pytgbot.api_types.receivable.media.", "Receivable", None),
    "File":                     ("pytgbot.api_types.receivable.media.", "Receivable", None),
    "Voice":                    ("pytgbot.api_types.receivable.media.", "Media", None),
    "VideoNote":                ("pytgbot.api_types.receivable.media.", "Media", None),  # May 18, 2017
    "Contact":                  ("pytgbot.api_types.receivable.media.", "Media", None),
    "Location":                 ("pytgbot.api_types.receivable.media.", "Media", None),
    "Venue":                    ("pytgbot.api_types.receivable.media.", "Media", None),
    "Audio":                    ("pytgbot.api_types.receivable.media.", "Media", None),
    "Document":                 ("pytgbot.api_types.receivable.media.", "Media", None),
    "Sticker":                  ("pytgbot.api_types.receivable.media.", "Media", None),  # Moved July 21, 2017
    "Video":                    ("pytgbot.api_types.receivable.media.", "Media", None),
    "Game":                     ("pytgbot.api_types.receivable.media.", "Media", None),
    "Animation":                ("pytgbot.api_types.receivable.media.", "Media", None),
    "Poll":                     ("pytgbot.api_types.receivable.media.", "Media", None),  # April 14, 2019
    "PollOption":               ("pytgbot.api_types.receivable.media.", "Receivable", None),  # April 14, 2019
    "PollAnswer":               ("pytgbot.api_types.receivable.media.", "Receivable", None),  # January 23, 2020
    "Dice":                     ("pytgbot.api_types.receivable.media.", "Media", None),  # March 30, 2020

    # pytgbot.api_types.receivable.service.
    "ServiceMessage":                ("pytgbot.api_types.receivable.service.", "Receivable", None),  # November 4, 2020
    "ProximityAlertTriggered":       ("pytgbot.api_types.receivable.service.", "ServiceMessage", None),  # November 4, 2020
    "MessageAutoDeleteTimerChanged": ("pytgbot.api_types.receivable.service.", "ServiceMessage", None),  # March 9, 2021, (import changed November 4, 2020)
    "VoiceChatStarted":              ("pytgbot.api_types.receivable.service.", "ServiceMessage", None),  # November 4, 2020
    "VoiceChatEnded":                ("pytgbot.api_types.receivable.service.", "ServiceMessage", None),  # November 4, 2020
    "VoiceChatParticipantsInvited":  ("pytgbot.api_types.receivable.service.", "ServiceMessage", None),  # November 4, 2020

    # pytgbot.api_types.receivable.responses.*
    "MessageId":       ("pytgbot.api_types.receivable.responses.", "Result", None),  # July 29, 2019

    # pytgbot.api_types.receivable.peer.*
    "ChatMemberUpdated":  ("pytgbot.api_types.receivable.peer.", "Result", None),  # March 9, 2021
    "ChatPermissions":    ("pytgbot.api_types.receivable.peer.", "Result", None),  # July 29, 2019
    "ChatInviteLink":     ("pytgbot.api_types.receivable.peer.", "Result", None),  # March 9, 2021
    "ChatLocation":       ("pytgbot.api_types.receivable.peer.", "Result", None),  # November 4, 2020
    "ChatMember":         ("pytgbot.api_types.receivable.peer.", "Result", None),
    "Peer":               ("pytgbot.api_types.receivable.peer.", "Result", None),
    "User":               ("pytgbot.api_types.receivable.peer.", "Peer", None),
    "Chat":               ("pytgbot.api_types.receivable.peer.", "Peer", None),

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

    # pytgbot.api_types.sendable.__init__.*
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
    "InputMediaPlayable":           ("pytgbot.api_types.sendable.input_media.", "InputMediaWithThumb", None),
    "InputMediaVideolike":           ("pytgbot.api_types.sendable.input_media.", "InputMediaPlayable", None),
    "InputMediaVideo":              ("pytgbot.api_types.sendable.input_media.", "InputMediaVideolike", None),
    "InputMediaAnimation":          ("pytgbot.api_types.sendable.input_media.", "InputMediaVideolike", None),
    "InputMediaAudio":              ("pytgbot.api_types.sendable.input_media.", "InputMediaPlayable", None),
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
    "logOut":                 {'return': {'expected': '', 'replace': 'Returns True on success'}, 'r_type': {'expected': '', 'replace': 'True'}},  # November 4, 2020
    "getWebhookInfo":         {'return': {'expected': 'On success, returns a WebhookInfo object. If the bot is using getUpdates, will return an object with the url field empty', 'replace': 'On success, returns a WebhookInfo object'}, 'r_type': {'expected': 'WebhookInfo or getUpdates or url', 'replace': 'WebhookInfo'}},
    "kickChatMember":         {'return': {'expected': 'In the case of supergroups and channels, the user will not be able to return to the chat on their own using invite links, etc. Returns True on success', 'replace': 'Returns True on success'}, 'r_type': {'expected': 'True', 'replace': 'True'}},
    "unbanChatMember":        {'return': {'expected': 'The user will not return to the group or channel automatically, but will be able to join via link, etc. Returns True on success', 'replace': 'Returns True on success'}, 'r_type': {'expected': 'True', 'replace': 'True'}},
    "getChatAdministrators":  {'return': {'expected': 'On success, returns an Array of ChatMember objects that contains information about all chat administrators except other bots. If the chat is a group or a supergroup and no administrators were appointed, only the creator will be returned', 'replace': 'On success, returns an Array of ChatMember objects that contains information about all chat administrators except other bots'}, 'r_type': {'expected': 'list of ChatMember', 'replace': 'list of ChatMember'}},
    "setChatStickerSet":      {'return': {'expected': 'Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success', 'replace': 'Returns True on success'}, 'r_type': {'expected': 'can_set_sticker_set or getChat or True', 'replace': 'True'}},
    "deleteChatStickerSet":   {'return': {'expected': 'Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success', 'replace': 'Returns True on success'}, 'r_type': {'expected': 'can_set_sticker_set or getChat or True', 'replace': 'True'}},
    "setGameScore":           {'return': {'expected': "On success, if the message was sent by the bot, returns the edited Message, otherwise returns True. Returns an error, if the new score is not greater than the user's current score in the chat and force is False", 'replace': 'On success, if the message was sent by the bot, returns the edited Message, otherwise returns True'}, 'r_type': {'expected': 'Message or True or force or False', 'replace': 'Message or True'}},
    "getGameHighScores":      {'return': {'expected': 'This method will currently return scores for the target user, plus two of their closest neighbors on each side. Will also return the top three users if the user and his neighbors are not among them. Please note that this behavior is subject to change.', 'replace': 'On success, returns an Array of GameHighScore objects'}, 'r_type': {'expected': '', 'replace': 'list of GameHighScore'}},
    "setPassportDataErrors":  {'return': {'expected': 'The user will not be able to re-submit their Passport to you until the errors are fixed (the contents of the field for which you returned the error must change). Returns True on success', 'replace': 'Returns True on success'}, 'r_type': {'expected': 'True', 'replace': 'True'}},
    "sendMediaGroup":         {'return': {'expected': 'On success, an array of Messages that were sent is returned', 'replace': 'On success, an array of Messages that were sent is returned'}, 'r_type': {'expected': 'list of Messages', 'replace': 'list of Message'}},
    "answerShippingQuery":    {'return': {'expected': 'On success, True is returned', 'replace': 'On success, True is returned'}, 'r_type': {'expected': '', 'replace': 'True'}},
    "answerPreCheckoutQuery": {'return': {'expected': 'On success, True is returned', 'replace': 'On success, True is returned'}, 'r_type': {'expected': '', 'replace': 'True'}},
    "getMyCommands":          {'return': {'expected': 'Returns Array of BotCommand on success', 'replace': 'On success, an array of the commands is returned'}, 'r_type': {'expected': 'list of BotCommand', 'replace': 'list of BotCommand'}},
}
"""
Array with names of functions which have no parameters table and thus wouldn't be detected, or default replacements of stuff which just won't get parsed correctly.
"""

WHITELISTED_CLASSES = [  # Array with names of classes which have no parameters table and thus wouldn't be detected.
    # "CallbackGame",
    # "InlineQueryResult",
    # #"InputMessageContent",
    # "InputMedia",
    # "PassportElementError",
    # "InputMediaWithThumb",
    "VoiceChatStarted",
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
    "Array of InputMediaAudio, InputMediaDocument, InputMediaPhoto and InputMediaVideo": "list of InputMediaAudio | list of InputMediaDocument | list of InputMediaPhoto | list of InputMediaVideo",  # sendMediaGroup
    "Messages": "list of Message",  # sendMediaGroup
}
"""
Overrides of send function classification for teleflask.
Function "sendMessage" => "Message" will be replaced with "TextMessage".
"""

from code_generator_classes import Clazz, Variable, Type, Import, CustomClazz, ReplacementBody
from typing import Dict

# noinspection PyCompatibility,PyDictCreation
CUSTOM_CLASSES: Dict[str, CustomClazz] = {}


CUSTOM_CLASSES["pytgbot.api_types.receivable.media.Media"] = CustomClazz(
    clazz='Media',
    import_path=Import(path=CLASS_TYPE_PATHS["Media"][CLASS_TYPE_PATHS__IMPORT].rstrip('.'), name="Media"),
    imports=[
        Import(
            path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["Media"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
            name=CLASS_TYPE_PATHS["Media"][CLASS_TYPE_PATHS__PARENT]
        ),
    ],
    parent_clazz=Type(
        string=CLASS_TYPE_PATHS["Media"][CLASS_TYPE_PATHS__PARENT],
        is_builtin=False,
        always_is_value=None,
        is_list=0,
        import_path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["Media"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
        description=None
    ),
    link=None,
    description='parent class for all receivable media.',
    body=ReplacementBody(
        before=[
            'pass',
        ],
        init=[],
        to_array=[],
        validate_array=[],
        from_array=[],
        str=[],
        repr=[],
        contains=[],
        after=[],
    ),
)

CUSTOM_CLASSES["pytgbot.api_types.receivable.service.ServiceMessage"] = CustomClazz(
    clazz='ServiceMessage',
    import_path=Import(path=CLASS_TYPE_PATHS["ServiceMessage"][CLASS_TYPE_PATHS__IMPORT].rstrip('.'), name="ServiceMessage"),
    imports=[
        Import(
            path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["ServiceMessage"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
            name=CLASS_TYPE_PATHS["ServiceMessage"][CLASS_TYPE_PATHS__PARENT]
        ),
    ],
    parent_clazz=Type(
        string=CLASS_TYPE_PATHS["ServiceMessage"][CLASS_TYPE_PATHS__PARENT],
        is_builtin=False,
        always_is_value=None,
        is_list=0,
        import_path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["ServiceMessage"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
        description=None
    ),
    link=None,
    description='parent class for all service messages, those are not directly media related special attributes of the Message object.',
    body=ReplacementBody(
        before=[
            'pass',
        ],
        init=[],
        to_array=[],
        validate_array=[],
        from_array=[],
        str=[],
        repr=[],
        contains=[],
        after=[],
    ),
)

CUSTOM_CLASSES["pytgbot.api_types.receivable.peer.Peer"] = CustomClazz(
    clazz='Peer',
    import_path=Import(path=CLASS_TYPE_PATHS["Peer"][CLASS_TYPE_PATHS__IMPORT].rstrip('.'), name="Peer"),
    imports=[
        Import(
            path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["Peer"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
            name=CLASS_TYPE_PATHS["Peer"][CLASS_TYPE_PATHS__PARENT],
        ),
    ],
    parent_clazz=Type(
        string=CLASS_TYPE_PATHS["Peer"][CLASS_TYPE_PATHS__PARENT],
        is_builtin=False,
        always_is_value=None,
        is_list=0,
        import_path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["Peer"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
        description=None
    ),
    link=None,
    description='parent class for both users and chats.',
    body=ReplacementBody(
        before=[
            'pass',
        ],
        init=[],
        to_array=[],
        validate_array=[],
        from_array=[],
        str=[],
        repr=[],
        contains=[],
        after=[],
    ),
)

CUSTOM_CLASSES["pytgbot.api_types.receivable.updates.UpdateType"] = CustomClazz(
    clazz='UpdateType',
    import_path=Import(path=CLASS_TYPE_PATHS["UpdateType"][CLASS_TYPE_PATHS__IMPORT].rstrip('.'), name="UpdateType"),
    imports=[
        Import(
            path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["UpdateType"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
            name=CLASS_TYPE_PATHS["UpdateType"][CLASS_TYPE_PATHS__PARENT],
        ),
    ],
    parent_clazz=Type(
        string=CLASS_TYPE_PATHS["UpdateType"][CLASS_TYPE_PATHS__PARENT],
        is_builtin=False,
        always_is_value=None,
        is_list=0,
        import_path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["UpdateType"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
        description=None
    ),
    link=None,
    description=(
        'All extending classes are an property of the Update type.\n'
        'Like Message: Update.message'
    ),
    body=ReplacementBody(
        before=[
            'pass',
        ],
        init=[],
        to_array=[],
        validate_array=[],
        from_array=[],
        str=[],
        repr=[],
        contains=[],
        after=[],
    ),
)

CUSTOM_CLASSES["pytgbot.api_types.receivable.updates.CallbackGame"] = CustomClazz(
    clazz="CallbackGame",
    import_path=Import(path=CLASS_TYPE_PATHS["CallbackGame"][CLASS_TYPE_PATHS__IMPORT].rstrip('.'), name="CallbackGame"),
    imports=[
        Import(
            path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["CallbackGame"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
            name=CLASS_TYPE_PATHS["CallbackGame"][CLASS_TYPE_PATHS__PARENT]
        ),
    ],
    parent_clazz=Type(
        string=CLASS_TYPE_PATHS["CallbackGame"][CLASS_TYPE_PATHS__PARENT],
        is_builtin=False,
        always_is_value=None,
        is_list=0,
        import_path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["CallbackGame"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
        description=None
    ),
    link='https://core.telegram.org/bots/api#callbackgame',
    description='A placeholder, currently holds no information. Use BotFather to set up your game.',
    body=ReplacementBody(
        before=[],
        init=None,
        to_array=[
            'def to_array(self):',
            '    return {}',
            '# end def',
        ],
        validate_array=[
            '@staticmethod',
            'def validate_array(array):',
            '    return {}',
            '# end def',
        ],
        from_array=None,
        str=None,
        repr=None,
        contains=None,
        after=[],
    ),
)

CUSTOM_CLASSES["pytgbot.api_types.receivable.sendable.inline.InlineQueryResult"] = CustomClazz(
    clazz='InlineQueryResult',
    import_path=Import(path=CLASS_TYPE_PATHS["InlineQueryResult"][CLASS_TYPE_PATHS__IMPORT].rstrip('.'), name="InlineQueryResult"),
    imports=[
        Import(
            path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["InlineQueryResult"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
            name=CLASS_TYPE_PATHS["InlineQueryResult"][CLASS_TYPE_PATHS__PARENT]
        ),
    ],
    parent_clazz=Type(
        string=CLASS_TYPE_PATHS["InlineQueryResult"][CLASS_TYPE_PATHS__PARENT],
        is_builtin=False,
        always_is_value=None,
        is_list=0,
        import_path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["InlineQueryResult"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
        description=None
    ),
    link='https://core.telegram.org/bots/api#inlinequeryresult',
    description=(
        'This object represents one result of an inline query.\n'
        '\n'
        'Telegram clients currently support results of 20 types.'
    ),
    body=ReplacementBody(
        before=[],
        init=[
            'def __init__(self, id, type):',
            '    assert_type_or_raise(id, unicode_type, int, parameter_name="id")',
            '    if not isinstance(id, unicode_type):',
            '        id = u(id)',
            '    assert(isinstance(id, unicode_type))',
            '    self.id = id',
            '    self.type = type',
            '    super(InlineQueryResult, self).__init__()',
            '# end def',
        ],
        to_array=[
            'def to_array(self):',
            '    return {',
            '        "type": u(self.type),',
            '        "id": u(self.id),',
            '    }',
            '# end def to_array',
        ],
        validate_array=[],
        from_array=[],
        str=[],
        repr=[],
        contains=[],
        after=[],
    ),
)

CUSTOM_CLASSES["pytgbot.api_types.receivable.sendable.inline.InlineQueryCachedResult"] = CustomClazz(
    clazz='InlineQueryCachedResult',
    import_path=Import(path=CLASS_TYPE_PATHS["InlineQueryCachedResult"][CLASS_TYPE_PATHS__IMPORT].rstrip('.'), name="InlineQueryCachedResult"),
    imports=[
        Import(
            path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["InlineQueryCachedResult"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
            name=CLASS_TYPE_PATHS["InlineQueryCachedResult"][CLASS_TYPE_PATHS__PARENT]
        ),
    ],
    parent_clazz=Type(
        string=CLASS_TYPE_PATHS["InlineQueryCachedResult"][CLASS_TYPE_PATHS__PARENT],
        is_builtin=False,
        always_is_value=None,
        is_list=0,
        import_path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["InlineQueryCachedResult"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
        description=None
    ),
    link=None,
    description=(
        'Parent class of all those cached inline results.'
    ),
    body=ReplacementBody(
        before=[
            'pass',
        ],
        init=[],
        to_array=[],
        validate_array=[],
        from_array=[],
        str=[],
        repr=[],
        contains=[],
        after=[],
    ),
)

CUSTOM_CLASSES["pytgbot.api_types.receivable.sendable.inline.InputMessageContent"] = CustomClazz(
    clazz='InputMessageContent',
    import_path=Import(path=CLASS_TYPE_PATHS["InputMessageContent"][CLASS_TYPE_PATHS__IMPORT].rstrip('.'), name="InputMessageContent"),
    imports=[
        Import(
            path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["InputMessageContent"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
            name=CLASS_TYPE_PATHS["InputMessageContent"][CLASS_TYPE_PATHS__PARENT]
        ),
    ],
    parent_clazz=Type(
        string=CLASS_TYPE_PATHS["InputMessageContent"][CLASS_TYPE_PATHS__PARENT],
        is_builtin=False,
        always_is_value=None,
        is_list=0,
        import_path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["InputMessageContent"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
        description=None
    ),
    link=None,
    description=(
        'Parent class of all those input message content.'
    ),
    body=ReplacementBody(
        before=[
            'pass',
        ],
        init=[],
        to_array=[],
        validate_array=[],
        from_array=[],
        str=[],
        repr=[],
        contains=[],
        after=[],
    ),
)

CUSTOM_CLASSES["pytgbot.api_types.receivable.sendable.input_media.InputMedia"] = CustomClazz(
    clazz="InputMedia",
    import_path=Import(path=CLASS_TYPE_PATHS["InputMedia"][CLASS_TYPE_PATHS__IMPORT].rstrip('.'), name="InputMedia"),
    imports=[
        Import(
            path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["InputMedia"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
            name=CLASS_TYPE_PATHS["InputMedia"][CLASS_TYPE_PATHS__PARENT]
        ),
    ],
    parent_clazz=Type(
        string=CLASS_TYPE_PATHS["InputMedia"][CLASS_TYPE_PATHS__PARENT],
        is_builtin=False,
        always_is_value=None,
        is_list=0,
        import_path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["InputMedia"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
        description=None
    ),
    link='https://core.telegram.org/bots/api#inputmedia',
    description=(
        'This object represents the content of a media message to be sent.'
    ),
    parameters=[
        Variable(
            api_name='type',
            name='type',
            pytg_name=None,
            types=[
                Type(string='str', is_builtin=True, always_is_value=None, is_list=0, import_path=None, description=None),
            ],
            optional=False,
            default=None,
            description='Type of the result, a fixed value per subclass'
        ),
        Variable(
            api_name='media',
            name='media',
            pytg_name=None,
            types=[
                    Type(string='InputFile', is_builtin=False, always_is_value=None, is_list=0, import_path='pytgbot.api_types.sendable.files', description=None),
                    Type(string='str', is_builtin=True, always_is_value=None, is_list=0, import_path=None, description=None),
            ],
            optional=False,
            default=None,
            description='File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »',
            additional_allowed_type_matchings=[
                [
                    Type(string='str', is_builtin=True, always_is_value=None, is_list=0, import_path=None, description=None),
                ],
            ]
        )
    ],
    keywords=[
        Variable(
            api_name='caption',
            name='caption',
            pytg_name=None,
            types=[
                Type(string='str', is_builtin=True, always_is_value=None, is_list=0, import_path=None, description=None),
            ],
            optional=True,
            default=None,
            description='Optional. Caption of the media to be sent, 0-1024 characters after entities parsing',
        ),
        Variable(
            api_name='parse_mode',
            name='parse_mode',
            pytg_name=None,
            types=[
                  Type(string='str', is_builtin=True, always_is_value=None, is_list=0, import_path=None, description=None),
            ],
            optional=True,
            default=None,
            description='Optional. Mode for parsing entities in the photo caption. See formatting options for more details.',
        ),
        Variable(
            api_name='caption_entities',
            name='caption_entities',
            pytg_name=None,
            types=[
                Type(string='MessageEntity', is_builtin=False, always_is_value=None, is_list=1, import_path='pytgbot.api_types.receivable.media', description=None),
            ],
            optional=True,
            default=None,
            description='Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode'
        ),
    ],
    body=ReplacementBody(
        before=[],
        init=None,
        to_array=[
            'def to_array(self, prefer_original=False):',
            '    """',
            '    Serializes this InputMedia to a dictionary.',

            '    :param prefer_original: If we should return the data this was constructed with if available. If it\'s not available, it will be constructed normally from the data of the object.',
            '    :type  prefer_original: bool',
            '',
            '    :return: dictionary representation of this object.',
            '    :rtype: dict',
            '    """',
            '    if prefer_original and self._raw:',
            '        return self._raw',
            '    # end if',                                                                                                                                                                                             '    array = super(InputMedia, self).to_array()',
            '',
            '    array[\'type\'] = u(self.type)  # py2: type unicode, py3: type str',
            '    # array[\'media\'] = u(self.media)  # py2: type unicode, py3: type str',
            '    if self.caption is not None:',
            '        array[\'caption\'] = u(self.caption)  # py2: type unicode, py3: type str',
            '    # end if',
            '    if self.parse_mode is not None:',
            '        array[\'parse_mode\'] = u(self.parse_mode)  # py2: type unicode, py3: type str',
            '    # end if',
            '    if self.caption_entities is not None:',
            '        array[\'caption_entities\'] = self._as_array(self.caption_entities)  # type list of MessageEntity',
            '    # end if',
            '',
            '    return array',
            '# end def to_array',
        ],
        validate_array=[
            '@staticmethod',
            'def validate_array(array):',
            '    """',
            '    Builds a new array with valid values for the InputMedia constructor.',
            '',
            '    :return: new array with valid values',
            '    :rtype: dict',
            '    """',
            '    assert_type_or_raise(array, dict, parameter_name="array")',
            '    data = InputMedia.validate_array(array)',
            '    data[\'type\'] = u(array.get(\'type\'))',
            '    data[\'media\'] = u(array.get(\'media\'))',
            '    data[\'caption\'] = u(array.get(\'caption\')) if array.get(\'caption\') is not None else None',
            '    data[\'parse_mode\'] = u(array.get(\'parse_mode\')) if array.get(\'parse_mode\') is not None else None',
            '    return data',
            '# end def validate_array',
        ],
        from_array=[
            '@staticmethod',
            'def from_array(array):',
            '    """',
            '    Deserialize a new InputMedia from a given dictionary.',
            '',
            '    :return: new InputMedia instance.',
            '    :rtype: InputMedia',
            '    """',
            '    if not array:  # None or {}',
            '        return None',
            '    # end if',
            '',
            '    data = InputMedia.validate_array(array)',
            '    instance = InputMedia(**data)',
            '    instance._raw = array',
            '    return instance',
            '# end def from_array',
        ],
        str=None,
        repr=None,
        contains=None,
        after=[
            'def get_request_data(self, var_name, full_data=False):',
            '    """',
            '    :param var_name:',
            '    :param full_data: If you want `.to_array()` with this data, ready to be sent.',
            '    :return: A tuple of `to_array()` dict and the files (:py:func:`InputFile.get_request_files()`).',
            '             Files can be None, if no file was given, but an url or existing `file_id`.',
            '             If `media` is :py:class:`InputFile` however, the first tuple element,',
            '             media, will have [\'media\'] set to `attach://{var_name}_media` automatically.',
            '    """',
            '    if full_data:',
            '        data = self.to_array()',
            '        data[\'media\'], file = self.get_inputfile_data(self.media, var_name, suffix=\'_media\')',
            '        return data, file',
            '    # end if',
            '    return self.get_inputfile_data(self.media, var_name, suffix=\'_media\')',
            '# end def get_request_data',
            '',
            '@staticmethod',
            'def get_inputfile_data(media, var_name, suffix=\'_media\'):',
            '    name = "{var_name}{suffix}".format(var_name=var_name, suffix=suffix)',
            '    if isinstance(media, InputFile):',
            '        # is file to be uploaded',
            '        string = \'attach://{name}\'.format(name=name)',
            '        return string, media.get_request_files(name)',
            '    else:',
            '        # is no upload',
            '        return media, None',
            '    # end if',
            '# end def get_inputfile_data',
        ],
    ),
)
CUSTOM_CLASSES["pytgbot.api_types.receivable.sendable.input_media.InputMedia"].body=ReplacementBody(
    before=CUSTOM_CLASSES["pytgbot.api_types.receivable.sendable.input_media.InputMedia"].body.before,
    init=None, to_array=None, validate_array=None, from_array=None, str=None, repr=None, contains=None,
    after=CUSTOM_CLASSES["pytgbot.api_types.receivable.sendable.input_media.InputMedia"].body.after,
)

CUSTOM_CLASSES["pytgbot.api_types.receivable.sendable.input_media.InputMediaWithThumb"] = CustomClazz(
    clazz="InputMediaWithThumb",
    import_path=Import(path=CLASS_TYPE_PATHS["InputMediaWithThumb"][CLASS_TYPE_PATHS__IMPORT].rstrip('.'), name="InputMediaWithThumb"),
    imports=[
        Import(
            path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["InputMediaWithThumb"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
            name=CLASS_TYPE_PATHS["InputMediaWithThumb"][CLASS_TYPE_PATHS__PARENT]
        ),
    ],
    parent_clazz=Type(
        string=CLASS_TYPE_PATHS["InputMediaWithThumb"][CLASS_TYPE_PATHS__PARENT],
        is_builtin=False,
        always_is_value=None,
        is_list=0,
        import_path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["InputMediaWithThumb"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
        description=None
    ),
    link='https://core.telegram.org/bots/api#inputmedia',
    description=(
        'InputMedia but with a thumb field.'
    ),
    parameters=[arg.clone() for arg in CUSTOM_CLASSES["pytgbot.api_types.receivable.sendable.input_media.InputMedia"].parameters] + [
        Variable(
            api_name='thumb',
            name='thumb',
            pytg_name=None,
            optional=True,
            types=[
                Type(string='InputFile', is_builtin=False, always_is_value=None, is_list=0, import_path='pytgbot.api_types.sendable.files', description=None),
                Type(string='str', is_builtin=True, always_is_value=None, is_list=0, import_path=None, description=None),
            ],
            description='Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail\'s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can\'t be reused and can be only uploaded as a new file.'
        ),
    ],
    keywords=[kwarg.clone() for kwarg in CUSTOM_CLASSES["pytgbot.api_types.receivable.sendable.input_media.InputMedia"].keywords],
    body=ReplacementBody(
        before=[
            'def get_request_data(self, var_name, full_data=False):',
            '    """',
            '    :param var_name:',
            '    :param full_data: If you want `.to_array()` with this data, ready to be sent.',
            '    :return: A tuple of `to_array()` dict and the files (:py:func:`InputFile.get_request_files()`).',
            '             Files can be None, if no file was given, but an url or existing `file_id`.',
            '',
            '             If `self.media` is an `InputFile` however,',
            '             the first tuple element (either the string, or the dict\'s `[\'media\']` if `full_data=True`),',
            '             will be set to `attach://{var_name}_media` automatically.',
            '             If `self.thumb` is an `InputFile` however, the first tuple element\'s `[\'thumb\']`, will be set to `attach://{var_name}_thumb` automatically.',
            '    """',
            '    if not full_data:',
            '        raise ArithmeticError(\'we have a thumbnail, please use `full_data=True`.\')',
            '    # end if',
            '    file = {}',
            '    data, file_to_add = super(InputMediaWithThumb, self).get_request_data(var_name, full_data=True)',
            '    if file_to_add:',
            '        file.update(file_to_add)',
            '    # end if',
            '    data[\'thumb\'], file_to_add = self.get_inputfile_data(self.thumb, var_name, suffix=\'_thumb\')',
            '    if data[\'thumb\'] is None:',
            '        del data[\'thumb\']  # having `\'thumb\': null` in the json produces errors.',
            '    # end if',
            '    if file_to_add:',
            '        file.update(file_to_add)',
            '    # end if',
            '    return data, (file or None)',
            '    # end if',
            '# end def',
        ],
        init=None,
        to_array=[
            'def to_array(self):',
            '    """',
            '    Serializes this InputMediaWithThumb to a dictionary.',
            '',
            '    :return: dictionary representation of this object.',
            '    :rtype: dict',
            '    """',
            '    array = super(InputMediaWithThumb, self).to_array()',
            '    # \'type\' is handled by superclass',
            '    array[\'media\'] = u(self.media)  # py2: type unicode, py3: type str',
            '    if self.caption is not None:',
            '        array[\'caption\'] = u(self.caption)  # py2: type unicode, py3: type str',
            '    if self.parse_mode is not None:',
            '        array[\'parse_mode\'] = u(self.parse_mode)  # py2: type unicode, py3: type str',
            '    return array',
            '# end def to_array',
        ],
        validate_array=[
            '@staticmethod',
            'def validate_array(array):',
            '    """',
            '    Builds a new array with valid values for the InputMediaWithThumb constructor.',
            '',
            '    :return: new array with valid values',
            '    :rtype: dict',
            '    """',
            '    assert_type_or_raise(array, dict, parameter_name="array")',
            '    data = InputMedia.validate_array(array)',
            '    # \'type\' is handled by the superclass.',
            '    data[\'media\'] = u(array.get(\'media\'))',
            '    data[\'caption\'] = u(array.get(\'caption\')) if array.get(\'caption\') is not None else None',
            '    data[\'parse_mode\'] = u(array.get(\'parse_mode\')) if array.get(\'parse_mode\') is not None else None',
            '    return data',
            '# end def validate_array',

        ],
        from_array=[
            '@staticmethod',
            'def from_array(array):',
            '    """',
            '    Deserialize a new InputMediaWithThumb from a given dictionary.',
            '',
            '    :return: new InputMediaWithThumb instance.',
            '    :rtype: InputMediaWithThumb',
            '    """',
            '    if not array:  # None or {}',
            '        return None',
            '    # end if',
            '',
            '    data = InputMediaWithThumb.validate_array(array)',
            '    instance = InputMediaWithThumb(**data)',
            '    instance._raw = array',
            '    return instance',
            '# end def from_array',

        ],
        str=None,
        repr=None,
        contains=None,
        after=[],
    ),
)
# CUSTOM_CLASSES["pytgbot.api_types.receivable.sendable.input_media.InputMediaWithThumb"].body=ReplacementBody(
#     before=CUSTOM_CLASSES["pytgbot.api_types.receivable.sendable.input_media.InputMediaWithThumb"].body.before,
#     init=None, to_array=None, validate_array=None, from_array=None, str=None, repr=None, contains=None,
#     after=CUSTOM_CLASSES["pytgbot.api_types.receivable.sendable.input_media.InputMediaWithThumb"].body.after,
# )


CUSTOM_CLASSES["pytgbot.api_types.receivable.sendable.input_media.InputMediaPlayable"] = CustomClazz(
    clazz="InputMediaPlayable",
    import_path=Import(path=CLASS_TYPE_PATHS["InputMediaPlayable"][CLASS_TYPE_PATHS__IMPORT].rstrip('.'), name="InputMediaPlayable"),
    imports=[
        Import(
            path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["InputMediaPlayable"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
            name=CLASS_TYPE_PATHS["InputMediaPlayable"][CLASS_TYPE_PATHS__PARENT]
        ),
    ],
    parent_clazz=Type(
        string=CLASS_TYPE_PATHS["InputMediaPlayable"][CLASS_TYPE_PATHS__PARENT],
        is_builtin=False,
        always_is_value=None,
        is_list=0,
        import_path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["InputMediaPlayable"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
        description=None
    ),
    link='https://core.telegram.org/bots/api#inputmedia',
    description=(
        'InputMedia with a thumb and duration.'
    ),
    parameters=[arg.clone() for arg in CUSTOM_CLASSES["pytgbot.api_types.receivable.sendable.input_media.InputMediaWithThumb"].parameters] + [
        Variable(
            api_name='duration',
            name='duration',
            pytg_name=None,
            types=[
                Type(string='int', is_builtin=True, always_is_value=None, is_list=0, import_path=None, description=None),
            ],
            optional=True,
            default=None,
            description='Optional. Duration of the media',
        ),
    ],
    keywords=[kwarg.clone() for kwarg in CUSTOM_CLASSES["pytgbot.api_types.receivable.sendable.input_media.InputMediaWithThumb"].keywords],
    body=None,
)

CUSTOM_CLASSES["pytgbot.api_types.receivable.sendable.input_media.InputMediaVideolike"] = CustomClazz(
    clazz='InputMediaVideolike',
    import_path=Import(path=CLASS_TYPE_PATHS["InputMediaVideolike"][CLASS_TYPE_PATHS__IMPORT].rstrip('.'), name="InputMediaVideolike"),
    imports=[
        Import(
            path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["InputMediaVideolike"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
            name=CLASS_TYPE_PATHS["InputMediaVideolike"][CLASS_TYPE_PATHS__PARENT]
        ),
    ],
    parent_clazz=Type(
        string=CLASS_TYPE_PATHS["InputMediaVideolike"][CLASS_TYPE_PATHS__PARENT],
        is_builtin=False,
        always_is_value=None,
        is_list=0,
        import_path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["InputMediaVideolike"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
        description=None
    ),
    link='https://core.telegram.org/bots/api#inputmedia',
    description=(
        'This object represents the content of a media message to be sent.'
    ),
    parameters=[arg.clone() for arg in CUSTOM_CLASSES["pytgbot.api_types.receivable.sendable.input_media.InputMediaPlayable"].parameters] + [
        Variable(
            api_name='width',
            name='width',
            pytg_name=None,
            types=[
                Type(string='int', is_builtin=True, always_is_value=None, is_list=0, import_path=None, description=None),
            ],
            optional=True,
            default=None,
            description='Optional. Media width',
        ),
        Variable(
            api_name='height',
            name='height',
            pytg_name=None,
            types=[
                Type(string='int', is_builtin=True, always_is_value=None, is_list=0, import_path=None, description=None),
            ],
            optional=True,
            default=None,
            description='Optional. Media height',
        ),
    ],
    keywords=[kwarg.clone() for kwarg in CUSTOM_CLASSES["pytgbot.api_types.receivable.sendable.input_media.InputMediaPlayable"].keywords],
    body=None,
)

CUSTOM_CLASSES["pytgbot.api_types.receivable.sendable.passport.PassportElementError"] = CustomClazz(
    clazz='PassportElementError',
    import_path=Import(path=CLASS_TYPE_PATHS["PassportElementError"][CLASS_TYPE_PATHS__IMPORT].rstrip('.'), name="PassportElementError"),
    imports=[
        Import(
            path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["PassportElementError"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
            name=CLASS_TYPE_PATHS["PassportElementError"][CLASS_TYPE_PATHS__PARENT]
        ),
    ],
    parent_clazz=Type(
        string=CLASS_TYPE_PATHS["PassportElementError"][CLASS_TYPE_PATHS__PARENT],
        is_builtin=False,
        always_is_value=None,
        is_list=0,
        import_path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["PassportElementError"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
        description=None
    ),
    link='https://core.telegram.org/bots/api#inputmedia',
    description=(
        'This object represents an error in the Telegram Passport element which was submitted that should be resolved by the user.'
    ),
    parameters=[],
    keywords=[],
    body=ReplacementBody(
        before=[
            'pass',
        ],
        init=[],
        to_array=[],
        validate_array=[],
        from_array=[],
        str=[],
        repr=[],
        contains=[],
        after=[],
    ),
)

CUSTOM_CLASSES["pytgbot.api_types.receivable.sendable.reply_markup.Button"] = CustomClazz(
    clazz='Button',
    import_path=Import(path=CLASS_TYPE_PATHS["Button"][CLASS_TYPE_PATHS__IMPORT].rstrip('.'), name="Button"),
    imports=[
        Import(
            path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["Button"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
            name=CLASS_TYPE_PATHS["Button"][CLASS_TYPE_PATHS__PARENT]
        ),
    ],
    parent_clazz=Type(
        string=CLASS_TYPE_PATHS["Button"][CLASS_TYPE_PATHS__PARENT],
        is_builtin=False,
        always_is_value=None,
        is_list=0,
        import_path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["Button"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
        description=None
    ),
    link=None,
    description=(
        'Class for grouping KeyboardButton, KeyboardButtonPollType and InlineKeyboardButton.'
    ),
    parameters=[],
    keywords=[],
    body=ReplacementBody(
        before=[],
        init=[
            'def __init__(self):',
            '    super(Button, self).__init__()',
            '# end def __init__',
        ],
        to_array=[],
        validate_array=[],
        from_array=[],
        str=[],
        repr=[],
        contains=[],
        after=[],
    ),
)

CUSTOM_CLASSES["pytgbot.api_types.receivable.sendable.reply_markup.ReplyMarkup"] = CustomClazz(
    clazz='ReplyMarkup',
    import_path=Import(path=CLASS_TYPE_PATHS["ReplyMarkup"][CLASS_TYPE_PATHS__IMPORT].rstrip('.'), name="ReplyMarkup"),
    imports=[
        Import(
            path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["ReplyMarkup"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
            name=CLASS_TYPE_PATHS["ReplyMarkup"][CLASS_TYPE_PATHS__PARENT]
        ),
    ],
    parent_clazz=Type(
        string=CLASS_TYPE_PATHS["ReplyMarkup"][CLASS_TYPE_PATHS__PARENT],
        is_builtin=False,
        always_is_value=None,
        is_list=0,
        import_path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["ReplyMarkup"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
        description=None
    ),
    link=None,
    description=(
        'Class for grouping ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup and ForceReply.'
    ),
    parameters=[],
    keywords=[],
    body=ReplacementBody(
        before=[],
        init=[
            'def __init__(self):',
            '    super(ReplyMarkup, self).__init__()',
            '# end def __init__',
        ],
        to_array=[],
        validate_array=[],
        from_array=[],
        str=[],
        repr=[],
        contains=[],
        after=[],
    ),
)

CUSTOM_CLASSES["pytgbot.api_types.receivable.Receivable"] = CustomClazz(
    clazz='Receivable',
    import_path=Import(path=CLASS_TYPE_PATHS["Receivable"][CLASS_TYPE_PATHS__IMPORT].rstrip('.'), name="Receivable", is_init=True),
    imports=[
        Import(
            path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["Receivable"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
            name=CLASS_TYPE_PATHS["Receivable"][CLASS_TYPE_PATHS__PARENT]
        ),
    ],
    parent_clazz=Type(
        string=CLASS_TYPE_PATHS["Receivable"][CLASS_TYPE_PATHS__PARENT],
        is_builtin=False,
        always_is_value=None,
        is_list=0,
        import_path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["Receivable"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
        description=None
    ),
    link=None,
    description=(
        'Base class for all classes for stuff which telegram sends us.'
    ),
    parameters=[],
    keywords=[],
    body=ReplacementBody(
        before=[
            'pass',
        ],
        init=[],
        to_array=[],
        validate_array=[],
        from_array=[],
        str=[],
        repr=[],
        contains=[],
        after=[],
    ),
)


CUSTOM_CLASSES["pytgbot.api_types.receivable.Receivable"] = CustomClazz(
    clazz='Receivable',
    import_path=Import(path=CLASS_TYPE_PATHS["Receivable"][CLASS_TYPE_PATHS__IMPORT].rstrip('.'), name="Receivable", is_init=True),
    imports=[
        Import(
            path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["Receivable"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
            name=CLASS_TYPE_PATHS["Receivable"][CLASS_TYPE_PATHS__PARENT]
        ),
    ],
    parent_clazz=Type(
        string=CLASS_TYPE_PATHS["Receivable"][CLASS_TYPE_PATHS__PARENT],
        is_builtin=False,
        always_is_value=None,
        is_list=0,
        import_path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["Receivable"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
        description=None
    ),
    link=None,
    description=(
        'Base class for all classes for stuff which telegram sends us.'
    ),
    parameters=[],
    keywords=[],
    body=ReplacementBody(
        before=[
            'pass',
        ],
        init=[],
        to_array=[],
        validate_array=[],
        from_array=[],
        str=[],
        repr=[],
        contains=[],
        after=[],
    ),
)

CUSTOM_CLASSES["pytgbot.api_types.sendable.Sendable"] = CustomClazz(
    clazz='Sendable',
    import_path=Import(path=CLASS_TYPE_PATHS["Sendable"][CLASS_TYPE_PATHS__IMPORT].rstrip('.'), name="Sendable", is_init=True),
    imports=[
        Import(
            path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["Sendable"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
            name=CLASS_TYPE_PATHS["Sendable"][CLASS_TYPE_PATHS__PARENT]
        ),
    ],
    parent_clazz=Type(
        string=CLASS_TYPE_PATHS["Sendable"][CLASS_TYPE_PATHS__PARENT],
        is_builtin=False,
        always_is_value=None,
        is_list=0,
        import_path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["Sendable"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
        description=None
    ),
    link=None,
    description=(
        'Base class for all classes for stuff which we throw in requests towards the telegram servers.'
    ),
    parameters=[],
    keywords=[],
    body=ReplacementBody(
        before=[
            "pass",
        ],
        init=[],
        to_array=[],
        validate_array=[],
        from_array=[],
        str=[],
        repr=[],
        contains=[],
        after=[],
    ),
)

CUSTOM_CLASSES["pytgbot.api_types.receivable.Result"] = CustomClazz(
    clazz='Result',
    import_path=Import(path=CLASS_TYPE_PATHS["Result"][CLASS_TYPE_PATHS__IMPORT].rstrip('.'), name="Result", is_init=True),
    imports=[
        Import(
            path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["Result"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
            name=CLASS_TYPE_PATHS["Result"][CLASS_TYPE_PATHS__PARENT]
        ),
    ],
    parent_clazz=Type(
        string=CLASS_TYPE_PATHS["Result"][CLASS_TYPE_PATHS__PARENT],
        is_builtin=False,
        always_is_value=None,
        is_list=0,
        import_path=CLASS_TYPE_PATHS[CLASS_TYPE_PATHS["Result"][CLASS_TYPE_PATHS__PARENT]][CLASS_TYPE_PATHS__IMPORT].rstrip('.'),
        description=None
    ),
    link=None,
    description=(
        'Base class for all classes for stuff which we throw in requests towards the telegram servers.'
    ),
    parameters=[],
    keywords=[],
    body=ReplacementBody(
        before=[
            "pass",
        ],
        init=[],
        to_array=[],
        validate_array=[],
        from_array=[],
        str=[],
        repr=[],
        contains=[],
        after=[],
    ),
)

CUSTOM_CLASSES["pytgbot.api_types.TgBotApiObject"] = CustomClazz(
    clazz='TgBotApiObject',
    import_path=Import(path=CLASS_TYPE_PATHS["TgBotApiObject"][CLASS_TYPE_PATHS__IMPORT].rstrip('.'), name="TgBotApiObject", is_init=True),
    imports=[],
    parent_clazz=Type(
        string='object',
        is_builtin=True,
        always_is_value=None,
        is_list=0,
        import_path=None,
        description=None
    ),
    link=None,
    description=(
        'Base class for every api object class.'
    ),
    parameters=[],
    keywords=[],
    body=ReplacementBody(
        before=[
            'def __init__(self):',
            '    self._raw = None',
            '    super(TgBotApiObject, self).__init__()',
            '# end def __init__',
            '',
            'def to_array(self):',
            '    array = dict()',
            '    return array',
            '# end def to_array',
            '',
            '@staticmethod',
            'def from_array(array):',
            '    if not array:',
            '        return None',
            '    return {}',
            '# end def',
            '',
            '# # # # # # # # # # # # # #',
            '# helper functions below #',
            '# # # # # # # # # # # # #',
            '',
            '@classmethod',
            'def from_array_list(cls, result, list_level):',
            '    """',
            '    Tries to parse the `result` as type given in `required_type`, while traversing into lists as often as specified in `list_level`.',
            '',
            '    :param cls: Type as what it should be parsed as. Can be any class extending :class:`TgBotApiObject`.',
            '                E.g. If you call `Class.from_array_list`, it will automatically be set to `Class`.',
            '    :type  cls: class',
            ','
            '    :param result: The result to parse',
            ','
            '    :param list_level: "list of" * list_level',
            '    :type  list_level: int',
            ','
            '    :return: the result as `required_type` type',
            '    """',
            '    return from_array_list(cls, result, list_level, is_builtin=False)  # the one below, not itself. Yes, same name...',
            '# end def from_array_list',
            '',
            '@staticmethod',
            'def _builtin_from_array_list(required_type, value, list_level):',
            '    """',
            '    Helper method to make :func:`from_array_list` available to all classes extending this,',
            '    without the need for additional imports.',
            '',
            '    :param required_type: Type as what it should be parsed as. Any builtin.',
            '    :param value: The result to parse',
            '    :param list_level: "list of" * list_level',
            '    :return:',
            '    """',
            '    return from_array_list(required_type, value, list_level, is_builtin=True)',
            '# end def _builtin_from_array_list',
            '',
            '@staticmethod',
            'def _as_array(obj):',
            '    """',
            '    Helper method to make :func:`as_array` available to all classes extending this,',
            '    without the need for additional imports.',
            '    """',
            '    return as_array(obj)',
            '# end def',
            '',
            'def __setattr__(self, key, value):',
            '    """',
            '    Remove `self._raw` if any other value is set.',
            '    """',
            '    super(TgBotApiObject, self).__setattr__(key, value)',
            '    if not key.startswith(\'_\') and hasattr(self, \'_raw\') and self._raw is not None:',
            '        self._raw = None',
            '    # end if',
            '# end def',
        ],
        init=[],
        to_array=[],
        validate_array=[],
        from_array=[],
        str=[],
        repr=[],
        contains=[],
        after=[],
    ),
)
