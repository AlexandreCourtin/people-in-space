#!/usr/local/bin/python3

import requests

getReq = requests.get('http://api.open-notify.org/astros.json')
print('There is ' + str(getReq.json()['number']) + ' people in space right now !')

for people in getReq.json()['people']:
    print(people['name'] + ' on the craft ' + people['craft'])
