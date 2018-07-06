# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 18:17:44 2018

@author: Qyark
"""
#  'junktext!_@!@-23ajunktext!_@!@-23ajunktext!_@!@-23ajunktext!_@!@-23ajunktext!_@!@-23aTEL:1239876541/TEL:3216549874/TEL:4568741235junktext!_@!@-23ajunktext!_@!@-23a'
#import re
import csv
import re
'''text = 'junktext!_@!@-23ajunktext!_@!@-23ajunktext!_@!@-23ajunktext!_@!@-23ajunktext!_@!@-23aTEL:1239876541/TEL:3216549874/TEL:4568741235/TelNums:3/junktext!_@!@-23ajunktext!_@!@-23a'
tels = (re.findall(r'[0-9]{10}', text))
print(tels)'''

from collections import defaultdict

columns = defaultdict(list) # each value in each column is appended to a list
     
     
with open('test.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for (k,v) in row.items():
            columns[k].append(v)
            
print(columns['street'])

text = str(columns['street'])
tels = list(re.findall(r'[0-9]{10}', text))
print(tels)