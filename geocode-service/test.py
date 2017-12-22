# -*- coding: ascii -*-
# --------------------------------------------------------------------------- #
# File Name   : test.py
# Designer    : Zach Chehayeb
# Description : Test getlocation microservice. 
# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# Imports
# --------------------------------------------------------------------------- #

from urllib2 import urlopen, HTTPError 
import json

# --------------------------------------------------------------------------- #
# Global Vars
# --------------------------------------------------------------------------- #
getlocation_base_url = "http://127.0.0.1:8001"
passed_msg = "Result...    PASSED\n"
failed_msg = "Result...    FAILED\n"

print "\nStarting Tests..\n\n"
# --------------------------------------------------------------------------- #
# /general test
# --------------------------------------------------------------------------- #
def unknown_url():
        print "Unknown URL test"
        url = "{0}".format(getlocation_base_url)
        print "Making Request to {0}".format(url)
        try:
                getlocation_service_call = urlopen(url)
                status_code = getlocation_service_call.getcode()
        except HTTPError, error:
                status_code = error.code

        if status_code == 404:
                print passed_msg
        else:
                print failed_msg

unknown_url()

# --------------------------------------------------------------------------- #
# /getlocation tests
# --------------------------------------------------------------------------- #
getlocation_url = "{0}/getlocation/".format(getlocation_base_url)
def getlocation_successful_request():
        print "GetLocation successful return test"
	print "Getting coor for Denver, CO"
        url = "{0}{1}".format(getlocation_url, 'Denver,CO')
        print "Making Request to {0}".format(url)
        try:
                location_service_call = urlopen(url)
                status_code = location_service_call.getcode()
        except HTTPError, error:
                status_code = error.code

        if status_code == 200:
		try:
			json.load(location_service_call)
			print "Result is JSON"
                	print passed_msg
		except:
			print failed_msg
        else:
                print failed_msg

getlocation_successful_request()
