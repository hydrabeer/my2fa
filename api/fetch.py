import requests


def fetch_2fa_data() -> dict[str, dict]:
    """Fetch data from the 2fa.directory API."""
    url = "https://api.2fa.directory/v4/all.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
