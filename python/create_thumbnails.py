#!/usr/bin/python

# @author Pablo Sanxiao <psanxiao@icarto.es>
# @license GPL v3

import os, sys
import Image

size = 350, 350

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    print "created " + outfile
    if infile != outfile:
        try:
            img = Image.open(infile)
            img.thumbnail(size)
            img.save(outfile, "JPEG")
        except IOError:
            print "cannot create thumbnail for", infile