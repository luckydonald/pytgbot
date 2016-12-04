# Changelog

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