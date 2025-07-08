# fo_live_feed.py

from smartapi import SmartConnect
import pyotp
import pandas as pd
from datetime import datetime

# Angel One Credentials (replace placeholders)
api_key = "YOUR_API_KEY"
client_code = "YOUR_CLIENT_CODE"
pwd = "YOUR_PASSWORD"
totp_key = "YOUR_TOTP_SECRET"
api_secret = "YOUR_API_SECRET"

# TOTP generation
totp = pyotp.TOTP(totp_key).now()

# Login
obj = SmartConnect(api_key=api_key)
session_data = obj.generateSession(client_code, pwd, totp)

# Function to get live OI snapshot (mocked logic for now)
def fetch_pcr_data(symbol):
    # Replace with real Angel One symbol token
    # This is mocked data. Replace with actual API call and F&O parsing.
    time_now = datetime.now().strftime("%H:%M")
    return {
        "Time": time_now,
        "Call OI": 2500000,
        "Put OI": 3200000,
        "Diff": 3200000 - 2500000,
        "PCR": round(3200000 / 2500000, 2),
        "Signal": "BUY" if round(3200000 / 2500000, 2) > 1 else "SELL"
    }

# For example
if __name__ == "__main__":
    nifty_data = fetch_pcr_data("NIFTY")
    banknifty_data = fetch_pcr_data("BANKNIFTY")

    df_nifty = pd.DataFrame([nifty_data])
    df_bank = pd.DataFrame([banknifty_data])

    df_nifty.to_csv("nifty_pcr.csv", index=False)
    df_bank.to_csv("banknifty_pcr.csv", index=False)
