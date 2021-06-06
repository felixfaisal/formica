---
sidebar_position: 1
---


### Frontend and Backend Setup 
```bash
# Add Client ID and Secret Key 
cd formica/backend/API
touch .env
nano .env
CLIENT_ID= <ClientID> 
CLIENT_SECRET= <ClientSecret> 
``` 
### Start the containers
```bash
#Run using Docker
cd formica
docker-compose build 
docker-compose up
```

### Setup Discord Bot
For security reasons, and to avoid disruptions with the bot, we highly advise you to create your own bot and use its token for local development. The token will be replaced with the Formica bot's token when your pull request is merged. For information on how to do this, check out the [external bot resources](external-resources/bot-resources.md)
```bash
#Add Bot Secret key
cd formica/bot
touch .env 
nano .env 
TOKEN = <BotToken>
``` 

### Start the bot
```bash
#Run the bot 
python formica_bot.py

```