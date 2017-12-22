# -*- coding: ascii -*-
# --------------------------------------------------------------------------- #
# File Name   : main.py
# Designer    : Zach Chehayeb
# Description : Microservice that takes an address string as part of the url
#               and returns the lat and long in JSON.
# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# Imports
# --------------------------------------------------------------------------- #

from bottle import Bottle, HTTPError
import urllib2
import json

app = Bottle()

@app.route('/getlocation/<location>')
def get_location(location):
	
	#Google URL Params
	google_url = "https://maps.googleapis.com/maps/api/geocode/json"
	google_key = "AIzaSyBRfJgXmZDT7xnUZIxrYnKhGXRb_oyqm-g"
	location_url = urllib2.quote("{0}?address={1}&key={2}".format(google_url, location, google_key), ':/?&=,')

	#Make call and catch error.
	try:
		location_call = urllib2.urlopen(location_url) 
		status_code = location_call.getcode()
	except HTTPError, error:
		status_code = error.code
	
	if status_code == 200:
		json_result = json.load(location_call)	
		if json_result["status"] == 'OK':
			geocode_json = json_result["results"][0]["geometry"]["location"]
		else:
			return HTTPError(400, "Unable to determine location")
		return geocode_json
	else:
		return HTTPError(400, "Unable to determine location")	

app.run(host='192.168.1.210', port = 8001)
