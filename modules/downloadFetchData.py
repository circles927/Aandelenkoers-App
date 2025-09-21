# I want to download the necessary data in this module
from dotenv import load_dotenv
import os
import requests
import pandas as pd
from datetime import datetime, timezone

load_dotenv()  # take environment variables from .env.
API_KEY_ALPHAV = os.getenv('API_KEY_ALPHAV')
API_KEY_FINNHUB = os.getenv('API_KEY_FINNHUB')

def fetch_alphavantage_data(symbol, market, outputsize='compact'):
    base_url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "market": market,
        "outputsize": outputsize,
        "apikey": API_KEY_ALPHAV,
        "datatype": "csv"
    }
    response = requests.get(base_url, params=params, timeout=10)
    if response.status_code == 200:
        with open(f"../data/raw/{symbol}_{market}.csv", "w") as f:
            f.write(response.text)
        return response.text  # CSV data as text
    else:
        response.raise_for_status()

def fetch_finnhub_data(symbol, start="2005-01-01", end=None):
    base_url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY_FINNHUB}"
    
    params = {
        "symbol": symbol,
        "resolution": "D",
        "from": _to_unix(start),
        "to": _to_unix(end),
        "token": API_KEY_FINNHUB,
    }

    response = requests.get(base_url, params=params, timeout=10)
    if response.status_code == 200:
        with open(f"../data/raw/{symbol}_finnhub.json", "w") as f:
            f.write(response.text)
        return response.json()
    else:
        response.raise_for_status()

def _to_unix(date_str):
    if date_str is None:
        return int(datetime.now(timezone.utc).timestamp())
    return int(pd.to_datetime(date_str).tz_localize(timezone.utc).timestamp())

if __name__ == "__main__":
    print(f"AlphaVantage data: {fetch_alphavantage_data('TSCO.LON', 'LON')}")
    print(f"Finnhub data: {fetch_finnhub_data('AAPL')}")