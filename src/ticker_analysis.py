import yfinance as yf
import time 
import os 
from collections import defaultdict


def yf_get_stock_info(ticker_symbol_list: list, interval = 3) -> dict:
    """Returns a dictionary containing useful long-term investing information for all 
    ticker symbols inthe ticker_symbol_list.
    
    Args:
        ticker_symbol_list (list): A string list containing ticker symbols.
        interval (int): a sleep interval used to avoid DDOS bans from yahoo.

    Returns:
        dict: Returns dictionary with 
        {
            ticker: [
                currency type,
                last price,
                52-week high,
                percent off 52-week high (percent),
                trailing P/E ratio,
                forward P/E ratio,
                dividend yield (percent)
            ]
        }
    """
    stock_info_dict = defaultdict(list)
    
    for ticker_string in ticker_symbol_list:
        ticker = yf.Ticker(ticker_string)
        currency_type = ticker.fast_info["currency"]
        last_price = ticker.fast_info["last_price"]
        year_high = ticker.fast_info["year_high"]
        percent_off_high = ((last_price - year_high) / year_high) * 100.0
        
        # 'forwardPE' often returns 'None' with etfs.
        # .info() is used to avoid crashes for tickers with no forward P/E.
        trailing_pe = ticker.info.get("trailingPE")
        forward_pe = ticker.info.get("forwardPE")
        dividend_yield = ticker.info.get("dividendYield", 0)
        
        stock_info_dict[ticker_string] = [
            currency_type,
            last_price,
            year_high,
            percent_off_high,
            trailing_pe,
            forward_pe,
            dividend_yield
        ]
        
        time.sleep(interval)
    
    return stock_info_dict

def yf_get_portfolio_info_detailed(ticker_symbol_list: list, interval = 3):
    """ Returns a detailed dictionary with data for each ticker in the ticker symbol list.
        
        Args:
            ticker_symbol_list (_list_): A list of string ticker symbols.
            interval (_int_): Interval for yfinance -- prevents DOS restrictions. Defaulted to 3.
        
        Return:
            dict: Returns dictionary with:
                {
                    ticker: [
                        ...    
                    ]
                }
    """

    try:
        for ticker_symbol in ticker_symbol_list:
            pass
    except IndexError:
        print("ERROR: Index out of range. ticker_symbol_list is likely empty.")
        return None
    
    
# def get_stock_prices_from_tickers(ticker_symbol_list: list) -> dict:
#     """Returns dictionary with {ticker: [price, currency]}.

#     Args:
#         ticker_symbol_list (list): A string list containing ticker symbols.
#     """
#     stock_price_dict = defaultdict(list)
    
#     for ticker_symbol in ticker_symbol_list:
#         price_and_currency = yf_poll_stock_price(ticker_symbol)
#         stock_price_dict[ticker_symbol] = price_and_currency
    
#     return stock_price_dict


# def yf_poll_stock_price(ticker_symbol, interval = 3) -> list:
#     """Returns [price, currency] for a specific ticker.

#     Args:
#         ticker_symbol (str): A string representation of a ticker symbol ($msft)
#     """
#     ticker = yf.Ticker(ticker_symbol)
#     last_price = ticker.fast_info["last_price"]
#     currency = ticker.fast_info["currency"]
#     time.sleep(interval)
#     return [last_price, currency]
