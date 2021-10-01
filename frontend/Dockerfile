FROM node:15

WORKDIR /app 

COPY package.json ./ 
RUN npm install -g increase-memory-limit
RUN increase-memory-limit
RUN npm update
RUN npm install --silent 


COPY . ./ 

ENTRYPOINT ["npm","start"]
