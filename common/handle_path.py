# -*- coding:utf-8 -*-
# @Time: 2022/10/24 22:40
# @Author: jooh
# @File: handle_path.py
"""
此模块专门用来处理项目中的绝对路径

"""


import  os

# 项目根目录的路径
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 用例数据文件夹所在目录的绝对路径
DATA_DIR=os.path.join(BASE_DIR,"datas")

# 配置文件所在目录
CONF_DIR=os.path.join(BASE_DIR,"conf")

# 日志所在目录
LOG_DIR=os.path.join(BASE_DIR,"logs")

# 报告文件所在目录
REPORT_DIR=os.path.join(BASE_DIR,"reports")

# 用例模块所在目录
CASES_DIR=os.path.join(BASE_DIR,"testcases")