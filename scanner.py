import pandas as pd
import yfinance as yf

from indicators import calculate_indicators
from universe import get_symbols

def calculate_score(row):

    score = 0

    if row["EMA50"] > row["EMA200"]:
        score += 20

    if row["EMA21"] > row["EMA50"]:
        score += 20

    if 50 <= row["RSI"] <= 70:
        score += 15

    if row["ATR_PCT"] > 2.5:
        score += 15

    if row["Close"] > row["EMA200"]:
        score += 20

    if row["DistanceATH"] < 15:
        score += 10

    return score

def scan_market(
    index_choice,
    ema50_over_ema200=True,
    ema21_over_ema50=True,
    use_rsi=True,
    rsi_min=50,
    rsi_max=70,
    atr_threshold=2.5,
    min_score=60
):

    symbols = get_symbols(index_choice)

    results = []

    for symbol in symbols:

        try:
            df = yf.download(
                symbol,
                period="1y",
                progress=False,
                auto_adjust=True
            )

            if df.empty or len(df) < 200:
                continue

            df = calculate_indicators(df)

            latest = df.iloc[-1]

            if ema50_over_ema200:
                if latest["EMA50"] <= latest["EMA200"]:
                    continue

            if ema21_over_ema50:
                if latest["EMA21"] <= latest["EMA50"]:
                    continue

            if use_rsi:
                if not (rsi_min <= latest["RSI"] <= rsi_max):
                    continue

            if latest["ATR_PCT"] < atr_threshold:
                continue

            score = calculate_score(latest)

            if score >= min_score:

                results.append({
                    "Ticker": symbol,
                    "Score": score,
                    "Close": round(float(latest["Close"]), 2),
                    "EMA21": round(float(latest["EMA21"]), 2),
                    "EMA50": round(float(latest["EMA50"]), 2),
                    "EMA200": round(float(latest["EMA200"]), 2),
                    "RSI": round(float(latest["RSI"]), 2),
                    "ATR %": round(float(latest["ATR_PCT"]), 2),
                    "ATH Abstand %": round(float(latest["DistanceATH"]), 2)
                })

        except Exception as e:
            print(f"Fehler bei {symbol}: {e}")

    results_df = pd.DataFrame(results)

    if not results_df.empty:
        results_df = results_df.sort_values(
            by="Score",
            ascending=False
        )

    return results_df