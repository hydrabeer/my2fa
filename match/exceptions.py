class ExportFileError(Exception):
    def __str__(self):
        return (
            "Sorry, that export file isn't recognized. Make sure its name contains "
            "the name of your password manager. If it does, your password manager "
            "may not be supported yet."
        )


class PasswordManagerError(Exception):
    def __str__(self):
        return "Sorry, that password manager isn't supported yet."
