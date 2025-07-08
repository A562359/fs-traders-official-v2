# === FILE 1: fo_live_feed.py ===
import os
import pandas as pd
from datetime import datetime
from smartapi import SmartConnect

# === Angel One API placeholders ===
API_KEY = "your_api_key"
CLIENT_ID = "your_client_id"
PASSWORD = "your_password"
TOTP = "your_totp"

obj = SmartConnect(api_key=API_KEY)
data = obj.generateSession(CLIENT_ID, PASSWORD, TOTP)

# === Replace with your actual logic to extract OI ===
def fetch_pcr(symbol):
    # Placeholder token for NSE indices (replace with actual options token)
    call_oi = 1500000
    put_oi = 1300000

    pcr = round(put_oi / call_oi, 2)
    signal = "BUY" if pcr > 1 else "SELL"
    return {
        "Time": datetime.now().strftime("%H:%M"),
        "Call OI": call_oi,
        "Put OI": put_oi,
        "Diff": put_oi - call_oi,
        "PCR": pcr,
        "Signal": signal
    }

def update_csv(file_name, symbol):
    if not os.path.exists(file_name):
        df = pd.DataFrame([])
    else:
        df = pd.read_csv(file_name)

    new_row = fetch_pcr(symbol)
    if df.empty or df["Time"].iloc[-1] != new_row["Time"]:
        df = pd.concat([df, pd.DataFrame([new_row])])
        df.to_csv(file_name, index=False)

update_csv("nifty_pcr.csv", "NIFTY")
update_csv("banknifty_pcr.csv", "BANKNIFTY")
