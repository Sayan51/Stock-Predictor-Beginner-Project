import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

st.markdown("""
<style>
.big-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Stock Predictor", page_icon="📈", layout="centered")

st.title("📈 AI Stock Direction Predictor")
st.markdown("Predicts 5-day stock movement using Machine Learning")

ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, MSFT, RELIANCE.NS)", "AAPL")

if st.button("Analyze"):

    with st.spinner("Fetching data and analyzing..."):

        try:
            data = yf.download(ticker, period="5y", interval="1d")

            if data.empty:
                st.error("❌ Invalid ticker symbol.")
                st.stop()

            # 📊 Show live stock chart
            st.subheader("📊 Price Chart (5 Years)")
            st.line_chart(data["Close"])

            # Feature Engineering
            data["MA10"] = data["Close"].rolling(10).mean()
            data["MA50"] = data["Close"].rolling(50).mean()
            data["MA_Diff"] = data["MA10"] - data["MA50"]
            data["Momentum_5"] = data["Close"] - data["Close"].shift(5)
            data["Volatility_5"] = data["Close"].pct_change().rolling(5).std()

            data["Future_Return"] = data["Close"].shift(-5) / data["Close"] - 1
            data["Target"] = (data["Future_Return"] > 0).astype(int)

            data = data.dropna()

            features = ["MA10", "MA50", "MA_Diff", "Momentum_5", "Volatility_5"]

            X = data[features]
            y = data["Target"]

            split = int(len(data) * 0.8)

            X_train = X[:split]
            X_test = X[split:]
            y_train = y[:split]
            y_test = y[split:]

            model = RandomForestClassifier(
                n_estimators=300,
                max_depth=8,
                min_samples_split=10,
                random_state=42
            )

            model.fit(X_train, y_train)

            # 📈 Model accuracy
            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)

            st.subheader("📈 Model Performance")
            st.write(f"Accuracy: **{round(accuracy*100,2)}%**")

            # 🎯 Prediction
            latest_data = X.iloc[-1:]
            prediction = model.predict(latest_data)[0]
            probability = model.predict_proba(latest_data)[0]

            st.subheader("🔮 5-Day Prediction")

            col1, col2 = st.columns(2)

            with col1:
                if prediction == 1:
                    st.success("📈 Likely to Move UP")
                else:
                    st.error("📉 Likely to Move DOWN")

            with col2:
                up_prob = round(probability[1] * 100, 2)
                down_prob = round(probability[0] * 100, 2)

                st.write(f"📊 Up Probability: **{up_prob}%**")
                st.write(f"📊 Down Probability: **{down_prob}%**")

            st.markdown("---")
            st.caption("Educational project. Not financial advice.")

        except Exception:
            st.error("⚠ Something went wrong. Try another ticker.")
