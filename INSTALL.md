# Normal install
```sh
pip3 install pytgbot
```

# Manual install:
```sh
sudo apt-get install python3-pip
sudo apt-get install libffi-dev
sudo apt-get install libbz2-dev
sudo apt-get install libncursesw5-dev
sudo pip3 install virtualenv

virtualenv -p /usr/bin/python3 virtualenv3.venv
source virtualenv3.venv

git clone https://github.com/luckydonald/pytgbot.git
cd pytgbot
python setup.py install
```