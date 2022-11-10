# -*- coding:utf-8 -*-
# @Time: 2022/11/6 10:28
# @Author: jooh
# @File: demo03_decima类型和float数据的扩展.py

from decimal import Decimal

a=10
b=10.10



# 定义一个decimal类型的数据
res=Decimal('10.10')   # 要传字符串
print(res,type(res))
# assert  a==res



from unittest import TestCase
test=TestCase()
# test.assertEqual(b,res)
test.assertEqual(b,float(res))   # 转化为浮点数就行



# python中精度问题
print(3.3-2.1)  # 1.1999999999999997

# 注意点:创建Decimal类型数据的时候,传入的数据要是字符串类型
aaa=Decimal('3.3')-Decimal('2.1')
print(aaa)   # 1.2

bbb=Decimal(3.3)-Decimal(2.1)
print(bbb)  # 1.199999999999999733546474090

# Decimal是python中用来表示浮点数精度的一种数值类型