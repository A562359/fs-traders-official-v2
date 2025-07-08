
import os
import pandas as pd
from dotenv import load_dotenv
from smartapi import SmartConnect

load_dotenv()

def get_connection():
    obj = SmartConnect(api_key=os.getenv("API_KEY"))
    obj.generateSession(os.getenv("CLIENT_CODE"), os.getenv("PASSWORD"), os.getenv("TOTP"))
    return obj

def get_live_fno_data():
    symbols = ["NIFTY", "BANKNIFTY"]
    obj = get_connection()
    fut_data = []
    opt_data = []

    for symbol in symbols:
        try:
            # Get LTP for Futures
            ltp_data = obj.ltpData("NFO", symbol, symbol + "23JULFUT")
            fut_data.append({
                "Symbol": symbol,
                "LTP": ltp_data['data']['ltp'],
                "Exchange": "NFO",
                "Instrument": "FUT"
            })

            # Get Option Chain (top 5 entries)
            option_chain = obj.getOptionChain(symbol=symbol)
            chain = option_chain["data"][:10]  # First 10 rows for simplicity

            for row in chain:
                opt_data.append({
                    "Symbol": symbol,
                    "Strike Price": row["strikePrice"],
                    "Type": row["optionType"],
                    "LTP": row["lastPrice"],
                    "Open Interest": row["openInterest"],
                    "Volume": row["volume"]
                })

        except Exception as e:
            continue

    return pd.DataFrame(fut_data), pd.DataFrame(opt_data)
