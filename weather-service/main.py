# -*- coding: ascii -*-
# --------------------------------------------------------------------------- #
# File Name   : main.py
# Designer    : Zach Chehayeb
# Description : Retrieve past 7 days weather information from Dark Sky using
#               latitude and longitude passed in url. And provide JSON msg
#               that contains weather.
# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# Imports
# --------------------------------------------------------------------------- #

from bottle import Bottle, HTTPError
from urllib2 import urlopen 
import json
from time import time
import threading

app = Bottle()

# --------------------------------------------------------------------------- #
# Global Vars
# --------------------------------------------------------------------------- #
#Dark Sky URL Params
darksky_url = "https://api.darksky.net/forecast"
darksky_key = "8bb170dfde985aeb11bc1e26ba2491e9"
excludes = "currently,minutely,hourly,alerts,flags"

#Current Time
current_time = int(time())
day_lenth = 86400

class Point(object):
	def __init__(self, lat, long):
		try:
			self.lat = float(lat)
			self.long = float(long)
		except ValueError:
			self.is_valid = 0
			self.lat = None 
			self.long = None
		if self.lat > 90.0 or self.lat < -90.0 or self.long > 180.0 or self.long < -180.0:
			self.is_valid = 0
		else:
			self.is_valid = 1

def get_days_weather(each, weather_list, lat, long):
	#Computes the epoch time for this day
	day = current_time - (day_lenth * (each + 1))
	
	#Build URL for Dark Sky request
	weather_url ="{0}/{1}/{2},{3},{4}?exclude={5}".format(darksky_url, darksky_key, lat, long, day, excludes)

	try:
		darksky_call = urlopen(weather_url)
		status_code = darksky_call.getcode()
	except HTTPError, error:
		status_code = error.code
 
	#Read status code of request to determine if request successful
	if status_code == 200:
		weather_json = json.load(darksky_call)
		day_weather = weather_json 
		weather_list[each] = {"status": status_code, "result": day_weather, "time": day_weather["daily"]["data"][0]["time"]}
	else:
		weather_list[each] = {"status": status_code, "result": None, "time": day}
	
@app.route('/getweather/<lat>,<long>')
def get_weather(lat, long):
	#Create Point
	coordinate = Point(lat, long)

	if coordinate.is_valid == 1:	
		num_of_days = 7

		#Create a list with an empty item for each day. We then can store the results in order so we do not have to sort later.	
		weather_list = [None] * num_of_days 
		jobs = []
		
		num_of_days = 7
		#Stats thread to call each day separately
		for x in range(0,num_of_days):
			process = threading.Thread(target = get_days_weather, args = (x, weather_list, coordinate.lat, coordinate.long))
			jobs.append(process)
			process.start()
		for proc in jobs:
			proc.join()
		weather_full_json = json.dumps(weather_list)
		return weather_full_json	
		
	else:
		return HTTPError(400, "Invalid latitude or longitude.")	

#app.run(host='0.0.0.0', port = 8000)
	
