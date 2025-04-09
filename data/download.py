import ccxt
import pandas as pd
from datetime import datetime, timedelta

exchange = ccxt.binance()

def fetch_price_data(symbol: str = "XRP/USDT", timeframe: str = "1h", since_days: int = 90) -> pd.DataFrame:
    since = exchange.parse8601((datetime.utcnow() - timedelta(days=since_days)).strftime('%Y-%m-%dT%H:%M:%S'))
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, since=since)
    df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("timestamp", inplace=True)
    df = df.astype(float)
    return df
