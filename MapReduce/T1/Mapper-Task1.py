#!/usr/bin/env python3

import sys
import json
import datetime
accident_info={}
for line in sys.stdin:
	line = line.strip()
	accident_info=json.loads(line)
	weather = ["Heavy Snow", "Thunderstorm", "Heavy Rain", "Heavy Rain Showers","Blowing Dust"]
	
	if( ("lane blocked" in accident_info["Description"] or "shoulder blocked" in accident_info["Description"] or "overturned vehicle" in accident_info["Description"] or "Lane blocked" in accident_info["Description"] or "Shoulder blocked" in accident_info["Description"] or "Overturned vehicle" in accident_info["Description"]) and accident_info["Severity"] >= 2 and accident_info["Sunrise_Sunset"]=="Night" and accident_info["Visibility(mi)"] <= 10.0 and accident_info["Precipitation(in)"] >= 0.2 and (accident_info["Weather_Condition"] in weather)):
		if(accident_info["Start_Time"]!="NaN"):
			datetimeobj=datetime.datetime.strptime(accident_info["Start_Time"], "%Y-%m-%d %H:%M:%S")
			if(datetimeobj.hour<10):
				hr='0'+str(datetimeobj.hour)
			else:
				hr = str(datetimeobj.hour)
			print('%s\t%d' % (hr, 1))
