FROM node:20-slim

WORKDIR /usr/src/app/frontend

COPY package.json package.json

RUN npm install && npm cache clean --force

COPY . .

EXPOSE 5173  

CMD [ "npm", "run", "dev", "--", "--host", "0.0.0.0"]