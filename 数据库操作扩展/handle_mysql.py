# -*- coding:utf-8 -*-
# @Time: 2022/11/5 16:47
# @Author: jooh
# @File: handle_mysql.py

"""

连接1个库的写法
"""

import pymysql
from common.handle_conf import conf

class HandleDB:

    def __init__(self,database):
        self.conn = pymysql.connect(
            host=conf.get("mysql","host"),
            port=eval(conf.get("mysql","port")),
            user=conf.get("mysql","user"),
            password=conf.get("mysql","password"),
            charset="utf8",
            database=database
        )



    def find_one(self,sql):
        """
        查询一条数据
        :param sql:
        :return:
        """
        with self.conn.cursor() as cur:
            cur.execute(sql)
        res =cur.fetchone()
        cur.close()
        return res

    def find_all(self,sql):
        """
        查询全部
        :param sql:
        :return:
        """
        with self.conn.cursor() as cur:
            cur.execute(sql)
        res=cur.fetchall()
        cur.close()
        return res

    def find_count(self, sql):
        """
        查询返回的总数
        :param sql:
        :return:
        """
        with self.conn.cursor() as cur:
            res=cur.execute(sql)
        cur.close()
        return res

    def __del__(self):
        print("--对象销毁时候自动执行--")
        self.conn.close()

if __name__=="__main__":
    # sql="SELECT * FROM futureloan.`member`  limit  5"
    sql="SELECT * FROM `member`  limit  5"
    db=HandleDB("futureloan")
    res=db.find_all(sql)
    print(res)
    print("======")
    res2 = db.find_one(sql)
    print(res2)
    print("======")
    res3 = db.find_count(sql)
    print(res3)
    print("======")
