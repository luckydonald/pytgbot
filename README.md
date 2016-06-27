# pytgbot
### Version [2.0.1 (stable)](https://github.com/luckydonald/pytgbot/blob/master/CHANGELOG.md#changelog) 
###### Python module to access the telegram bot api.

[Official Telegram Bot API Documentation](https://core.telegram.org/bots)

#### Installation  ####
```sh
python setup.py install
```

#### Usage ####


```python
from pytgbot import Bot

bot = Bot(API_KEY)


# getting events:
for x in bot.get_updates():
	print(x)

# sending messages:
bot.send_message(CHAT_ID, "Test!")
```

All the functions can be found in [pytgbot/bot.py](https://github.com/luckydonald/pytgbot/blob/master/pytgbot/bot.py).

#### Examples ####
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
