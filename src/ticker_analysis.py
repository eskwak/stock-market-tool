import yfinance as yf
import time 
import os 
from collections import defaultdict


def get_stock_prices_from_tickers(ticker_symbol_list: list) -> dict:
    """Returns dictionary with {ticker: [price, currency]}.

    Args:
        ticker_symbol_list (list): A string list containing ticker symbols.
    """
    stock_price_dict = defaultdict(list)
    
    for ticker_symbol in ticker_symbol_list:
        price_and_currency = yf_poll_stock_price(ticker_symbol)
        stock_price_dict[ticker_symbol] = price_and_currency
    
    return stock_price_dict


def yf_poll_stock_price(ticker_symbol, interval = 3) -> list:
    """Returns [price, currency] for a specific ticker.

    Args:
        ticker_symbol (str): A string representation of a ticker symbol ($msft)
    """
    ticker = yf.Ticker(ticker_symbol)
    last_price = ticker.fast_info["last_price"]
    currency = ticker.fast_info["currency"]
    time.sleep(interval)
    return [last_price, currency]