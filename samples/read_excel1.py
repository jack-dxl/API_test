#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: read_excel1.py
@time: 2021/6/9 21:54
@desc:
"""

import xlrd
import os
from common.excel_utils import ExccelUtils

excel_path = os.path.join(os.path.dirname(__file__), 'data/test_data.xlsx')
excelUtils = ExccelUtils(excel_path)
sheet_list = []
for row in range(1,excelUtils.get_row_count()):
    '''获取表格数据'''
    row_dict = {}
    row_dict["事件"] = excelUtils.get_merged_cell_value(row,0)
    row_dict["步骤序号"] = excelUtils.get_merged_cell_value(row, 1)
    row_dict["步骤操作"] = excelUtils.get_merged_cell_value(row, 2)
    row_dict["完成情况"] = excelUtils.get_merged_cell_value(row, 3)
    sheet_list.append(row_dict)

#for row in sheet_list:
#    print(row)

alldata_list = []
first_row = excelUtils.sheet.row(0)
for row in range(1,excelUtils.get_row_count()):
    row_dict = {}
    for col in range(excelUtils.get_col_count()):
        row_dict[first_row[col].value] = excelUtils.get_merged_cell_value(row,col)
    alldata_list.append(row_dict)
for row in alldata_list:
    print(row)

row_dict1 = {}
row_dict1["事件1"] = excelUtils.get_merged_cell_value(0, 0)
row_dict1["步骤序号1"] = excelUtils.get_merged_cell_value(0, 1)
print(row_dict1)