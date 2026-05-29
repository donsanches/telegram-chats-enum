# telegram-chats-enum

Small Python utility which lists all your Telegram chats. It uses Telethon library.

## Features

- Authenticate with Telegram API
- Enumerate available chats/dialogs
- Display chat names and IDs
- Useful for Telegram automation and bot development
- Can use MTProto FakeTLS proxy (with ee... secrets)

## Requirements

- Python 3.10+
- Telegram API credentials

## Installation

Clone the repository:

```bash
git clone https://github.com/donsanches/telegram-chats-enum.git
cd telegram-chats-enum
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### Linux/macOS

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `config.ini` file:

```env
[Telegram]
api_id = your_api_id
api_hash = your_api_hash
session = session_name
```

`session_name` is arbitrary. After you run the script for the first time and log into your Telegram account, a file `session_name.session` will be created. Make sure this file is not shared in any way since this is the key to your Telegram account.

You can obtain Telegram API credentials at:

https://my.telegram.org

## Usage

Run the script:

```bash
python chatsenum.py
```

## Using a proxy

Proxies which use MTProto FakeTLS (with ee... secret) are supported. For that, TelethonFakeTLS library is used.

Add the following section to the `config.ini` file:

```env
[Proxy]
; Remove this section entirely if you don't need a proxy
host = 127.0.0.1
port = 1080
secret = your_secret_here
```

Remove “ee” from the starting of hex secret as described in TelethonFakeTLS docs at https://pypi.org/project/TelethonFakeTLS/

## Security Notes

- Never make your `config.ini` or `*.session` files publicly available in any way 
- Never expose API credentials publicly
- Use GitHub private email if desired

## License

MIT License