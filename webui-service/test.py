# -*- coding: ascii -*-
# --------------------------------------------------------------------------- #
# File Name   : test.py
# Designer    : Zach Chehayeb
# Description : Test webui. 
# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# Imports
# --------------------------------------------------------------------------- #

from webtest import TestApp 
import main

# --------------------------------------------------------------------------- #
# Global Vars
# --------------------------------------------------------------------------- #
webui_base_url = "http://127.0.0.1:62100"
app = TestApp(main.app)
passed_msg = "...    PASSED"
failed_msg = "...    FAILED"

print "\nStarting Tests..\n\n"
# --------------------------------------------------------------------------- #
# /general test
# --------------------------------------------------------------------------- #
def test_sucessful_load():
	response = app.get('/')
	print "Checking index '/' page.. succesful load"
	if response.status_int == 200:
		print "Page loaded with 200 status{0}".format(passed_msg)
	else:
		print "Page loaded with 200 status{0}".format(failed_msg)
	if response.mustcontain("Enter location below for previous weather:"):
		print "Page contains 'Enter location below' string{0}".format(passed_msg)
	else:
		print "Page contains 'Enter location below' string{0}".format(passed_msg)

test_sucessful_load()

def test_sucessful_submit():
        response = app.get('/')
        print "\nChecking index '/' page.. succesful submit"
	form = response.form
	form['address'] = "Colorado, CA"
	result = form.submit()
	
        if result.status_int == 200:
                print "Page loaded with 200 status{0}".format(passed_msg)
        else:
                print "Page loaded with 200 status{0}".format(failed_msg)
	
        if result.mustcontain("Weather for Colorado, CA"):
                print "Page contains 'Weather for Colorado, CA' string{0}".format(passed_msg)
        else:
                print "Page contains 'Weather for Colorado, CA' string{0}".format(passed_msg)
        
	if result.mustcontain("<table"):
                print "Weather table included in result{0}".format(passed_msg)
        else:
                print "Weather table included in result{0}".format(passed_msg) 

test_sucessful_submit()

def test_empty_submit():
        response = app.get('/')
        print "\nChecking index '/' page.. Empty form submit"
        form = response.form 
        result = form.submit()

        if result.status_int == 200:
                print "Page loaded with 200 status{0}".format(passed_msg)
        else:
                print "Page loaded with 200 status{0}".format(failed_msg)

        if result.mustcontain("Invalid Address"):
                print "Page contains error msg string ('Invalid Address...'){0}".format(passed_msg)
        else:
                print "Page contains error msg string ('Invalid Address...'){0}".format(passed_msg)
        
        if result.mustcontain("<form"):
                print "Form to resubmit is included{0}".format(passed_msg)
        else:
                print "Form to resubmit is included{0}".format(passed_msg)

test_empty_submit()
