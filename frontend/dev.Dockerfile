FROM node:15

WORKDIR /app 

RUN npm install 

ENTRYPOINT ["npm","start"]
