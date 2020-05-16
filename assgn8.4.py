# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:55:13 2020

@author: Nikhil Yadav
"""

fname = input("Enter file name: ")
fh = open(fname,'r')
l = []
for line in fh:
	l.append(line.rstrip().split(' '))
fl = [item for sublist in l for item in sublist]
fl = list(set(fl))
fl.sort()
print(fl)