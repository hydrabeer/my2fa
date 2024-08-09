"""Tells the rest of the program how different password managers format their export
files.

COLUMN_NAMES = {"password_manager_name_lower": {"item_name": "...", "uri_name": "...",}}
"""

# Password manager names should be lowercase and in alphabetical order
COLUMN_NAMES: dict[str, dict[str, str]] = {
    "1password": {"item_name": "Title", "uri_name": "Url"},
    "bitwarden": {"item_name": "name", "uri_name": "login_uri"},
    "dashlane": {"item_name": "title", "uri_name": "url"},
    "lastpass": {"item_name": "name", "uri_name": "url"},
}
