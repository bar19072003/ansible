#!/usr/bin/env python3

import requests

# Splunk deployment server and authentication information
deployment_server = "https://10.0.0.61:8089"
username = "bar"
password = "19072003"
app_name = "forwarder_python_APP"


# Authentication and get session key
auth_response = requests.post(f"{deployment_server}/services/auth/login", data={"username": username, "password": password}, verify=False)
auth_response.raise_for_status()
session_key = auth_response.text.split("<sessionKey>")[1].split("</sessionKey>")[0]


# Upload the scripts
script_paths = [
    ("/home/bar/ansible/forwarder_python_APP/bin/get_cert_expiry.py", "get_cert_expiry.py"),
    ("/home/bar/ansible/forwarder_python_APP/bin/get_server_version.py", "get_server_version.py"),
    ("/home/bar/ansible/forwarder_python_APP/bin/get_packages.py", "get_packages.py")
]

for script_path, script_name in script_paths:
    with open(script_path, 'rb') as script_file:
        files = {'file': (script_name, script_file)}
        script_upload_response = requests.post(
            f"{deployment_server}/services/apps/local/{app_name}/data/inputs/script/{script_name}",
            files=files,
            headers={"Authorization": f"Splunk {session_key}"},
            verify=False
        )
        script_upload_response.raise_for_status()

# Configure inputs
inputs_config = """
[script:///opt/splunkforwarder/etc/apps/forwarder_python_APP/bin/get_cert_expiry.py]
sourcetype = ssl_certificate_expiry
interval = 86400
disabled = false

[script:///opt/splunkforwarder/etc/apps/forwarder_python_APP/bin/get_server_version.py]
sourcetype = server_version
interval = 86400
disabled = false

[script:///opt/splunkforwarder/etc/apps/forwarder_python_APP/bin/get_packages.py]
sourcetype = packages_verison
interval = 86400
disabled = false
"""

input_response = requests.post(
    f"{DEPLOYMENT_SERVER}/services/apps/local/{APP_NAME}/inputs",
    data={"name": "inputs.conf", "content": inputs_config},
    headers={"Authorization": f"Splunk {session_key}"},
    verify=False
)
input_response.raise_for_status()

# Configure outputs
outputs_config = """
[tcpout]
defaultGroup=indexer1
disabled=false

[tcpout:indexer1]
server=10.0.0.32:9997
"""

output_response = requests.post(
    f"{deployment_server}/services/apps/local/{app_name}/outputs",
    data={"name": "outputs.conf", "content": outputs_config},
    headers={"Authorization": f"Splunk {session_key}"},
    verify=False
)
output_response.raise_for_status()

# Restart Splunk
restart_response = requests.post(
    f"{deployment_server}/services/server/control/restart",
    headers={"Authorization": f"Splunk {session_key}"},
    verify=False
)
restart_response.raise_for_status()