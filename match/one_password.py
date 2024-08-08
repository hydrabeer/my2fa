"""Parse 1Password export files."""

import csv
from os import PathLike


def one_password_items(path: str | PathLike[str]) -> dict[str, list[str]]:
    """Accept a path to a 1Password export file (.csv) and return a dictionary mapping
    login item names to lists of their URIs.
    """
    output = {}
    if path[-3:] == "csv":
        with open(path, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row: dict
                output[row["Title"]] = [row["Url"]]
    else:
        raise NameError("File type not supported")

    return output
