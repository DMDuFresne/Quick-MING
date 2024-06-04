#!/bin/sh

# Ensure NODE_RED_PASSWORD is provided
if [ -z "$NODE_RED_PASSWORD" ]; then
  echo "NODE_RED_PASSWORD environment variable is not set."
  exit 1
fi

# Generate the password hash
PASSWORD_HASH=$(node hash-password.js "$NODE_RED_PASSWORD")

# Use `sed` to replace the password placeholder in settings.js
sed -i "s|<PASSWORD_HASH_PLACEHOLDER>|$PASSWORD_HASH|g" /data/settings.js

# Start Node-RED
exec node-red --userDir /data