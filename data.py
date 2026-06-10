import yfinance as yf

df = yf.download(
    "SPY",
    interval="1m",
    period="30d"
)

df.to_csv("spy.csv")
