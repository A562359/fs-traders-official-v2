from SmartApi.smartConnect import SmartConnect
import pandas as pd
from datetime import datetime
import os
import time
from dotenv import load_dotenv

# 🌐 Load environment variables from .env
load_dotenv()

# 🔐 Angel One credentials (set these in your .env file)
API_KEY=SkyKgmn2
SECRET_KEY=b3291046-3915-4f78-affe-e606418a8920
CLIENT_CODE=A57362432
PASSWORD=Anis@1978
TOTP=O7VIUTCBCIFCGSRMXCQQK67LPQ


# 🎯 Live option tokens for NIFTY 25400 strike, 10 JULY 2024 expiry
NIFTY_CALL_TOKEN = "2020203"
NIFTY_PUT_TOKEN = "2020204"

# 🛑 Replace with real tokens if using BANKNIFTY
BANKNIFTY_CALL_TOKEN = "YOUR_BANKNIFTY_CALL_TOKEN"
BANKNIFTY_PUT_TOKEN = "YOUR_BANKNIFTY_PUT_TOKEN"

# 🚀 Connect to Angel One
obj = SmartConnect(api_key=API_KEY)
session = obj.generateSession(CLIENT_CODE, PASSWORD, TOTP)

# 🧠 PCR Calculator
def fetch_live_pcr(symbol_token_call, symbol_token_put):
    try:
        call_data = obj.getQuote(symbol_token=symbol_token_call)
        put_data = obj.getQuote(symbol_token=symbol_token_put)

        call_oi = int(call_data["data"]["openInterest"])
        put_oi = int(put_data["data"]["openInterest"])
        pcr = round(put_oi / call_oi, 2) if call_oi else 0
        signal = "BUY" if pcr > 1 else "SELL"

        return {
            "Time": datetime.now().strftime("%H:%M"),
            "Call OI": call_oi,
            "Put OI": put_oi,
            "Diff": put_oi - call_oi,
            "PCR": pcr,
            "Signal": signal
        }

    except Exception as e:
        print(f"❌ Error fetching OI: {e}")
        return None

# 📝 Save new data to CSV
def update_csv(file_name, call_token, put_token):
    df = pd.read_csv(file_name) if os.path.exists(file_name) else pd.DataFrame()
    new_row = fetch_live_pcr(call_token, put_token)

    if new_row:
        if df.empty or df.get("Time", pd.Series()).iloc[-1] != new_row["Time"]:
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_csv(file_name, index=False)
            print(f"✔ {file_name} updated at {new_row['Time']}")
        else:
            print(f"⏸ No update (duplicate time: {new_row['Time']})")

# 🔁 Repeat every 3 minutes
if __name__ == "__main__":
    while True:
        update_csv("nifty_pcr.csv", NIFTY_CALL_TOKEN, NIFTY_PUT_TOKEN)
        # Uncomment if using BANKNIFTY
        # update_csv("banknifty_pcr.csv", BANKNIFTY_CALL_TOKEN, BANKNIFTY_PUT_TOKEN)
        print("⏳ Waiting 3 minutes...\n")
        time.sleep(180)
