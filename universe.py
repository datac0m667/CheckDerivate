def get_symbols(index_choice):

    dax = [
        "SAP.DE",
        "SIE.DE",
        "ALV.DE",
        "DTE.DE",
        "BMW.DE"
    ]

    nasdaq = [
        "AAPL",
        "MSFT",
        "NVDA",
        "AMZN",
        "META"
    ]

    sp500 = [
        "JPM",
        "XOM",
        "UNH",
        "V",
        "MA"
    ]

    eurostoxx = [
        "ASML.AS",
        "MC.PA",
        "OR.PA",
        "SAN.MC"
    ]

    symbols = []

    if "DAX" in index_choice:
        symbols.extend(dax)

    if "Nasdaq100" in index_choice:
        symbols.extend(nasdaq)

    if "S&P500" in index_choice:
        symbols.extend(sp500)

    if "EuroStoxx50" in index_choice:
        symbols.extend(eurostoxx)

    return sorted(list(set(symbols)))