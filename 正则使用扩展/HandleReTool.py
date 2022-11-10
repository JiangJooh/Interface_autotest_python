# -*- coding:utf-8 -*-
# @Time: 2022/11/6 22:01
# @Author: jooh
# @File: HandleReTool.py

import re



def replace_data(data,cls):
    """
    替换数据的方法
    :param data: 要进行替换的用例数据(字符串)
    :param cls: 测试类
    :return:
    """
    while re.search("#(.+?)#", data):
        res2 = re.search("#(.+?)#", data)
        item = res2.group()
        # print("被替换的内容", item)
        attr = res2.group(1)
        # print("替换的属性名", attr)
        value = getattr(cls, attr)
        # print("获取出来的类属性值", value)
        # 进行替换
        data = data.replace(item, str(value))
    return data


if __name__=="__main__":
    class TestData:
        id = 123
        name = 'jzh'
        age = '18'
        title = '加油奥里给'


    s = '{"id":"#id#","name":"#name#","age":"#age#","title":"#title#","aaa":111,"bbb":222}'

    res=replace_data(s,TestData)
    print(res)