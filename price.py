import aiohttp
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, JobQueue

TELEGRAM_TOKEN = "YOUR_TOKEN"
CHAT_ID = "-1003187181841"  # Channel ID

# Coins we want to track
COINS = {
    "USDT": "💵",
    "BTC": "🪙",
    "ETH": "💎"
}

# Fetch prices from Bitpin
async def get_prices():
    url = "https://api.bitpin.ir/v1/mkt/markets/"
    result = {}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.json()
                for market in data.get("results", []):
                    code = market["currency1"]["code"]
                    if code in COINS and market["currency2"]["code"] == "IRT":
                        buy_price = float(market.get("internal_price_info", {}).get("price", 0))
                        sell_price = float(market.get("price_info", {}).get("price", 0))
                        result[code] = (buy_price, sell_price)
    except Exception as e:
        print("Error fetching prices:", e)
    return result

# Format numbers with commas
def format_number(n):
    try:
        return "{:,.0f}".format(n)
    except:
        return "❌"

# Send prices automatically
async def send_prices(context: ContextTypes.DEFAULT_TYPE):
    prices = await get_prices()
    msg = ""
    for coin, emoji in COINS.items():
        if coin in prices:
            buy, sell = prices[coin]
            msg += f"{emoji} {coin}: Buy {format_number(buy)} Toman | Sell {format_number(sell)} Toman\n"
        else:
            msg += f"{emoji} {coin}: ❌ Error fetching price\n"
    await context.bot.send_message(chat_id=CHAT_ID, text=msg)

# Command /now to fetch current prices
async def now_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prices = await get_prices()
    msg = ""
    for coin, emoji in COINS.items():
        if coin in prices:
            buy, sell = prices[coin]
            msg += f"{emoji} {coin}: Buy {format_number(buy)} Toman | Sell {format_number(sell)} Toman\n"
        else:
            msg += f"{emoji} {coin}: ❌ Error fetching price\n"
    await update.message.reply_text(msg)

# Main function
def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("now", now_command))

    job_queue: JobQueue = app.job_queue
    job_queue.run_repeating(send_prices, interval=300, first=5)  # Every 5 minutes

    print("Bot started ✅")
    app.run_polling()

if __name__ == "__main__":
    main()
