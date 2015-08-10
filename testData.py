#!/usr/bin/python

# Nancy Agrawal

# Script to generate random data at specified sampling rate
# for testing air quality sensor integration with raspberry pi
# NOTE: A folder named sensorData must be created where this script is run.

import random
import time
import csv

def getDuplet(samplingRate, newFileDelay):		
	now = time.time()
	delay =  newFileDelay*60
	data = []
	while (time.time()-now) < delay:
		duplet = str(random.uniform(0,20)) + "," + str(time.time())
		data += [duplet.split(",")]
		time.sleep(samplingRate)
	path = "./sensorData/" + time.ctime(time.time()) + ".csv"
	with open(path,"wb") as csv_file:
		writer = csv.writer(csv_file,delimiter=',')
		for line in data:
			writer.writerow(line)

# Get sampling rate and newFileDelay from user
samplingRate = float(raw_input('Enter sampling rate in seconds. (For 1 ms, enter 0.001):  '))
newFileDelay = float(raw_input('Enter time in minutes after which new file should be created: '))
fileCount = 1
while 1:
	print "Creating file no. " + str(fileCount)
	fileCount += 1
	getDuplet(samplingRate,newFileDelay)
