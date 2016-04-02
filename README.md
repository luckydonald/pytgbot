# pytgbot `v1.0.1` (stable)
###### Python module to access the telegram bot api.

`1.0.1`: Added ability to ignore network errors in `get_updates(...)` without raising a exception by setting `error_as_empty=True`. Useful in `for` constructs. 
New in version `1.0.0`: [Inline mode](https://telegram.org/blog/inline-bots) including [inlinefeedback](https://core.telegram.org/bots/inline#collecting-feedback).


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
for x in bot.get_updates()["result"]:
	print(x)

# sending messages:
bot.send_msg(CHAT_ID, "another test.")
```
