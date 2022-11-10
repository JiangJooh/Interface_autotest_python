# -*- coding:utf-8 -*-
# @Time: 2022/11/6 18:31
# @Author: jooh
# @File: demo06正则在项目中的使用.py
import re

s='{"id":"#id#","name":"#name#","age":"#age#","title":"#title#","aaa":111,"bbb":222}'

# findall:匹配字符串中所有符合规则的数据,以列表形式返回
res=re.findall("#.+?#",s)
print(res)   #['#id#', '#name#', '#age#', '#title#'] 返回的是一个列表


# search:匹配并返回第一个符合规则的对象,返回的是对象
#       没匹配到就返回None
res2=re.search("#(.+?)#",s)
print(res2)   # 返回的是一个对象<re.Match object; span=(7, 11), match='#id#'>
# .group() 提取匹配对象中内容
print(res2.group())   #  #id#
print(res2.group(1))  #  id




class TestData:
    id=123
    name='jzh'
    age='18'
    title='加油奥里给'


# print(getattr(TestData,"id"))  # 获取类属性的值

# -------------继续执行下面这段代码就会继续替换-----------
res2=re.search("#(.+?)#",s)
item=res2.group()   #  #id#
print("被替换的内容",item)
attr=res2.group(1)  #  id
print("替换的属性名",attr)
value=getattr(TestData,attr)
print("获取出来的类属性值",value)
# 进行替换
s=s.replace(item,str(value))
print(s)

# -------------继续执行这段代码就会继续替换-----------
