# -*- coding: utf-8 -*-
# @Time : 2020/6/5 16:55
# @Author : Vothin
# @File : main.py

# ********************************************************

from common.dml_mysql import DML_Mysql
from common.write_excel import WriteExcel
from common.record_log import logs

class Main(DML_Mysql):

    def main(self, parent_ip):

        # 查询数据
        logs.info('查询shop_id为%s的科室' % parent_ip)
        data = self.selectData(parent_ip)

        # 写入到Excel表格
        logs.info('写入到excel表格')
        w = WriteExcel()
        w.writeExcel(data)
        w.closeExcel()

if __name__ == '__main__':
    m = Main('mysql_39')
    m.main('200')




