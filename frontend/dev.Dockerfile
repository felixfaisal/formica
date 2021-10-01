FROM node:15

WORKDIR /app 

RUN npm install 
EXPOSE 3000 

ENTRYPOINT ["npm","start"]
