# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 18:02:56 2019

@author: 201610034
"""

f = open('./sample.txt', 'r') 
lines = f.readlines()
f.close()

total = 0;
for line in lines:
    score = int(line)
    total += score
    
average = total / len(lines)

f = open('./result.txt', 'w') 
f.write("총합 : {0}, 평균 : {1}".format(total, average))
f.close()