FROM nodered/node-red:latest

USER root

COPY package.json .
COPY hash-password.js .
COPY entrypoint.sh /entrypoint.sh

COPY settings.js /data/settings.js
COPY flows.json /data/flows.json

RUN npm install --unsafe-perm --no-update-notifier --no-fund --only=production bcryptjs
RUN chmod +x /entrypoint.sh

USER node-red

ENTRYPOINT ["/entrypoint.sh"]
