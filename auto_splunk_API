#!/bin/bash

# create the forwarder application using splunk API


# Splunk deployment server and authentication information
DEPLOYMENT_SERVER="https://10.0.0.61:8089"
USERNAME="splunk"
PASSWORD="19072003"
APP_NAME="forwarder_APP"

# Authentication and get session key
auth_response=$(curl -k -s -d "username=bar&password=19072003" "$DEPLOYMENT_SERVER/services/auth/login")
session_key=$(echo "$auth_response" | grep -oPm1 "(?<=<sessionKey>)[^<]+")

# Upload the script
app_create_response=$(curl -k -s -X POST -d "name=$APP_NAME" -H "Authorization: Splunk $session_key" "$DEPLOYMENT_SERVER/services/apps/local")
# create the script
script_path="/home/bar/ansible/ssl_certificate_monitor/bin/get_cert_expiry.sh"
script_upload_response=$(curl -k -s -X POST -d "name=get_cert_expiry.sh&file=$script_path" -H Authorization: Splunk $session_key "$DEPLOYMENT_SERVER/services/apps/local/$APP_NAME/data/inputs/script/get_cert_expiry.sh")

script_path2="/home/bar/ansible/ssl_certificate_monitor/bin/get_server_version.sh"
script2_upload_response=$(curl -k -s -X POST -d "name=get_server_version.sh&file=$script_path2" -H Authorization: Splunk $session_key "$DEPLOYMENT_SERVER/services/apps/local/$APP_NAME/data/inputs/script/get_server_version.sh")

script_path3="/home/bar/ansible/ssl_certificate_monitor/bin/get_packages.sh"
script3_upload_response=$(curl -k -s -X POST -d "name=get_packages.sh&file=$script_path3" -H Authorization: Splunk $session_key "$DEPLOYMENT_SERVER/services/apps/local/$APP_NAME/data/inputs/script/get_packages.sh")

# Configure inputs
inputs_config="[script:///opt/splunkforwarder/etc/apps/ssl_certificate_monitor/bin/get_cert_expiry.sh]
sourcetype = ssl_certificate_expiry
interval = 86400
disabled = false

[script:///opt/splunkforwarder/etc/apps/ssl_certificate_monitor/bin/get_server_version.sh]
sourcetype = server_version
interval = 86400
disabled = false

[script:///opt/splunkforwarder/etc/apps/ssl_certificate_monitor/bin/get_packages.sh]
sourcetype = packages_verison
interval = 86400
disabled = false
"
input_response=$(curl -k -s -X POST -d "name=inputs.conf&content=$input_config" -H "Authorization: Splunk $session_key" "$DEPLOYMENT_SERVER/services/apps/local/$APP_NAME/inputs")

# Configure outputs
outputs_config="[tcpout]
defaultGroup=indexer1
disabled=false

[tcpout:indexer1]
server=10.0.0.32:9997
"
output_response=$(curl -k -s -X POST -d "name-outputs.conf&content=$outputs_config" -H "Authorization: Splunk $session_key" "$DEPLOYMENT_SERVER/services/apps/local/$APP_NAME/outputs")

# Restart splunk
restart_response=$(curl -k -s -X POST -H "Authorization: Splunk $session_key" "$DEPLOYMENT_SERVER/services/server/control/restart")

