# -*- coding: utf-8 -*-
# @Time : 2020/6/4 15:52
# @Author : Vothin
# @File : read_yaml.py

# ********************************************************

import yaml
from common.record_log import logs

class ReadYaml():

    def __init__(self, yaml_name):
        self.conf = self.getConfig(yaml_name)

    # 读取配置文件yaml_path
    def getConfig(self, yaml_name):
        # 读取配置文件
        with open(yaml_name, 'r', encoding='utf-8') as f:
            conf_obj = f.read()

        # 转化成字典格式
        conf_dict = yaml.load(conf_obj, Loader=yaml.FullLoader)
        return conf_dict

    # 获取配置文件的值
    def getValue(self, sec_name):
        try:
            return self.conf[sec_name]
        except Exception as e:
            logs.error(e)


if __name__ == '__main__':
    from base.global_path import hospital_path

    r = ReadYaml(hospital_path)
    r_dict = r.getValue("hospital_name")
    print(r_dict)