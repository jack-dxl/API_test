#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: log_utils.py
@time: 2021/6/16 21:03
@desc: 
"""

import os
import logging
import time
from common.localconfig_utils import local_conifg

log_output_path = os.path.join(os.path.dirname(__file__), '..',local_conifg.LOG_PATH)

class LogUtils():
    def __init__(self,log_output_path=log_output_path):
        self.log_name = os.path.join(log_output_path,'Apitest_%s.log' %time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger('Apitestlog')
        self.logger.setLevel(local_conifg.LOG_LEVEL)
        #控制台输出
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(self.log_name,'a',encoding='utf-8')
        formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

        console_handler.close()
        file_handler.close()

    def get_log(self):
        return self.logger

logger = LogUtils().get_log()

if __name__ == '__main__':
    logger.info('hello')

