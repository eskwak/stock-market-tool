import ticker_analysis
import time
import tkinter as tk
import threading

# List of tickers selected #
tracked_tickers_list = []

# Custom colors #
window_background_color = "#303030"
new_ticker_frame_color = "#C3CEFA"
tracked_tickers_list_frame_color = "#EDC3FA"
        
def add_new_ticker(new_ticker_label, tracked_tickers_list_label):
    """ Adds new ticker to tracked tickers list if it's not already being tracked.

    Args:
        new_ticker_label (tk.Entry): The string content from new ticker entry.
        tracked_tickers_list_label (tk.Label): Label to display tracked tickers.
    """
    ticker_symbol = new_ticker_label.get().strip().lower()
    if not ticker_symbol:
        return
    
    if len(tracked_tickers_list) == 5:
        print("ERROR: Currently tracking the maximum number of tickers.")
        print("Tracked Tickers:")
        for i in range(len(tracked_tickers_list)):
            print(f"{i + 1}. ${tracked_tickers_list[i]}")
            
    if ticker_symbol not in tracked_tickers_list and len(tracked_tickers_list) < 5:
        tracked_tickers_list.append(ticker_symbol)
        tracked_tickers_list_label.config(text = f"Tracking: {"  ".join(tracked_tickers_list)}")
        new_ticker_label.delete(0, tk.END)
    elif ticker_symbol in tracked_tickers_list:
        print(f"${ticker_symbol} is already being tracked.")

def monitor_tickers():
    """ Function to run in the background to fetch stock data.
    """
    query_count = 0
    while True:
        if len(tracked_tickers_list) > 0:
            ticker_info_dict = ticker_analysis.yf_get_stock_info(tracked_tickers_list)
            for ticker, info in ticker_info_dict.items():
                query_count += 1
                # For debug only #
                # print(f"Query Count: {query_count}")
                # print(f"Ticker: ${ticker}")
                # print(f"Last Price: {info[1]}")
            time.sleep(5)
        else:
            time.sleep(1)

def main():
    ### GUI WINDOW SETUP ### 
    window = tk.Tk()
    window.title("Market Monitoring Tool Dashboard")
    window.geometry("1600x800")
    window.configure(background = window_background_color)
    
    ### ADDING NEW TICKERS ### 
    new_ticker_frame = tk.Frame(window, background = new_ticker_frame_color)
    new_ticker_frame.place(x = 0, y = 0)
    
    # Label for the new ticker entry. #
    new_ticker_label = tk.Label(
        new_ticker_frame,
        text = "Enter ticker symbol (e.g., aapl):",
        background = new_ticker_frame_color
    )
    new_ticker_label.grid(row = 0, column = 0)
    
    # Entry field for user's to enter new tickers to be tracked. #
    new_ticker_entry = tk.Entry(
        new_ticker_frame,
        background = new_ticker_frame_color,
    )
    new_ticker_entry.grid(row = 1, column = 0)
    
    # Button to confirm new ticker to be added to the list of tracked tickers. #
    new_ticker_button = tk.Button(
        new_ticker_frame,
        text = "Press to add ticker",
        background = new_ticker_frame_color,
        command = lambda: add_new_ticker(new_ticker_entry, tracked_tickers_list_label)
    )
    new_ticker_button.grid(row = 2, column = 0)
    
    ### DISPLAY TRACKED TICKERS ###
    tracked_tickers_list_frame = tk.Frame(window, background = tracked_tickers_list_frame_color)
    tracked_tickers_list_frame.place(x = 200, y = 0)
    
    # Text label to show which tickers are currently being tracked. #
    tracked_tickers_list_label = tk.Label(
        tracked_tickers_list_frame,
        text = "Tracking: None",
        wraplength = 300,
        background = tracked_tickers_list_frame_color,
    )
    tracked_tickers_list_label.grid(row = 0, column = 0)
    
    ### MONITORING TICKERS ###
    monitoring_thread = threading.Thread(target = monitor_tickers, daemon = True)
    monitoring_thread.start()
    
    # Tkinter event loop #
    window.mainloop()
    

    
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