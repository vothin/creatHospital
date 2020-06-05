# -*- coding: utf-8 -*-
# @Time : 2020/6/5 12:12
# @Author : Vothin
# @File : make_qrcode.py

# ********************************************************

import qrcode
from base.global_path import image_path
from common.record_log import logs

class MakeQRCode():

    def __init__(self, data):

        qr = qrcode.QRCode(
                version=1,          #生成二维码尺寸的大小 1-40  1:21*21（21+(n-1)*4）
                error_correction=qrcode.constants.ERROR_CORRECT_L,      #L:7% M:15% Q:25% H:30%
                box_size=6,        #每个格子的像素大小
                border=1            #边框的格子宽度大小
            )

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image()
        img.save(image_path)
        logs.info('制作科室二维码')


if __name__ == '__main__':
    m = MakeQRCode('123')