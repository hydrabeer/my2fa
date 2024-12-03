import pytest
from match.parse_csv import parse_csv

def test_parse_csv_1password(tmp_path):
    # Create a temporary CSV file for 1password
    csv_content = "Title,Url\nExample,https://example.com\n"
    csv_file = tmp_path / "1password_export.csv"
    csv_file.write_text(csv_content)

    # Test the parse_csv function
    result = parse_csv(str(csv_file), "1password")
    assert result == {"Example": ["https://example.com"]}

def test_parse_csv_bitwarden(tmp_path):
    # Create a temporary CSV file for Bitwarden
    csv_content = "name,login_uri\nExample,https://example.com\n"
    csv_file = tmp_path / "bitwarden_export.csv"
    csv_file.write_text(csv_content)

    # Test the parse_csv function
    result = parse_csv(str(csv_file), "bitwarden")
    assert result == {"Example": ["https://example.com"]}

def test_parse_csv_dashlane(tmp_path):
    # Create a temporary CSV file for Dashlane
    csv_content = "title,url\nExample,https://example.com\n"
    csv_file = tmp_path / "dashlane_export.csv"
    csv_file.write_text(csv_content)

    # Test the parse_csv function
    result = parse_csv(str(csv_file), "dashlane")
    assert result == {"Example": ["https://example.com"]}

def test_parse_csv_lastpass(tmp_path):
    # Create a temporary CSV file for LastPass
    csv_content = "name,url\nExample,https://example.com\n"
    csv_file = tmp_path / "lastpass_export.csv"
    csv_file.write_text(csv_content)

    # Test the parse_csv function
    result = parse_csv(str(csv_file), "lastpass")
    assert result == {"Example": ["https://example.com"]}

def test_parse_csv_invalid_file_extension(tmp_path):
    # Create a temporary file with an invalid extension
    invalid_file = tmp_path / "invalid_export.txt"
    invalid_file.write_text("Title,Url\nExample,https://example.com\n")

    # Test the parse_csv function with an invalid file extension
    with pytest.raises(ValueError, match="<path> must point to a .csv file."):
        parse_csv(str(invalid_file), "1password")