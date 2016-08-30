#!/usr/bin/python3
#! -*- coding: utf-8 -*-

from cgi import parse_qs, escape

def application(env, start_response):
	#Debug mode
	print(env)
	print(start_response)
	


	start_response('200 OK', [('Content-Type','text/html')])

	#output = "Hello User and welcome to me Website.\nFor some testing please read that unicode letters: äöÄÖ".encode('utf-8')
	
	html = open('/var/www/index.html')
	print('#####################################################################################################################')
	return [html.read().encode('utf-8')]
	#return [b'Hello World']

