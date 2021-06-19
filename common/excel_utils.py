#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: excel_utils.py
@time: 2021/6/8 22:56
@desc: 
"""
import os
import xlrd


class ExccelUtils():
    def __init__(self, file_path, sheet_id=0):
        self.file_path = file_path
        self.sheet_id = sheet_id
        self.sheet = self.get_sheet()  #整个表格对象

    def get_sheet(self):
        wb = xlrd.open_workbook(self.file_path)
        sheet = wb.sheet_by_index(self.sheet_id)
        return sheet

    def get_row_count(self):
        #获取行
        row_count = self.sheet.nrows
        return row_count

    def get_col_count(self):
        #获取列
        col_count = self.sheet.ncols
        return col_count

    def get_cell_value(self,row_index,col_index):
        cell_value = self.sheet.cell_value(row_index,col_index)
        return cell_value

    def get_merged_info(self):
        merged_info = self.sheet.merged_cells
        return merged_info

    def get_merged_cell_value(self, row_index, col_index):
        '''既能获取单元格的数据又能获取合并单元格数据'''
        cell_values = None
        for (rlow, rhigh, clow, chigh) in self.get_merged_info():
            if rlow <= row_index < rhigh:
                if clow <= col_index < chigh:
                    cell_values = self.get_cell_value(rlow, clow)
                    break
                else:
                    cell_values = self.get_cell_value(row_index, col_index)
            else:
                cell_values = self.get_cell_value(row_index, col_index)
        return cell_values

    def get_sheet_data_dict(self):
        '''获取所有值'''
        alldata_list = []
        first_row = self.sheet.row(0) #获取首行数据
        for row in range(1, self.get_row_count()):
            row_dict = {}
            for col in range(0, self.get_col_count()):
                row_dict[first_row[col].value] = self.get_merged_cell_value(row, col)
            alldata_list.append(row_dict)
        return alldata_list

if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    excel_path = os.path.join(current_path,'..','samples/data/test_data.xlsx')
    excelUtils = ExccelUtils(excel_path)
    for i in range (1,9):
        print(excelUtils.get_merged_cell_value(i,0))