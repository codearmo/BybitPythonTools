import os
from dotenv import load_dotenv
from pybit.unified_trading import HTTP

load_dotenv()


def get_client(testnet: bool, verbose=False) -> HTTP:
    if testnet:
        api_key = os.getenv("BYBIT_TESTNET_API_KEY")
        api_secret = os.getenv("BYBIT_TESTNET_API_SECRET")
    else:
        api_key = os.getenv("BYBIT_LIVE_API_KEY")
        api_secret = os.getenv("BYBIT_LIVE_API_SECRET")

    client = HTTP(api_key=api_key, api_secret=api_secret, testnet=testnet)
    try:
        response = client.get_account_info()
        if verbose:
            print("✅ API keys are working!")
            print("Account Info:", response.get("retMsg"))
        return client
    except Exception as e:
        if verbose:
            print("❌ Failed to authenticate. Please check your API keys.")
            print("Error:", e)
        return client
