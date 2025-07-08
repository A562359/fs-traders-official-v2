vfrom SmartApi.smartConnect import SmartConnect
import os
import time
from datetime import datetime
from dotenv import load_dotenv

# Load API credentials from .env
load_dotenv()

API_KEY=SkyKgmn2
SECRET_KEY=b3291046-3915-4f78-affe-e606418a8920
CLIENT_CODE=A57362432
PASSWORD=Anis@1978
TOTP=O7VIUTCBCIFCGSRMXCQQK67LPQ 

# Angel One Tokens - NIFTY 25400 Strike, 10 JULY 2024
NIFTY_CALL_TOKEN = "2020203"
NIFTY_PUT_TOKEN = "2020204"

# Login to Angel One
smart = SmartConnect(api_key=API_KEY)
session = smart.generateSession(CLIENT_CODE, PASSWORD, TOTP)

# Fetch live PCR from Angel One
def fetch_pcr(call_token, put_token):
    try:
        call_data = smart.getQuote(symbol_token=call_token)
        put_data = smart.getQuote(symbol_token=put_token)

        call_oi = int(call_data["data"]["openInterest"])
        put_oi = int(put_data["data"]["openInterest"])
        pcr = round(put_oi / call_oi, 2) if call_oi else 0
        signal = "BUY" if pcr > 1 else "SELL"

        print(f"\n📊 PCR Update - {datetime.now().strftime('%H:%M:%S')}")
        print(f"Call OI: {call_oi:,} | Put OI: {put_oi:,}")
        print(f"PCR: {pcr} → {signal}")

    except Exception as e:
        print(f"❌ Error fetching PCR: {e}")

# Loop every 3 minutes
if __name__ == "__main__":
    while True:
        fetch_pcr(NIFTY_CALL_TOKEN, NIFTY_PUT_TOKEN)
        time.sleep(180)  # Wait 3 minutes
