"""Provides the MatchInterface class, serving as the interface between the app and the
password manager parsing modules.
"""

import urllib.parse

from match.exceptions import ExportFileError
from match.parse_csv import parse_csv


class MatchInterface:
    """The interface between the app and the password manager parsing modules.

    Attributes:
        _api_dict: A dictionary matching the 2FA Directory API v4 format.
        _export_file_path: The path to the password manager export file.
        _pwm_name: The name of the password manager from which the export
                   file came.
    """

    _api_dict: dict[str, dict[str, str | list[str]]]
    _export_file_path: str
    _pwm_name: str

    def __init__(
        self,
        api_data: dict[str, dict[str, str | list[str]]],
        export_file_path: str,
    ) -> None:
        """Accept a dictionary of 2FA Directory API v4 data <api_data> and a path to a
        password manager export file <export_file_path> and return a new instance of
        the MatchInterface class.
        """

        self._api_dict = api_data
        self._export_file_path = export_file_path
        self._pwm_name = self._get_pwm_name()

    def _get_pwm_name(self) -> str:
        """Return the name of the password manager from which the export file at
        self._export_file_path came.

        Preconditions:
            isinstance(self._export_file_path, str)
        """

        path_lower = self._export_file_path.lower()
        if (name := "1password") in path_lower:
            return name
        elif (name := "bitwarden") in path_lower:
            return name
        elif (name := "dashlane") in path_lower:
            return name
        elif (name := "lastpass") in path_lower:
            return name
        else:
            raise ExportFileError

    def _get_uri_dict(self) -> dict[str, list[str]]:
        """Return a dictionary mapping login item names from the export file at
        self._export_file_path to lists of their URIs.
        """

        if self._pwm_name == "bitwarden" and self._export_file_path[-4:] == "json":
            from match.bitwarden import bitwarden_items

            return bitwarden_items(self._export_file_path)
        else:
            return parse_csv(self._export_file_path, self._pwm_name)

    def match(self) -> dict[str, list[str]]:
        """Return a dictionary mapping login item names from the export file at
        self._export_file_path to lists of their supported 2FA methods.
        """

        matched_items = {}

        uri_dict = self._get_uri_dict()
        for login_name in uri_dict:
            for uri in uri_dict[login_name]:
                parse_result = urllib.parse.urlparse(uri)

                # If the hostname of the URI is a key in the API dict, assign the
                # corresponding dictionary value to <service>
                if service := self._api_dict.get(parse_result.hostname):
                    matched_items[login_name] = service.get("methods")

        return matched_items
