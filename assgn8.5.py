# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:55:41 2020

@author: Nikhil Yadav
"""

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname,'r')
count = 0
for x in fh:
    if x.startswith('From:'):
		l = x.split(' ')
		count += 1
		print(l[1].strip())
print("There were", count, "lines in the file with From as the first word")