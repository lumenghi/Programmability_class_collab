import requests
import json

import fileinput

base_url = 'https://webexapis.com/v1'
endpoint = '/rooms?type=group'
token = "NDY3ZGIwMDktNWZmMS00MDQ3LTk3MDQtMDhiZjA1MWQ2MTczNDk5NTI2ZDMtN2M0_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

try:
    response = requests.get(url=f"{base_url}{endpoint}", headers=headers)
    if response.status_code == 200:
        get_rooms = response.json()
        rooms=get_rooms['items']
        for room in rooms:
            if room['title']=="CSAP Programmability CTF - Team 2":
                roomid=room['id']
                print(roomid)
    
    # Read in file
    with open('env.py', 'r') as file :
        filedata = file.read()

    # Replace target string
    filedata = filedata.replace('<Replace me in stage 0>', roomid)

    # Write file again
    with open('env.py', 'w') as file:
        file.write(filedata)
                
except Exception as ex:
    print(ex)