from data.download import fetch_price_data
from indicators.ta_utils import calculate_indicators
from strategy.signal_generator import generate_signals
from backtest.backtest_engine import run_backtest
from alerts.alert_engine import send_alert
from risk_control.exit_manager import apply_exit_rules

def main():
    symbol = "XRP/USDT"
    df = fetch_price_data(symbol)

    df = calculate_indicators(df)
    signals = generate_signals(df)
    df = apply_exit_rules(df, signals)

    results = run_backtest(df, signals)
    print(results)

    if signals.iloc[-1] == "buy":
        send_alert(symbol, "Buy signal detected!")

if __name__ == "__main__":
    main()
