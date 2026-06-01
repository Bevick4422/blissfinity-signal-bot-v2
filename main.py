import asyncio

from config import (
    SYMBOLS,
    MAX_SIGNALS,
    TIMEFRAME
)

from scanner import get_klines

from signal_engine import (
    bullish_setup,
    bearish_setup
)

from telegram_sender import send_signal


async def scan_market():

    print("\n========================")
    print("BLISSFINITY V2")
    print("========================\n")

    # Telegram test
    try:

        await send_signal(
            "TEST",
            "SYSTEM ONLINE",
            0,
            0,
            0,
            0
        )

        print("Telegram test sent.\n")

    except Exception as e:

        print("Telegram test failed:")
        print(e)

    signals_sent = 0

    for pair in SYMBOLS:

        if signals_sent >= MAX_SIGNALS:
            break

        print(f"Scanning {pair}...")

        df = get_klines(
            pair,
            TIMEFRAME
        )

        if df is None:

            print(f"{pair} -> no data")
            continue

        latest_close = df["close"].iloc[-1]

        previous_high = (
            df["high"]
            .iloc[-6:-1]
            .max()
        )

        previous_low = (
            df["low"]
            .iloc[-6:-1]
            .min()
        )

        print(
            f"{pair} | "
            f"Close={latest_close:.4f} | "
            f"PrevHigh={previous_high:.4f} | "
            f"PrevLow={previous_low:.4f}"
        )

        # LONG

        if bullish_setup(df):

            entry = round(
                latest_close,
                4
            )

            stoploss = round(
                entry * 0.985,
                4
            )

            tp1 = round(
                entry * 1.02,
                4
            )

            tp2 = round(
                entry * 1.04,
                4
            )

            await send_signal(
                pair,
                "LONG",
                entry,
                stoploss,
                tp1,
                tp2
            )

            print(f"{pair} LONG sent")

            signals_sent += 1

        # SHORT

        elif bearish_setup(df):

            entry = round(
                latest_close,
                4
            )

            stoploss = round(
                entry * 1.015,
                4
            )

            tp1 = round(
                entry * 0.98,
                4
            )

            tp2 = round(
                entry * 0.96,
                4
            )

            await send_signal(
                pair,
                "SHORT",
                entry,
                stoploss,
                tp1,
                tp2
            )

            print(f"{pair} SHORT sent")

            signals_sent += 1

        await asyncio.sleep(1)

    print("\n========================")
    print("SCAN COMPLETE")
    print("========================\n")


import asyncio

async def main():

    while True:

        try:

            await scan_market()

            print(
                "\nSleeping for 5 minutes...\n"
            )

            await asyncio.sleep(300)

        except Exception as e:

            print(
                f"Bot error: {e}"
            )

            await asyncio.sleep(60)

import asyncio

async def main():

    while True:

        try:

            await scan_market()

            print(
                "\nSleeping for 5 minutes...\n"
            )

            await asyncio.sleep(300)

        except Exception as e:

            print(
                f"Bot error: {e}"
            )

            await asyncio.sleep(60)

import asyncio

async def main():

    while True:

        try:

            await scan_market()

            print(
                "\nSleeping for 5 minutes...\n"
            )

            await asyncio.sleep(300)

        except Exception as e:

            print(
                f"Bot error: {e}"
            )

            await asyncio.sleep(60)

if __name__ == "__main__":

    asyncio.run(main())