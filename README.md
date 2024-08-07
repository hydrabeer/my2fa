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

This setup will create a locally run server using Flask, which you can access via a web browser. The application will fetch data from the [2FA Directory API](https://2fa.directory/api/), match it with the user's password manager items, and display the results on a web page.

**Please note that your IP address will be subject to [2FA Directory's privacy policy](https://2fa.directory/privacy/) when you use this tool. No information about your accounts is revealed.**
