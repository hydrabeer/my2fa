"""Parse Bitwarden export files."""

import json


def bitwarden_items(path: str) -> dict[str, list[str]]:
    """Accept a path to a Bitwarden export file (.json) <path> and return a dictionary
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
    else:
        raise ValueError(f"Expected a json, got {path} instead")
    return output
