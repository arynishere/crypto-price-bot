# Crypto Price Telegram Bot

A Telegram bot that provides real-time cryptocurrency prices from Bitpin for **USDT**, **BTC**, and **ETH** in Iranian Toman. Prices include both **buy** and **sell** values, updated automatically every 5 minutes. Users can also get the latest prices on-demand using the `/now` command.

---

## Features

- 💵 **USDT**, 🪙 **BTC**, 💎 **ETH** prices
- Show **buy and sell prices**
- Automatic updates every **5 minutes** to a Telegram channel
- On-demand price checking using `/now` command
- Nicely formatted numbers with thousand separators
- Handles errors gracefully and shows ❌ if price fetching fails

---

## Screenshots

Example of bot messages:

💵 USDT: خرید 114,476 تومان | فروش 115,000 تومان
🪙 BTC: خرید 13,972,814,636 تومان | فروش 14,000,000,000 تومان
💎 ETH: خرید 513,810,644 تومان | فروش 520,000,000 تومان

csharp
Copy code

If there is a problem fetching prices:

💵 USDT: ❌ خطا در دریافت قیمت
🪙 BTC: ❌ خطا در دریافت قیمت
💎 ETH: ❌ خطا در دریافت قیمت

yaml
Copy code

---

## Requirements

- Python 3.10+
- [`python-telegram-bot`](https://pypi.org/project/python-telegram-bot/)
- [`aiohttp`](https://pypi.org/project/aiohttp/)

Install dependencies:

```bash
pip install python-telegram-bot aiohttp
```
Setup
Clone this repository:

```bash

Copy code
git clone https://github.com/arynishere/crypto-price-telegram-bot.git
cd crypto-price-telegram-bot
```
Edit the script and set your Telegram bot token and channel ID:

```python
Copy code
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "-100XXXXXXXXX"  # Your channel or group ID
```
Run the bot:

```bash
Copy code
python price_bot.py
```
The bot will start sending cryptocurrency prices every 5 minutes and respond to /now commands.

Usage
/now → Get the current buy and sell prices for USDT, BTC, ETH

Example message sent by the bot:

yaml
Copy code
💵 USDT: خرید 114,476 تومان | فروش 115,000 تومان
🪙 BTC: خرید 13,972,814,636 تومان | فروش 14,000,000,000 تومان
💎 ETH: خرید 513,810,644 تومان | فروش 520,000,000 تومان
License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
arynisHere

GitHub: https://github.com/arynishere

Telegram bot creator and crypto enthusiast

yaml
Copy code

---

If you want, I can also **create the full GitHub repository structure** for you with:  

- `price_bot.py` (your main bot script)  
- `README.md` (this one)  
- `requirements.txt` with exact dependencies  

This way, you can **push directly to GitHub** and it will be ready to use.  

Do you want me to do that next?
