import requests
import json

import fileinput

base_url = 'https://webexapis.com/v1'
endpoint1 = '/meetings'
token = "NDY3ZGIwMDktNWZmMS00MDQ3LTk3MDQtMDhiZjA1MWQ2MTczNDk5NTI2ZDMtN2M0_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

numberMeetings=0
response = requests.get(url=f"{base_url}{endpoint1}", headers=headers).json()
for meeting in response['items']:
    numberMeetings=numberMeetings+1



endpoint2 = '/rooms?type=group'

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

numberSpaces=0
response = requests.get(url=f"{base_url}{endpoint2}", headers=headers).json()
for space in response['items']:
    numberSpaces=numberSpaces+1



endpoint3 = '/messages?roomId=Y2lzY29zcGFyazovL3VzL1JPT00vODA1MTE4NDAtODBlMC0xMWViLWIzN2YtMDc4NmVlNDAzOTg3'

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

numberMessages=0
response = requests.get(url=f"{base_url}{endpoint3}", headers=headers).json()
for msg in response['items']:
    numberMessages=numberMessages+1



endpoint4 = '/messages'

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

body ={
    "roomId":"Y2lzY29zcGFyazovL3VzL1JPT00vODA1MTE4NDAtODBlMC0xMWViLWIzN2YtMDc4NmVlNDAzOTg3",
    "text": f"The number of meetings I have planned is: {numberMeetings}. The  number of spaces I am part of is: {numberSpaces}. The number of messages that I had sent in this space until now is: {numberMessages}."
}

response = requests.post(url=f"{base_url}{endpoint4}", headers=headers, data=json.dumps(body)).json()