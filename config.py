#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7639447946:AAHzVWhmRA184lRYoQk44T_kyM4anupgx2s")
    API_ID = int(os.environ.get("API_ID", "28748671"))
    API_HASH = os.environ.get("API_HASH", "f53ec7c41ce34e6d585674ed9ce6167c")
    AUTH_USERS = "1169394017"

