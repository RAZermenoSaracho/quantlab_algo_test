def generate_signal(ctx):

    history = ctx["history"]

    if len(history) < 5:
        return "HOLD"

    closes = [c["close"] for c in history]
    close_price = ctx["candle"]["close"]

    sma = sum(closes[-5:]) / 5

    if close_price > sma:
        return "BUY"

    if close_price < sma:
        return "SELL"

    return "HOLD"
