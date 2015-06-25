# pytgbot
###### Python module to access the telegram bot api.

**Note:** This is a work in progress. ```Pre-Alpha 0.0.¼```

[Official Telegram Bot API Documentation](https://core.telegram.org/bots)

#### Installation  ####
```sh
python setup.py install
```

#### Usage ####


```
from pytgbot import Bot

bot = Bot(API_KEY)


# getting events:
for x in bot.get_updates()["result"]:
	print(x)

# sending messages:
bot.send_msg(TEST_CHAT, "another test.")
```
