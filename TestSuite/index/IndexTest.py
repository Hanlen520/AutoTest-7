#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project -> File   ：AutoTest -> IndexTest
# @Author ：Zhang Jing
# @Date   ：2020/5/14 19:33
# @Desc   ：
import time
import unittest
import os, sys

sys.path.append("D:\Pycharm\PythonProject\AutoTest\Base")
from HTMLTestRunner import HTMLTestRunner
# print(sys.path)
from Base.BaseSettings import TEST_REPORT_HTML
from Base.PublicFunc import new_report, send_email
from TestCase.index import TestIndexRegister


def testreport():
    suite = unittest.TestSuite()
    test_register = unittest.TestLoader().loadTestsFromModule(TestIndexRegister)
    suite.addTest(test_register)
    filename = TEST_REPORT_HTML + time.strftime('%m-%d %H_%M_%S') + "index.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='注册测试报告', description='测试用例执行情况', tester='ZhangJing')
    runner.run(suite)
    fp.close()

    file_path, filename = new_report(TEST_REPORT_HTML)  # 调用模块生成最新的报告
    send_email("测试报告", file_path, filename)  # 调用发送邮件模块


if __name__ == '__main__':
    testreport()
    # pass
