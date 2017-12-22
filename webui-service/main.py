# -*- coding: ascii -*-
# --------------------------------------------------------------------------- #
# File Name   : main.py
# Designer    : Zach Chehayeb
# Description : Web interface that gets last 7 days weather based on location.
# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# Imports
# --------------------------------------------------------------------------- #

from bottle import Bottle, request, template
from urllib2 import urlopen, quote, HTTPError
import json
from time import time, strftime, localtime

app = Bottle()

@app.route('/')
def index(errors=[]):
	title = "Weather App"
	header = "Enter location below for previous weather:"
	info = {"title": title, "header": header, "errors": errors}	
	return template("index.tpl", info) 
	

@app.post('/weather')
def display_weather():
	#Get address (city, state) from form 
	address = request.forms.get('address')
	
	#Build geocode url and make call
	geocode_service_url = quote("https://arcuschallenge-getlocation.appspot.com/getlocation/{0}".format(address), ':/?&=,')
	try:
		geocode_service_call = urlopen(geocode_service_url)
		geocode_status_code = geocode_service_call.getcode()
	except HTTPError, error:
		geocode_status_code = error.code

        if geocode_status_code == 200:
                geocode_json = json.load(geocode_service_call)
                lat = geocode_json["lat"]
                long = geocode_json["lng"]
        else:
                return index(errors=["Invalid Address - Please check, renter and try again."])


	title = "Weather App"
	header = "Weather for {2} ({0}, {1})".format(lat, long, address)

	#Build weather url and make call
	weather_service_url = quote("https://arcuschallenge-getweather.appspot.com/getweather/{0},{1}".format(lat,long), ':/?&=,')
	try:
		weather_service_call = urlopen(weather_service_url)
		weather_status_code = weather_service_call.getcode()
	except HTTPError, error:
		weather_status_code = error.code
		error = error.reason
	
	#Check weather call status code
	if weather_status_code == 200:
		weather_json = json.load(weather_service_call) 
		content = []
		 
		#Loop through each day weather and take variables that we want to display
		for each_day in weather_json:
			
			#Check each days weather to see if we got weather for that day
			if each_day["status"] == 200:
				day_weather = each_day["result"]["daily"]["data"][0]
				weather_summary = day_weather["summary"]
				weather_high = day_weather["temperatureHigh"]
				weather_low = day_weather["temperatureLow"]
			else:
				weather_summary = "Could not get weather for this day."
				weather_high = "Unknown"
				weather_low = "Unknown"

			weather_time = strftime('%A, %B %d, %Y', localtime(each_day["time"]))
			content.append([weather_time, weather_summary, weather_high, weather_low])
		
		info = {"title": title, "header": header, "days": content, "errors": ""}
		return template("display_weather.tpl", info)
	else:
		return index(errors=[error])

#app.run(host='0.0.0.0', port = 62100)
