"""Abstract csv parser."""

import csv

from match.export_format import COLUMN_NAMES


def parse_csv(path: str, pwm_name: str) -> dict[str, list[str]]:
    """Accept a path to a password manager export file (.csv) <path> and the name of
    the password manager <pwm_name> and return a dictionary mapping login item names to
    lists of their URIs.

    Preconditions:
        pwm_name.lower() in COLUMN_NAMES
    """
    pwm_name_lower = pwm_name.lower()
    name_column = COLUMN_NAMES[pwm_name_lower]["item_name"]
    uri_column = COLUMN_NAMES[pwm_name_lower]["uri_name"]

    output = {}
    if path[-3:] == "csv":
        with open(path, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row: dict
                if row[uri_column]:
                    output[row[name_column]] = [row[uri_column]]
    else:
        raise ValueError("<path> must point to a .csv file.")

    return output
