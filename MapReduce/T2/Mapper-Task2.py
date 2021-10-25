#!/usr/bin/env python3
import sys
import requests
import json
from math import sqrt

lat1 = float(sys.argv[1])
lon1 = float(sys.argv[2])
d = float(sys.argv[3])
url = 'http://20.185.44.219:5000'
# accident_map = []
i=0
for data in sys.stdin:
    obj = json.loads(data)
    lat2 = float(obj['Start_Lat'])
    lon2 = float(obj['Start_Lng'])
    dist = sqrt((lat2-lat1)**2 + (lon2-lon1)**2)
    if dist<d:
        req = {"latitude":obj['Start_Lat'],"longitude": obj['Start_Lng']}
        # print(req)
        res = requests.post(url, json = req)
        res = res.text
        res = json.loads(res)
        res = {"state":res["state"],"city":res["city"]}
        # accident_map.append(res)
        print(json.dumps(res))
    

