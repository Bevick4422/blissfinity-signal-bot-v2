import asyncio

from config import (
    SYMBOLS,
    MAX_SIGNALS,
    TREND_TIMEFRAME,
    ENTRY_TIMEFRAME
)

from scanner import (
    get_market_data
)

from signal_engine import (
    bullish_structure,
    bearish_structure,
    bullish_setup,
    bearish_setup
)

from telegram_sender import (
    send_signal
)

from trade_tracker import (
    main as run_tracker
)

# ========================================
# MARKET SCANNER
# ========================================

async def scan_market():

    print("\n========================")
    print("BLISSFINITY V2.1")
    print("========================\n")

    signals_sent = 0

    for pair in SYMBOLS:

        if signals_sent >= MAX_SIGNALS:
            break

        print(f"Scanning {pair}...")

        trend_df, entry_df = get_market_data(
            pair,
            TREND_TIMEFRAME,
            ENTRY_TIMEFRAME
        )

        if trend_df is None or entry_df is None:

            print(
                f"{pair} -> no data"
            )

            continue

        # ====================================
        # LONG
        # ====================================

        if (
            bullish_structure(trend_df)
            and
            bullish_setup(entry_df)
        ):

            entry = round(
                float(
                    entry_df["close"].iloc[-1]
                ),
                4
            )

            stoploss = round(
                entry * 0.97,
                4
            )

            tp1 = round(
                entry * 1.05,
                4
            )

            tp2 = round(
                entry * 1.10,
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

            print(
                f"{pair} LONG sent"
            )

            signals_sent += 1

        # ====================================
        # SHORT
        # ====================================

        elif (
            bearish_structure(trend_df)
            and
            bearish_setup(entry_df)
        ):

            entry = round(
                float(
                    entry_df["close"].iloc[-1]
                ),
                4
            )

            stoploss = round(
                entry * 1.03,
                4
            )

            tp1 = round(
                entry * 0.95,
                4
            )

            tp2 = round(
                entry * 0.90,
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

            print(
                f"{pair} SHORT sent"
            )

            signals_sent += 1

        await asyncio.sleep(1)

    print("\n========================")
    print("SCAN COMPLETE")
    print("========================\n")


# ========================================
# MASTER LOOP
# ========================================

async def main():

    while True:

        try:

            await scan_market()

            try:

                await run_tracker()

            except Exception as e:

                print(
                    f"Tracker error: {e}"
                )

            print(
                "\nSleeping for 5 minutes...\n"
            )

            await asyncio.sleep(300)

        except Exception as e:

            print(
                f"Bot error: {e}"
            )

            await asyncio.sleep(60)


# ========================================
# START
# ========================================

if __name__ == "__main__":

    asyncio.run(main())