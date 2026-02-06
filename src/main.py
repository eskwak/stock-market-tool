import ticker_analysis
import time
import tkinter as tk

# List of tickers selected.
tracked_tickers = []

def add_new_ticker(ticker_entry, tracked_tickers_label):
    """Adds new ticker to tracked tickers list if it's not already being tracked.

    Args:
        ticker_entry (tk.Entry): New ticker to track.
        tracked_tickers_label (tk.Label): Label to display tracked tickers.
    """
    ticker_symbol = ticker_entry.get().strip().lower()
    if ticker_symbol and ticker_symbol not in tracked_tickers:
        tracked_tickers.append(ticker_symbol)
        tracked_tickers_label.config(text = f"Tracking: {', '.join(tracked_tickers)}")
        ticker_entry.delete(0, tk.END)
    elif ticker_symbol in tracked_tickers:
        print(f"${ticker_symbol} is alreaady being tracked.")

def main():
    """Main. Sets up and runs the dashboard.
    """
    master = tk.Tk()
    master.title("Market Analysis Tool Dashboard")
    master.geometry("1600x800")
    master.configure(bg="#D4F3FC")
    
    # Entry to add new tickers to track.
    add_ticker_instruction_label = tk.Label(master, text = "Enter ticker symbol (e.g. aapl):")
    add_ticker_instruction_label.pack(side = "top", anchor = "nw", padx = 20, pady = (20, 0))
    new_ticker_entry = tk.Entry(master)
    new_ticker_entry.pack(side = "top", anchor = "nw", padx = 35, pady = (5, 0))
    
    # Label to display tracked tickers.
    tracked_tickers_label = tk.Label(master, text = "Tracking: None", wraplength = 350)
    tracked_tickers_label.pack(side = "top", anchor = "nw", padx = 50, pady = (5, 0))
    
    # Button to add new tickers to ticker list.
    add_ticker_button = tk.Button(
        master,
        text = "Add to list",
        command = lambda: add_new_ticker(new_ticker_entry, tracked_tickers_label)
    )
    add_ticker_button.pack(side = "top", anchor = "nw", padx = 60, pady = (5, 0))
    
    # Data frame for tracked tickers.
    ticker_data_frame = tk.Frame(master)
    ticker_data_frame.pack(side = "top", anchor = "nw", padx = 20, pady = 20)
    
    # Data frame headers.
    tk.Label(ticker_data_frame, text = "Last Price").grid(row = 0, column = 0, padx = 10)
    tk.Label(ticker_data_frame, text = "Year High").grid(row = 0, column = 1, padx = 10)
    tk.Label(ticker_data_frame, text = "Percent Off Year High").grid(row = 0, column = 2, padx = 10)
    tk.Label(ticker_data_frame, text = "Trailing P/E").grid(row = 0, column = 3, padx = 10)
    tk.Label(ticker_data_frame, text = "Forward P/E").grid(row = 0, column = 4, padx = 10)
    tk.Label(ticker_data_frame, text = "Dividend Yield").grid(row = 0, column = 5, padx = 10)
    
    
    # If there are tickers being tracked, extract data and output to dashboard.
    if len(tracked_tickers) > 0:
        stock_info_dict = ticker_analysis.yf_get_stock_info(tracked_tickers)
        
        while True:
            try:
                for ticker in stock_info_dict.keys():
                    currency_type = stock_info_dict[ticker][0]
                    last_price = stock_info_dict[ticker][1]
                    year_high = stock_info_dict[ticker][2]
                    percent_off_high = stock_info_dict[ticker][3]
                    trailing_pe = stock_info_dict[ticker][4]
                    forward_pe = stock_info_dict[ticker][5]
                    dividend_yield = stock_info_dict[ticker][6]
            except KeyboardInterrupt:
                ### Interrupt will never be caught here. ###
                print("Stopped monitoring.")
                break
    
    master.mainloop()

    
def pre_gui():
    """Decpreciated code prior to implementing a GUI.
    """
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
    ######################
    ### END OF PRE-GUI ###
    ######################
    
if __name__ == "__main__":
    main()