# Stock-Predictor-Beginner-Project
## 🚀 Live Web App

[Click here to try the live app](https://stock-predictor-beginner-project-mzhpqyxlztjb6ywiqgzayx.streamlit.app/)

Machine learning project that predicts 5-day stock direction using historical market data from Yahoo Finance. Built with Python, Pandas, and Random Forest, using time-series split to prevent data leakage. Achieved ~53% accuracy with trend-based features like moving averages, momentum, and volatility. Developed for educational purposes.
# 📈 Stock Market Direction Prediction using Machine Learning

## 📌 Overview

This project builds a time-series classification model to predict 
whether a stock's price will move upward over the next 5 trading days.

The model is trained using historical stock data and technical indicators 
such as moving averages, momentum, and volatility.

The goal is not to guarantee profit, but to explore how machine learning 
can extract limited predictive signals from financial time-series data.

---

## 📊 Dataset

- Source: Yahoo Finance
- Stock: AAPL
- Time Period: 5 Years
- Frequency: Daily
- Data Fields: Open, High, Low, Close, Volume

---

## ⚙ Feature Engineering

The following features were created:

- MA10 (10-day Moving Average)
- MA50 (50-day Moving Average)
- MA Difference (Trend Strength)
- 5-day Momentum
- 5-day Volatility

These features help capture trend and short-term price dynamics.

---

## 🎯 Target Variable

The model predicts whether the stock price will be higher 
after 5 trading days.

This multi-day horizon reduces daily market noise.

---

## 🤖 Model Used

Random Forest Classifier

Why Random Forest?

- Handles non-linear relationships
- Robust to noise
- Suitable for structured tabular data

---

## 📊 Results

- Accuracy: ~53%
- Time-series split used (no data leakage)
- Model slightly outperforms baseline majority-class prediction

Note: In financial markets, even small improvements above 50% 
can represent meaningful predictive edge.

---

## ⚠ Limitations

- Financial markets are highly stochastic.
- Model does not use macroeconomic or sentiment data.
- Not suitable for live trading without risk management.
- This project is for educational purposes only.

---

## 🚀 Future Improvements

- Add news sentiment analysis
- Implement walk-forward validation
- Try gradient boosting models (XGBoost)
- Build live dashboard using Streamlit

---

## 📌 Disclaimer

This project is developed for educational and research purposes only.
It does not constitute financial advice.
