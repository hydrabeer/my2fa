import pytest
from match.interface import MatchInterface
from match.exceptions import ExportFileError

def test_get_pwm_name_valid():
    api_data = {}
    export_file_path = "path/to/1password_export.csv"
    interface = MatchInterface(api_data, export_file_path)
    assert interface._get_pwm_name() == "1password"

    export_file_path = "path/to/bitwarden_export.json"
    interface = MatchInterface(api_data, export_file_path)
    assert interface._get_pwm_name() == "bitwarden"

    export_file_path = "path/to/dashlane_export.csv"
    interface = MatchInterface(api_data, export_file_path)
    assert interface._get_pwm_name() == "dashlane"

    export_file_path = "path/to/lastpass_export.csv"
    interface = MatchInterface(api_data, export_file_path)
    assert interface._get_pwm_name() == "lastpass"

def test_get_pwm_name_invalid():
    api_data = {}
    export_file_path = "path/to/unknown_export.csv"
    with pytest.raises(ExportFileError):
        MatchInterface(api_data, export_file_path)

def test_get_uri_dict_bitwarden(mocker):
    api_data = {}
    export_file_path = "path/to/bitwarden_export.json"
    mocker.patch("match.bitwarden.bitwarden_items", return_value={"example": ["https://example.com"]})
    interface = MatchInterface(api_data, export_file_path)
    assert interface._get_uri_dict() == {"example": ["https://example.com"]}

def test_get_uri_dict_csv(mocker):
    api_data = {}
    export_file_path = "path/to/1password_export.csv"
    mocker.patch("match.interface.parse_csv", return_value={"example": ["https://example.com"]})
    interface = MatchInterface(api_data, export_file_path)
    assert interface._get_uri_dict() == {"example": ["https://example.com"]}

def test_match(mocker):
    api_data = {"example.com": {"methods": ["sms", "totp"]}}
    export_file_path = "path/to/bitwarden_export.json"
    mocker.patch("match.bitwarden.bitwarden_items", return_value={"example": ["https://example.com"]})
    interface = MatchInterface(api_data, export_file_path)
    assert interface.match() == {"example": ["sms", "totp"]}