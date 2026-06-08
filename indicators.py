import pandas as pd

def calculate_rsi(series, period=14):

    delta = series.diff()

    gain = delta.clip(lower=0).rolling(period).mean()
    loss = -delta.clip(upper=0).rolling(period).mean()

    rs = gain / loss

    return 100 - (100 / (1 + rs))

def calculate_atr(df, period=14):

    high_low = df["High"] - df["Low"]

    high_close = (df["High"] - df["Close"].shift()).abs()

    low_close = (df["Low"] - df["Close"].shift()).abs()

    ranges = pd.concat(
        [high_low, high_close, low_close],
        axis=1
    )

    true_range = ranges.max(axis=1)

    return true_range.rolling(period).mean()

def calculate_indicators(df):

    df["EMA21"] = df["Close"].ewm(span=21).mean()

    df["EMA50"] = df["Close"].ewm(span=50).mean()

    df["EMA200"] = df["Close"].ewm(span=200).mean()

    df["RSI"] = calculate_rsi(df["Close"])

    df["ATR"] = calculate_atr(df)

    df["ATR_PCT"] = (
        df["ATR"] / df["Close"]
    ) * 100

    ath = df["Close"].max()

    df["DistanceATH"] = (
        (ath - df["Close"]) / ath
    ) * 100

    return df