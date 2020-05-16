# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:54:38 2020

@author: Nikhil Yadav
"""

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
avg = 0
cnt = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    i = line.find(':')
    val = float(line[i+1:])
    avg += val
    cnt+=1
