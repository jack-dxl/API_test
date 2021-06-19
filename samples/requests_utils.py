#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: requests_utils.py
@time: 2021/6/18 22:07
@desc: 
"""
import json

import requests,ast
from common.localconfig_utils import local_conifg

class RequesteUtils():
    def __init__(self):
        self.hosts = local_conifg.URL
        self.headers = {'content_type':'application/json;charset=utf-8'}
        self.session = requests.session()

    def get(self,get_infos):
        url = self.hosts + get_infos["请求地址"]
        response = self.session.get(url=url,
                                    params = ast.literal_eval(get_infos["请求参数(get)"])
                                    )
        response.encoding = response.apparent_encoding
        print(response.text)
        result = {
            'code':0, #请求是否成功标志
            'response_reason':response.reason,
            'response_code':response.status_code,
            'response_headers': response.headers,
            'response_body': response.text
        }
        return result

    def post(self,get_infos):
        url = self.hosts + get_infos["请求地址"]
        response = self.session.post(url=url,
                                    headers = self.headers,
                                    params = {"access_token":"46_t5xqV26TXQCwiGzITLkM8oorwbPPY-IpfYdWtF_IaOiYODgvWMzEWnjx2OJQ9FYJMqH3KGrboRAkcQQYXHILTXllqJXuYQ-DOKPQQJ9LNOTDGj8u_MhxuP4RDucRlUIOxeaYNwuUlVWZiim5KJTeAGAQPZ"},
                                    #params = ast.literal_eval(get_infos["请求参数(get)"]),
                                    #data = get_infos["提交数据（post）"]
                                    json = ast.literal_eval(get_infos["提交数据（post）"])
                                    )

        print(type(get_infos["提交数据（post）"]))
        print(type(json.dumps(ast.literal_eval(get_infos["提交数据（post）"]))))
        response.encoding = response.apparent_encoding
        print(response.text)
        result = {
            'code':0, #请求是否成功标志
            'response_reason':response.reason,
            'response_code':response.status_code,
            'response_headers': response.headers,
            'response_body': response.text
        }
        return result


if __name__ == '__main__':
    dict = {'测试用例编号': 'case01', '测试用例名称': '测试能否正确执行获取access_token接口', '用例执行': '是', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '提交数据（post）': '', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键是否存在', '期望结果': 'access_token,expires_in', '测试结果': ''}

    #RequesteUtils().get(dict)
    #字符串转字典 eval()
    post_info = {'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_02', '接口名称': '删除标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":${token}}', '提交数据（post）': '{"tag":{"id":4}}', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键值对', '期望结果': '{"errcode":0,"errmsg":"ok"}', '测试结果': ''}
    RequesteUtils().post(post_info)
