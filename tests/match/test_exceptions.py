import pytest
from match.exceptions import ExportFileError, PasswordManagerError

def test_export_file_error():
    with pytest.raises(ExportFileError) as excinfo:
        raise ExportFileError()
    assert str(excinfo.value) == (
        "Sorry, that export file isn't recognized. Make sure its name contains "
        "the name of your password manager. If it does, your password manager "
        "may not be supported yet."
    )

def test_password_manager_error():
    with pytest.raises(PasswordManagerError) as excinfo:
        raise PasswordManagerError()
    assert str(excinfo.value) == "Sorry, that password manager isn't supported yet."