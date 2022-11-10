# -*- coding:utf-8 -*-
# @Time: 2022/11/6 11:01
# @Author: jooh
# @File: demo01_关于用例参数替换存在的痛点.py

class Test01:
    id=10
    name="jzh"
    age="15"
    title="ok"

params='{"id":"#id#","name":"#name#","age":"#age#","title":"#title#","aaa":111,"bbb":222}'
# 当前问题:每次要替换都只能一次一次替换,这就是痛点
params=params.replace("#id#",str(Test01.id))
params=params.replace("#name#",Test01.name)
print(params)



# 解决方案:通过正则表达式替换