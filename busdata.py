# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 19:01:33 2016

Given task:

Write a Python program that records real time location data about the buses of the Tampere public transportation network.
Such data can be retrieved easily from the Journeys API offered by ITS Factory.

The program receives three command line parameters:

- The name of the file into which it should store the information.
- The time interval (in seconds) between successive data retrievals from the Journeys API.
     E.g. if this parameter is 5, then new data is retrieved every 5 seconds.
- The time (in seconds) how long the program should keep recording the information.
     E.g. if this parameter is 3600, then the program should continue to retrieve and store
     the data for one hour. If the time interval specified by the preceding parameter would be 5,
     then this would mean that the program would retrieve roughly 3600/5 = 720 pieces of data during its execution.

@author: Kimmo Ronkainen
"""

#importing needed libraries, sys for reading args, urllib for getting data from www and time
#for timing loop
import sys
import urllib.request
import time

#getting args
timeleft = int(sys.argv[3])
sleeptime = int(sys.argv[2])

#untill time runs out, we get data and store it to given file.
while timeleft > 0:
    with urllib.request.urlopen("http://data.itsfactory.fi/journeys/api/1/vehicle-activity") as response:
        data = response.read()
    my_file = open(sys.argv[1], "w")
    my_file.write(str(data))
    my_file.close()
    time.sleep(sleeptime)
    timeleft = timeleft - sleeptime