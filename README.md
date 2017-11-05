# PyConHK2017-Chatbot-Tutorial

## Introduction

It's a simple telegram chatbot tutorial sharing on PyCon HK 2017. 

## Installation

```
$ mkdir venv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

This tutoial is using [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) this library with Python3.5.


## Project Objective
Make a simple paper-rock-scissor game with chatbot with a single user

## How do I create a bot?

Just talk to BotFather(***@BotFather***) and follow a few simple steps. Once you've created a bot and received your authorization token, head down to the Bot API manual to see what you can teach your bot to do.

Use the /newbot command to create a new bot. The BotFather will ask you for a name and username, then generate an authorization token for your new bot.

The name of your bot is displayed in contact details and elsewhere.

The Username is a short name, to be used in mentions and telegram.me links. Usernames are 5-32 characters long and are case insensitive, but may only include Latin characters, numbers, and underscores. Your bot's username must end in ‘bot’, e.g. ‘tetris_bot’ or ‘TetrisBot’.

The token is a string along the lines of `110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw` that is required to authorize the bot and send requests to the Bot API.

Ref: [Bots: An introduction for developers](https://core.telegram.org/bots)
