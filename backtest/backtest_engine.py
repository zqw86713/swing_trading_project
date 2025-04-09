import pandas as pd

def run_backtest(df: pd.DataFrame, signals: pd.Series, fee: float = 0.001) -> dict:
    df = df.copy()
    df["signal"] = signals

    capital = 10000
    position = 0
    entry_price = 0
    trades = []

    for i in range(1, len(df)):
        row = df.iloc[i]
        prev = df.iloc[i - 1]

        if row.signal == "buy" and position == 0:
            entry_price = row.close
            position = capital / entry_price
            capital = 0

        elif position > 0:
            hit_tp = row.high >= row.take_profit
            hit_sl = row.low <= row.stop_loss
            exit = row.signal == "sell"

            if hit_tp or hit_sl or exit:
                exit_price = row.take_profit if hit_tp else row.stop_loss if hit_sl else row.close
                capital = position * exit_price * (1 - fee)
                trades.append(capital)
                position = 0

    final_balance = capital if capital > 0 else position * df.iloc[-1].close
    total_return = (final_balance - 10000) / 10000 * 100

    return {
        "final_balance": round(final_balance, 2),
        "total_return_%": round(total_return, 2),
        "trades_count": len(trades)
    }
