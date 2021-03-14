# Changelog

## Version 5.1 (not released yet)
⚠️ Breaking changes:
- ⚠️ Moved `ProximityAlertTriggered` from `pytgbot.api_types.receiveable.media.ProximityAlertTriggered` to `pytgbot.api_types.receiveable.services.ProximityAlertTriggered`. It also no longer subclasses `receiveable.media.Media`, but a new `receiveable.services.ServiceMessage`
    - there should be a import from the old location making that backwards compatible, but that's not something you should depend on as we will remove it in a newer version.

Random observations:
- `id`: This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
- polls can have 45 more letters now

## Version 5.0.0.1
Added `download_url` parameter to the constructor of the `Bot`s, so one can set the download url for non-official API servers.
Those might be different for a selfhosted server.
If that is not given but only a `base_url` is, we'll try to guess it but show a warning.
That is used in `get_download_url(…)`.

## Version 5.0.0
Fixed syntax error in `get_download_url(…)`.
Also cut a stable release (too early again).

## Version 5.0b4
Fixed Sync bot not resolving username and id correctly.

## Version 5.0b3
Fixed importing the wrong bot, the async one, per default.

## Version 5.0.0b2
This is a re-release of `5.0.0-beta.1`, as PyPi did like that short version format better.
Other than the version number it is exactly the same as `5.0.0-beta.1`.

## Version 5.0.0-beta.1
Core:
- The already for a while now deprecated `pytgbot.api_types.sendable.InputFile`, `pytgbot.api_types.sendable.InputFileFromURL` and `pytgbot.api_types.sendable.InputFileFromDisk` can no longer be found in `pytgbot.api_types.sendable.\*`
  They are now only available at `pytgbot.api_types.sendable.files.\*`, resulting in
  - `pytgbot.api_types.sendable.files.InputFile`,
  - `pytgbot.api_types.sendable.files.InputFileFromURL` and
  - `pytgbot.api_types.sendable.files.InputFileFromDisk`.
- `.as_array()` now has a `prefer_original=False` boolean, if it should return the data this was constructed with if available. Otherwise, it will be constructed normally from the data of the object, as it was before.

Licence:
- Switched from GPL to LGPL.

## Version 4.9.1
- Fixed `pytgbot.bot` not being part of the pip release.

## Version 4.9
- Make exceptions inherit from Exception and not BaseException.
- Added Updates from the Bot API 4.9, including:
    - Added StickerSet.thumb.
    - Added Dice
    - Shifting around of argument order in Message.
    - Also adds Message.via_bot, Message.dice.
    - Added InlineQueryResultGif
    .thumb_mime_type.
    - Added InlineQueryResultMpeg4Gif.thumb_mime_type.
    - Added Bot.set_sticker_set_thumb(…)
    - Added Bot.get_my_commands(…)

## Version 4.6.1
- Added `language` to `MessageEntity` for real now.
- Added `poll_answer` to `Update` as well.

## Version 4.6
- Added API definitions of v4.6, (January 23, 2020) with the following changelog:
    - Supported [Polls 2.0](https://telegram.org/blog/polls-2-0-vmq).
    - Added the ability to send non-anonymous, multiple answer, and quiz-style polls: added the parameters `is_anonymous`, `type`, `allows_multiple_answers`, `correct_option_id`, `is_closed` options to the method `sendPoll`.
    - Added the object `KeyboardButtonPollType` and the field `request_poll` to the object `KeyboardButton`.
    - Added updates about changes of user answers in non-anonymous polls, represented by the object `PollAnswer` and the field `poll_answer` in the `Update` object.
    - Added the fields `total_voter_count`, `is_anonymous`, `type`, `allows_multiple_answers`, `correct_option_id` to the `Poll` object.
    - Bots can now send polls to private chats.
    - Added more information about the bot in response to the `getMe` request: added the fields `can_join_groups`, `can_read_all_group_messages` and `supports_inline_queries` to the User object.
    - Added the optional field `language` to the `MessageEntity` object.
- The new stuff:
    - New Fields:
        - `pytgbot.api_types.receivable.media.MessageEntity`: `language`
        - `pytgbot.api_types.receivable.media.Poll`: `total_voter_count`, `is_closed`, `is_anonymous`, `type`, `allows_multiple_answers` and `correct_option_id`
        - `pytgbot.api_types.receivable.updates.Update`: `poll_answer`
        - `pytgbot.api_types.sendable.reply_markup.KeyboardButton`: `request_poll`
        - `pytgbot.api_types.receivable.peer.User`: `can_join_groups`, `can_read_all_group_messages`, `supports_inline_queries`
        - `pytgbot.api_types.receivable.peer.Chat`: `slow_mode_delay`
        - `pytgbot.api_types.receivable.peer.ChatMember`: `custom_title`
    - New Arguments:
        - `pytgbot.bot.Bot.get_me`:
    - New Classes:
        - `pytgbot.api_types.sendable.reply_markup.KeyboardButtonPollType`
        - `pytgbot.api_types.receivable.media.PollAnswer`


## Version 4.5.2
- Fixed failing to merge the `file_unique_id` field into the media constructors.

## Version 4.5.1
This is a re-release of `4.5.0` as I thought it didn't upload correctly
## Version 4.5.0
- Updated API definitions of v4.5, (December 31th, 2019) with the following changelog:
    - <kbd>(not affected)</kbd> Added support for two new MessageEntity types, underline and strikethrough.
    Added support for nested MessageEntity objects. Entities can now contain other entities. If two entities have common characters then one of them is fully contained inside the other.
    - <kbd>(not affected)</kbd> Added support for nested entities and the new tags <u>/<ins> (for underlined text) and <s>/<strike>/<del> (for strikethrough text) in parse mode HTML.
    - <kbd>(not affected)</kbd> Added a new parse mode, MarkdownV2, which supports nested entities and two new entities __ (for underlined text) and ~ (for strikethrough text). Parse mode Markdown remains unchanged for backward compatibility.
    - <kbd>(not affected)</kbd> Added the field file_unique_id to the objects Animation, Audio, Document, PassportFile, PhotoSize, Sticker, Video, VideoNote, Voice, File and the fields small_file_unique_id and big_file_unique_id to the object ChatPhoto. The new fields contain a unique file identifier, which is supposed to be the same over time and for different bots, but can't be used to download or reuse the file.
    - Added the field custom_title to the ChatMember object.
    - Added the new method setChatAdministratorCustomTitle to manage the custom titles of administrators promoted by the bot.
    - Added the field slow_mode_delay to the Chat object.

## Version 4.4.0
- Array validation is now a separate function to allow super calls.
- Added API definitions of v4.4, (July 29th, 2019) with the following changelog:
    - Added support for animated stickers. New field `is_animated` in `Sticker` and `StickerSet` objects, animated stickers can now be used in `send_sticker` and `InlineQueryResultCachedSticker`.
    - Added support for default permissions in groups. New object `ChatPermissions`, containing actions which a member can take in a chat. New field permissions in the Chat object; new method setChatPermissions.
    - The field `all_members_are_administrators` has been removed from the documentation for the `Chat` object. The field is still returned in the object for backward compatibility, but new bots should use the permissions field instead.
    - Added support for more permissions for group and supergroup members: added the new field `can_send_polls` to `ChatMember` object, added `can_change_info`, `can_invite_users`, `can_pin_messages` in `ChatMember` object for restricted users (previously available only for administrators).
    - The method `restrict_chat_member` now takes the new user permissions in a single argument of the type `ChatPermissions`.
    - Added `description` support for basic groups (previously available in supergroups and channel chats). You can pass a group's `chat_id` to `set_chat_description` and receive the group's description in the `Chat` object in the response to `get_chat` method.
    - Added `invite_link` support for basic groups (previously available in supergroups and channel chats). You can pass a group's chat_id to `export_chat_invite_link` and receive the group's invite link in the `Chat` object in the response to `get_chat` method.
## Version 4.1.0
- Renamed `InputFile`'s `file_name` to simply `name`. (`InputFileFromDisk`, `InputFileFromURL`, `InputFileFromBlob`)
- Renamed `InputFile`'s `file_mime` to simply `mime`. (`InputFileFromDisk`, `InputFileFromURL`, `InputFileFromBlob`)
- Renamed `InputFile`'s `file_blob` to simply `blob`. (`InputFileFromDisk`, `InputFileFromURL`, `InputFileFromBlob`)
- Renamed `InputFileFromURL`'s `file_url` to simply `url`.
- Renamed `InputFileFromBlob`'s `file_blob` to simply `blob`.
- Renamed `InputFileFromDisk`'s `file_path` to simply `path`.
- Added `InputFileUseUrl` and `InputFileUseFileID` as an abstract way for url/file_id instead of the plain string.
- Now `InputFile(...)` wrappes the new `InputFile.factory(...)`, which can be used to create a instance of a matching subclass by parameter.
    - e.g. `InputFile(url="https://example.com")` results in the same as `InputFileFromURL("https://example.com")` which is in long form `InputFileFromURL(url="https://example.com")`.

## Version 4.0.3
- Added `.size` property for all file based `InputFile` subclasses.

## Version 4.0.2
- Bugfix release fixing request logic: when checking for api success, the condition for success was corrupted in 4.0.1.

## Version 4.0.1
- the `.raw` value will now be reset if you set any value of an `TgBotApiObject` object.
- Handle Responses with aren't valid json,
    e.g. `413 Request Entity Too Large` when uploading too large files

    Because the API responded with status `413`, as `text/html`:
    ```html
    <html>\r\n<head><title>413 Request Entity Too Large</title></head>\r\n<body bgcolor="white">\r\n<center><h1>413 Request Entity Too Large</h1></center>\r\n<hr><center>nginx/1.12.2</center>\r\n</body>\r\n</html>\r\n
    ```

    The code would fail with generic json decode exception:
    ```py
    json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
    ```

    Now we wrap that in a new exception type, which also subclasses from `TgApiException`:
    ```py
    TgApiResponseException(message:str, response: requests.Response, exception: Exception)
    ```


## Version 4.0.0
- [`Bot API 4`.`0` (July 26, 2018)](https://core.telegram.org/bots/api-changelog#july-26-2018)
    - Added [Telegram Passport](https://telegram.org/blog/passport)
        - Added bot methods:
        - New `pytgbot.api_types.receivable.passport` containing:
        `PassportData`, `PassportFile`, `EncryptedPassportElement` and `EncryptedCredentials`
        - New `pytgbot.api_types.sendable.passport` containing:
        `PassportElementError`, `PassportElementErrorDataField`, `PassportElementErrorFrontSide`, `PassportElementErrorReverseSide`, `PassportElementErrorSelfie`, `PassportElementErrorFile` and `PassportElementErrorFiles`
    - More Changes:
        - `api_types.receivable.media`:
            - `MessageEntity` added `"cashtag"` as possible entity type.
            - Added `thumb` parameter to `Audio`.
            - Added `vcard` parameter to `Contact`.
            - Added `foursquare_type` parameter to `Venue`.
            - Added `Animation` class.
        - `api_types.receivable.passport`:
            - Added, see above.
        - `api_types.receivable.updates`:
            - Added parameters `animation` and `passport_data` to `Message`.
        - `api_types.sendable.inline`:
            - Added `foursquare_type` parameter to `InlineQueryResultVenue` and `InputVenueMessageContent`.
            - Added `vcard` parameter to `InlineQueryResultContact` and `InputContactMessageContent`.
        - `api_types.sendable.input_media`:
            - `InputMedia`: Created `caption` field, this is contained in all subclasses.
            - `InputMediaPhoto`:
                - moved the `caption` into the superclass.
                - fixed `parse_mode` not working in `from_array(...)`
            - `InputMediaVideo`:
                - moved the `caption` into the superclass.
                - fixed `parse_mode` not working in `from_array(...)`
                - added `thumb` parameter.
             - Added new `InputMediaAnimation`.
             - Added new `InputMediaAudio`.
             - Added new `InputMediaDocument`.
        - `api_types.receivable.passport`:
            - Added, see above.
        - `bot.Bot`:
            - Added `thumb` parameter to `send_audio(...)`, `send_video(...)`, `send_video_note(...)` and `send_video_note(...)`.
            - Added `foursquare_type` parameter to `send_venue(...)`.
            - Added `vcard` parameter to `send_contact(...)`.
            - Added new `send_animation(...)` function.
            - Added new `edit_message_media(...)` function.
            - Added new `set_passport_data_errors(...)` function.
    - Documentation changes:
        - `bot.Bot.set_webhook`: Returns True, only on success.
        - `bot.Bot.send_media_group`: Instead of generic `InputMedia`, now only accepts `InputMediaPhoto` or `InputMediaVideo`
        - `api_types.sendable.reply_markup.InlineKeyboardButton` can now use `tg://` urls, too.
- Also, while at it
  - Fixed `'live_period' in inlinequeryresultlocation_instance` wrongly returning `False`
  - Fixed `InputFileFromBlob` and `InputFileFromURL`: Reworked that whole `InputFile` piece, which should fix [#6](https://github.com/luckydonald/pytgbot/issues/6).
  - Fixed `certificate` argument in `Bot.set_webhook(...)` not working.
        - Therefore in `_do_fileupload(...)`, the file can be set to be optional (`_file_is_optional=True`).
  - Added `get_request_media(...)` method to `InputMedia`, to allow sending easier. Is very similar to `InputFile.get_request_files(...)`.
  - Fixed `Bot.send_media_group(...)` now supporting `InputMediaPhoto` and `InputMediaVideo` elements, so sending files is actually possible.
  - Fixed `Bot.edit_message_media(...)` now supporting `InputMedia` elements, so sending files is actually possible.

## Version 3.6.0
- [`Bot API 3`.`6` (February 13, 2018)](https://core.telegram.org/bots/api-changelog#february-13-2018)
    - Added `connected_website` attribute to the `Update` class.
- Added `parse_mode` attribute all stuff that has captions, in the bot functions and the sendable inline objects.
- Also added `supports_streaming` to `Bot.send_video(...)` and  `sendable.inputmedia.InputMediaVideo`.

## Version 3.5.2
- Added `username` and `id` property to the `Bot` class.
   This is basically the implementation used in [Teleflask](https://github.com/luckydonald/Teleflask) already, but calling it `id` and not `user_id` as it is a bot, not a user.
- Added `__str__` class, so that `str(bot)` displays as `Bot(username="luckybot", id=108721382)`

## Version 3.5.1
- Fixed `InputFileFromDisk`.
- Usage of `InputFile` with `file_blob` is now **deprecated**.
  Use `InputFileFromBlob` instead.

## Version 3.5.0
Updated official API changes of
- [`Bot API 3`.`4` (October 11, 2017)](https://core.telegram.org/bots/api-changelog#october-11-2017)
- [`Bot API 3`.`5` (November 17, 2017)](https://core.telegram.org/bots/api-changelog#november-17-2017)

## Version 3.3.1
- Removed doubled `WebhookInfo` classes at two different places. They are now the same.
- Fixed importing `Message` in `pytgbot.api_types.receivable.peer.Chat`.

## Version 3.3.0
- Updated Official API changes of [`Bot API 3`.`3` (August 23, 2017)](https://core.telegram.org/bots/api-changelog#august-23-2017)
    - Added new fields:
        + `peer.Chat.pinned_message`
        + `peer.User.is_bot`
        + `updates.Message.forward_signature`
        + `updates.Message.author_signature`
    - Removed fields:
        - `updates.Message.new_chat_member`
            - but `updates.Message.new_chat_members` still exists

## Version 3.2.0 __Not released__ `8eb2ff860af4ce6e44d3fcf5c012d8a070e046ee`
- Updated Official API changes of [`Bot API 3`.`2` (July 21, 2017)](https://core.telegram.org/bots/api-changelog#july-21-2017)
    - Stickers'n'stuff

## Version 3.1.1 __Not released__ `6654e962ce42e305be138efa90f9262098bf2b7d`
- fixed `send_video_note`, `send_video`, `send_voice`, `set_chat_photo` of `pytgbot.bot.Bot`.

## Version 3.1.0
- Updated Official API changes of [`Bot API 3`.`1` (June 30, 2017)](https://core.telegram.org/bots/api-changelog#june-30-2017)
    - Added new functions:
        - `pytgbot.bot.Bot.restrict_chat_member`
        - `pytgbot.bot.Bot.promote_chat_member`
        - `pytgbot.bot.Bot.export_chat_invite_link`
        - `pytgbot.bot.Bot.set_chat_photo`
        - `pytgbot.bot.Bot.delete_chat_photo`
        - `pytgbot.bot.Bot.set_chat_title`
        - `pytgbot.bot.Bot.set_chat_description`
        - `pytgbot.bot.Bot.pin_chat_message`
        - `pytgbot.bot.Bot.unpin_chat_message`
    - Updated `pytgbot.bot.Bot.kick_chat_member` function, added `until_date` parameter.
    - Updated `pytgbot.bot.Bot.send_invoice` function, `description` parameter now _optional_.
    - Updated parameter `chat_id` in game related methods to no longer allows string, so no more "@username".
        - `pytgbot.bot.Bot.send_game`
        - `pytgbot.bot.Bot.set_game_score`
        - `pytgbot.bot.Bot.get_game_high_scores`
    - Added `pytgbot.api_types.receivable.media.ChatPhoto`.
    - Updated `pytgbot.api_types.receivable.peer.Chat` to include the new fields:
        - `photo`
        - `description`
        - `invite_link`
    - Updated `api_types.receivable.peer.ChatMember`:
        - `status` field can now also be `"restricted"`
        - Added fields:
        - `until_date`
        - `can_be_edited`
        - `can_change_info`
        - `can_post_messages`
        - `can_edit_messages`
        - `can_delete_messages`
        - `can_invite_users`
        - `can_restrict_members`
        - `can_pin_messages`
        - `can_promote_members`
        - `can_send_messages`
        - `can_send_media_messages`
        - `can_send_other_messages`
        - `can_add_web_page_previews`
    - Removed documentation saying `pytgbot.api_types.sendable.inline.InlineQueryResultCachedDocument` was limited to sending only pdf-files and zip archives.
- Also now storing the incoming (decoded json) data in the `_raw` field of the object.


## Version 3.0.0
- Updated Official API changes of [`Bot API 3`.`0` (May 18, 2017)](https://core.telegram.org/bots/api-changelog#may-18-2017)
    - Added `pytgbot.api_types.receivable.VideoNote`.
    - Updated `pytgbot.api_types.receivable.peer.User` to include the new `language_code` field.
    - Updated `pytgbot.api_types.receivable.updates.Update` to include the new `shipping_query` and `pre_checkout_query` fields.
    - Updated `pytgbot.api_types.receivable.updates.Message` to include the new `video_note`, `new_chat_members`, `invoice` and `successful_payment` fields.
    - Added `pytgbot.api_types.receivable.updates.WebhookInfo`
    - Updated `pytgbot.api_types.sendable.inline.InlineQueryResultGif` to include the new `gif_duration` field.
    - Updated `pytgbot.api_types.sendable.inline.InlineQueryResultMpeg4Gif` to include the new `mpeg4_duration` field.
    - Added `pytgbot.api_types.sendable.payments.LabeledPrice`
    - Added `pytgbot.api_types.sendable.payments.ShippingOption`
    - Updated `pytgbot.api_types.sendable.reply_markup.InlineKeyboardButton` to include the new `pay` field.
    - Added `pytgbot.bot.Bot.delete_webhook` function.
    - Added `pytgbot.bot.Bot.send_video_note` function.
    - Documented that `pytgbot.bot.Bot.unban_chat_member` now works with channels too.
    - Added `pytgbot.bot.Bot.delete_message` function.
    - Added `pytgbot.bot.Bot.send_invoice` function.
    - Added `pytgbot.bot.Bot.answer_shipping_query` function.
    - Added `pytgbot.bot.Bot.answer_pre_checkout_query` function.


## Version 2.3.3
- Updated Official API changes of [`Bot API 2`.`3`.`1` (December 4, 2016)](https://core.telegram.org/bots/api-changelog#december-4-2016)


### Version 2.3.2
- Fixed failed version bump, which causing importing this package impossible.

### Version 2.3.1
- This is **not** Telegram `Bot API 2.3.1`!
- This version doesn't work. Use `2.3.2` instead.
- Fixed InlineQueryResultCachedSticker.


## Version 2.3
- Updated API changes of [`Bot API 2.3` (November 21, 2016)](https://core.telegram.org/bots/api-changelog#november-21-2016)

Changes I observed:
> Bot
>> **`answer_callback_query`**: added `cache_time`
>> **`edit_message_text`**: works for game messages too.
>> **`set_game_score`**: added `force`
>> **`set_game_score`**: added `disable_edit_message`
>> **`set_game_score`**: removed `edit_message`
>> **`set_game_score`**: `score` can be `0`. Now must be non-negative, before it must be postive.
>
> Classes:
>> **`updates.Update`**: added `channel_post`
>> **`updates.Update`**: added `edited_channel_post`
>> **`updates.Message`**: added `forward_from_message_id`
>
> Documentation:
>> **`Message`** ids are not called _unique_ no more.
>> **`CallbackQuery`** ids are not called _global_ no more.
>> **Inline Keyboard** Warnings removed.
>
> Might be a incomplete list, also have a look at the api changelog.

## Version 2.2.1

> Bugfix release

**Version 2.2.1a4**

- Fixed importing of `Game` in `Update.from_array(array)`.

**Version 2.2.1a3**

- Fixed importing of `InputFile*` after the package location change in [V2.2.0](#version-220).

**Version 2.2.1a2**

- Manually added placeholder class `pytgbot.api_types.receiveable.updates.`[`CallbackGame`](https://core.telegram.org/bots/api#callbackgame)

**Version 2.2.1a1**

- Fixed using wrong templates

## Version 2.2.0 ##
 - Moving `InputFile`, `InputFileFromDisk`, `InputFileFromURL` to `api_types.sendable.files.*` [#4](https://github.com/luckydonald/pytgbot/issues/4)
 - Implemented the changes from [`Bot API 2.2` (October 3, 2016)](https://core.telegram.org/bots/api-changelog#october-3-2016) ([gaming](https://core.telegram.org/bots/api#games) platform)
 - Improved templates, separated some stuff in the `Bot.do(...)` function for better subclassing. This will hopefully allow a subclass capable of returning infos, from an open webhook, later.

## Version 2.1.4 ##
- Reworked `InputFile`, `InputFileFromDisk`, `InputFileFromURL` internals.
    They now should handle input better. [#3](https://github.com/luckydonald/pytgbot/issues/3), [`luckydonald/bonbot` #131](https://github.com/luckydonald/bonbot/issues/131)

## Version 2.1.2 ##
- Fix: Also catching `TgApiException`s if `get_updates(..., error_as_empty=True)`

## Version 2.1.1 ##
- Renamed `get_updates(...)`'s `timeout` parameter to `poll_timeout`.
- Added `request_timeout` to `do(...)` method. Currently only `get_updates(...)` has that.

## Version 2.1.0 ##
- Renamed `pytgbot.api_types.receivable.media.File.download_url(token)` to `get_download_url(token)`
- Added a `pytgbot.bot.Bot.get_download_url(file)` method.

## Version 2.0.1 ##
- Renamed `InputFileURL` to `InputFileFromURL`
- Added `InputFileFromDisk`
- `InputFile` is for buffers (strings) now

## Version 2.0.0 ##

Big overhaul:

- Real Objects for everything.
- Also most of this module can now be generated from the api website automatically, making updates a breeze.

## Version 1.0.1 ##
- Added ability to ignore network errors in `get_updates(...)` without raising a exception by setting `error_as_empty=True`.
  Useful in `for update in bot.get_updates(error_as_empty=True)` constructs.

## Version 1.0.0 ##
- Added [Inline mode](https://telegram.org/blog/inline-bots) including [inlinefeedback](https://core.telegram.org/bots/inline#collecting-feedback).
  This should be [`Bot API 2.0` (April 9, 2016)](https://core.telegram.org/bots/api-changelog#april-9-2016).

## Version 0.0.0 ##
- First implementation
