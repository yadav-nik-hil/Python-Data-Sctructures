# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:54:16 2020

@author: Nikhil Yadav
"""

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname,'r')
for i in fh:
    i = i.strip()
    i = i.upper()
    print(i)