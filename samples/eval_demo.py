#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: eval_demo.py
@time: 2021/6/18 23:16
@desc: 
"""
import ast

sum = eval("66+32")
print(sum)
print(ast.literal_eval("{'name':'tesx'}"))
print(eval("{'name':'tesx'}"))
print(eval("{'name':'tesx','age':'13'}",{"age":123}))
age = 10
print(eval("{'name':'linu','age':age}",{"age":age}))