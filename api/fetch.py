import requests


def fetch_2fa_data() -> dict[str, dict[str, str | list[str]]]:
    """Fetch data from the 2fa.directory API and return it as a dictionary."""
    url = "https://api.2fa.directory/v4/all.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
