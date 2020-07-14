#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project -> File   ：AutoTest -> PublicFunc
# @Author ：Zhang Jing
# @Date   ：2020/5/14 20:28
# @Desc   ：
import os
# 处理邮件内容的库
import smtplib
from email.mime.text import MIMEText
# 发送邮件附件 需要导入别的库  MIMEMultipart,Header,MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.base import MIMEBase

from Base.BaseSettings import TEST_REPORT_HTML


def send_email(email_Subject,file_path,  filename, received_Email=["接收邮箱"], mailserver="smtp.qq.com",
               userName_SendEmail='邮箱', userName_AuthCode='邮箱码'):
    mailserver = mailserver
    userName_SendEmail = userName_SendEmail
    userName_AuthCode = userName_AuthCode
    received_Email = received_Email

    print(file_path)
    # 创建邮件对象
    msg = MIMEMultipart()

    msg["Subject"] = Header(email_Subject, 'utf-8')
    msg["From"] = userName_SendEmail
    msg["To"] = ",".join(received_Email)

    content = open(file_path, 'rb').read()
    # # 发送普通文本
    html_content = MIMEText(content, 'html', 'utf-8')
    msg.attach(html_content)

    # 邮件中发送附件
    att = MIMEText(content, "base64", "utf-8")

    att["Content-Type"] = "application/octet-stream"  # 一种传输形式
    att["Content-Disposition"] = "attachment;filename=%s" % filename
    msg.attach(att)

    smtp = smtplib.SMTP_SSL(mailserver)  # 创建客户端
    smtp.login(userName_SendEmail, userName_AuthCode)
    smtp.sendmail(userName_SendEmail, ",".join(received_Email), msg.as_string())
    smtp.quit()


def new_report(testreport):
    lists = os.listdir(testreport)
    # print(lists)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    return file_new,lists[-1]


if __name__ == '__main__':
    #file_new = new_report("..\\report\\html")

    file_path = TEST_REPORT_HTML + "05-15 11_10_48index.html"
    email_Subject = "邮件主题"
    filename = "testreport.html"  # 附件名
    received_Email = ["邮箱12","邮箱1"]
    send_email(email_Subject,file_path,  filename, received_Email)