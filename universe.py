import pandas as pd
import streamlit as st

@st.cache_data(ttl=86400)
def get_sp500_symbols():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

    tables = pd.read_html(url)

    df = tables[0]

    return sorted(df["Symbol"].tolist())


@st.cache_data(ttl=86400)
def get_nasdaq100_symbols():
    url = "https://en.wikipedia.org/wiki/Nasdaq-100"

    tables = pd.read_html(url)

    for table in tables:
        cols = [str(c) for c in table.columns]

        if "Ticker" in cols:
            symbols = table["Ticker"].tolist()

            return sorted(
                [
                    str(x).replace(".", "-")
                    for x in symbols
                ]
            )

    return []


@st.cache_data(ttl=86400)
def get_dax40_symbols():

    url = "https://en.wikipedia.org/wiki/DAX"

    tables = pd.read_html(url)

    for table in tables:

        cols = [str(c) for c in table.columns]

        if "Ticker symbol" in cols:

            tickers = table["Ticker symbol"].tolist()

            return sorted(
                [
                    f"{x}.DE"
                    for x in tickers
                ]
            )

    return []


@st.cache_data(ttl=86400)
def get_eurostoxx50_symbols():

    url = "https://en.wikipedia.org/wiki/EURO_STOXX_50"

    tables = pd.read_html(url)

    for table in tables:

        cols = [str(c) for c in table.columns]

        if "Ticker" in cols:

            return sorted(
                table["Ticker"].astype(str).tolist()
            )

    return []


def get_symbols(index_choice):

    symbols = []

    if "DAX" in index_choice:
        symbols.extend(get_dax40_symbols())

    if "Nasdaq100" in index_choice:
        symbols.extend(get_nasdaq100_symbols())

    if "S&P500" in index_choice:
        symbols.extend(get_sp500_symbols())

    if "EuroStoxx50" in index_choice:
        symbols.extend(get_eurostoxx50_symbols())

    return sorted(list(set(symbols)))
