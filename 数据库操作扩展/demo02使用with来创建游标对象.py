# -*- coding:utf-8 -*-
# @Time: 2022/11/3 23:32
# @Author: jooh
# @File: demo02使用with来创建游标对象.py

import pymysql
# 第一步：连接数据库
conn=pymysql.connect(
    host="api.lemonban.com",
    port=3306,
    user="future",
    password="123456",
    charset="utf8",
    database="futureloan",
    # cursorclass=pymysql.cursors.DictCursor   #扩展： 设置游标对象返回类型为字典类型
)


# 第二步：创建一个游标对象(自动提交事务)
with conn.cursor() as cur:
    # sql="SELECT leave_amount FROM `member` WHERE mobile_phone=13211111111"
    sql="SELECT * FROM `member` WHERE mobile_phone=13211111111"
    # execute执行完后返回的是查询的条数
    res=cur.execute(sql)

# execute执行完后返回的是查询的条数
# print(res)


# 第三步：获取查询结果，返回的是元组数据  ((字段1，字段2，...),(字段1，字段2，...),(字段1，字段2，...))
# fetchall 获取查询集中所有的内容
# fetchone 获取查询集中第一条的内容
res=cur.fetchone()
print(res)
# # 返回的数据是迭代器，不能重复获取
res=cur.fetchall()
print(res)


cur.close()
conn.close()



"""
with...   启动对象 上下文管理器 的关键字

上下文管理器协议:如果一个类中定义了如下两个方法，那么该类就实现了上下文管理器协议（可以通过with去进行操作）
    __enter__:    with XXX as 后面的变量接收的是该方法的返回值
    __exit__   with中的代码执行完毕后会执行该方法

conn.__enter__()
conn.__exit__()
"""

