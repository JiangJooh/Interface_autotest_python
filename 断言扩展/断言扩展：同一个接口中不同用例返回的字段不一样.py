# -*- coding:utf-8 -*-
# @Time: 2022/10/30 22:54
# @Author: jooh
# @File: 断言扩展：同一个接口中不同用例返回的字段不一样.py

# res={"code":0,"msg":"OK","time":"2022-10-19"}
# expected={"code":0,"msg":"OK"}
#
# for k,v in expected.items():
#     if res.get(k) == v:
#         print(k,v,"res中找到这个键值对")
#         pass
#     else:
#         raise AssertionError("{}[k,v] not in {}".format(expected,res))



# 封装一下方法
import unittest


class TestDemo(unittest.TestCase):

    def assertDictIn(self,expected,res):
        for k,v in expected.items():
            if res.get(k) == v:
                print(k,v,"res中找到这个键值对")
                pass
            else:
                raise AssertionError("{} not in {}".format(expected,res))

    def test_demo(self):
        res={"code":0,"msg":"OK","time":"2022-10-19"}
        expected={"code":0,"msg":"OK"}

        res2 = {"code": 110, "msg": "OK", "time": "2022-10-19"}
        expected2 = {"code": 0, "msg": "OK"}

        try:
            self.assertDictIn(expected,res)
            self.assertDictIn(expected2,res2)

        except AssertionError as e:
            raise e


