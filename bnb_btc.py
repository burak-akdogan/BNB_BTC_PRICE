import requests
import time
import datetime
import tkinter as tk
from tkinter import messagebox

prev_bnb_btc_price = None

# API
def get_price(coin):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=btc"
    response = requests.get(url)
    data = response.json()
    price = data[coin]['btc']
    return price

root = tk.Tk()
root.withdraw()

#Target price for alert
target_price = 0.00661

while True:
    bnb_btc_price = get_price('binancecoin')
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Price Change
    if prev_bnb_btc_price is not None:
        price_change = bnb_btc_price - prev_bnb_btc_price
        if price_change > 0:
            price_direction = "⬆️ up"
        elif price_change < 0:
            price_direction = "⬇️ down"
        else:
            price_direction = "⏺ unchanged"
        
        # Alert if price reaches target price
        if bnb_btc_price >= target_price:
            messagebox.showinfo(title="Alert", message=f"BNB/BTC price has reached {target_price} BTC!\n\nCurrent Time: {current_time}", icon=messagebox.INFO)
        
        # Logs
        print(f"║ BNB/BTC price: {bnb_btc_price} BTC, BNB/BTC price: {price_direction} ║")
    
    prev_bnb_btc_price = bnb_btc_price
    
    time.sleep(10)
