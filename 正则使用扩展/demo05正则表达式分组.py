# -*- coding:utf-8 -*-
# @Time: 2022/11/6 17:56
# @Author: jooh
# @File: demo05正则表达式分组.py

"""
表示分组

"""
import re

params='{"id":"#id#","name":"#name#","age":"#age#","title":"#title#","aaa":111,"bbb":222}'

res=re.findall("#.+?#",params)
print(res)   # ['#id#', '#name#', '#age#', '#title#']

# ------------()分组,提取括号中的内容-------------------
res=re.findall("#(.+?)#",params)
print(res)   # ['id', 'name', 'age', 'title']


s="asdafsas--BBBaa112aa-aa234aa-aa345aaBBB---dsadsadsa"
res=re.findall("BBB(.+?)BBB",s)
print(res)  # ['aa112aa-aa234aa-aa345aa']


res=re.findall("aa(.+?)aa",s)
print(res)   # ['112', '234', '345']


s2="ddassafsddfsa#username=jzh-pwd=123456#dsfjkjjkdf#username=jzh111-pwd=122223456#gjkojhkf"
res=re.findall(r"#username=(.+?)-pwd=(.+?)#",s2)
print(res)   # [('jzh', '123456'), ('jzh111', '122223456')]
res=re.findall(r"#username=.+?-pwd=(.+?)#",s2)
print(res)    # ['123456', '122223456']  只提取密码 就括密码

# -------------- |管道符:表示多个匹配规则满足其中一个就行-------
s="java12322342pythonsadfsaf21313"
res=re.findall("python|java",s)
print(res)  # ['java', 'python']


s="@@java@@12322342##python##sadfsaf21313"
res=re.findall("@@(.+?)@@|##(.+?)##",s)
print(res)   # [('java', ''), ('', 'python')]




