import requests
import pandas as pd

# ========================================
# MEXC KLINES
# ========================================

def get_klines(
    symbol,
    timeframe,
    limit=100
):

    try:

        url = (
            "https://contract.mexc.com"
            f"/api/v1/contract/kline/{symbol}"
            f"?interval={timeframe}"
        )

        response = requests.get(
            url,
            timeout=15
        )

        if response.status_code != 200:

            print(
                f"{symbol} API error: "
                f"{response.status_code}"
            )

            return None

        data = response.json()

        if "data" not in data:

            print(
                f"{symbol} no data returned"
            )

            return None

        candles = data["data"]

        if len(candles["close"]) < 20:

            print(
                f"{symbol} insufficient candles"
            )

            return None

        df = pd.DataFrame({

            "open": candles["open"],

            "high": candles["high"],

            "low": candles["low"],

            "close": candles["close"]

        })

        df = df.astype(float)

        return df.tail(limit)

    except Exception as e:

        print(
            f"{symbol} data error:"
        )

        print(e)

        return None


# ========================================
# TREND + ENTRY DATA
# ========================================

def get_market_data(
    symbol,
    trend_timeframe,
    entry_timeframe
):

    trend_df = get_klines(
        symbol,
        trend_timeframe
    )

    entry_df = get_klines(
        symbol,
        entry_timeframe
    )

    if trend_df is None:

        return None, None

    if entry_df is None:

        return None, None

    return trend_df, entry_df