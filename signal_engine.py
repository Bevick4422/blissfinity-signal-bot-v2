# ========================================
# ENTRY CONFIRMATION
# ========================================

def bullish_setup(df):

    try:

        if df is None:
            return False

        if len(df) < 10:
            return False

        latest_close = (
            float(
                df["close"].iloc[-1]
            )
        )

        latest_open = (
            float(
                df["open"].iloc[-1]
            )
        )

        previous_high = (
            df["high"]
            .iloc[-6:-1]
            .max()
        )

        breakout = (
            latest_close >
            previous_high
        )

        bullish_candle = (
            latest_close >
            latest_open
        )

        if breakout and bullish_candle:

            print(
                "Bullish entry confirmed."
            )

            return True

        return False

    except Exception as e:

        print(
            f"Bullish entry error: {e}"
        )

        return False


def bearish_setup(df):

    try:

        if df is None:
            return False

        if len(df) < 10:
            return False

        latest_close = (
            float(
                df["close"].iloc[-1]
            )
        )

        latest_open = (
            float(
                df["open"].iloc[-1]
            )
        )

        previous_low = (
            df["low"]
            .iloc[-6:-1]
            .min()
        )

        breakdown = (
            latest_close <
            previous_low
        )

        bearish_candle = (
            latest_close <
            latest_open
        )

        if breakdown and bearish_candle:

            print(
                "Bearish entry confirmed."
            )

            return True

        return False

    except Exception as e:

        print(
            f"Bearish entry error: {e}"
        )

        return False