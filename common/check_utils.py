#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: check_utils.py
@time: 2021/6/20 19:26
@desc: 
"""
import ast
import re


class CheckUtils:
    def __init__(self,check_response=None):
        self.ck_response = check_response
        self.pass_result = {
            'code':0, #请求是否成功标志
            'response_reason':self.ck_response.reason,
            'response_code':self.ck_response.status_code,
            'response_headers': self.ck_response.headers,
            'response_body': self.ck_response.text,
            'check_result':True,
            'message':'' #扩展
        }
        self.fail_result = {
            'code':2, #请求是否成功标志
            'response_reason':self.ck_response.reason,
            'response_code':self.ck_response.status_code,
            'response_headers': self.ck_response.headers,
            'response_body': self.ck_response.text,
            'check_result':False,
            'message': ''  # 扩展
        }
        self.ck_rule = {
            '无':self.no_check,
            'json是否存在':self.check_key,
            'json键值对':self.check_keyvalue,
            '正则匹配':self.check_regexp
        }

    def no_check(self):
        return self.pass_result

    def check_key(self,check_data=None):
        check_data_list = check_data.split(',')
        res_list = [] #存放每次比较的结果
        wrong_key = [] #存放比较失败的key
        for check_data in check_data_list:
            if check_data in self.ck_response.json().keys():
                res_list.append(self.pass_result)
            else:
                res_list.append(self.fail_result)
                wrong_key.append(check_data)
        #print(res_list,wrong_key)
        if self.fail_result in res_list:
            return self.fail_result
        else:
            return self.pass_result

    def check_keyvalue(self,check_data=None):
        res_list = []  # 存放每次比较的结果
        wrong_key = []  # 存放比较失败的key
        for check_item in ast.literal_eval(check_data).items():
            if check_item in self.ck_response.json().items():
                res_list.append(self.pass_result)
            else:
                res_list.append(self.fail_result)
                wrong_key.append(check_item)
        print(res_list)
        if self.fail_result in res_list:
            return self.fail_result
        else:
            return self.pass_result

    def check_regexp(self,check_data=None):
        pattern = re.compile(check_data)
        if re.findall(pattern,self.ck_response.text):
            print(1)
            return self.pass_result
        else:
            print(2)
            return self.fail_result


    def run_check(self,check_type=None,check_data=None):
        #入口函数
        code = self.ck_response.status_code
        if code == 200:
            if check_type in self.ck_rule.keys():
                result = self.ck_rule[check_type](check_data) #self.check_keyvalue(check_key)
                return result
            else:
                self.fail_result['massage'] = "不支持%s判断方式"% check_type
                return self.fail_result
        else:
            self.fail_result['message'] = "请求的响应状态码非%s" % str(code)
            return self.fail_result


if __name__ == '__main__':
    #CheckUtils({"access_token":"hello","expires_in":"test"}).check_keyvalue('{"expires_in": "tes"}')
    print(CheckUtils('{"access_token":"hello","expires_in":7200}').check_regexp('"access_token":"(.+?)"'))
    #s = {"access_token":"hello","expires_in":"test"}
    #print(s.keys())
    # str = '{"access_token":"hello","expires_in":7200}'
    # patten = re.compile('"access_token":"(.+?)"')
    # print(re.findall(patten,str))
    # if []:
    #     print('hello')
