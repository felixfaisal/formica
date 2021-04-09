![Imgur](https://i.imgur.com/mBTeFwN.png)
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
