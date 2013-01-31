#!/usr/bin/env python

import CGIHTTPServer
import BaseHTTPServer
from optparse import OptionParser
import os, sys, inspect
# realpath() with make your script run, even if you symlink it :)
#cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
#if cmd_folder not in sys.path:
#    sys.path.insert(0, cmd_folder)

#  include modules from a subforder
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"subfolder")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)

import daemonize


class Handler(CGIHTTPServer.CGIHTTPRequestHandler):
    cgi_directories = ["/cgi-bin"]

PORT = 8888

def main():
    parser = OptionParser()
    opts, args = parser.parse_args()
    if args:
        httpd = BaseHTTPServer.HTTPServer((args[0], int(args[1])), Handler)
        print "Collectd-web server running at http://%s:%s/" % (args[0], args[1])
    else:
        httpd = BaseHTTPServer.HTTPServer(("127.0.0.1", PORT), Handler)
        print "Collectd-web server running at http://%s:%s/" % ("127.0.0.1", PORT)
    httpd.serve_forever()

if __name__ == "__main__":
    pid = "/var/run/collectd-web.pid"
    daemonize.start(main, pid, debug=True)
