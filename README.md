# pytgbot
### Version [2.2.1.a5.0post1 (stable)](https://github.com/luckydonald/pytgbot/blob/master/CHANGELOG.md#changelog) 
###### Python module to access the telegram bot api.

Native python package witch pure Python interface for the [Telegram Bot API](https://core.telegram.org/bots).
> The code is genereated directly from the API documentation, meaning up-to-date code is a matter of minutes.

#### Latest changes:
 - Moving `InputFile`, `InputFileFromDisk`, `InputFileFromURL` to `api_types.sendable.files.*` [#4](https://github.com/luckydonald/pytgbot/issues/4)
 - Implemented the changes from [October 3, 2016](https://core.telegram.org/bots/api-changelog#october-3-2016) ([gaming](https://core.telegram.org/bots/api#games) platform)
 - Improved templates, seperated some stuff in the `Bot.do(...)` function for better subclassing. This will hopefully allow a subclass capable of returning infos, from an open webhook, later.
 - [Older changes...](CHANGELOG.md)

#### Installation  ####
```sh
python setup.py install
```

#### Usage ####

```python
from pytgbot import Bot

bot = Bot(API_KEY)

# sending messages:
bot.send_message(CHAT, "Example Text!")  # CHAT can be a @username or a id

# getting events:
for x in bot.get_updates():
	print(x)

```

All the functions can be found in the `Bot` class in the [pytgbot/bot.py](https://github.com/luckydonald/pytgbot/blob/master/pytgbot/bot.py) file.
They are pythonic in small letters with underscores instead of camel case, for example [getUpdates](https://core.telegram.org/bots/api#getupdates) is `bot.get_updates`

## Examples ##
Have a look into the [examples](https://github.com/luckydonald/pytgbot/tree/master/examples) folder.

## In case of errors ##
First you should set logging to level `DEBUG` to see what's going on.
```python
# add this to the first lines in your file
import logging
logging.basicConfig(level=logging.DEBUG)
```
If you are about to open a new issue, search the existing ones (open and closed) first.
Sometimes they are already reported or even solved.
