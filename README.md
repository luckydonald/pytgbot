# pytgbot - Telegram Bot API [`3`.`6`](https://core.telegram.org/bots/api)
### Version [3.6.0 (stable)](https://github.com/luckydonald/pytgbot/blob/master/CHANGELOG.md#changelog) [![Join pytgbot group on telegram](https://img.shields.io/badge/Telegram%20Group-Join-blue.svg)](https://telegram.me/pytg_group)
###### Python module to access the telegram bot api.

Native python package with a pure Python interface for the [Telegram Bot API](https://core.telegram.org/bots).
> The code is generated directly from the API documentation, meaning up-to-date code is a matter of minutes.

#### Recent changes:
 - Updated official API changes of [`Bot API 3`.`6` (February 13, 2018)](https://core.telegram.org/bots/api-changelog#february-13-2018)
 - [Older changes...](CHANGELOG.md)

#### Installation  ####
Via pip:
```sh
pip install pytgbot
```
Or manually:
```sh
git clone https://github.com/luckydonald/pytgbot.git
cd pytgbot
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
