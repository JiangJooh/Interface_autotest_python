# -*- coding:utf-8 -*-
# @Time: 2022/11/6 13:47
# @Author: jooh
# @File: demo04正则表达式匹配边界.py

"""
正则边界
    字符串边界
        ^  表示字符串开头(起始位置)
        $  表示字符串结尾(终止位置)

    单词边界
        \b  表示单词边界
        \B  表示非单词边界
"""
import re

s="123456python65java4123java"

res=re.findall('^123',s)
print(res)

res=re.findall('java$',s)
print(res)


s="python is best language?javapython python"
# \b  表示单词边界
res = re.findall(r'\bpython',s)
print(res)

res = re.findall(r'python\b',s)
print(res)

# \B  表示非单词边界
res = re.findall(r'java\B',s)
print(res)