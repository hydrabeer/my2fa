"""Parse LastPass export files."""

import csv
from os import PathLike


def lastpass_items(path: str | PathLike[str]) -> dict[str, list[str]]:
    """Accept a path to a LastPass export file (.csv) and return a dictionary mapping
    login item names to lists of their URIs.
    """
    output = {}
    if path[-3:] == "csv":
        with open(path, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row: dict
                output[row["name"]] = [row["url"]]
    else:
        raise NameError("File type not supported")
    return output
