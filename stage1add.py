import requests
import json

import fileinput

base_url = 'https://webexapis.com/v1'
endpoint = '/memberships'
token = "NDY3ZGIwMDktNWZmMS00MDQ3LTk3MDQtMDhiZjA1MWQ2MTczNDk5NTI2ZDMtN2M0_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

body1 ={
    "roomId":"Y2lzY29zcGFyazovL3VzL1JPT00vODA1MTE4NDAtODBlMC0xMWViLWIzN2YtMDc4NmVlNDAzOTg3",
    "personEmail":"frewagne@cisco.com"
}

body2 ={
    "roomId":"Y2lzY29zcGFyazovL3VzL1JPT00vODA1MTE4NDAtODBlMC0xMWViLWIzN2YtMDc4NmVlNDAzOTg3",
    "personEmail":"mneiding@cisco.com"
}

response = requests.post(url=f"{base_url}{endpoint}", headers=headers, data=json.dumps(body1)).json()
response = requests.post(url=f"{base_url}{endpoint}", headers=headers, data=json.dumps(body2)).json()