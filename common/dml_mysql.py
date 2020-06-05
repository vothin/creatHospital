# -*- coding: utf-8 -*-
# @Time : 2020/6/5 16:56
# @Author : Vothin
# @File : dml_mysql.py

# ********************************************************

from common.record_log import logs
from base.base import Base

class DML_Mysql(Base):

    # 查询数据
    def selectData(self, parent_id):
        # 执行查询语句
        sql = 'select shop_name, shop_id from es_shop where parent_id = "%s"'
        self.cursor.execute(sql % parent_id)

        # 将结果字典化
        url = r'http://m.wdklian.com/care/apk/care.user?type=BIND_PART&no=%s'

        office_dict = {}
        for i in self.cursor.fetchall():
            office_dict[i[0]] = i[1]

        # 关闭游标
        self.connect.commit()

        return office_dict


if __name__ == '__main__':
    d = DML_Mysql('mysql_39')
    d.selectData('200')