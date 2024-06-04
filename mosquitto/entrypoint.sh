#!/bin/sh

# Create Mosquitto username and password
if [ -n "${MOSQUITTO_USERNAME}" ] && [ -n "${MOSQUITTO_PASSWORD}" ]; then
    mosquitto_passwd -b -c /mosquitto/config/pass "${MOSQUITTO_USERNAME}" "${MOSQUITTO_PASSWORD}"
    chown mosquitto:mosquitto /mosquitto/config/pass
fi

# Execute the main CMD from the Dockerfile
exec "$@"
