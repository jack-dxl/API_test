#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: log_demo.py
@time: 2021/6/16 20:48
@desc: 
"""

import logging

logger = logging.getLogger('logger')
handler1 = logging.StreamHandler() #控制台
logger.setLevel(10)
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
handler1.setFormatter(formatter)
logger.addHandler(handler1)

handler2 = logging.FileHandler('./test.log','a',encoding='utf-8')
handler2.setLevel(10)
handler2.setFormatter(formatter)
logger.addHandler(handler2)

logger.info('hello')
