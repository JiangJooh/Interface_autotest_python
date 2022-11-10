# -*- coding:utf-8 -*-
# @Time: 2022/10/30 13:12
# @Author: jooh
# @File: test_register.py
import unittest
import os
import requests
import random
from unittestreport import ddt,list_data
from common.handle_excel import HandleExcel
from common.handle_path import DATA_DIR
from common.handle_conf import conf
from common.handle_log import my_log
from common.tools import replace_data


@ddt
class TestRegister(unittest.TestCase):
    """
    注册类测试
    """

    # 读取excel用例数据
    excel=HandleExcel(os.path.join(DATA_DIR,"QCD_apicases.xlsx"),"Register")
    cases=excel.read_data()

    # 项目基本地址
    base_url = conf.get("env", "base_url")
    # 请求头
    headers= conf.get("env", "headers")

    @list_data(cases)
    def test_register(self,item):
      # 第一步：准备用例数据
        # 1、接口地址
        url = self.base_url+item["url"]

        # 2、请求参数, 【参数化手机号码，先判断是否有手机号需要替换】
        # if "#mobile_phone#" in item["data"]:
        #     phone=self.random_mobile()
        #     item["data"]=item["data"].replace("#mobile_phone#",phone)
        #     params=eval(item["data"])

        if "#mobile_phone#" in item["data"]:
            phone = self.random_mobile()
            setattr(TestRegister,'mobile',phone)   # 动态设置类属性
        item["data"] = replace_data(item["data"], TestRegister)
        params = eval(item["data"])

        # 3、请求头
        headers=eval(self.headers)
        # 4、请求方法,转化成小写
        method = item["method"].lower()
        # 5、用例期望结果
        expected=eval(item["expected"])

        # 获取执行的行号
        row_id=item["case_id"]+1
      # 第二步：请求接口，返回实际结果    requests.request()可以发动所有类型请求
        response=requests.request(method,url,json=params,headers=headers)
        res=response.json()
      # 第三步：断言
        try:
            self.assertEqual(expected["code"],res["code"])
            self.assertEqual(expected["msg"],res["msg"])
        except AssertionError as e:
            # 回写结果到excel,根据需要写,因为回写excel需要花费时间
            self.excel.write_excel(row=row_id,column=8,value="不通过")
            my_log.error("用例--[{}]--执行失败".format(item["title"]))
            my_log.exception(e)
            raise e
        else:
            self.excel.write_excel(row=row_id, column=8, value="通过")
            my_log.info("用例--[{}]--执行成功".format(item["title"]))


    # 随机生成手机号码
    def random_mobile(self):
        phone=str(random.randint(13300000000,13399999999))
        return phone

