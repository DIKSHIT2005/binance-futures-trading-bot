# 🚀 Binance Futures Trading Bot (Testnet)

A modular Python CLI trading bot for Binance Futures Testnet.

## Features
- MARKET & LIMIT Orders
- BUY / SELL
- Logging & Error Handling
- Clean Architecture

## Setup
pip install -r requirements.txt

Create .env file:
API_KEY=your_key
API_SECRET=your_secret

## Run
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
