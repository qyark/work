# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 19:55:33 2018

@author: Qyark
"""

import csv
import re

results = []
with open("test.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)
print(results[1])
tik = str(results[1])
tels = (re.findall(r'[0-9]{10}', tik))



