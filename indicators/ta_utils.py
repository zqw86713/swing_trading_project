import pandas as pd
import numpy as np

def calculate_rsi(df: pd.DataFrame, period: int = 14, column: str = "close") -> pd.Series:
    delta = df[column].diff()
    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_ema(df: pd.DataFrame, period: int = 20, column: str = "close") -> pd.Series:
    return df[column].ewm(span=period, adjust=False).mean()

def calculate_macd(df: pd.DataFrame, fast: int = 12, slow: int = 26, signal: int = 9) -> pd.DataFrame:
    ema_fast = calculate_ema(df, period=fast)
    ema_slow = calculate_ema(df, period=slow)
    macd = ema_fast - ema_slow
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    histogram = macd - signal_line
    df["macd"] = macd
    df["macd_signal"] = signal_line
    df["macd_hist"] = histogram
    return df

def calculate_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df["rsi"] = calculate_rsi(df)
    df["ema20"] = calculate_ema(df, 20)
    df["ema50"] = calculate_ema(df, 50)
    df = calculate_macd(df)
    return df
