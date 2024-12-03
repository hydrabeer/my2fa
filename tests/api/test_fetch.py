import pytest
from api.fetch import fetch_2fa_data


def test_fetch_type() -> None:
    data = fetch_2fa_data()
    assert isinstance(data, dict)

