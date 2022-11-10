# -*- coding:utf-8 -*-
# @Time: 2022/10/31 21:38
# @Author: jooh
# @File: test_recharge.py

"""
充值的前提：登录---》获取token
unittest:
    用例级别的前置：setUp
    测试类级别的前置：setUpClass

充值的前提中，登录一次就行，所以前置用setUpClass就行
"""
import unittest
import os
import requests
from jsonpath import jsonpath
from common.handle_path import DATA_DIR
from common.handle_excel import HandleExcel
from unittestreport import ddt,list_data
from common.handle_conf import conf
from common.handle_log import my_log
from common.handle_mysql import HandleDB
from common.tools import replace_data

@ddt
class TestRecharge(unittest.TestCase):
    # 读取excel用例数据
    excel=HandleExcel(os.path.join(DATA_DIR,"QCD_apicases.xlsx"),'Recharge')
    cases=excel.read_data()
    # 项目基本地址
    base_url = conf.get("env", "base_url")
    # 数据库
    db=HandleDB("futureloan")

    # 前置操作
    @classmethod
    def setUpClass(cls):
        """
        前置操作：登录获取token
        :return:token
        """
        # 第一步：请求登录接口，进行登录
        # *************************************************************************
        url_login=conf.get("env", "base_url")+"/member/login"
        params= {
            "mobile_phone":conf.get("test_data","mobile"),
            "pwd":conf.get("test_data","pwd")
        }
        headers = eval(conf.get("env", "headers"))
        response=requests.post(url=url_login,json=params,headers=headers)
        res=response.json()
        # *************************************************************************


        # 第二步：登录成功后 提取token
        # *************************************************************************
        token=jsonpath(res,"$..token")[0]

        # token的格式是 Bearer TOKEN
        # 封装请求头，加上token
        #     方式1
        TOKEN="Bearer "+token
        headers.update({"Authorization":TOKEN})
        #     方式2
        # headers["Authorization"]="Bearer "+token

        # 保存含有token的请求头为类属性
        #     方法1
        cls.headers=headers
        #     方法2
        # setattr(TestRecharge,'headers','headers')
        # *************************************************************************


        # 第三步、提取用户id给充值接口使用------参数依赖，用于给下一个接口使用
        # *************************************************************************
        # member_id  这类属性的名字必须要和 #member_id# 中包起来的名字一样,才能进行replace_data()方法中替换
        cls.member_id=jsonpath(res,'$..id')[0]
        # *************************************************************************


    # 自定义断言函数
    def assertDictIn(self,expected,res):
        for k,v in expected.items():
            if res.get(k)==v:
                # print(k, v, "res中找到这个键值对")
                pass
            else:
                raise AssertionError("{} not in {}".format(expected, res))

    # 测试函数
    @list_data(cases)
    def test_recharge(self,item):
        # 一、准备数据
        #   1、请求地址
        url=self.base_url+item["url"]
        #   2、请求方法
        method=item["method"].lower()
        # *************************3、参数---动态处理需要进行替换的参数  ***************
        # 【面试题】如何处理接口之间依赖的参数？
        # item["data"]= item["data"].replace("#member_id#",str(self.member_id))
        # params=eval(item["data"])

        # 通过正则表达式的方式,替换会变化的值,可以一句替换全部的
        item["data"]=replace_data(item["data"],TestRecharge)
        params = eval(item["data"])
        # *************************************************************************
        #  4、期望结果
        expected=eval(item["expected"])
        row_id=item["case_id"]+1

        # -------------------------这块要进行数据库校验---------------------------------------
        # $$$$$$$$$$$$$$$$$$$$$$$$请求接口之前,查询用户余额$$$$$$$$$$$$$$$$$$$$$
        sql="SELECT leave_amount FROM `member`  WHERE mobile_phone={}".format(conf.get("test_data","mobile"))
        start_amount=self.db.find_one(sql)[0]
        print("用例执行之前,用户的余额:",start_amount)

        # 二、请求，获取返回
        response=requests.request(method=method,url=url,json=params,headers=self.headers)
        res=response.json()

        # $$$$$$$$$$$$$$$$$$$$$$$$请求接口之后,查询用户余额$$$$$$$$$$$$$$$$$$$$$
        end_amount=self.db.find_one(sql)[0]
        print("用例执行之前,用户的余额:",end_amount)

        # 三、断言
        try:
            self.assertDictIn(expected,res)

            # $$$$$$$$$$$$$$$$$$$$$$$$校验数据库中用户余额的变化是否等于充值的金额$$$$$$$$$$$$$$$$$$$$$
            if res["msg"]=="OK":
                # 充值成功,用户余额的变化为充值金额
                self.assertEqual(float(end_amount-start_amount),params["amount"])
            else:
                # 充值失败,用户余额的变化为0
                self.assertEqual(float(end_amount-start_amount),0)

        except AssertionError as e:
            self.excel.write_excel(row=row_id,column=8,value="失败")
            my_log.error("====用例【{}】执行失败！！！".format(item["title"]))
            my_log.exception(e)
            raise e
        else:
            self.excel.write_excel(row=row_id,column=8,value="通过")
            my_log.info("----用例【{}】执行成功~~~".format(item["title"]))

