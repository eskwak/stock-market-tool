import ticker_analysis
import time

def main():
    ticker_symbol_list = [
        "aapl",
        "nvda",
        "msft",
        "pltr",
        "voo",
        "vea",
        "shld"
    ]
    
    stock_info_dict = ticker_analysis.yf_get_stock_info(ticker_symbol_list)
    # Order of returns:
    # dict[0]: currency type
    # dict[1]: last price
    # dict[2]: 52-week high
    # dict[3]: percent off 52-week high (percent)
    # dict[4]: trailing P/E ratio
    # dict[5]: forward P/E ratio
    # dict[6]: dividend yield (percent)
    
    # print(stock_info_dict)
    
    while True:
        try:
            # All info to be put on dashboard later.
            for ticker in stock_info_dict.keys():
                currency_type = stock_info_dict[ticker][0]
                last_price = stock_info_dict[ticker][1]
                year_high = stock_info_dict[ticker][2]
                percent_off_high = stock_info_dict[ticker][3]
                trailing_pe = stock_info_dict[ticker][4]
                forward_pe = stock_info_dict[ticker][5]
                dividend_yield = stock_info_dict[ticker][6]
                
                print(f"${ticker}")
                print(f"Price: ${last_price:.2f} {currency_type}")
                print(f"52-Week High: ${year_high:.2f}")
                print(f"Percent Off 52-Week High: {percent_off_high:.2f}%")
                print(f"Trailing P/E: {trailing_pe}")
                print(f"Forward P/E: {forward_pe}")
                print(f"Dividend Yield: {dividend_yield:.2f}%\n")
                
        except KeyboardInterrupt:
            print("Stopped monitoring.")
            break

        print("\n\n")
        time.sleep(3)

if __name__ == "__main__":
    main()