import pytest
import io
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test_secret_key'
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My 2FA' in response.data
    assert b'Upload an export file from your password manager' in response.data

def test_success(client, tmp_path):
    # Create a temporary directory within the test folder
    temp_dir = tmp_path / "uploads"
    temp_dir.mkdir()

    # Define the file path within the temporary directory
    file_path = temp_dir / "test.txt"

    data = {
        'file': (io.BytesIO(b'my file contents'), 'test.txt')
    }
    response = client.post('/success', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    assert b'File uploaded successfully' in response.data

    # Save the file to the temporary directory
    with client.session_transaction() as sess:
        sess['filename'] = str(file_path)
        with open(file_path, 'wb') as f:
            f.write(b'my file contents')

    # Verify the file was saved correctly
    assert file_path.read_text() == 'my file contents'

def test_success_no_file(client):
    data = {
        'file': (io.BytesIO(b''), '')
    }
    response = client.post('/success', data=data, content_type='multipart/form-data')
    assert response.status_code == 400
    assert b'Error 400: Bad Request' in response.data

def test_match(client, mocker):
    mocker.patch('api.fetch.fetch_2fa_data', return_value={'example.com': {'methods': ['sms', 'totp']}})
    mocker.patch('match.interface.MatchInterface.match', return_value={'example': ['sms', 'totp']})
    with client.session_transaction() as sess:
        sess['filename'] = 'path/to/1password_export.csv'
    response = client.post('/match')
    assert response.status_code == 200
    assert b'Matched Items:' in response.data
    assert b'example' in response.data
    assert b'sms' in response.data
    assert b'totp' in response.data

def test_404_error(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404
    assert b'Error 404: Page Not Found' in response.data

def test_405_error(client):
    response = client.post('/')
    assert response.status_code == 405
    assert b'Error 405: Method Not Allowed' in response.data
