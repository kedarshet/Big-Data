#!/usr/bin/env python3
import sys
import json

out = {}

for data in sys.stdin:
    obj = json.loads(data)
    
    state = obj['state']
    city = obj['city']

    if state in out:
        if(city in out[state]):
            out[state][city]+=1
        else:
            out[state][city] = 1
    else:
        out[state] = {}
        out[state][city] = 1
for state in out:
    print(state)
    total=0
    for city in out[state]:
        print(city,out[state][city])
        total+=out[state][city]
    print(state,total)
        
