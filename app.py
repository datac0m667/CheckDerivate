import streamlit as st
from scanner import scan_market
from strategy_loader import load_strategy_names, load_strategy

st.set_page_config(page_title="Derivate Scanner", layout="wide")

st.title("📈 Derivate Aktien Scanner")

index_choice = st.sidebar.multiselect(
    "Indizes",
    ["DAX", "S&P500", "Nasdaq100", "EuroStoxx50"],
    default=["DAX", "Nasdaq100"]
)

strategy_names = load_strategy_names()

selected_strategy = st.sidebar.selectbox(
    "Strategieprofil",
    strategy_names
)

strategy = load_strategy(selected_strategy)

ema50_over_ema200 = st.sidebar.checkbox(
    "EMA50 > EMA200",
    value=strategy["ema50_over_ema200"]["enabled"]
)

ema21_over_ema50 = st.sidebar.checkbox(
    "EMA21 > EMA50",
    value=strategy["ema21_over_ema50"]["enabled"]
)

use_rsi = st.sidebar.checkbox(
    "RSI Filter",
    value=strategy["rsi_filter"]["enabled"]
)

rsi_min = st.sidebar.slider("RSI Minimum", 0, 100, 50)
rsi_max = st.sidebar.slider("RSI Maximum", 0, 100, 70)

atr_threshold = st.sidebar.slider(
    "ATR Mindestwert (%)",
    0.0,
    10.0,
    2.5
)

min_score = st.sidebar.slider(
    "Mindestscore",
    0,
    100,
    60
)

if st.button("Scanner starten"):

    results = scan_market(
        index_choice=index_choice,
        ema50_over_ema200=ema50_over_ema200,
        ema21_over_ema50=ema21_over_ema50,
        use_rsi=use_rsi,
        rsi_min=rsi_min,
        rsi_max=rsi_max,
        atr_threshold=atr_threshold,
        min_score=min_score
    )

    if results.empty:
        st.warning("Keine Treffer gefunden")
    else:
        st.success(f"{len(results)} Treffer gefunden")
        st.dataframe(results, use_container_width=True)