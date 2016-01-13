# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 19:02:30 2015

@author: nathy_000
"""

fname = raw_input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
        line = line[line.find(' '):]
        num = float(line)
        total = total + num
        count = count + 1
print "Average spam confidence: ", total/count