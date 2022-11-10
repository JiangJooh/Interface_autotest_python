# -*- coding:utf-8 -*-
# @Time: 2022/11/2 22:53
# @Author: jooh
# @File: test_withdraw.py
import unittest
import os
import jsonpath
import requests
from common.handle_conf import conf
from unittestreport import ddt,list_data
from common.handle_excel import HandleExcel
from common.handle_path import DATA_DIR
from common.handle_log import my_log
from common.tools import replace_data

@ddt
class TestWthdraw(unittest.TestCase):
    # 获取用例数据
    excel=HandleExcel(os.path.join(DATA_DIR,"QCD_apicases.xlsx"),"Withdraw")
    cases=excel.read_data()

    # 前置操作：获取登录token和member_id
    def setUpClass(cls) :
        # 第一步：请求登录接口，进行登录
        url_login=conf.get("env","base_url")+"/member/login"
        headers=eval(conf.get("env","headers"))
        params={
            "mobile_phone": conf.get("test_data", "mobile"),
            "pwd": conf.get("test_data", "pwd")
        }
        response = requests.post(url=url_login, json=params, headers=headers)
        res = response.json()

        # 第二步：获取token，并且放到请求头中，请求头定义为为类变量
        token=jsonpath.jsonpath(res,"$..token")[0]
        headers["Authorization"]=token
        cls.headers=headers

        # 第三步、提取用户id给充值接口使用
        cls.member_id=jsonpath(res,'$..id')[0]


    # 提现接口测试方法
    @list_data(cases)
    def test_withdraw(self,item):
        # 一、准备数据
        withdraw_url=conf.get("env","base_url")+item["url"]
        method=item["method"].lower()
        headers=self.headers

        # item["data"]=item["data"].replace("#member_id#",str(self.member_id))
        # params=eval(item["data"])
        item["data"]=replace_data(item["data"],TestWthdraw)
        params = eval(item["data"])

        expected=eval(item["expected"])
        row_id=item["case_id"]+1
        # 二、请求接口，返回数据
        response = requests.request(method, url=withdraw_url, json=params, headers=headers )
        res = response.json()
        # 三、断言及输出日志
        try:
            self.assertEqual(expected["code"],res["code"])
            self.assertEqual(expected["msg"],res["msg"])
        except AssertionError as e:
            self.excel.write_excel(row=row_id,column=8,value="不通过")
            my_log.error("====用例【{}】执行失败！！！".format(item["title"]))
            my_log.exception(e)
            raise e
        else:
            self.excel.write_excel(row=row_id, column=8, value="通过")
            my_log.info("----用例【{}】执行成功~~~".format(item["title"]))
