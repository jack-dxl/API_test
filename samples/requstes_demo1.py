#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: requstes_demo1.py
@time: 2021/6/19 13:05
@desc: 
"""

import requests

response = requests.get('http://www.hnxmxit.com/')
#print(response.json())
# response.encoding = 'utf-8'
#
# print(response.text)
print(response.apparent_encoding)
response.encoding = response.apparent_encoding
print(response.text)
# print(response.content.decode('utf-8'))
# print(response.headers)
