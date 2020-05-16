# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:56:40 2020

@author: Nikhil Yadav
"""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
f = open(name)
d = {}
for line in f:
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
        lst = line.strip().split(' ')
        date = lst[6][:2]
        if date in d.keys():
            d[date] += 1
        else:
            d[date] = 1
l = []
for k,v in d.items():
    l.append([k,v])
l.sort(key = lambda x:x[0])
for x in l:
    print(x[0],x[1])