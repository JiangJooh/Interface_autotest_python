# -*- coding:utf-8 -*-
# @Time: 2022/10/22 15:00
# @Author: jooh
# @File: run.py

# 运行程序入口


import unittest
from unittestreport import TestRunner
from  common.handle_path import CASES_DIR,REPORT_DIR
from unittestreport.core.sendEmail import SendEmail

def main():
    """
    程序执行入口
    :return:
    """

    test_data_dir=CASES_DIR
    suite=unittest.defaultTestLoader.discover(start_dir=test_data_dir)
    runner=TestRunner(suite,
                      filename="report.html",
                      report_dir=REPORT_DIR,
                      tester="jzh",
                      title="python接口自动化测试报告"
                      )
    runner.run()

    # ----------------使用unittestreport模块将测试结果发送邮箱----------------
    # runner.send_email(host="smtp.163.com",
    #                   port=465,
    #                   user="m13265156303@163.com",
    #                   password="AOAXGDTCZYWKJOQD",
    #                   to_addrs=['297181441@qq.com',"m13265156303@163.com","20153704073@m.scnu.edu.cn"],
    #                   is_file=True)


    # ----------------使用unittestreport模块将测试结果发送到钉钉群----------------
    Webhook="https://oapi.dingtalk.com/robot/send?access_token=4e0049e99502f3901f9f45d46fc6ba86ad3bc41b44e13da45716eeb7ebf63430"
    runner.dingtalk_notice(url=Webhook,key="测试")


# --------------扩展：自定义邮件内容--------
# em=SendEmail(host="smtp.163.com",
#              port=465,
#              user="m13265156303@163.com",
#              password="AOAXGDTCZYWKJOQD")
# em.send_email(subject="测试报告", content=None, filename=None, to_addrs=None)








if __name__=="__main__":
    main()


"""
扩展知识讲解
    一、测试结果推送
        1、通过邮件发送到相关人员邮箱
        2、推送结果到钉钉群
        
"""