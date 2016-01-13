# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:20:54 2015

@author: nathy_000
"""

text = 'X-DSPAM-Confidence:    0.8475';
spcPos = text.rfind(' ');
lastPart = text[spcPos:];
num = float(lastPart);
print num;


