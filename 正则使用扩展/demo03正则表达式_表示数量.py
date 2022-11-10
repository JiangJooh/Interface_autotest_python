# -*- coding:utf-8 -*-
# @Time: 2022/11/6 13:08
# @Author: jooh
# @File: demo03正则表达式_表示数量.py
"""
正则表达式-表示次数
    贪婪模式: 默认是开启贪婪模式进行匹配的
    非贪婪模式  加一个?

    {n} 表示前面出现字符连续出现n次
    {n,} 表示前面出现字符连续出现n次 以上
    {n,m} 表示前面出现字符连续出现n次 到m次------贪婪模式
    {n,m}? 表示前面出现字符连续出现n次 到m次----非贪婪模式(?可以表示关闭贪婪)

    +: 表示一次以上    等同于{1,}
    *: 表示0次以上    等同于{0,}
    ?: 表示1次或者0次

"""

import re

s1="21444583w33745sas __  s447+-! @eew21#$$3453"
# {n} 表示前面出现字符连续出现n次
res1=re.findall('\d{5}',s1)
# res1=re.findall('\d\d\d\d\d',s1)   # 与上面的相同
print(res1)  # ['21444', '33745']


# {n,} 表示前面出现字符连续出现n次 以上
res2=re.findall('\d{3,}',s1)
print(res2)   # ['21444583', '33745', '447', '3453']

# {n,m} 表示前面出现字符连续出现n次 到m次------贪婪模式
res3=re.findall('\d{3,5}',s1)
print(res3)


# {n,m}? 表示前面出现字符连续出现n次 到m次----非贪婪模式
res4=re.findall('\d{3,5}?',s1)
print(res4)

# 非贪婪模式的应用
params='{"id":"#id#","name":"#name#","age":"#age#","title":"#title#","aaa":111,"bbb":222}'
res=re.findall("#.{1,}?#",params)
print(res)   # ['#id#', '#name#', '#age#', '#title#']


# +: 表示一次以上
params='{"id":"#id#","name":"#name#","age":"#age#","title":"#title#","aaa":111,"bbb":222}'
res5=re.findall("#.+?#",params)
print(res5)   # ['#id#', '#name#', '#age#', '#title#']



# *: 表示0次以上
s="2454ads"
res6=re.findall('\d*',s)
print(res6)  # ['2454', '', '', '', '']
res7=re.findall('\d{0,}',s)
print(res7) # ['2454', '', '', '', '']


html="<p>python</p><p>python11111</p><p>py</p><p></p>"
res8=re.findall("<p>.*?</p>",html)
print(res8)   # ['<p>python</p>', '<p>python11111</p>', '<p>py</p>', '<p></p>']
res9=re.findall("<p>.+?</p>",html)
print(res9)  # ['<p>python</p>', '<p>python11111</p>', '<p>py</p>']
