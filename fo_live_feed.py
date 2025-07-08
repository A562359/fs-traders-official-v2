from SmartApi.smartConnect import SmartConnect
import os
from dotenv import load_dotenv
from datetime import datetime
import time

# ✅ Load credentials
load_dotenv()

API_KEY=SkyKgmn2
SECRET_KEY=b3291046-3915-4f78-affe-e606418a8920
CLIENT_CODE=A57362432
PASSWORD=Anis@1978
TOTP=838541

# ✅ Connect to Angel One
obj = SmartConnect(api_key=API_KEY)
try:
    session = obj.generateSession(CLIENT_CODE, PASSWORD, TOTP)
    print("✅ Login successful!")
except Exception as e:
    print("❌ Login failed:", e)
    exit()

# ✅ Replace these with real strike/expiry tokens
NIFTY_CALL_TOKEN = "2020203"
NIFTY_PUT_TOKEN = "2020204"

def fetch_pcr(call_token, put_token):
    try:
        call_data = obj.getQuote(exchange="NFO", symbol_token=call_token)
        put_data = obj.getQuote(exchange="NFO", symbol_token=put_token)

        call_oi = int(call_data["data"]["openInterest"])
        put_oi = int(put_data["data"]["openInterest"])
        pcr = round(put_oi / call_oi, 2) if call_oi else 0
        signal = "BUY" if pcr > 1 else "SELL"

        print(f"\n🕒 {datetime.now().strftime('%H:%M:%S')}")
        print(f"📈 Call OI: {call_oi:,} | 📉 Put OI: {put_oi:,}")
        print(f"📊 PCR = {pcr} → Signal: {signal}")

    except Exception as e:
        print(f"❌ Error fetching PCR data: {e}")

# 🔁 Run every 3 minutes
if __name__ == "__main__":
    while True:
        fetch_pcr(NIFTY_CALL_TOKEN, NIFTY_PUT_TOKEN)
        print("🔁 Waiting 3 minutes...\n")
        time.sleep(180)
