FROM eclipse-mosquitto:latest

# Copy the entrypoint script
COPY docker-entrypoint.sh /docker-entrypoint.sh

# Ensure the entrypoint script is executable
RUN chmod +x /docker-entrypoint.sh

# Copy the custom mosquitto.conf
COPY mosquitto.conf /mosquitto/config/mosquitto.conf

# Set the entrypoint
ENTRYPOINT ["/docker-entrypoint.sh"]

# Continue with the standard Mosquitto CMD
CMD ["/usr/sbin/mosquitto", "-c", "/mosquitto/config/mosquitto.conf"]
