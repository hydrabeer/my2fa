# my2FA

### See what 2FA methods your accounts support, all at once

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![codecov](https://codecov.io/gh/hydrabeer/my2fa/graph/badge.svg?token=9GOOHFA8EQ)](https://codecov.io/gh/hydrabeer/my2fa)

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [License](#license)

## Overview

my2FA is a tool that allows you to see which of your accounts support two-factor authentication (2FA) and which
methods they support. It does this by comparing the accounts in your password manager with the entries in the
[2FA Directory](https://2fa.directory/).

## Installation

- Install [Python](https://www.python.org/downloads/), if you haven't already

Install venv:

```bash 
pip install virtualenv
```

Clone the repository:

```bash
git clone https://github.com/hydrabeer/my2fa.git
cd my2fa
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash 
# On macOS and Linux
source venv/bin/activate
```

```batch
:: On Windows
venv/Scripts/activate.bat
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python3 app.py
```

## Usage

This setup will create a locally run server using Flask, which you can access via a web browser. The application
fetches data from the [2FA Directory API](https://2fa.directory/api/), matches entries with items from your password
manager export file, and displays the results on a web page.

![image](https://github.com/user-attachments/assets/a33ed504-a0c5-4f2c-a8a3-a1a34b352ee3)

- [1Password](https://support.1password.com/export/) (Choose `.csv`)
- [Bitwarden](https://bitwarden.com/learning/passwordmanager-how-to-export-your-bitwarden-vault/)
- [Dashlane](https://support.dashlane.com/hc/en-us/articles/202625092-Export-Dashlane-data-to-a-CSV-file) (Use
  `credentials.csv` and add `dashlane` to the filename)
- [LastPass](https://support.lastpass.com/s/document-item?bundleId=lastpass&topicId=LastPass/export-vault.html&_LANG=enus)

*Don't see your favorite password manager? Feel free to open an issue and request support for it.*

This tool currently only supports unencrypted export files, so you should delete your export file from its original
location and the my2fa directory and empty your trash/recycle bin as soon as you are finished with the tool.

Please note that your IP address will be subject to [2FA Directory's privacy policy](https://2fa.directory/privacy/)
when you use this tool. **This tool never reveals information about your accounts outside your local machine.**

## License

my2fa is covered by the GPLv3 (GNU General Public License version 3). Check out
the [quick guide](https://www.gnu.org/licenses/quick-guide-gplv3) to the license.
