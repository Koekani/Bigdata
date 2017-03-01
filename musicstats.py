# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 17:19:25 2016

@author: Kimmo Ronkainen

Given task:

Your task is to write a Python program that reads the two above described files and then computes and
prints out the following information (based on the logged information):

- What is the maximum number of different tracks listened by any single customer?
  Also print out the names of all customers (may be one or several) who listened
  to the maximum number of different tracks.
  
- By using the  Welch's t-test, print out a conclusion regarding the hypothesis that men and women
  listen to on average as many tracks. ​That is: is the average number of tracks listened to by men
   statistically significantly different from the average number of tracks listened to by women?
   
- By using the t-test between dependent samples, print out a conclusion regarding the hypothesis
  that users listen to as many tracks when connecting from a mobile device as when connecting from
  a non-mobile device.

"""

from scipy import stats


#classes for holding track and customer data
class Track(object):
    
    def __init__(self, eventid, cid, trackid, mobile):
        self.eventId = eventid
        self.trackid = trackid
        self.cid = cid
        self.mobile = mobile
        
        
        
class Customer(object):
    
    def __init__(self, cid, name, gender):
        self.cid = cid
        self.name = name
        self.gender = gender
        self.tracks_listened = []
        self.countTracks = 0
    
    def check_track(self, track):
        if track not in self.tracks_listened:
            self.tracks_listened.append(track)
            self.countTracks += 1
    
    def print_name(self):
        print (self.name)
        
    def print_info(self):
        print (self.name)
        print (self.gender)
        print (self.countTracks)
        print ("listened tracks: ")
        for item in self.tracks_listened:
            print (item)
    
    def tracks(self):
        return self.countTracks
    

#lists for holding instances from classes
custarr = []
trackarr = []

#opening file and creating new track instance and storing it to list per iteration
with open("tracks.csv", "r") as f:
    for line in f:
        data = line.split(',')
        y = Track(int(data[1]), int(data[1]), int(data[2]), int(data[4]))
        trackarr.append(y)

#opening file and creating new customer instance and storing it to list per iteration
with open("cust.csv", "r") as f:
    for line in f:
        data = line.split(',')
        if data[0] != "CustID":
            x = Customer(int(data[0]),str(data[1]),int(data[2]))
            custarr.append(x)
    
#Loop goes through all tracks and checks if user has listened
#it before. If not, it should add that track to tracks user has listened and increased
#total number of listened tracks by one.
for track in trackarr:
    customer = int(track.cid)
    song = int(track.trackid)    
    custarr[customer].check_track(song)

#these loops should check which is highest count for listened songs and
#second loop prints names of all customers with highest count         
most_songs = 0

for cus in custarr:
    if cus.countTracks > most_songs:
        most_songs = cus.countTracks

print ("Most tracks listened by: ")
for cus in custarr:     
    if cus.countTracks == most_songs:
        cus.print_name()
        print (cus.countTracks)

#two lists for holding info about men and woman
menarr = []
womanarr = []

#loop that tracks how many songs have men and women listened, adding both to own arrays
for cus in custarr:   
    if cus.countTracks > 0:
        if cus.gender == 0:
            menarr.append(cus.tracks())
        else:
            womanarr.append(cus.tracks())            

#printing results from test from scipy library
print ("Welch-T test to hypothesis that womans and men listen to average same amount of tracks")
print (stats.ttest_ind(menarr, womanarr))


#creating arrays to hold data for each customers usage in mobile and nonmobile
#array index in same as customer id
nonmobarr = [0] * len(custarr)
mobarr = [0] * len(custarr)

#going through data to find
for track in trackarr:
    user = int(track.cid)    
    if track.mobile == 0:
        nonmobarr[user] += 1
    else:
        mobarr[user] += 1
        
#printing test results from test from scipy library
print ("T-test for hypothesis that users listen to as many tracks")
print ("when connecting from a mobile device as when connecting from a non-mobile device")
print (stats.ttest_rel(nonmobarr, mobarr))
        
    
