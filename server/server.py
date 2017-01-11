#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import os
import time

PORT_NUMBER = int(os.environ['PORT'])
COLOR = os.environ['COLOR']
VERSION = "0"

#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):

	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		self.wfile.write("Hello World from "+COLOR+", version "+VERSION+"!")
		return

#Create a web server and define the handler to manage the
#incoming request
server = HTTPServer(('0.0.0.0', PORT_NUMBER), myHandler)
print 'Started ',COLOR,'on port',PORT_NUMBER

#Sleep to simulate slow loading
time.sleep(10)

#Wait forever for incoming htto requests
server.serve_forever()
