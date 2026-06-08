import requests
import pandas as pd

# ========================================

# VALID MEXC INTERVALS

# ========================================

VALID_INTERVALS = {
"Min1",
"Min5",
"Min15",
"Min30",
"Min60",
"Hour4",
"Hour8",
"Day1",
"Week1",
"Month1"
}

# ========================================

# GET KLINES

# ========================================

def get_klines(
symbol,
timeframe,
limit=100
):


try:

    # --------------------------------
    # TIMEFRAME CHECK
    # --------------------------------

    if timeframe not in VALID_INTERVALS:

        print(
            f"{symbol} INVALID TIMEFRAME: {timeframe}"
        )

        return None

    url = (
        "https://contract.mexc.com"
        f"/api/v1/contract/kline/{symbol}"
        f"?interval={timeframe}"
    )

    print(
        f"{symbol} requesting:"
    )

    print(url)

    response = requests.get(
        url,
        timeout=15
    )

    if response.status_code != 200:

        print(
            f"{symbol} HTTP ERROR:"
        )

        print(response.status_code)

        return None

    data = response.json()

    # --------------------------------
    # API ERROR CHECK
    # --------------------------------

    if not isinstance(data, dict):

        print(
            f"{symbol} invalid response"
        )

        return None

    if data.get("success") is False:

        print(
            f"{symbol} API ERROR:"
        )

        print(data)

        return None

    if "data" not in data:

        print(
            f"{symbol} missing data field"
        )

        print(data)

        return None

    candles = data["data"]

    if not candles:

        print(
            f"{symbol} empty candle data"
        )

        return None

    required_keys = [
        "open",
        "high",
        "low",
        "close"
    ]

    for key in required_keys:

        if key not in candles:

            print(
                f"{symbol} missing key:"
            )

            print(key)

            return None

    df = pd.DataFrame({

        "open": candles["open"],
        "high": candles["high"],
        "low": candles["low"],
        "close": candles["close"]

    })

    df = df.astype(float)

    if len(df) < 20:

        print(
            f"{symbol} insufficient candles"
        )

        return None

    return df.tail(limit)

except Exception as e:

    print(
        f"{symbol} scanner error:"
    )

    print(e)

    return None


# ========================================

# MULTI-TIMEFRAME DATA

# ========================================

def get_market_data(
symbol,
trend_tf,
entry_tf
):


print(
    f"{symbol} TREND TF = {trend_tf}"
)

print(
    f"{symbol} ENTRY TF = {entry_tf}"
)

trend_df = get_klines(
    symbol,
    trend_tf
)

entry_df = get_klines(
    symbol,
    entry_tf
)

if trend_df is None:

    return None, None

if entry_df is None:

    return None, None

return trend_df, entry_df

