#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project -> File   ：AutoTest -> IndexRegister
# @Author ：Zhang Jing
# @Date   ：2020/5/14 10:45
# @Desc   ：
from Base.BaseLog import Log
from Base.BasePage import Page
import unittest
log = Log()

class Register(Page):
    def register(self,**kwargs):
        data = kwargs.get('data')
        self.send_key("id", "mobileCodeCheck", data['phone'])
        self.send_key("name", "mobileCode", data['code'])
        self.send_key("id", "password", data['password'])
        self.send_key("id", "repeat_password", data['confirmpassword'])
        self.click("xpath", "//input[@type='submit']")


if __name__ == '__main__':
    register = Register()
    register.get("http://mastercsyhsk.runbayun.com/Park/Public/login")
    register.click("xpath", "//*[@id=\"form1\"]/div/div/div/p[2]/a")
    register.register()
    text = register.get_text('id', "mobile_error")
    print(text)

