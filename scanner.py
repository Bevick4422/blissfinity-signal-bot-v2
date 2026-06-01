import requests
import pandas as pd


def get_klines(symbol, interval="Min15", limit=50):

    try:

        url = (
            f"https://contract.mexc.com"
            f"/api/v1/contract/kline/{symbol}"
            f"?interval={interval}"
        )

        response = requests.get(
            url,
            timeout=10
        )

        data = response.json()

        candles = data.get(
            "data",
            {}
        )

        if not candles:
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

        print(f"{symbol} data error:")

        print(e)

        return None