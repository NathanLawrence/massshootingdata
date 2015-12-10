import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "massshootingdata.settings")


import csv
from django.db import models
from eventsdb.models import *

with open('../toparse.csv', 'rb') as csvread:
	sheetreader = csv.DictReader(csvread, delimiter = ',', quotechar = '\"')
	print sheetreader.fieldnames

	for row in sheetreader:
		date = row['Date']
		shooter = row['Shooter']
		article_1 = row['Article_1']
		dead = int(row['Dead']) #As it turns out, dynamic typing is a dangerous thing. Without these, some numbers were being concatenated as strings.
		injured = int(row['Injured']) #As it turns out, dynamic typing is a dangerous thing. Without these, some numbers were being concatenated as strings.
		locArray = row['Location'].split(', ')
		city = locArray[0]
		state = locArray[1]
		print str(total) + " killed or injured in " + state + " by " + shooter #String casting was a necessity to make acceptable output since the variables were cast as int literals.
		location = Location(city = city, state = state)
		location.save()