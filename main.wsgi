#!/usr/bin/env python
#!c:\usr\bin\python27\python.exe
# -*- coding: utf-8 -*-
# author: va1ret
# version: 0.1

import json

def parse_request_uri(environ):
	return environ['REQUEST_URI'].split('/')
def application(environ, start_response):
	status = '200 OK'
	output = 'freecmp '+json.dumps(parse_request_uri(environ)[1:])
	response_headers = [('Content-type', 'text/html; charset=utf-8'), ('Content-Length', str(len(output)))]
	start_response(status, response_headers)

	return [output]
