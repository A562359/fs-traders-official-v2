import os
import pandas as pd

# Check if data files exist, else create dummy data
if not os.path.exists("nifty_pcr.csv"):
    dummy_nifty = pd.DataFrame([{
        "Time": "09:30",
        "Call OI": 0,
        "Put OI": 0,
        "Diff": 0,
        "PCR": 0,
        "Signal": "N/A"
    }])
    dummy_nifty.to_csv("nifty_pcr.csv", index=False)

if not os.path.exists("banknifty_pcr.csv"):
    dummy_bank = pd.DataFrame([{
        "Time": "09:30",
        "Call OI": 0,
        "Put OI": 0,
        "Diff": 0,
        "PCR": 0,
        "Signal": "N/A"
    }])
    dummy_bank.to_csv("banknifty_pcr.csv", index=False)
