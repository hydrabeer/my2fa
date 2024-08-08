import csv
from os import PathLike


def lastpass_items(path: str | PathLike) -> dict[str, list[str]]:
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
