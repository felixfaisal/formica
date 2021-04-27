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