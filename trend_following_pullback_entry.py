CONFIG = {
    "signal_mode": "trend_following",

    "fast_ma_window": 20,
    "slow_ma_window": 100,

    "rsi_window": 14,
    "rsi_entry_threshold": 40,
    "rsi_exit_threshold": 65,

    "batch_size": 100,
    "batch_size_type": "percent_balance",

    "stop_loss_pct": 5,
    "take_profit_pct": 15,

    "direction": "long_only",

    "min_bars": 120
}


def generate_signal(ctx):

    indicators = ctx["indicators"]
    position = ctx["position"]
    candle = ctx["candle"]

    ema_fast = indicators["ema_fast"]
    ema_slow = indicators["ema_slow"]
    rsi = indicators["rsi"]

    price = candle["close"]

    if ema_fast is None or ema_slow is None or rsi is None:
        return "HOLD"

    trend_up = ema_fast > ema_slow

    # ENTRY
    if position is None:

        pullback = rsi < CONFIG["rsi_entry_threshold"]

        if trend_up and pullback and price > ema_slow:
            return "LONG"

        return "HOLD"

    # EXIT
    else:

        if rsi > CONFIG["rsi_exit_threshold"]:
            return "CLOSE"

        if price < ema_slow:
            return "CLOSE"

        return "HOLD"
