FROM nodered/node-red:latest

COPY package.json .
RUN npm install --unsafe-perm --no-update-notifier --no-fund --only=production

COPY settings.js /data/settings.js
COPY flows.json /data/flows.json
