import requests
import json

import fileinput

base_url = 'https://webexapis.com/v1'
endpoint = '/messages'
token = "NDY3ZGIwMDktNWZmMS00MDQ3LTk3MDQtMDhiZjA1MWQ2MTczNDk5NTI2ZDMtN2M0_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

body ={
    "roomId":"Y2lzY29zcGFyazovL3VzL1JPT00vODA1MTE4NDAtODBlMC0xMWViLWIzN2YtMDc4NmVlNDAzOTg3",
    "text":"I'm sorry that you have to receive a ton of messages, here's a joke to make you smile: What's the best thing about switzerland? I do not know, but the flag is a big plus!"
}

response = requests.post(url=f"{base_url}{endpoint}", headers=headers, data=json.dumps(body)).json()