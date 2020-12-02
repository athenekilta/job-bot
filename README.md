# Athenen Job-bot

Botti lähettää ilmoituksen Athene Jobs -telegram ryhmään, aina kun [https://athene.fi/jobs/](athene.fi/jobs) sivulle lisätään uusia työpaikkoja.

## Setup

```
$ git clone [url]
$ cd job-bot
$ touch data.json
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python main.py
```
