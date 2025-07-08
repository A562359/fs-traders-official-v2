
# 🚀 FS Traders Official – Live Futures & Options Dashboard

Welcome to the **FS Traders Official** 24/7 Research Dashboard – built for **real-time F&O market insights** using the **Angel One SmartAPI**.  
Stay on top of the market with **live Futures & Options data**, updated automatically every 3 minutes.

---

## 🔧 Features

✅ **Live Futures Prices** (NIFTY, BANKNIFTY, and more)  
✅ **Real-time Option Chain Scanner** (CE/PE LTP, Strike, OI, Volume)  
✅ Auto-refresh every **3 minutes** – ideal for day trading & scalping  
✅ Built for **Streamlit Cloud** 🚀  
✅ Fully integrated with **Angel One SmartAPI** 🔗  

---

## 🧪 Preview

```
| Symbol    | LTP    | Instrument | Type |
|-----------|--------|------------|------|
| NIFTY     | 23580  | NFO        | FUT  |
| BANKNIFTY | 51320  | NFO        | FUT  |
```

```
| Symbol | Strike | Type | LTP | OI     | Volume |
|--------|--------|------|-----|--------|--------|
| NIFTY  | 23500  | CE   | 240 | 230000 | 112000 |
```

---

## ⚙️ How to Deploy (Streamlit Cloud)

1. **Create a new GitHub repo** → Upload all files from this ZIP  
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) → Click **New App**
3. Set main file as: `dashboard.py`
4. Set your `secrets.toml` with Angel One credentials:

```toml
API_KEY = "your_api_key_here"
CLIENT_CODE = "your_client_code"
PASSWORD = "your_password"
TOTP = "your_totp_code"
```

---

## 📞 Contact
Need help or want to extend this bot with Telegram alerts, Trend Scanner, or F&O Calls?
Message @FSTradersOfficial on Telegram 📲

---

🧠 Built for traders. By traders. With code.
