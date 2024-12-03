from match.export_format import COLUMN_NAMES

def test_column_names_structure():
    # Check that COLUMN_NAMES is a dictionary
    assert isinstance(COLUMN_NAMES, dict)

    # Check that each key in COLUMN_NAMES is a string
    for key in COLUMN_NAMES:
        assert isinstance(key, str)

    # Check that each value in COLUMN_NAMES is a dictionary
    for value in COLUMN_NAMES.values():
        assert isinstance(value, dict)

    # Check that each nested dictionary has the correct keys
    for value in COLUMN_NAMES.values():
        assert "item_name" in value
        assert "uri_name" in value

def test_column_names_content():
    # Check specific content for known password managers
    assert COLUMN_NAMES["1password"] == {"item_name": "Title", "uri_name": "Url"}
    assert COLUMN_NAMES["bitwarden"] == {"item_name": "name", "uri_name": "login_uri"}
    assert COLUMN_NAMES["dashlane"] == {"item_name": "title", "uri_name": "url"}
    assert COLUMN_NAMES["lastpass"] == {"item_name": "name", "uri_name": "url"}