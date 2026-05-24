#!/usr/bin/env python3
import configparser
from telethon.sync import TelegramClient

config = configparser.ConfigParser()
config.read("config.ini")

api_id   = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
session  = config['Telegram']['session']

client = TelegramClient(session, api_id, api_hash)
client.start()

print("Fetching chat details...\n")
for dialog in client.iter_dialogs():
    print(f"Chat Name: {dialog.name}, Chat ID: {dialog.id}")
