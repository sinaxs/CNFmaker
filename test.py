#!/usr/bin/python
import sys


for x in xrange(1,20):
	for y in xrange(1,20):
		z = x * y
		sys.stdout.write(str(z)+" ")
		sys.stdout.flush()
print 