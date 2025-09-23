import requests
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.
API_KEY_MARKETSTACK = os.getenv('API_KEY_MARKETSTACK')
symbols = "PHIA.AS"

response = requests.get(f"https://api.marketstack.com/v1/eod?access_key={API_KEY_MARKETSTACK}&symbols={symbols}")
print(response.json())