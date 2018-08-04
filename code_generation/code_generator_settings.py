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
    "VideoNote":            ("pytgbot.api_types.receivable.media.", "Media", None), # May 18, 2017
    "Contact":              ("pytgbot.api_types.receivable.media.", "Media", None),
    "Location":             ("pytgbot.api_types.receivable.media.", "Media", None),
    "Venue":                ("pytgbot.api_types.receivable.media.", "Media", None),
    "Audio":                ("pytgbot.api_types.receivable.media.", "Media", None),
    "Document":             ("pytgbot.api_types.receivable.media.", "Media", None),
    "Sticker":              ("pytgbot.api_types.receivable.media.", "Media", None), # Moved July 21, 2017
    "Video":                ("pytgbot.api_types.receivable.media.", "Media", None),
    "Game":                 ("pytgbot.api_types.receivable.media.", "Media", None),
    "Animation":            ("pytgbot.api_types.receivable.media.", "Media", None),

    # pytgbot.api_types.receivable.responses.*

    # pytgbot.api_types.receivable.peer.*
    "ChatMember":   ("pytgbot.api_types.receivable.peer.", "Result", None),
    "Peer":         ("pytgbot.api_types.receivable.peer.", "Result", None),
    "User":         ("pytgbot.api_types.receivable.peer.", "Peer", None),
    "Chat":         ("pytgbot.api_types.receivable.peer.", "Peer", None),

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
    "InputMediaVideo":              ("pytgbot.api_types.sendable.input_media.", "InputMedia", None),
    "InputMediaAnimation":          ("pytgbot.api_types.sendable.input_media.", "InputMedia", None),
    "InputMediaAudio":              ("pytgbot.api_types.sendable.input_media.", "InputMedia", None),
    "InputMediaDocument":           ("pytgbot.api_types.sendable.input_media.", "InputMedia", None),

    # pytgbot.api_types.sendable.reply_markup.*
    "Button":               ("pytgbot.api_types.sendable.reply_markup.", "Sendable", None),
    "ReplyMarkup":          ("pytgbot.api_types.sendable.reply_markup.", "Sendable", None),
    "ReplyKeyboardMarkup":  ("pytgbot.api_types.sendable.reply_markup.", "ReplyMarkup", None),
    "ReplyKeyboardRemove":  ("pytgbot.api_types.sendable.reply_markup.", "ReplyMarkup", None),
    "ForceReply":           ("pytgbot.api_types.sendable.reply_markup.", "ReplyMarkup", None),
    "InlineKeyboardMarkup": ("pytgbot.api_types.sendable.reply_markup.", "ReplyMarkup", None),
    "KeyboardButton":       ("pytgbot.api_types.sendable.reply_markup.", "Button", None),
    "InlineKeyboardButton": ("pytgbot.api_types.sendable.reply_markup.", "Button", None),

    # pytgbot.api_types.sendable.payments.*
    "LabeledPrice":     ("pytgbot.api_types.sendable.payments.", "Sendable", None),  # May 18, 2017
    "ShippingOption":   ("pytgbot.api_types.sendable.payments.", "Sendable", None),  # May 18, 2017


    # pytgbot.api_types.sendable.passport.*
    "PassportElementError":            ("pytgbot.api_types.sendable.passport.", "Sendable", None),  # July 26, 2018
    "PassportElementErrorDataField":   ("pytgbot.api_types.sendable.passport.", "PassportElementError", None),  # July 26, 2018
    "PassportElementErrorFrontSide":   ("pytgbot.api_types.sendable.passport.", "PassportElementError", None),  # July 26, 2018
    "PassportElementErrorReverseSide": ("pytgbot.api_types.sendable.passport.", "PassportElementError", None),  # July 26, 2018
    "PassportElementErrorSelfie":      ("pytgbot.api_types.sendable.passport.", "PassportElementError", None),  # July 26, 2018
    "PassportElementErrorFile":        ("pytgbot.api_types.sendable.passport.", "PassportElementError", None),  # July 26, 2018
    "PassportElementErrorFiles":       ("pytgbot.api_types.sendable.passport.", "PassportElementError", None),  # July 26, 2018
}

WHITELISTED_FUNCS = {  # Array with names of functions which have no parameters table and thus wouldn't be detected, or default replacements of stuff which just won't get parsed correctly.
    # "func": {'return': {'expected': '', 'replace': ''}, 'r_type': {'expected': '', 'replace': ''}},
    "getMe":                 {'return': {'expected': '', 'replace': 'Returns basic information about the bot in form of a User object'}, 'r_type': {'expected': '', 'replace': 'User'}},
    "deleteWebhook":         {'return': {'expected': '', 'replace': 'Returns True on success'}, 'r_type': {'expected': '', 'replace': 'True'}},
    "getWebhookInfo":        {'return': {'expected': 'On success, returns a WebhookInfo object. If the bot is using getUpdates, will return an object with the url field empty', 'replace': 'On success, returns a WebhookInfo object'}, 'r_type': {'expected': 'WebhookInfo or getUpdates or url', 'replace': 'WebhookInfo'}},
    "kickChatMember":        {'return': {'expected': 'In the case of supergroups and channels, the user will not be able to return to the group on their own using invite links, etc. Returns True on success', 'replace': 'Returns True on success'}, 'r_type': {'expected': 'True', 'replace': 'True'}},
    "unbanChatMember":       {'return': {'expected': 'The user will not return to the group or channel automatically, but will be able to join via link, etc. Returns True on success', 'replace': 'Returns True on success'}, 'r_type': {'expected': 'True', 'replace': 'True'}},
    "getChatAdministrators": {'return': {'expected': 'On success, returns an Array of ChatMember objects that contains information about all chat administrators except other bots. If the chat is a group or a supergroup and no administrators were appointed, only the creator will be returned', 'replace': 'On success, returns an Array of ChatMember objects that contains information about all chat administrators except other bots'}, 'r_type': {'expected': 'list of ChatMember', 'replace': 'list of ChatMember'}},
    "setChatStickerSet":     {'return': {'expected': 'Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success', 'replace': 'Returns True on success'}, 'r_type': {'expected': 'can_set_sticker_set or getChat or True', 'replace': 'True'}},
    "deleteChatStickerSet":  {'return': {'expected': 'Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success', 'replace': 'Returns True on success'}, 'r_type': {'expected': 'can_set_sticker_set or getChat or True', 'replace': 'True'}},
    "setGameScore":          {'return': {'expected': "On success, if the message was sent by the bot, returns the edited Message, otherwise returns True. Returns an error, if the new score is not greater than the user's current score in the chat and force is False", 'replace': 'On success, if the message was sent by the bot, returns the edited Message, otherwise returns True'}, 'r_type': {'expected': 'Message or True or force or False', 'replace': 'Message or True'}},
    "getGameHighScores":     {'return': {'expected': 'This method will currently return scores for the target user, plus two of his closest neighbors on each side. Will also return the top three users if the user and his neighbors are not among them. Please note that this behavior is subject to change.', 'replace': 'On success, returns an Array of GameHighScore objects'}, 'r_type': {'expected': '', 'replace': 'list of GameHighScore'}},
    "setPassportDataErrors": {'return': {'expected': 'The user will not be able to re-submit their Passport to you until the errors are fixed (the contents of the field for which you returned the error must change). Returns True on success', 'replace': 'Returns True on success'}, 'r_type': {'expected': 'True', 'replace': 'True'}},
}
WHITELISTED_CLASSES = [  # Array with names of classes which have no parameters table and thus wouldn't be detected.
    "CallbackGame",
    "InlineQueryResult",
    "InputMedia",
    "PassportElementError",
]

"""
You can either pass a file_id as String to resend a photo
                      file that is already on the Telegram servers (recommended),
                      pass an HTTP URL as a String for Telegram to get a photo from the Internet,
                      or upload a new photo, by specifying the file path as
                      :class:`InputFile <pytgbot/pytgbot.api_types.sendable.files.InputFile>`.
                      

"""

#list of GameHighScore