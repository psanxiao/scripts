#!/usr/bin/python

# @author Pablo Sanxiao <psanxiao@icarto.es>
# @license GPL v3

import os, sys
import pycurl

if len(sys.argv) < 4:
    print("Usage: %s <user> <api key> <file to upload>" % sys.argv[0])
    raise SystemExit

user = sys.argv[1]
apiKey = sys.argv[2]
filename = sys.argv[3]
url = "https://%s.cartodb.com/api/v1/imports/?api_key=%s" % (user, apiKey) 

if not os.path.exists(filename):
    print("Error: the file '%s' does not exist" % filename)
    raise SystemExit

# Initialize pycurl
c = pycurl.Curl()
c.setopt(pycurl.URL, url)
c.setopt(c.HTTPPOST, [("file", (c.FORM_FILE, filename))])

# Start transfer
print("Uploading file %s" % filename)
c.perform()
c.close()
print