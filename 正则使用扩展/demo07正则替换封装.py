# -*- coding:utf-8 -*-
# @Time: 2022/11/6 21:10
# @Author: jooh
# @File: demo07正则替换封装.py

import re

class TestData:
    id=123
    name='jzh'
    age='18'
    title='加油奥里给'

s='{"id":"#id#","name":"#name#","age":"#age#","title":"#title#","aaa":111,"bbb":222}'
s2='{"id":"#id#","name":"#name#","aaa":111,"bbb":222}'



while re.search("#(.+?)#",s):
    res2 = re.search("#(.+?)#", s)
    item = res2.group()
    # print("被替换的内容", item)
    attr = res2.group(1)
    # print("替换的属性名", attr)
    value = getattr(TestData, attr)
    # print("获取出来的类属性值", value)
    # 进行替换
    s = s.replace(item, str(value))
print(s)


while re.search("#(.+?)#",s2):
    res2 = re.search("#(.+?)#", s2)
    item = res2.group()
    # print("被替换的内容", item)
    attr = res2.group(1)
    # print("替换的属性名", attr)
    value = getattr(TestData, attr)
    # print("获取出来的类属性值", value)
    # 进行替换
    s2 = s2.replace(item, str(value))
print(s2)