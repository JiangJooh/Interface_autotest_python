# -*- coding:utf-8 -*-
# @Time: 2022/11/6 11:26
# @Author: jooh
# @File: demo02正则表达式_元字符.py


import re

str1="aaasss13265156666ddddss13111saaaa"

res=re.findall('\d{11}',str1)
print(res)




"""
正则表达式 语法介绍
    方法:re.findall('匹配方式',要匹配的串)
    \d表示一个数字
    \D表示一个非数字
    \s 表示一个空格字符
    \S 表示一个非空格字符
    \w 表示一个单词字符(数字\字母\下划线)
    \W 表示一个非单词字符(非数字\字母\下划线)
    . 表示任意字符(通配符)
    []:例举匹配的单字符
"""

# --------------------单字符(元字符):表示单个字符----------
s1="21458745sas __  s447+-! @#$$%"
# \d表示一个数字
res1=re.findall('\d',s1)
print(res1)

# \D表示一个非数字
res2=re.findall('\D',s1)
print(res2)

# \s 表示一个空格字符
res3=re.findall('\s',s1)
print(res3)

# \S 表示一个非空格字符
res4=re.findall('\S',s1)
print(res4)

#  \w 表示一个单词字符(数字\字母\下划线)
res5=re.findall('\w',s1)
print(res5)

#  \W 表示一个非单词字符(非数字\字母\下划线)
res6=re.findall('\W',s1)
print(res6)

# . 表示任意字符(通配符)
res7=re.findall('../数据库操作扩展', s1)
print(res7)

# []:例举匹配的单字符
s2="00123444558477ssqsqa"
res8=re.findall('[1-4a-z]',s2)
print(res8)
