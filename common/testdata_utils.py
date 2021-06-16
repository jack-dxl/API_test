#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: testdata_utils.py
@time: 2021/6/15 20:25
@desc: 
"""

import os
from common.excel_utils import ExccelUtils
from common import config
from common.localconfig_utils import local_conifg

current_path = os.path.dirname(__file__)
test_data_path = os.path.join(current_path,'..',local_conifg.PATH)
print(test_data_path)

class TestdataUtils():
    def __init__(self, test_data_path = test_data_path):
        self.test_data_path = test_data_path
        self.test_data_path = ExccelUtils(test_data_path).get_sheet_data_dict()

    def __get_testcase_data(self):
        testcase_list = {}
        for row_data in self.test_data_path:
            testcase_list.setdefault(row_data['测试用例编号'],[]).append(row_data)
        return testcase_list

    def get_testcase_data_list(self):
        testcase_list = []
        for k,v in self.__get_testcase_data().items():
            one_case_dict = {}
            one_case_dict["case_name"] = k
            one_case_dict["case_info"] = v
            testcase_list.append(one_case_dict)
        return testcase_list


if __name__ == '__main__':
    testdataUtils = TestdataUtils()
    for i in testdataUtils.get_testcase_data_list():
        print(i)