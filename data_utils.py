import yfinance as yf
import pandas as pd

def load_data(start="2020-01-01", end="2026-01-01"):
    
    tickers = {
        "oil": "BZ=F",
        "rep": "REP.MC",
        "bp": "BP",
        "shell": "SHEL",
        "exxon": "XOM",
        "chevron": "CVX"
    }
    
    data = {}
    
    for name, ticker in tickers.items():
        df = yf.download(ticker, start=start, end=end, auto_adjust=True)
        
        if not df.empty:
            data[name] = df["Close"]
    
    df = pd.concat(data, axis=1)
    df.columns = data.keys()
    
    df = df.dropna()
    
    returns = df.pct_change().dropna()
    
    return df, returns