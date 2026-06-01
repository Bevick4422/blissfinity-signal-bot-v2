from telegram import Bot
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

bot = Bot(token=TELEGRAM_TOKEN)


async def send_signal(
    pair,
    direction,
    entry,
    stoploss,
    tp1,
    tp2
):
    message = f"""
🚨 BLISSFINITY V2

Pair: {pair}

Direction: {direction}

Entry: {entry}

Stop Loss: {stoploss}

TP1: {tp1}

TP2: {tp2}
"""

    await bot.send_message(
        chat_id=TELEGRAM_CHAT_ID,
        text=message
    )

    print(
        f"{pair} {direction} signal sent."
    )