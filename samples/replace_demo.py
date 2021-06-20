#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: replace_demo.py
@time: 2021/6/20 13:59
@desc: 
"""
import re
import ast
import requests

temp_variables = {"token":"FUKaAAAAPF"}

params  = "{'access_token':${token}}"  #考虑一个以上的情况
value = re.findall('\\${\w+}',params)[0]
print(value[2:-1])
params = params.replace(value,'"%s"'%temp_variables[value[2:-1]])
print(params)

temp_variables = {"token":"FUKaAAAAPF","number":"123","age":"29"}
str1 = '{"access_token":${token},"${age}>>>${number}"}'
for v in re.findall('\\${\w+}',str1):
    #print(v)
    #print(temp_variables.get(v[2:-1]))
    #print(v[2:-1])
    str1 = str1.replace(v,temp_variables.get(v[2:-1]))

str1 = re.sub('\\${\w+}',r'FUKaAAAAPF',str1,1)
print(str1)

dicta = {}
#第一个用例  添加标签
dicta["access_token"] = "i8B2zTdia_KWhTvgBqjNoAqiUDNbAJAHQA"

dicta = {}
#第二个用例
dicta["access_token"] = "123123"

url = "/cgi-bin/tags/delete"

#requests.get(url=url,
#             params = ast.literal_eval(params))