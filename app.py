import yfinance as yf

df = yf.download(
    "SPY",
    interval="1m",
    period="30d"
)

df.to_csv("spy.csv")

grad_norm = 0

for p in model.parameters():

    if p.grad is not None:

        grad_norm += (
            p.grad.norm().item()
        )

gradient_history.append(
    grad_norm
)

plt.plot(
    gradient_history
)

def detect(
    pred,
    sigma
):

    if abs(pred) > 3*sigma:

        return "ALERT"

    return "NORMAL"

import streamlit as st

st.title(
    "Industrial Signal Monitor"
)

st.metric(
    "Predicted Return",
    "0.25%"
)

st.metric(
    "Status",
    "NORMAL"
)

