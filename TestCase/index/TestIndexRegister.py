#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project -> File   ：AutoTest -> TestIndexRegister
# @Author ：Zhang Jing
# @Date   ：2020/5/14 11:32
# @Desc   ：
import time
import unittest
import HTMLTestRunner
import ddt

from Base.BaseDB import MonitorDB
from Base.BaseLog import Log
from Base.BaseSettings import TEST_DATA_YAML
from PageObject.index.IndexRegister import Register

filepath = TEST_DATA_YAML + "\\index\\register.yaml"
sqlfilepath = TEST_DATA_YAML + "\\index\\test.sql"
log = Log()


@ddt.ddt
class TestIndexRegister(unittest.TestCase):
    def setUp(self) -> None:
        self.register = Register()

    def tearDown(self) -> None:
        self.register.quit()

    @classmethod
    def setUpClass(cls) -> None:
        db = MonitorDB()
        db.sql_execute_file(sqlfilepath)
    @classmethod
    def tearDownClass(cls) -> None:
        pass

    @ddt.file_data(filepath)
    @ddt.unpack
    def test_register(self, **kwargs):
        self.filename = kwargs.get("screenshot") + ".png"
        self.register.get("http://mastercsyhsk.runbayun.com/Park/Public/login")
        self.register.click("xpath", "//*[@id=\"form1\"]/div/div/div/p[2]/a")
        self.register.register(**kwargs)
        detail = kwargs.get("detail")

        try:
            if detail != "手机号和密码正确":
                errorarray = []
                mobile_error = self.register.get_text('id', "mobile_error")
                mobile_code_dis = self.register.get_text('id', "mobile_code_dis")
                password_error = self.register.get_text('id', "password_error")
                repeat_password_error = self.register.get_text('id', "repeat_password_error")
                errorarray.append(mobile_error if mobile_error else "")
                errorarray.append(mobile_code_dis if mobile_code_dis else "")
                errorarray.append(password_error if password_error else "")
                errorarray.append(repeat_password_error if repeat_password_error else "")
                print(errorarray)
                self.assertListEqual(errorarray, kwargs.get("check"))
            else:
                self.register.element_wait("xpath", "//*[@id=\"register\"]/div[2]/div/span")
        except AssertionError as e:
            self.register.get_screen(self.filename)
            log.info("打印断言日志" + "*" * 100)
            log.error(e)
            log.info("打印断言日志" + "^" * 100)
            raise AssertionError(e)


if __name__ == '__main__':
    unittest.main()
