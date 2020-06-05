# -*- coding: utf-8 -*-
# @Time : 2020/6/5 10:31
# @Author : Vothin
# @File : write_excel.py

# ********************************************************

import xlsxwriter
from base.global_path import output_path
from base.global_path import image_path
from common.make_qrcode import MakeQRCode
from common.record_log import logs

class WriteExcel():

    def __init__(self):
        # 创建sheet页
        self.workbook = xlsxwriter.Workbook(output_path)
        self.worksheet = self.workbook.add_worksheet('科室表')



    # 写入数据
    def writeExcel(self, data=None):

        self.worksheet.write(0, 0, '科室名')
        self.worksheet.write(0, 1, '二维码')
        logs.info('创建表格')

        # 判断是否有值
        if data != None:

            # 写入科室名
            self.worksheet.write_column('A2', list(data.keys()))
            logs.info('科室名写入完成')

            for i in range(len(list(data.values()))):

                # 形成二维码
                MakeQRCode(list(data.values())[i])

                # 写入二维码
                num = 'B' + str(i + 1)
                self.worksheet.insert_image(num, image_path)

            logs.info('二维码写入完成')


    # 关闭入口
    def closeExcel(self):
        self.workbook.close()



if __name__ == '__main__':
    data = {
        '科室1' : '123',
        '科室2' : '1234'
    }

    w = WriteExcel()

    w.writeExcel(data)
    w.closeExcel()



