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

str1 = "comm on! newdream on"
str2 = "china1usa2german3english"


pattrn0 = re.compile(r"(\w+),(\w+) (\w+)(?P<sign>.*)")
pattrn1 = re.compile(r"on")
pattrn2 = re.compile(r"\d+")
# result1 = re.match(pattrn1,str1)  #匹配以什么开头
# result1 = re.search(pattrn1,str1)  #扫描整体string查找匹配
# result1 = re.split(pattrn2,str2)
# result1 = re.findall(pattrn2,str2)  #搜索string 以列表形式返回全部能匹配的字串
result1 = re.finditer(pattrn2,str2) #返回迭代器
# for r in result1:
#     print(r)

# print(result1)
# print(result1.re)
# print(result1.pos)
# print(result1.endpos)
# print(result1.lastindex)
# print('~~~~~~~~~~~~')
# print(result1.group(0))
# print(result1.groups(0))
# print(result1.groupdict(0))
# print(result1.start(0))
# print(result1.end())
# print(result1.span())
# print(result1.expand(r"\2 \3 \1+\4"))  #拼接

str3 = 'summer hot ~~'
pattrn3 = re.compile(r"(\w+) (\w+)")
#print(re.sub(pattrn3, r"\2 \1",str3))
#print(str3)
# result=re.match(pattrn3,str3)
# print(result.group(1).title())
def func(m):
    return m.group(1).title()+ '' +m.group(2).title()


str1 = re.sub(pattrn3, func, str3)
print(str1)

str2 = re.subn(pattrn3, r"\2 \1",str3)
print(str2)

#写法2
str2 = "china1usa2german3english"
v_list = re.split(r'\d',str2)
print(v_list)
