"""1Password"""

import csv
from os import PathLike


def one_password_items(path: str | PathLike) -> dict[str, list[str]]:
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
