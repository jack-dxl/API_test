#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: config_utils.py
@time: 2021/6/15 23:25
@desc: 
"""

import os
import configparser
config_path = os.path.join(os.path.dirname(__file__), '..','conf/config.ini')

class ConfigUtils():
    def __init__(self, config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_path)

    def read_value(self,section,key):
        return self.cfg.get(section,key)

