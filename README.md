# pytgbot `v2.0.1` (stable)
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

All the functions can be find in [pytgbot/bot.py](https://github.com/luckydonald/pytgbotapi/blob/master/pytgbot/bot.py).

#### Examples ####
Have a look into the `examples` folder.

## In case of errors ##
First you should set logging to level `DEBUG` to see what's going on.
```python
# add this to the first lines in your file
import logging
logging.basicConfig(level=logging.DEBUG)
```
If you are about to open a new issue, search the existing ones (open and closed) first.
Sometimes they are already reported or even solved.
