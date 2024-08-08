# My2FA
## Setting Up the Project
### Clone the repository:

```bash
git clone https://github.com/hydrabeer/my2fa.git
cd my2fa
```
### Install dependencies:

```bash
pipenv install
```
### Run the application:

```bash
pipenv run python app.py
```

This setup will create a locally run server using Flask, which you can access via a web browser. The application will fetch data from the [2FA Directory API](https://2fa.directory/api/), match entries with items from your password manager export file, and display the results on a web page.

Your password manager export file must be placed in `my2fa/`. This tool currently only supports unencrypted export files, so you should delete your export file and empty your trash bin as soon as you are finished with the tool.

### Export instructions:
[Bitwarden](https://bitwarden.com/learning/passwordmanager-how-to-export-your-bitwarden-vault/) (Choose `.json`)

**Please note that your IP address will be subject to [2FA Directory's privacy policy](https://2fa.directory/privacy/) when you use this tool. This tool never reveals information about your accounts outside your local machine.**
