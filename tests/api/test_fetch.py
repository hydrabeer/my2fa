import pytest
from unittest import mock
from requests.exceptions import HTTPError, RequestException, Timeout
from api.fetch import fetch_2fa_data

def test_fetch_success():
    mock_response = mock.Mock()
    mock_response.json.return_value = {"example.com": {"methods": ["sms"]}}
    mock_response.raise_for_status.return_value = None

    with mock.patch('requests.get', return_value=mock_response):
        data = fetch_2fa_data()
        assert data == {"example.com": {"methods": ["sms"]}}

def test_fetch_http_error():
    with mock.patch('requests.get', side_effect=HTTPError("HTTP Error")):
        with pytest.raises(RuntimeError, match="Failed to fetch 2fa.directory data after multiple attempts."):
            fetch_2fa_data()

def test_fetch_request_exception():
    with mock.patch('requests.get', side_effect=RequestException("Request Exception")):
        with pytest.raises(RuntimeError, match="Failed to fetch 2fa.directory data after multiple attempts."):
            fetch_2fa_data()

def test_fetch_timeout():
    with mock.patch('requests.get', side_effect=Timeout("Timeout Error")):
        with pytest.raises(RuntimeError, match="Failed to fetch 2fa.directory data after multiple attempts."):
            fetch_2fa_data()

def test_fetch_invalid_json():
    mock_response = mock.Mock()
    mock_response.json.side_effect = ValueError("Invalid JSON")
    mock_response.raise_for_status.return_value = None

    with mock.patch('requests.get', return_value=mock_response):
        with pytest.raises(RuntimeError, match="Failed to fetch 2fa.directory data after multiple attempts."):
            fetch_2fa_data()

def test_fetch_unexpected_json_format():
    mock_response = mock.Mock()
    mock_response.json.return_value = ["unexpected", "format"]
    mock_response.raise_for_status.return_value = None

    with mock.patch('requests.get', return_value=mock_response):
        with pytest.raises(RuntimeError, match="Failed to fetch 2fa.directory data after multiple attempts."):
            fetch_2fa_data()