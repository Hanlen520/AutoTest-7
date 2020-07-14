#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project -> File   ：AutoTest -> BasePage
# @Author ：ZhangJing
# @Date   ：2020/5/13 16:03
# @Desc   ：基础类，用于页面对象类的继承
import os
import time
from functools import wraps
from Base.BaseLog import Log
from Base.BaseSettings import DEBUG_MODEL, local_chromdriver, LOG_DIR
# 导入显性等待的API需要的模块
from selenium import webdriver
from selenium.webdriver import ActionChains
# 1> 等待对象模块
from selenium.webdriver.support.wait import WebDriverWait
# 2> 导入等待条件模块
from selenium.webdriver.support import expected_conditions as EC
# 3> 导入查询元素模块
from selenium.webdriver.common.by import By

log = Log()


def decorate_func(func):
    @wraps(func)
    def element_location_element(self, *args, **kwargs):
        self.element_wait(*args, **kwargs)
        e1 = self.location_element(*args, **kwargs)
        func(self, e1)

    return element_location_element


class Page(object):
    """
    基础类，用于页面对象类的继承
    """

    def __init__(self, ):
        """

        :type driver: object
        """
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-gpu')  # 禁用gpu，解决一些莫名的问题
        options.add_argument('--no-sandbox')  # 取消沙盒模式
        options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
        options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 以键值对的形式加入参数
        options.add_argument(
            'user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"')
        # 无界面 模式选项
        if not DEBUG_MODEL:
            options.add_argument('--headless')  # 开启无界面模式

        browser = webdriver.Chrome(local_chromdriver, chrome_options=options)
        self.driver = browser
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, 20, 0.2)

        browser.maximize_window()
    def get(self, url):
        self.driver.get(url)

    def return_driver(self, ):
        return self.driver

    def location_element(self, fangfa, dingwei):  # 定位
        try:
            self.element_wait(fangfa, dingwei)
            if fangfa == 'id':
                element = self.driver.find_element_by_id(dingwei)
            elif fangfa == "name":
                element = self.driver.find_element_by_name(dingwei)
            elif fangfa == "class":
                element = self.driver.find_element_by_class_name(dingwei)
            elif fangfa == "link_text":
                element = self.driver.find_element_by_link_text(dingwei)
            elif fangfa == "xpath":
                element = self.driver.find_element_by_xpath(dingwei)
            elif fangfa == "tag":
                element = self.driver.find_element_by_tag_name(dingwei)
            elif fangfa == "css":
                element = self.driver.find_element_by_css_selector(dingwei)
            else:
                log.error("Please enter the  elements,'id','name','class','link_text','xpath','css','tag'.")
            return element
        except Exception as e:
            log.error(e)

    def location_elements(self, fangfa, dingwei):  # 组定位
        try:
            self.element_wait(fangfa, dingwei)
            if fangfa == 'id':
                element = self.driver.find_elements_by_id(dingwei)
            elif fangfa == "name":
                element = self.driver.find_elements_by_name(dingwei)
            elif fangfa == "class":
                element = self.driver.find_elements_by_class_name(dingwei)
            elif fangfa == "link_text":
                element = self.driver.find_elements_by_link_text(dingwei)
            elif fangfa == "xpath":
                element = self.driver.find_elements_by_xpath(dingwei)
            elif fangfa == "tag":
                element = self.driver.find_elements_by_tag_name(dingwei)
            elif fangfa == "css":
                element = self.driver.find_elements_by_css_selector(dingwei)
            else:
                log.error("Please enter the  elements,'id','name','class','link_text','xpath','css','tag'.")
            return element
        except Exception as e:
            log.error(e)

    def element_wait(self, fangfa, dingwei):  # 等待
        try:
            if fangfa == "id":
                self.wait.until(EC.presence_of_element_located((By.ID, dingwei)))
            elif fangfa == "name":
                self.wait.until(EC.presence_of_element_located((By.NAME, dingwei)))
            elif fangfa == "class":
                self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, dingwei)))
            elif fangfa == "link_text":
                self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, dingwei)))
            elif fangfa == "xpath":
                self.wait.until(EC.presence_of_element_located((By.XPATH, dingwei)))
            elif fangfa == "css":
                self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, dingwei)))
            else:
                log.error("Please enter the  elements,'id','name','class','link_text','xpath','css'.")
        except Exception as e:
            log.error("{0}页面中未能找到{1}元素, 错误日志 {2}".format(self, dingwei, e))

    def make_maxwindow(self):  # 最大化浏览器
        self.driver.maximize_window()

    def set_winsize(self, wide, hight):  # 设置窗口
        self.driver.set_window_size(wide, hight)

    def send_key(self, fangfa, dingwei, text):  # 发送内容
        self.element_wait(fangfa, dingwei)
        e1 = self.location_element(fangfa, dingwei)
        e1.clear()
        e1.send_keys(text)

    @decorate_func
    def clear(self, e1):  # 清空
        e1.clear()

    @decorate_func
    def click(self, e1):  # 单击
        e1.click()

    @decorate_func
    def right_click(self, e1):  # 右击
        ActionChains(self.driver).context_click(e1).perform()

    @decorate_func
    def move_element(self, e1):  # 移动到
        ActionChains(self.driver).move_to_element(e1).perform()

    @decorate_func
    def double_click(self, e1):  # 双击
        ActionChains(self.driver).double_click(e1).perform()

    def drag_and_drop(self, fangfa1, e1, fangfa2, e2):  # 从e1到e2
        self.element_wait(fangfa1, e1)
        eme1 = self.location_element(fangfa1, e1)
        self.element_wait(fangfa2, e2)
        eme2 = self.location_element(fangfa2, e2)
        ActionChains(self.driver).drag_and_drop(eme1, eme2).perform()

    def click_text(self, text):  # 点击文字
        self.driver.find_element_by_link_text(text).click()

    def close(self):  # 关闭
        self.driver.close()

    def quit(self):  # 退出
        self.driver.quit()

    @decorate_func
    def sublimit(self, e1):  # 提交
        e1.sublimit()

    def f5(self):  # 刷新
        self.driver.refresh()

    def js(self, sprit):  # 执行js
        self.driver.execute_script(sprit)

    def get_attribute(self, fangfa, dingwei, attribute):
        self.element_wait(fangfa, dingwei)
        e1 = self.location_element(fangfa, dingwei)
        return e1.get_attribute(attribute)

    def get_text(self, fangfa, dingwei):
        self.element_wait(fangfa, dingwei)
        e1 = self.location_element(fangfa, dingwei)
        return e1.text

    def get_is_dis(self, fangfa, dingwei):
        self.element_wait(fangfa, dingwei)
        e1 = self.location_element(fangfa, dingwei)
        return e1.is_displayed()

    def get_title(self):  # 获取title
        return self.driver.title

    def get_screen(self, filename):  # 截屏
        today = time.strftime('%Y%m%d')
        todaylogdir = os.path.join(LOG_DIR, today)
        if not os.path.exists(todaylogdir):
            os.mkdir(todaylogdir)
        filename = time.strftime('%m%d-%H_%M_%S') + filename
        file_path = os.path.join(todaylogdir, filename)
        self.driver.get_screenshot_as_file(file_path)

    def wait(self, fangfa, dingwei):  # 等待
        self.driver.implicitly_wait((fangfa, dingwei))

    def accpet(self):  # 允许
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    @decorate_func
    def switch_to_frame(self, if1):  # 切换
        self.driver.switch_to.frame(if1)

    def switch_to_windows(self, window_name):
        return self.driver.switch_to.window(window_name)

    def switch_to_alert(self):
        return self.driver.switch_to.alert()

    def get_screenshot_as_file(self):
        return self.driver.get_screenshot_as_file()

    def get_screenshot_as_png(self):
        return self.driver.get_screenshot_as_png()
