# -*- coding:utf-8 -*-
# @Time: 2022/10/22 14:14
# @Author: jooh
# @File: handle_conf.py

from configparser import ConfigParser
from common.handle_path import CONF_DIR
import os

# conf = ConfigParser()
# conf.read(r"E:\hctest\ningmengban\pythonProject\day16\config.ini",encoding="utf-8")




class Config(ConfigParser):
    """
    在创建对象时候，直接加载配置文件的内容
    """
    def __init__(self,conf_file):
        super().__init__()
        self.read(conf_file,encoding="utf-8")


# 目前因为只有一个配置文件,直接写死
# conf=Config(r"E:\hctest\ningmengban\pythonProject\day17_project\conf\config.ini")

conf=Config(os.path.join(CONF_DIR,"config.ini"))

