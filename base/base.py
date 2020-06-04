# -*- coding: utf-8 -*-
# @Time : 2020/6/4 15:48
# @Author : Vothin
# @File : base.py

# ********************************************************

import pymysql
from base.global_path import mysql_path
from common.read_yaml import ReadYaml



class Base():

    # 初始化读取配置文件url.ini
    def __init__(self, sec_name):
        self.mysql = ReadYaml(mysql_path)
        self.mysql_conf = self.mysql.getValue(sec_name)

        self.connect = pymysql.Connect(
            host = self.mysql_conf['url'],
            port = self.mysql_conf['port'],
            user = str(self.mysql_conf['username']),
            passwd = str(self.mysql_conf['password']),
            db = self.mysql_conf['db'],
            charset = 'utf8'
        )
