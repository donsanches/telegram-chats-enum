#!/usr/bin/env python3
import asyncio
import configparser
from telethon import TelegramClient, connection
import TelethonFakeTLS

async def main():
    config = configparser.ConfigParser()
    config.read("config.ini")

    api_id   = config['Telegram']['api_id']
    api_hash = config['Telegram']['api_hash']
    session  = config['Telegram']['session']

    if config.has_section('Proxy'):
        proxy = (config['Proxy']['host'], int(config['Proxy']['port']), config['Proxy']['secret'])
        conn = TelethonFakeTLS.ConnectionTcpMTProxyFakeTLS
    else:
        proxy = None
        conn = connection.ConnectionTcpFull

    async with TelegramClient(session, api_id, api_hash, connection=conn, proxy=proxy) as client:
        await client.start()
        print("Fetching chat details...\n")
        async for dialog in client.iter_dialogs():
            print(f"Chat Name: {dialog.name}, Chat ID: {dialog.id}")


if __name__ == "__main__":
    asyncio.run(main())
