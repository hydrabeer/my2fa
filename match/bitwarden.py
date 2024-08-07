import json
from os import PathLike


def bitwarden_items(path: str | PathLike) -> dict[str, list[str]]:
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
        raise NameError  # cry about it

    return output
