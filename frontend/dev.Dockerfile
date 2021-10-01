FROM node:15
RUN mkdir /app
WORKDIR /app 

COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json
