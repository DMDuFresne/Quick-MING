# Quick MING Setup

This repository provides a rapid deployment setup for the MING stack: **MQTT, InfluxDB, Node-RED, and Grafana**. Designed for simplicity, this environment is containerized using Docker and orchestrated with `docker-compose`.

## Prerequisites

Before you begin, ensure you have the following:
- Docker and Docker Compose installed on your system.
- A fundamental understanding of Docker and containerization concepts.

## Project Structure

```
Quick MING/
│
├── mosquitto               # MQTT Broker configurations
│   ├── Dockerfile
│   └── ...
│
├── node-red                # Node-RED configurations and flows
│   ├── Dockerfile
│   └── ...
│
├── .env                    # Environment variables for services
└── docker-compose.yaml     # Docker Compose configuration
```

## Setting Node-Red Password Using bcrypt

Node-Red requires the use of bcrypt for hashing passwords. To generate a bcrypt hash:

- Visit an online bcrypt generator, like [bcrypt.online](https://bcrypt.online/).

- Enter your desired password and select a Cost Factor. Generate the hash by clicking Generate Hash.

- Copy the generated hash into the .env file for the NODE_RED_PASSWORD. Use single quotes around the hash (e.g. generatedhash'). This is important because Docker Compose interprets $ as a special character for variable substitution.

## Configuration

1. Clone the repository:

    ```bash
    git clone https://github.com/DMDuFresne/Quick-MING.git
    ```

2. Rename  `example.env` to ` .env` and configure the environment variables according to your setup.

3. Ensure ports in `docker-compose.yaml` are not in use or change them accordingly.

## Usage

1. Start the environment by running:

    ```bash
    docker-compose up -d --build
    ```

2. Use the stack to build whatever you want.

## Services

The stack includes:

- **Mosquitto:** MQTT broker on port `1883`.

- **InfluxDB:** Time-series database on port `8086`.

- **Node-RED:** Wiring tool for devices and online services on port `1880`.

- **Grafana:** Monitoring and observability platform on port `3000`.

- **Telegraf:** An agent for collecting, processing, aggregating, and writing metrics.

## Attribution

This project is possible thanks to the use and support from the following open-source projects:

- [Eclipse Mosquitto](https://mosquitto.org/): A reliable and lightweight MQTT broker.

- [InfluxDB](https://www.influxdata.com/): A purpose-built database designed to handle time-stamped data at scale.

- [Node-RED](https://nodered.org/): A visual tool for wiring the Internet of Things.

- [Grafana](https://grafana.com/): An analytics platform for all your metrics.

- [Telegraf](https://github.com/influxdata/telegraf/): A server agent to collect metrics.

- [mpous/ming](https://github.com/mpous/ming): The MING stack as used in this project is inspired by the work done by [Marc Pous](https://github.com/mpous).

Each tool brings unique capabilities to any project, and their combination allows for a robust data monitoring solution. For their individual licensing terms, please refer to their respective websites or documentation.
