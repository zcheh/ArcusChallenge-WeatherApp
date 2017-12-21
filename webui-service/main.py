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

app = Bottle()

@app.route('/')
def index(errors=""):
	title = "Weather App"
	header = "Enter info below:"
	info = {"title": title, "header": header, "errors": errors}	
	return template("index.tpl", info) 
	

@app.post('/weather')
def display_weather():
	#Get lat long from form 
	lat = request.forms.get('lat')
	long = request.forms.get('long')

	title = "Weather App"
	header = "Weather for ({0}, {1})".format(lat, long)

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
		info = {"title": title, "header": header, "days": weather_json, "errors": ""}		 
		return template("display_weather.tpl", info)
	else:
		return index(error)

app.run(host='192.168.1.210', port = 62100)
