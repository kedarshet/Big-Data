#!/usr/bin/env python3

import sys
curr_hour=None
curr_count=0
hour=None
dict1={}
for line in sys.stdin:

	line=line.strip()
	hour, count = line.split('\t',1)
	try:
		count=int(count)
		hour=int(hour)
	except ValueError:
		continue
	if(curr_hour==hour):
		curr_count+=count
	else:
		if curr_hour:
			print('%s\t%d' % (curr_hour, curr_count))
		curr_count=count
		curr_hour=hour
if curr_hour==hour:
	print('%s\t%d' % (curr_hour, curr_count))
	
