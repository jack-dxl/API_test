#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: config.py.py
@time: 2021/6/16 19:22
@desc: 
"""
import os
from common.config_utils import ConfigUtils
config_path = os.path.join(os.path.dirname(__file__), '..','conf/config.ini')

configUtils = ConfigUtils(config_path)
URL = configUtils.read_value('default','URL')
PATH = configUtils.read_value('path', 'CASE_DATA_PATH')