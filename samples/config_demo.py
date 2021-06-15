#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: config_demo.py
@time: 2021/6/15 23:12
@desc: 
"""
import os
import configparser


config_path = os.path.join(os.path.dirname(__file__), '..','conf/config.ini')
print(config_path)
cfg = configparser.ConfigParser()
cfg.read(config_path)
print(cfg.get('default','URL'))