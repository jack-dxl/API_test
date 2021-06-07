#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: read_excel.py
@time: 2021/4/21 20:27
@desc: 
"""
import xlrd
import os
excle_path = os.path.join(os.path.dirname(__file__), 'data/teest_data.xlsx')
print(excle_path)

wb = xlrd.open_workbook(excle_path)
sheet = wb.sheet_by_name("Sheet1")