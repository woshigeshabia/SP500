import pandas as pd

def create_feature(df):

    df["return"] = df["Close"].pct_change()

    df["ma5"] = df["Close"].rolling(5).mean()

    df["ma20"] = df["Close"].rolling(20).mean()

    df["volatility"] = (
        df["return"]
        .rolling(20)
        .std()
    )

    df.dropna(inplace=True)

    return df
