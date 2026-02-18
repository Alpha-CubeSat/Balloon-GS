# Balloon Ground Station
Ground Station for the SP26 Balloon Launch. Based on https://github.com/Alpha-CubeSat/Alpha-Cubesat-Ground-Python

Install ElasticSearch. ElasticSearch is what the ground system uses to store telemetry data received from the satellite. A guide for installation can be found in Elastic's documentation. Then, configure ElasticSearch as necessary (configuration at /etc/elasticsearch/elasticsearch.yml). By default Elasticsearch will listen on localhost:9200.

Install Kibana. Kibana is a visualization tool for creating graphics out of data in ElasticSearch. This will be useful for configuring alerts, graphs, and other aggregations of telemetry data. A guide for installation can be found in Kibana's documentation. Kibana can be configured as needed in the configuration file (at /etc/kibana/kibana.yml). By default Kibana will listen on localhost:5601.

Configure the Backend Server. Navigate to cubesat-backend and configure the backend by creating an .env file in the folder. You will need to configure the following environmental variables:

ROCKBLOCK_USER, ROCKBLOCK_PASS: The username and password of the RockBlock Web Services account used for receiving telemetry and sending commands.
GS_ADMIN_PASS: The password for the ground station's admin user.
ELASTIC_USER, ELASTIC_PASS: The username and password of the Elasticsearch superuser account.
ELASTIC_CERTS: The filepath to Elasticsearch's HTTPS certificates, usually located in <elasticsearch base path>/config/certs/http_ca.crt.
Run the Backend Server. Run the command flask run. This will start the backend server that listens for requests at localhost:5000. On first run, it many neccessary to run the flask init-db command to setup the user database. An interactive API documentation playground will also be generated when the development server is booted, which can be found at /docs.

Configure the Frontend. Navigate to cubesat-frontend and configure the frontned by creating an .env file in the folder. You will need to configure the following environmental variables:

REACT_APP_BASE_API_URL: The URL of the backend server that the frontend makes API requests to.
REACT_APP_KIBANA_URL: The URL of the Kibana server (used to form the base URL for viewing normal reports in Kibana).
REACT_APP_KIBANA_NR_DOC_ID: The ID of the Kibana cubesat_normal_report document (used to form the base URL for viewing normal reports in Kibana).
Run the Frontend UI. Once configured, run the command npm start (make sure the backend server is still running). This will start the fronend server which is assessable at localhost:3000.
