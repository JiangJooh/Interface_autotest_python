# -*- coding:utf-8 -*-
# @Time: 2022/11/2 22:21
# @Author: jooh
# @File: demo01-pymysql模块链接数据库.py
import pymysql

# 第一步：连接数据库
conn=pymysql.connect(
    host="api.lemonban.com",
    port=3306,
    user="future",
    password="123456",
    charset="utf8",
    database="futureloan"
)

# print(conn)


# 第二步：创建游标对象
cur=conn.cursor()

# 第三步：执行sql语句
sql = "SELECT leave_amount FROM `member` WHERE mobile_phone=13211111111"
res=cur.execute(sql)
print(res)
result=cur.fetchall()
print(result)
# 第四步：提交事务,如果涉及到增删改查操作的sql执行完之后，一定要提交事务才能生效
conn.commit()

# 第五步：关闭游标对象
cur.close()

# 第六步：断开连接
conn.close()