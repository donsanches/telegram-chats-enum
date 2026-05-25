#!/usr/bin/env python3
import asyncio
import configparser
from telethon import TelegramClient

config = configparser.ConfigParser()
config.read("config.ini")

api_id   = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
session  = config['Telegram']['session']


async def main():
    async with TelegramClient(session, api_id, api_hash) as client:
        await client.start()
        print("Fetching chat details...\n")
        async for dialog in client.iter_dialogs():
            print(f"Chat Name: {dialog.name}, Chat ID: {dialog.id}")


if __name__ == "__main__":
    asyncio.run(main())
