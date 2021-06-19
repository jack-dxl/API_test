#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: jsonpath_demo.py
@time: 2021/6/19 16:20
@desc: 
"""

import jsonpath
import os
d1 = {"access_token":"46_4AtqT4dRLty9Wx49oxxR15iXvpOEtBgZW0NooRUpShwl4lfxIziTYRsbt-_ZzvR3mKPGQCDquwZAGXKCvlkAh7PYSSQFnUIubsBAM--iAj-qxjB6wh3EQ-m4cUAKnTJ9say-KQrUAhwgGOXyVWCjAIABCI","expires_in":7200}
print(jsonpath.jsonpath(d1,'$.access_token')[0])
d2 = {
"tags":[{
    "id":1,
    "name":"每天一罐可乐星人",
    "count":0
},
{
    "id":2,
    "name":"星标组",
    "count":0
},
{
    "id":127,
    "name":"广东",
    "count":5
 }
] }
test = "__import__('os').system('pwd')"
print(eval("__import__('os').system('dxl')"))
#print(eval(os.system('whoami')))

print(d1['access_token'])
#print(d2['tags'][1]['name'])
print(jsonpath.jsonpath(d2,'$.tags[1].name')[0])