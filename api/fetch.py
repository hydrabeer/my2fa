import requests


def fetch_2fa_data() -> dict:
    """Fetch data from the 2fa.directory API."""
    data = requests.get("https://api.2fa.directory/v4/all.json")
    return data.json()
