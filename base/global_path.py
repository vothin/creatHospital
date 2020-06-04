# -*- coding: utf-8 -*-
# @Time : 2020/6/4 14:57
# @Author : Vothin
# @File : global_path.py

# ********************************************************8



import os, sys

BIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BIR)

excel_path = os.path.join(BIR, r'data\食物表.xlsx')
mysql_path = os.path.join(BIR, r'config\mysql_url.yaml')
log_path = os.path.join(BIR, r'log\log.log')