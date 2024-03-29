#!/usr/bin/env python3
#Need to install requests package for python
#easy_install requests
import requests

# Set the request parameters
url = 'https://dev211781.service-now.com/api/now/table/incident?sysparm_display_value=true&sysparm_exclude_reference_link=true&sysparm_fields=short_description%2Cnumber'

# Eg. User name="admin", Password="admin" for this code sample.
user = 'admin'
pwd = 'Barbibi2003!'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.post(url, auth=(user, pwd), headers=headers ,data="{\"short_description\":\"test via python\"}")

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)