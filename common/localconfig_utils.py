#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: localconfig_utils.py
@time: 2021/6/16 19:30
@desc: 
"""

import os
import configparser

config_path = os.path.join(os.path.dirname(__file__), '..','conf/config.ini')

class LocalconfigUtils():
    def __init__(self, config_path = config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_path)

    @property  #把方法变为属性方法
    def URL(self):
        return self.cfg.get('default','URL')

    @property
    def PATH(self):
        return self.cfg.get('path', 'CASE_DATA_PATH')

local_conifg = LocalconfigUtils()

