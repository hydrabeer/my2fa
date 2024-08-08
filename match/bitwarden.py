"""Parse Bitwarden export files."""

import csv
import json
from os import PathLike


def bitwarden_items(path: str | PathLike[str]) -> dict[str, list[str]]:
    """Accept a path to a Bitwarden export file (.csv or .json) and return a dictionary
    mapping login item names to lists of their URIs.
    """
    output = {}
    if path[-4:] == "json":
        with open(path, "r") as f:
            vault_data = json.load(f)
            for item in vault_data["items"]:
                if item.get("login"):
                    output[item["name"]] = [
                        entry["uri"] for entry in item["login"]["uris"]
                    ]
    elif path[-3:] == "csv":
        with open(path, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row: dict
                if row["type"] == "login":
                    output[row["name"]] = [row["login_uri"]]
    else:
        raise NameError("File type not supported")
    return output
