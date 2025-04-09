import pandas as pd

def apply_exit_rules(df: pd.DataFrame, signals: pd.Series,
                     stop_loss_pct: float = 0.03,
                     take_profit_pct: float = 0.06) -> pd.DataFrame:
    df = df.copy()
    df["signal"] = signals
    df["entry_price"] = df["close"].where(df["signal"] == "buy")
    df["entry_price"] = df["entry_price"].ffill()

    df["stop_loss"] = df["entry_price"] * (1 - stop_loss_pct)
    df["take_profit"] = df["entry_price"] * (1 + take_profit_pct)

    return df
