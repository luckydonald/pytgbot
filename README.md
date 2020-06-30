# pytgbot - Telegram Bot API [`4`.`6`](https://core.telegram.org/bots/api)
### Version [4.6.2 (stable)](https://github.com/luckydonald/pytgbot/blob/master/CHANGELOG.md#changelog) [![Join pytgbot group on telegram](https://img.shields.io/badge/Telegram%20Group-Join-blue.svg)](https://telegram.me/pytg_group)
###### Python module to access the telegram bot api.

Native python package with a pure Python interface for the [Telegram Bot API](https://core.telegram.org/bots).
> The code is generated directly from the API documentation, meaning up-to-date code is a matter of minutes.

# Recent changes
 - ⚠️ BREAKING CHANGES ⚠️ :
    - `pytgbot` now comes in two flavors, sync and async, making it fit for asyncio.
    - Those need different dependencies, as the favorite web framework for the normal mode is `requests`, but that one isn't suited for asyncio.
    - Therefore you have to now install it as `pytgbot[sync]` instead of just `pytgbot`.
    - Your pip command looks like `pip install pytgbot[sync]`.
    - If you want to install the async version it's `pytgbot[async]`.
    - If you just install `pytgbot` (without the version in square brackets), you have to install `requests` for the sync bot or `httpx` for the `async` bot yourself.
 - Added API definitions of v4.7, (March 30, 2020) with the following changelog:
 - Added API definitions of v4.8, (April 24, 2020) with the following changelog:
 - Added API definitions of v4.9, (June 4, 2020) with the following changelog:
 - Fixed `get_update` where the time `delta` would easily underflow to being days, making it wait forever, and `error_as_empty=True` and `return_python_objects=True` were not playing well together, and returning the wrong type.
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
The [latest version](#releases) seems to be version `4.9`. For other releases you must adapt the examples below.
Also check the [release section](https://github.com/luckydonald/pytgbot/releases), if there are newer versions available.

##### Python package index (recommended)
```sh
pip install pytgbot[sync]==4.9
```

##### Using a specific git version
You have to replace `289ad8c330282cadcb70309e5d08c888ab38a0f3` with the specific commit hash of the version you want.
```sh
pip install -e git://github.com/luckydonald/pytgbot.git@289ad8c330282cadcb70309e5d08c888ab38a0f3#egg=pytgbot[sync]
```

##### Manually
```sh
git clone -b v4.9 https://github.com/luckydonald/pytgbot.git
cd pytgbot
pip install -e .[sync]
```

#### Bleeding edge
To get the most current code manually
```
git clone https://github.com/luckydonald/pytgbot.git
cd pytgbot
python setup.py install
```

# Updating
Note, since version `4`.`9` you have to add `[sync]`.

#### Latest Stable
The [latest version](#releases) seems to be version `4.9`. For other releases you must adapt the examples below.

##### Python package index (recommended)
```sh
pip install -U pytgbot[sync]==4.9
```

##### Using a specific git version
You have to replace `289ad8c330282cadcb70309e5d08c888ab38a0f3` with the specific commit hash of the version you want.
```sh
pip install -e git://github.com/luckydonald/pytgbot.git@289ad8c330282cadcb70309e5d08c888ab38a0f3#egg=pytgbot[sync]
```


##### Manually
```sh
cd pytgbot
git fetch
git checkout v4.9
pip install -e .[sync]
```

#### Bleeding edge
To get the most current code manually
```
cd pytgbot
git fetch
git checkout master
git pull
pip install -e .[sync]
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
