# -*- coding:utf-8 -*-
# @Time: 2022/11/6 22:15
# @Author: jooh
# @File: tools.py

import re
from common.handle_conf import conf
# def replace_data(data,cls):
#     """
#     替换数据的方法
#     :param data: 要进行替换的用例数据(字符串)
#     :param cls: 测试类
#     :return:
#     """
#     while re.search("#(.+?)#", data):
#         res2 = re.search("#(.+?)#", data)
#         item = res2.group()
#         # print("被替换的内容", item)
#         attr = res2.group(1)
#         # print("替换的属性名", attr)
#         value = getattr(cls, attr)
#         # print("获取出来的类属性值", value)
#         # 进行替换
#         data = data.replace(item, str(value))
#     return data



# -------升级版:可以同时从测试类和配置文件中查找替换的数据-----------
def replace_data(data,cls):
    """
    替换数据的方法
    什么数据保存在类属性:数据是动态生成的,保存在类属性
    之前已经写好在配置文件的,就保存在配置文件

    :param data: 要进行替换的用例数据(字符串)
    :param cls: 测试类
    :return:
    """
    while re.search("#(.+?)#", data):
        res2 = re.search("#(.+?)#", data)
        item = res2.group()
        attr = res2.group(1)
        try:
            # 类中找
            value = getattr(cls, attr)
        except AttributeError:
            # 去配置文件中查找
            value=conf.get("test_data",attr)
        # 进行替换
        data = data.replace(item, str(value))
    return data
