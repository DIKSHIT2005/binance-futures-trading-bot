from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

class BinanceClient:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.api_secret = os.getenv("API_SECRET")

        self.client = Client(self.api_key, self.api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def get_client(self):
        return self.client
