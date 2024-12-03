import requests
import logging
from requests.exceptions import HTTPError, RequestException, Timeout


# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def fetch_2fa_data(
    retries: int = 3, timeout: int = 5
) -> dict[str, dict[str, str | list[str]]]:
    """Fetch data from the 2fa.directory API.

    Args:
        retries (int): The number of retries to attempt if the request fails.
                       Defaults to 3.
        timeout (int): The timeout in seconds for the request. Defaults to 5.

    Returns:
        dict[str, dict[str, str | list[str]]]: The data from the 2fa.directory API.

    Raises:
        RuntimeError: If the data could not be fetched after retries.

    >>> _fetch_2fa_data()
    {
    'example.com': {
            # All keys are optional, but there are keys iff 'methods' is present
            'methods': [
                    'sms',
                    'call',
                    'email',
                    'totp'
                    'u2f',
                    'custom-software',
                    'custom-hardware'
                    ],
            # Only present if 'custom-software' is in 'methods'
            'custom-software': ['Duo Mobile'],
            # Only present if 'custom-hardware' is in 'methods'
            'custom-hardware': ['Duo token', 'Touch ID'],
            'documentation': 'https://example.com/docs/mfa',
            'recovery': 'https://example.com/docs/recovery',
            'notes': '2FA via SMS can only be enabled by the support team.'
            },
    'example.org': {}
    }
    """
    url = "https://api.2fa.directory/v4/all.json"

    for attempt in range(1, retries + 1):
        try:
            logger.info(f"Fetching data from {url}, attempt {attempt} of {retries}")
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)
            data = response.json()  # Parse the JSON response

            if isinstance(data, dict):  # Ensure the data is in the expected format
                logger.info("Data fetched and validated successfully.")
                return data
            else:
                logger.error("Unexpected JSON format received.")
                raise ValueError("Unexpected JSON format")
        except (HTTPError, RequestException, Timeout) as e:
            logger.warning(f"Attempt {attempt} failed due to: {e}")
        except ValueError as ve:
            logger.error(f"Data format error: {ve}")
            break  # Stop retries if the format is invalid

    # If all retries fail
    logger.error("Failed to fetch 2fa.directory data after multiple attempts.")
    raise RuntimeError("Failed to fetch 2fa.directory data after multiple attempts.")