#! /usr/bin/env python3.6
# coding: utf-8

import os
import datetime as dt
from pathlib import Path

import pytz
from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

slack_verification_token = os.environ["slack_verification_token"]
slack_bot_user_token = os.environ["slack_bot_user_token"]
bot_id = os.environ["bot_id"]
bot_name = os.environ["bot_name"]

home = Path(os.getenv("home_folder", os.getcwd()))

db_host = os.environ["db_host"]
db_user = os.environ["db_user"]
db_passwd = os.environ["db_passwd"]
db_name = os.environ["db_name"]

ssh_host = os.environ["ssh_host"]
ssh_username = os.environ["ssh_username"]
ssh_password = os.environ["ssh_password"]
ssh_db_host_name = os.environ["ssh_db_host_name"]
ssh_port = int(os.environ["ssh_port"])

dropbox_token = os.environ["dropbox_token"]

tz = pytz.timezone(os.environ["tz"])

app_id = os.environ["app_id"]

test_channel = os.environ["test_channel"]

main_channel = os.environ["main_channel"]

countdown_message = os.environ["countdown_message"]
ongoing_message = os.environ["ongoing_message"]
finished_message = os.environ["finished_message"]

countdown_date = dt.datetime.fromtimestamp(int(os.environ["countdown_date"]), tz=tz)

countdown_args = os.environ["countdown_args"].split(", ")
