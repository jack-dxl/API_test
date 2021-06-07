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

excle_path = os.path.join(os.path.dirname(__file__), 'data/test_data.xlsx')
print(excle_path)

wb = xlrd.open_workbook(excle_path)
sheet = wb.sheet_by_name("Sheet1")
# cell_value = sheet.cell_value(3,2)
cell_value = sheet.cell_value(0, 0)
print(cell_value)
cell_value = sheet.cell_value(1, 0)
print(cell_value)
cell_value = sheet.cell_value(2, 0)
print(cell_value)

# 合并单元格处理方式 merged_cells属性 返回列表 起始行 结束行 起始列 结束列
print(sheet.merged_cells)
merged = sheet.merged_cells
# 逻辑：凡是属性范围内的值 都要等于左上角的值
row_index = 3
col_index = 0
for (rlow, rhigh, clow, chigh) in merged:
    if (row_index >= rlow and row_index < rhigh):
        if (col_index >= clow and col_index < chigh):
            cell_value = sheet.cell_value(rlow, clow)
print(cell_value)


def get_merged_cell_value(row_index, col_index):
    for (rlow, rhigh, clow, chigh) in merged:
        if rlow <= row_index < rhigh:
            if clow <= col_index < chigh:
                return sheet.cell_value(rlow, clow)


print(get_merged_cell_value(4,0))