#!/usr/bin/env python3
import sys 
import json
import math

v_file = sys.argv[1]
v_dict = {}
with open(v_file,'r') as v:
    for line in v:
        line = line.strip()
        node = line.split(',')
        v_dict[node[0]] = node[1]

page_embeddings_file = open(sys.argv[2]) #json
page_embeddings = json.load(page_embeddings_file)

def similarity(p,q):
    mag_p = 0
    mag_q = 0
    product=0
    for i in range(0,len(p)):
        product += p[i]*q[i]
        mag_p += (p[i])**2
        mag_q += (q[i])**2
    mag_p = math.sqrt(mag_p)
    mag_q = math.sqrt(mag_q)
    return product/(mag_p*mag_q)

for line in sys.stdin:
    line=line.strip()
    nodes = line.split(' ')
    links = eval(nodes[1])
    print(nodes[0]+'\t'+"0")
    len1 = len(links)
    key = str(nodes[0])
    prev_rank = float(v_dict[key])
    for j in links:
        j = str(j)
        contribution = prev_rank*similarity(page_embeddings[key],page_embeddings[j])* (1/len1)
        print(j+'\t'+str(contribution))
