prices = []

def generate_signal(candle):
    # RAZS TEST 2
    global prices

    close_price = candle["close"]
    prices.append(close_price)

    # Wait until we have enough data
    if len(prices) < 5:
        return "HOLD"

    # Simple moving average
    sma = sum(prices[-5:]) / 5

    if close_price > sma:
        return "BUY"
    elif close_price < sma:
        return "SELL"
    else:
        return "HOLD"
