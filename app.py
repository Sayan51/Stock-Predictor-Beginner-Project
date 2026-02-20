import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.title("📈 Stock Direction Predictor")

ticker = st.text_input("Enter Stock Ticker (e.g., AAPL)", "AAPL")

if st.button("Predict"):

    # Download data
    data = yf.download(ticker, period="5y", interval="1d")

    # Feature engineering
    data["MA10"] = data["Close"].rolling(10).mean()
    data["MA50"] = data["Close"].rolling(50).mean()
    data["MA_Diff"] = data["MA10"] - data["MA50"]
    data["Momentum_5"] = data["Close"] - data["Close"].shift(5)
    data["Volatility_5"] = data["Close"].pct_change().rolling(5).std()

    # Target creation
    data["Future_Return"] = data["Close"].shift(-5) / data["Close"] - 1
    data["Target"] = (data["Future_Return"] > 0).astype(int)

    data = data.dropna()

    features = ["MA10", "MA50", "MA_Diff", "Momentum_5", "Volatility_5"]

    X = data[features]
    y = data["Target"]

    # Time-series split
    split = int(len(data) * 0.8)
    X_train = X[:split]
    y_train = y[:split]

    # Train model
    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=8,
        min_samples_split=10,
        random_state=42
    )

    model.fit(X_train, y_train)

    # Predict latest
    latest_data = X.iloc[-1:]
    prediction = model.predict(latest_data)[0]

    if prediction == 1:
        st.success("Prediction: Stock likely to move UP in next 5 days 📈")
    else:
        st.error("Prediction: Stock likely to move DOWN in next 5 days 📉")
