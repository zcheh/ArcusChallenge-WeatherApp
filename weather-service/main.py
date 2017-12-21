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

from bottle import Bottle
import urllib2 
import json
from time import time

app = Bottle()

@app.get('/getweather/<lat>,<long>')
def get_weather2(lat, long):
	darksky_url = "https://api.darksky.net/forecast"
	darksky_key = "8bb170dfde985aeb11bc1e26ba2491e9"
	current_time = int(time())
	excludes = "currently,minutely,hourly,alerts,flags"
	day_lenth = 86400
	day = current_time
	weather_list = []

	for each in range(0, 7):	
		weather_url ="{0}/{1}/{2},{3},{4}?exclude={5}".format(darksky_url, darksky_key, lat, long, day, excludes)
		darksky_call = urllib2.urlopen(weather_url)
		
		#Basic status code check to ensure we get back data
		status_code = darksky_call.getcode()
		if status_code == 200:
			weather_json = json.load(darksky_call)
			day_weather = weather_json
			weather_list.append({"status": status_code, "result": day_weather, "time": day})
		else:
			weather_list.append({"status": status_code, "result": None, "time": day})
	
		day -= day_lenth
	
	weather_full_json = json.dumps(weather_list)
	return weather_full_json	

app.run(host='192.168.1.210', port = 8000)
