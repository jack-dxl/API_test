#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: requests_demo.py
@time: 2021/6/16 21:53
@desc: 
"""
import requests

hosts = 'https://api.weixin.qq.com'
#获取token
params = {
    'grant_type':'client_credential',
    'appid':'wx39a72e8c2007e722',
    'secret' : '06f831591c5e88313a688593f4071197'
}
res01 = requests.get(url = hosts + '/cgi-bin/token',
                     params = params
                     )
token_id = res01.json()['access_token']
print(res01.json())
#创建标签

get_params = {
    'access_token':token_id
}
post_params ='{"tag" : {     "name" : "test"   }}'
headers = {
    'content_type':'application/json'
}
res02 = requests.post(url = hosts + '/cgi-bin/tags/create',
                     params = get_params,
                     data = post_params,
                     headers = headers
                     )

print(res02.json())
#获取信息
params = {
    'access_token':token_id,
    'openid':'ozYLF6FMBEsD_pa-l5C21J7mcOoQ',
    'lang': 'zh_CN'
}
res03 = requests.get(url = hosts + '/cgi-bin/user/info',
                     params = params
                     )


print(res03.json())
