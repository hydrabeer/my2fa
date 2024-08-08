import urllib.parse


class PasswordManagerNotSupportedError(Exception):
    def __str__(self):
        return "Sorry, that password manager isn't supported yet."


class ExportFileNotRecognizedError(Exception):
    def __str__(self):
        return (
            "Sorry, that export file isn't recognized. Make sure its name contains "
            "the name of your password manager. If it does, your password manager "
            "may not be supported yet."
        )


class MatchInterface:
    """
    Attributes:
        _api_data: A dictionary matching the 2fa.directory API v4 format.
        _password_items_path: The path to the password manager export file.
        _password_manager: The name of the password manager from which the export file
                           came.
    """

    _api_data: dict[str, dict]
    _password_items_path: str
    _password_manager: str

    def __init__(self, api_data: dict[str, dict], password_items_path: str) -> None:
        self._api_data = api_data
        self._password_items_path = password_items_path
        self._password_manager = self._detect_password_manager()

    def _detect_password_manager(self) -> str:
        path_lower = self._password_items_path.lower()
        if "1password" in path_lower:
            return "1password"
        elif "bitwarden" in path_lower:
            return "bitwarden"
        elif "lastpass" in path_lower:
            return "lastpass"
        else:
            raise ExportFileNotRecognizedError

    def _get_password_items(self) -> dict[str, list[str]]:
        match self._password_manager:
            case "1password":
                from match.one_password import one_password_items

                return one_password_items(self._password_items_path)
            case "bitwarden":
                from match.bitwarden import bitwarden_items

                return bitwarden_items(self._password_items_path)
            case "lastpass":
                from match.lastpass import lastpass_items

                return lastpass_items(self._password_items_path)
            case _:
                raise PasswordManagerNotSupportedError

    def match(self) -> dict[str, list[str]]:
        matched_items = {}

        password_items = self._get_password_items()
        for key in password_items:
            for uri in password_items[key]:
                parse_result = urllib.parse.urlparse(uri)
                if service := self._api_data.get(parse_result.hostname):
                    matched_items[key] = service.get("methods")

        return matched_items
