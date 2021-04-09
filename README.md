![Imgur](https://i.imgur.com/mBTeFwN.png)
![Discord](https://img.shields.io/badge/Made%20for%20-Discord-purple)
![Django](https://img.shields.io/badge/Made%20with%20%20-Django%20-green)
![React](https://img.shields.io/badge/Made%20with%20%20-React%20-blue)
![Web](https://img.shields.io/badge/Made%20for%20%20-Web%20-Red)
![Code Size](https://img.shields.io/github/languages/code-size/felixfaisal/formica)
![Licesne](https://img.shields.io/github/license/felixfaisal/formica)
![issue](https://img.shields.io/github/issues/felixfaisal/formica)


A discord form bot that lets you create forms and visualize the data via a web interface 

## Web Interface 
![Imgur](https://i.imgur.com/aHZr15T.gif)

## Discord Bot 
![Imgur](https://i.imgur.com/PmphjEm.gif)

### How to run locally 
```
git clone https://github.com/felixfaisal/formica.git
cd formica
docker-compose build
docker-compose up 
```

### Add Client ID and Client Secret 
```
cd formica/backend/API/
touch .env
``` 
Add the following 
```
CLIENT_ID= <ClientID> 
CLIENT_SECRET= <ClientSecret> 
``` 

### Add Bot Secret Token 
```
cd formica/bot/
touch .env
```
Add the following 
```
TOKENT = <BotToken>
```

## Contribution 
Check out our ![Contribution Guidelines](/CONTRIBUTING.md)
