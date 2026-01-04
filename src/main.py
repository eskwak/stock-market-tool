import ticker_analysis
import time

def main():
    ticker_symbol_list = [
        "aapl",
        "nvda",
        "msft",
        "pltr"
    ]
    
    stock_price_dict = ticker_analysis.get_stock_prices_from_tickers(ticker_symbol_list)
    # print(stock_price_dict)
    
    while True:
        try:
            for ticker in stock_price_dict.keys():
                price, currency = stock_price_dict[ticker][0], stock_price_dict[ticker][1]
                print(f"Ticker: {ticker} | Price: {price:.2f} {currency}")
        except KeyboardInterrupt:
            print("Stopped monitoring.")
            break
        print()
        time.sleep(3)

if __name__ == "__main__":
    main()