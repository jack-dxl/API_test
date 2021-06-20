#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: requests_utils.py
@time: 2021/6/18 22:07
@desc: 
"""
import json

import requests
import ast
import jsonpath
import re
from common.localconfig_utils import local_conifg
from common.check_utils import CheckUtils

class RequesteUtils():
    def __init__(self):
        self.hosts = local_conifg.URL
        self.headers = {'content_type':'application/json;charset=utf-8'}
        self.session = requests.session()
        self.temp_variables = {}

    def __get(self,get_infos):
        url = self.hosts + get_infos["请求地址"]
        response = self.session.get(url=url,
                                    params = ast.literal_eval(get_infos["请求参数(get)"])
                                    )
        response.encoding = response.apparent_encoding
        if get_infos["取值方式"] == "json取值":
            value = jsonpath.jsonpath(response.json(),get_infos["取值代码"])[0]
            self.temp_variables[get_infos["传值变量"]] = value
        elif get_infos["取值方式"] == "正则取值":
            value = re.findall(get_infos["取值代码"],response.text)[0]
            self.temp_variables[get_infos["传值变量"]] = value
        #print(response.text)
        result = CheckUtils(response).run_check(get_infos['期望结果类型'],get_infos['期望结果'])
        return result

    def __post(self,post_infos):
        url = self.hosts + post_infos["请求地址"]
        response = self.session.post(url=url,
                                    headers = self.headers,
                                    params = ast.literal_eval(post_infos["请求参数(get)"]),
                                    #data = get_infos["提交数据(post)"]
                                    json = ast.literal_eval(post_infos["提交数据(post)"])
                                    )
        response.encoding = response.apparent_encoding
        if post_infos["取值方式"] == "json取值":
            value = jsonpath.jsonpath(response.json(), post_infos["取值代码"])[0]
            self.temp_variables[post_infos["传值变量"]] = value
        elif post_infos["取值方式"] == "正则取值":
            value = re.findall(post_infos["取值代码"],response.text)[0]
            self.temp_variables[post_infos["传值变量"]] = value
        #print(type(post_infos["提交数据(post)"]))
        #print(type(json.dumps(ast.literal_eval(post_infos["提交数据(post)"]))))
        #response.encoding = response.apparent_encoding
        #print(response.text)
        result = CheckUtils(response).run_check(post_infos['期望结果类型'],post_infos['期望结果'])
        return result

    def request(self,step_infos):
        requests_type = step_infos["请求方式"]
        param_variables_list = re.findall('\\${\w+}', step_infos["请求参数(get)"])
        if param_variables_list:
            for param_variables in param_variables_list:
                step_infos["请求参数(get)"] = step_infos["请求参数(get)"].replace \
                    (param_variables, '"%s"' % self.temp_variables.get(param_variables[2:-1]))
        if requests_type == "get":
            result = self.__get(step_infos)
        elif requests_type == "post":
            param_variables_list = re.findall('\\${\w+}', step_infos["提交数据(post)"])
            if param_variables_list:
                for param_variables in param_variables_list:
                    step_infos["提交数据(post)"] = step_infos["提交数据(post)"].replace \
                        (param_variables, '"%s"' % self.temp_variables.get(param_variables[2:-1]))
            result = self.__post(step_infos)
        else:
            result = {'code':3,'result':'请求方式不支持'}
        return result

    def request_by_step(self,step_infos):
        for step_infos in step_infos:
            result =self.request(step_infos)
            if result['code'] !=0:
                break
            #print(result['response_body'])
        return result
if __name__ == '__main__':
    #dict = {'测试用例编号': 'case01', '测试用例名称': '测试能否正确执行获取access_token接口', '用例执行': '是', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '提交数据(post)': '', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键是否存在', '期望结果': 'access_token,expires_in', '测试结果': ''}
    #print(RequesteUtils().request(dict))
    #dict2 ={'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '提交数据(post)': '', '取值方式': '正则取值', '传值变量': 'token', '取值代码': '"access_token":"(.+?)"', '期望结果类型': '正则匹配', '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}', '测试结果': ''}
    #print(RequesteUtils().request(dict2))
    #字符串转字典 eval()
    #post_info = {'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_02', '接口名称': '删除标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":${token}}', '提交数据(post)': '{"tag":{"id":4}}', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键值对', '期望结果': '{"errcode":0,"errmsg":"ok"}', '测试结果': ''}
    #RequesteUtils().request(post_info)
    #request1 = RequesteUtils()
    #case_info = [{'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '提交数据(post)': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': '正则匹配', '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}', '测试结果': ''}, {'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_02', '接口名称': '创建标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":${token}}', '提交数据(post)': '{"tag" : {"name" : "test12"}}', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键值对', '期望结果': '{"errcode":45157}', '测试结果': ''}]
    case_info = [{ '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx39a72e8c2007e722","secret":"06f831591c5e88313a688593f4071197"}', '提交数据(post)': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': '正则匹配', '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}', '测试结果': ''},
                 { '请求方式': 'post', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":${token}}', '提交数据(post)': '{"tag" : {"name" : "test13"}}', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键值对', '期望结果': '{"errcode":45157}', '测试结果': ''}]
    RequesteUtils().request_by_step(case_info)
    #for c in case_info:
    #    request1.request(c)