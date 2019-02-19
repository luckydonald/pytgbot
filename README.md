# pytgbot - Telegram Bot API [`4`.`1`](https://core.telegram.org/bots/api)
### Version [4.1.1 (stable)](https://github.com/luckydonald/pytgbot/blob/master/CHANGELOG.md#changelog) [![Join pytgbot group on telegram](https://img.shields.io/badge/Telegram%20Group-Join-blue.svg)](https://telegram.me/pytg_group)
###### Python module to access the telegram bot api.

Native python package with a pure Python interface for the [Telegram Bot API](https://core.telegram.org/bots).
> The code is generated directly from the API documentation, meaning up-to-date code is a matter of minutes.

# Recent changes
 - Updated official API changes of [`Bot API 4`.`1` (August 27, 2018)](https://core.telegram.org/bots/api-changelog#august-27-2018)
 - [And more...](CHANGELOG.md)

 [Older changes...](CHANGELOG.md)

# Are you using pytgbot?

If you're using this library to build your Telegram Bots, We'd love to know and share the bot with the world.
Tell us about it - **[here](https://github.com/luckydonald/pytgbot/wiki/Who's-using-pytgbot%3F)**

Check out the [Who's using pytgbot](https://github.com/luckydonald/pytgbot/wiki/Who's-using-pytgbot%3F) wiki page to know more about what people have been building with this library.

# Installation
### Releases
Released versions can be found at several locations:
- The [python package index](https://pypi.org/project/pytgbot/#history) (`pip install`),
- on GitHub in the [release section](https://github.com/luckydonald/pytgbot/releases)
- and in the git files as regular tags.

#### Latest Stable
The [latest version](#releases) seems to be version `4.0.2`. For other releases you must adapt the examples below.

##### Python package index (recommended)
```sh
pip install pytgbot==4.0.2
```

##### Manually
```sh
git clone -b v4.0.2 https://github.com/luckydonald/pytgbot.git
cd pytgbot
python setup.py install
```

#### Bleeding edge
To get the most current code manually
```
git clone https://github.com/luckydonald/pytgbot.git
cd pytgbot
python setup.py install
```

# Updating

#### Latest Stable
The [latest version](#releases) seems to be version `4.0.2`. For other releases you must adapt the examples below.

##### Python package index (recommended)
```sh
pip install -U pytgbot==4.0.2
```

##### Manually
```sh
cd pytgbot
git fetch
git checkout v4.0.2
python setup.py install
```

#### Bleeding edge
To get the most current code manually
```
cd pytgbot
git fetch
git checkout master
git pull
python setup.py install
```


# Usage

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
They are pythonic in small letters with underscores instead of camel case, for example [getUpdates](https://core.telegram.org/bots/api#getupdates) is `bot.get_updates()`.
## Documentation
You can always inspect the documentation inside the code.
You can also use the python `help()` command in the interactive interpreter:
```py
>>> from pytgbot import Bot
>>> help(Bot)
>>> # or
>>> help(Bot.get_updates)
```


## Examples
Have a look into the [examples](https://github.com/luckydonald/pytgbot/tree/master/examples) folder.

# In case of errors
First you should set logging to level `DEBUG` to see what's going on.
```python
# add this to the first lines in your file
import logging
logging.basicConfig(level=logging.DEBUG)
```

If you are about to open a new issue, search the existing ones (open and closed) first.
Sometimes they are already reported or even solved.

# Note for maintainers of this package:
Best way to apply changes is to create a patch from the commit containing the new generated files `output`.

```
git apply --verbose --reject --no-index -C1 --whitespace=fix --ignore-space-change --ignore-whitespace --directory pytgbot/ NAME.patch
find ./pytgbot/ -type f -name '*.rej' | xargs --replace={}  --max-args=1   echo "{} {}"
find ./pytgbot/ -type f -name '*.rej' |  xargs  --replace={}  --max-args=1  bash -c 'file="{}";file="${file%.*}"; echo wiggle --replace ${file} {};'
wiggle --replace pytgbot
```
You may need to install wiggle: `brew install wiggle`
_See also https://stackoverflow.com/questions/4770177/git-patch-does-not-apply_
