# Spidey Checker

This script checks if a specific item (e.g., Spiderman SKU on BestBuy) is available for purchase. If available, it sends email alerts to configured recipients. This script is expected to be paired with a cron job to repeatedly check for Spider-man and email users if available.

This project uses [Poetry](https://python-poetry.org/) for dependency management.

## Requirements

- Python 3.9+
- [Poetry](https://python-poetry.org/docs/#installation)
- Gmail App Password (or SMTP-compatible credentials)
- `.env` file with the required environment variables

## Installation

1. Clone the repository

```bash
git clone https://github.com/asingh1299/Best-Buy-Spider-Man-Collector-Booster-Box.git
cd spidey-checker
```

2. Install Poetry using pipx

```bash
pipx install poetry
```

3. Install dependencies using Poetry

```bash
poetry install
```

## Configuration

Create a `.env` file in the root of the project. You can start from `.env.example`.

Example `.env` file:

```
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_gmail_app_password
EMAIL_RECIPIENTS=you@gmail.com,another@example.com
SPIDERMAN_SKU=6621977
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

## Running the Script

Use Poetry to run the script in the virtual environment:

```bash
poetry run python bin/check_spiderman.py
```

The script will check availability of the Spider-man box. If the item becomes available, it will send email alerts and then exit.