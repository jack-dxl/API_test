#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: re_demo.py
@time: 2021/6/19 20:18
@desc: 
"""

import re

#newdream

str1 = "newdream,comm on!"

pattrn = re.compile(r"(\w+),(\w+) (\w+)(?P<sign>.*)")
result1 = re.match(pattrn,str1)
print(result1)
print(result1.re)
print(result1.pos)
print(result1.endpos)
print(result1.lastindex)
print('~~~~~~~~~~~~')
print(result1.group(0))
print(result1.groups(0))
print(result1.groupdict(0))
print(result1.start(0))
print(result1.end())
print(result1.span())
print(result1.expand(r"\2 \3 \1+\4"))  #拼接