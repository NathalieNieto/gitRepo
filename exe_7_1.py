# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 18:47:47 2015

@author: nathy_000
"""

fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    newLine = line.rstrip()
    print newLine.upper()