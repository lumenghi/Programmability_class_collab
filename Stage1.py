import requests
import json

import fileinput

base_url = 'https://webexapis.com/v1'
endpoint = '/rooms'
token = "NDY3ZGIwMDktNWZmMS00MDQ3LTk3MDQtMDhiZjA1MWQ2MTczNDk5NTI2ZDMtN2M0_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

room_body ={
    "title":" Room Luca "
}

response = requests.post(url=f"{base_url}{endpoint}", headers=headers, data=json.dumps(room_body)).json()    
roomid=response['id']
print(roomid)

# Read in the file
with open('env.py', 'r') as file :
    filedata = file.read()

# Replace the target string
filedata = filedata.replace('<Replace me in stage 1>', roomid)

# Write the file out again
with open('env.py', 'w') as file:
    file.write(filedata)