# Athenen Job-bot

Botti lähettää ilmoituksen Athene Jobs -telegram ryhmään, aina kun [Athenen työnhakusivuille](https://athene.fi/jobs/) sivulle lisätään uusia työpaikkoja.

## Setup

```
$ git clone git@github.com:athenekilta/job-bot.git
$ cd job-bot
$ touch data.json
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
Lisätään env-muuttujat
```
$ export BOT_TOKEN=your_telegrambot_token
$ export CHAT_TOKEN=your_chat_token
```

Lopuksi botti ajetaan komennolla
```
$ python main.py
```
## Mistä saat tokenit
#### BOT_TOKEN
Tee uusi botti telegramiin. [Ohjeet löytyvät täältä!](https://core.telegram.org/bots) Ota token talteen ja anna komento
```
$ export BOT_TOKEN=your_bot_token
```

#### CHAT_TOKEN
Lisää tekemäsi botti haluamaasi telegram ryhmään. Mene osoitteeseen https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates
Etsi sivulta 'chat' ja ota sen id talteen, (esimerkiksi '-123456789') ja anna komento
```
$ export CHAT_TOKEN=your_chat_token
```
