# -*- coding: ascii -*-
# --------------------------------------------------------------------------- #
# File Name   : test.py
# Designer    : Zach Chehayeb
# Description : Test getweather microservice. 
# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# Imports
# --------------------------------------------------------------------------- #

from urllib2 import urlopen, HTTPError 
import json
from random import uniform

# --------------------------------------------------------------------------- #
# Global Vars
# --------------------------------------------------------------------------- #
getweather_base_url = "http://127.0.0.1:8000"
passed_msg = "Result...    PASSED\n"
failed_msg = "Result...    FAILED\n"

print "\nStarting Tests..\n\n"
# --------------------------------------------------------------------------- #
# /general test
# --------------------------------------------------------------------------- #
def unknown_url():
        print "Unknown URL test"
        url = "{0}".format(getweather_base_url)
        print "Making Request to {0}".format(url)
        try:
                weather_service_call = urlopen(url)
                status_code = weather_service_call.getcode()
        except HTTPError, error:
                status_code = error.code

        if status_code == 404:
                print passed_msg
        else:
                print failed_msg

unknown_url()

# --------------------------------------------------------------------------- #
# /getweather tests
# --------------------------------------------------------------------------- #
getweather_url = "{0}/getweather/".format(getweather_base_url)
def getweather_successful_request():
        print "GetWeather successful return test"
	lat = uniform(-90.0, 90.0)
	long = uniform(-180.0, 180.0)
	print "Lat = {0} and Long = {1}".format(lat, long)
        url = "{0}{1},{2}".format(getweather_url, lat, long)
        print "Making Request to {0}".format(url)
        try:
                weather_service_call = urlopen(url)
                status_code = weather_service_call.getcode()
        except HTTPError, error:
                status_code = error.code

        if status_code == 200:
		try:
			json.load(weather_service_call)
			print "Result is JSON"
                	print passed_msg
		except:
			print failed_msg
        else:
                print failed_msg

getweather_successful_request()

def test_out_bounds_request():
	print "Out of bounds test (both lat/long)"
	url = "{0}91.0,182.0".format(getweather_url)
	print "Making Request to {0}".format(url)
	try:
		weather_service_call = urlopen(url)
		status_code = weather_service_call.getcode()
        except HTTPError, error:
                status_code = error.code
	
	if status_code == 400:
		print passed_msg 
	else:
		print failed_msg

	print "Out of bounds test (just long out of bounds)"
        url = "{0}79.0,182.0".format(getweather_url)
        print "Making Request to {0}".format(url)
        try:
                weather_service_call = urlopen(url)
                status_code = weather_service_call.getcode()
        except HTTPError, error:
                status_code = error.code
 
        if status_code == 400:
                print passed_msg
        else:
                print failed_msg

        print "Out of bounds test (just lat out of bounds)"
        url = "{0}91.52,179.265".format(getweather_url)
        print "Making Request to {0}".format(url)
        try:
                weather_service_call = urlopen(url)
                status_code = weather_service_call.getcode()
        except HTTPError, error:
                status_code = error.code

        if status_code == 400:
                print passed_msg
        else:
                print failed_msg

test_out_bounds_request()

def no_lat_long_request():
        print "No Lat/Long test"
        url = "{0}".format(getweather_url)
        print "Making Request to {0}".format(url)
        try:
                weather_service_call = urlopen(url)
                status_code = weather_service_call.getcode()
        except HTTPError, error:
                status_code = error.code

        if status_code == 404:
                print passed_msg
        else:
                print failed_msg	

no_lat_long_request()

def unknown_format_extra():
        print "Unknown format test (extra extra param)"
        url = "{0}32.0,-185.5,65.2".format(getweather_url)
        print "Making Request to {0}".format(url)
        try:
                weather_service_call = urlopen(url)
                status_code = weather_service_call.getcode()
        except HTTPError, error:
                status_code = error.code

        if status_code == 400:
                print passed_msg
        else:
                print failed_msg

unknown_format_extra()

def unknown_format():
        print "Unknown format test ('/' instead of ',')"
        url = "{0}32.0/-185.5".format(getweather_url)
        print "Making Request to {0}".format(url)
        try:
                weather_service_call = urlopen(url)
                status_code = weather_service_call.getcode()
        except HTTPError, error:
                status_code = error.code

        if status_code == 404:
                print passed_msg
        else:
                print failed_msg

unknown_format()
