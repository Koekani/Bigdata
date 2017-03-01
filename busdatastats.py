# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 19:48:25 2016

Given task:

Write a Python program that reads the bus location data recorded in busdata.py
and prints out the following information separately for each bus line that appears in the data:

- How many different vehicles appear in the data (for the particular bus line)?
- How many unique data points were recorded (for the particular bus line)?
  Here "unique" means unique in terms of time and a particular vehicle:
  the data may contain several data points that correspond to the same time and the same vehicle.


@author: Kimmo Ronkainen
"""

import StringIO
import json
import sets

lines = {}

busdata = open("busdata.json", "r")

databuf = StringIO.StringIO()  # Initialize an empty StringIO file.
for line in busdata:       # Read the original busdata file one line at a time.
    databuf.write(line)    # Write the read line into the StringIO file.
    if line == '}\n':      # Did we reach the end of a top-level dictionary?
        databuf.seek(0)    # Set the StringIO to enable reading from its beginning.
        data = json.load(databuf)   # Read the single top-level JSON dictionary.
        databuf.close()             # Discard the current StringIO object.
        databuf = StringIO.StringIO()  # Initialize a new empty StringIO object.
        # Now data can be used as a normal Python dictionary.
        for item in data['body']:
            #getting line id in question            
            line = item['monitoredVehicleJourney']['lineRef']
            #if line is not in dict yet, add it. Then update             
            if not lines.has_key(line):
                 lines[line] = {'datapoints': 0, 'busses': set()}
            lines[line]['datapoints'] += 1
            #getting bus id in question and adding it to lines set of busses            
            bus = item['monitoredVehicleJourney']['vehicleRef']
            lines[line]['busses'].add(bus)
            
databuf.close()            # Discard the StringIO file also in the end.


#printing doest work right. Problem with number of different busses. Not sure if set works right
for item in sorted(lines):
    print item + ": "
    print len(item['busses'])
    print "venicles and "
    print item['datapoints']
    print " datapoints"
    
    
    
    