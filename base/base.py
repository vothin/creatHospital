# -*- coding: utf-8 -*-
# @Time : 2020/6/4 15:48
# @Author : Vothin
# @File : base.py

# ********************************************************

from common.read_config import ReadConfig


class Base():

    # 初始化读取配置文件url.ini
    def __init__(self):
        self.c = ReadConfig()
        self.suffix = ''  # section参数
        self.url = ''  # url地址
        self.token = ''  # token参数
        self.uid = ''  # uid参数
        self.headers = None  # headers参数
