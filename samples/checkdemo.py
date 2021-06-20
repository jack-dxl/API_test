#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: checkdemo.py
@time: 2021/6/20 17:20
@desc: 
"""


import re
import ast
# 正则匹配测试
#实际结果：
str1 = '{"access_token":"35_BKh82IAvv_7Obcdwyre-v60qGrcS5rrWo-XN24oxrKZ4Xxh8OIcsa3FahcUsrB_6hY5zEXpx7adPDHNLkFGQuqJY80BHsZc8fIXXkXiMTlvA-hZe5o_KJRlyyVnAXWsywtW5k9vw_1lZ-1IiINAdACAMRE","expires_in":7200}'
#期望结果：
str2 = '{"access_token":"(.+?)","expires_in":(.+?)}'

if re.findall(str2,str1):
    print( True )
else:
    print( False )

# 是否包含 json key
jsondata1 = ast.literal_eval( str1 )
print(jsondata1.keys())
str2 = 'access_token,expires_in'
check_key_list = str2.split(',')
for check_key in check_key_list:
    result = True
    if check_key in jsondata1.keys():
        result =  True
    else:
        result =  False
    if not result:
        break
print( result )
# print( 'access_token' in jsondata1.keys() )

# 健值对正确的情况
str2 = '{"expires_in":7200,"tet":"12"}'
#print(type(str2))
#str3 = ast.literal_eval(str2).items()
#print(type(str3))
# ast.literal_eval(str2) in
for v in ast.literal_eval(str2).items():
    result = True
    if v in jsondata1.items():
        result =  True
    else:
        result =  False
    if not result:
        break
print(ast.literal_eval(str2).items())
print( result )