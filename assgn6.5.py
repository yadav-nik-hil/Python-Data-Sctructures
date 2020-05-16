# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:50:10 2020

@author: Nikhil Yadav
"""

text = "X-DSPAM-Confidence:    0.8475"
i = text.find(':')
val = float(text[i+1:])
print(val)