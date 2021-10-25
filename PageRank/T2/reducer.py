#!/usr/bin/env python3
import sys 

prev = '-1'
rank = 0.15
contri = 0
for line in sys.stdin:
    line = line.strip()
    nodes = line.split()
    if prev!=nodes[0]:
        if prev != '-1':
            rank += 0.85*contri
            print("{},{:.2f}".format(prev,rank))
            rank = 0.15
            contri = 0
        prev = nodes[0]
        contri = float(nodes[1])
    else:
        contri += float(nodes[1])
rank += 0.85*contri
print("{},{:.2f}".format(prev,rank))