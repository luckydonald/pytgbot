# Changelog
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

## Version 0.0.0 ##
- First implementation