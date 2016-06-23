# pytgbot `v2.0.0` (stable)
###### Python module to access the telegram bot api.

`2.0.1`: Renamed `InputFileURL` to `InputFileFromURL`, added `InputFileFromDisk` (`InputFile` is for buffers now) 
`2.0.0`: Big overhaul. Real Objects for everything. Also most of this module can now be generated from the api website automatically.
`1.0.1`: Added ability to ignore network errors in `get_updates(...)` without raising a exception by setting `error_as_empty=True`. Useful in `for` constructs. 
New in version `1.0.0`: [Inline mode](https://telegram.org/blog/inline-bots) including [inlinefeedback](https://core.telegram.org/bots/inline#collecting-feedback).


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
bot.send_msg(CHAT_ID, "another test.")
```
