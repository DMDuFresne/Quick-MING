#!/bin/sh

# Create Mosquitto username and password
if [ -n "${MOSQUITTO_USERNAME}" ] && [ -n "${MOSQUITTO_PASSWORD}" ]; then
    mosquitto_passwd -b /mosquitto/config/mosquitto.passwd "${MOSQUITTO_USERNAME}" "${MOSQUITTO_PASSWORD}"
fi

# Execute the main CMD from the Dockerfile
exec "$@"
