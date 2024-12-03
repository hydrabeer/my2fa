import pytest
import json
from match.bitwarden import bitwarden_items

def test_bitwarden_items_valid_json(tmp_path):
    # Create a temporary JSON file
    data = {
        "items": [
            {
                "name": "example",
                "login": {
                    "uris": [
                        {"uri": "https://example.com"}
                    ]
                }
            }
        ]
    }
    file_path = tmp_path / "vault.json"
    with open(file_path, "w") as f:
        json.dump(data, f)

    # Call the function and check the result
    result = bitwarden_items(str(file_path))
    assert result == {"example": ["https://example.com"]}

def test_bitwarden_items_invalid_extension(tmp_path):
    # Create a temporary file with an invalid extension
    file_path = tmp_path / "vault.txt"
    with open(file_path, "w") as f:
        f.write("This is not a JSON file.")

    # Call the function and check for ValueError
    with pytest.raises(ValueError, match="Expected a json, got .* instead"):
        bitwarden_items(str(file_path))

def test_bitwarden_items_no_login(tmp_path):
    # Create a temporary JSON file without login information
    data = {
        "items": [
            {
                "name": "example"
            }
        ]
    }
    file_path = tmp_path / "vault.json"
    with open(file_path, "w") as f:
        json.dump(data, f)

    # Call the function and check the result
    result = bitwarden_items(str(file_path))
    assert result == {}