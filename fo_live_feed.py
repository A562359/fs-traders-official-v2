import os
import pandas as pd
from dotenv import load_dotenv
from angel_one.smartconnect import SmartConnect

load_dotenv()

def get_connection():
    obj = SmartConnect(api_key=os.getenv("API_KEY"))
    obj.generateSession(
        user_id=os.getenv("CLIENT_CODE"),
        password=os.getenv("PASSWORD"),
        twoFA=os.getenv("TOTP")
    )
    return obj

def get_live_fno_data():
    symbols = ["NIFTY", "BANKNIFTY"]
    obj = get_connection()
    fut_data = []
    opt_data = []

    for symbol in symbols:
        try:
            fut_ltp = obj.ltpData("NFO", symbol, symbol + "23JULFUT")['data']['ltp']
            fut_data.append({"Symbol": symbol, "LTP": fut_ltp, "Instrument": "FUT"})

            chain = obj.getOptionChain(symbol=symbol)["data"][:10]
            for row in chain:
                opt_data.append({
                    "Symbol": symbol,
                    "Strike": row["strikePrice"],
                    "Type": row["optionType"],
                    "LTP": row["lastPrice"],
                    "OI": row["openInterest"],
                    "Volume": row["volume"]
                })
        except Exception:
            continue

    return pd.DataFrame(fut_data), pd.DataFrame(opt_data)
