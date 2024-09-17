# Icarus Dump

Quickly and easily get all the emails gathered by the Icarus harvesting website!

## How To Use

1. Make sure you install all dependencies as specified in the requirements.txt file (tested with Python 3.10.*)
2. Create a `.env` file with the following variables:
```
TURSO_DATABASE_URL=...
TURSO_AUTH_TOKEN=...

SINCH_MAILGUN_API_KEY=...
```
3. Run `python main.py` for dumping the emails to `emails.csv` file. Otherwise, run `python send.py` for sending the emails using a Mailgun template, with a subject.
