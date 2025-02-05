FROM nodered/node-red:latest

USER root

COPY --chmod=0644 package.json .
COPY --chmod=0644 hash-password.js .
COPY --chmod=0755 entrypoint.sh /entrypoint.sh

COPY --chmod=0644 settings.js /data/settings.js
COPY --chmod=0644 flows.json /data/flows.json

RUN rm -rf /data/.npm

USER node-red

RUN npm i

ENTRYPOINT ["/entrypoint.sh"]
