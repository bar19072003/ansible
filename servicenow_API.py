#!/usr/bin/env python3
#ServiceNow API post request, insert "test via python" to short description field
#Need to install requests package for python
import requests

url = 'https://dev211781.service-now.com/api/now/table/incident?sysparm_display_value=true&sysparm_exclude_reference_link=true&sysparm_fields=short_description%2Cnumber'

user = 'admin'
pwd = 'Barbibi2003!'

headers = {"Content-Type":"application/json","Accept":"application/json"}


response = requests.post(url, auth=(user, pwd), headers=headers ,data="{\"short_description\":\"test via python\"}")


if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

data = response.json()
print(data)
