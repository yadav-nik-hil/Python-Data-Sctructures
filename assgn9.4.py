# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:56:05 2020

@author: Nikhil Yadav
"""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)

from_lines = []
emails = {}

for line in fh:
    line = line.rstrip()
    if line.find('From ') == 0:
        line = line.split(' ')
        email = line[1]
        if email not in emails:
            emails[email] = 1
        else:
            emails[email] += 1

email = ''
count = 0

for key in emails:
    if emails[key] > count:
        count = emails[key]
        email = key

print(email, str(count))