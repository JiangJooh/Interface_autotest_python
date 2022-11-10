# -*- coding:utf-8 -*-
# @Time: 2022/10/20 22:03
# @Author: jooh
# @File: handle_log.py
# 封装一个日志收集器

import logging
import os

from common.handle_path import LOG_DIR
from  common.handle_conf import conf

def create_log(name="mylog",level="DEBUG",filename="log.log",sh_level="DEBUG",fh_level="INFO"):

    # 第一步：创建日志收集器
    log = logging.getLogger(name)

    # 第二步：设置收集器收集日志等级
    log.setLevel(level)

    # 第三步：设置日志输出渠道
    # 3.1、输出到控制台
    sh = logging.StreamHandler()
    sh.setLevel(sh_level)
    log.addHandler(sh)
    # 3.2、输出到文件
    fh =logging.FileHandler(filename,encoding="utf-8")
    fh.setLevel(fh_level)
    log.addHandler(fh)

    # 第四步：设置日志输出格式
    formats = '%(asctime)s - [%(filename)s-->%(lineno)d] - %(levelname)s:%(message)s'
    log_format = logging.Formatter(formats)

    sh.setFormatter(log_format)
    fh.setFormatter(log_format)
    # 返回一个日志收集器
    return log


# 为了避免程序创建多个日志收集器材导致日志重复记录
# 所以我们可以只创建一个日志收集器，别的模块使用时候都导入这个日志收集器
my_log=create_log(
    name=conf.get("logging", "name"),
    level=conf.get("logging", "level"),
    # filename=conf.get("logging", "filename"),   # 之前输入文件名
    # 拼接 -整个路径
    filename=os.path.join(LOG_DIR,conf.get("logging","filename")),
    sh_level=conf.get("logging", "sh_level"),
    fh_level=conf.get("logging", "fh_level")
)



if __name__ =="__main__":
    try:
       assert 1==2
    except AssertionError as e:
        my_log.error("错误")
        my_log.error(e)
