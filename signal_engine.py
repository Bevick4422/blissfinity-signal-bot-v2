def bullish_structure(df):

    try:

        latest_close = (
            df["close"].iloc[-1]
        )

        previous_high = (
            df["high"]
            .iloc[-20:-1]
            .max()
        )

        return (
            latest_close >
            previous_high
        )

    except Exception as e:

        print(
            f"Bullish structure error: {e}"
        )

        return False


def bearish_structure(df):

    try:

        latest_close = (
            df["close"].iloc[-1]
        )

        previous_low = (
            df["low"]
            .iloc[-20:-1]
            .min()
        )

        return (
            latest_close <
            previous_low
        )

    except Exception as e:

        print(
            f"Bearish structure error: {e}"
        )

        return False


# ========================================
# ENTRY CONFIRMATION
# ========================================

def bullish_setup(df):

    try:

        latest_close = (
            df["close"].iloc[-1]
        )

        latest_open = (
            df["open"].iloc[-1]
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

        return (
            breakout and
            bullish_candle
        )

    except Exception as e:

        print(
            f"Bullish setup error: {e}"
        )

        return False


def bearish_setup(df):

    try:

        latest_close = (
            df["close"].iloc[-1]
        )

        latest_open = (
            df["open"].iloc[-1]
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

        return (
            breakdown and
            bearish_candle
        )

    except Exception as e:

        print(
            f"Bearish setup error: {e}"
        )

        return False