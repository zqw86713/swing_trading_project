import pandas as pd

def generate_signals(df: pd.DataFrame) -> pd.Series:
    signal = pd.Series("hold", index=df.index)

    buy_condition = (
        (df["rsi"] < 30) &
        (df["macd"].shift(1) < df["macd_signal"].shift(1)) &
        (df["macd"] > df["macd_signal"])
    )

    sell_condition = (
        (df["rsi"] > 70) &
        (df["macd"].shift(1) > df["macd_signal"].shift(1)) &
        (df["macd"] < df["macd_signal"])
    )

    signal[buy_condition] = "buy"
    signal[sell_condition] = "sell"

    return signal
