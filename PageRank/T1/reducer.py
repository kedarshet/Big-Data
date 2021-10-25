#!/usr/bin/env python3
import sys 
v_loc = sys.argv[1].strip()
v_file = open(v_loc,'w+')
prev = -1

for line in sys.stdin:
    line=line.strip()
    nodes=line.split('\t')
    if prev != int(nodes[0]):
        v_file.write(nodes[0]+',1\n')
        if prev!=-1:
            print(']')
        print(nodes[0]+' ['+nodes[1],end='')
        prev=int(nodes[0])
    else:
        print(','+nodes[1],end='')

print(']')
v_file.close()