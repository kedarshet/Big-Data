#!/usr/bin/env python3
import sys 

for line in sys.stdin:
  line=line.strip()
  nodes = line.split()
  print('%s\t%s' % (nodes[0], nodes[1]))