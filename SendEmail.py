# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import os
import re
 
# 获取ifconfig命令内容
cmd='ifconfig'
# cmd = 'ip addr' # debian 高版本用 "ip addr"

m = os.popen(cmd)
specific_info = m.read()
m.close()

# 匹配正则表达式，找到 ipv6 地址
pattern = r"inet6.*\n"

matches = re.findall(pattern, specific_info)

find_info = ""
if matches:
    find_info = "========================\n"
    for match in matches:
        find_info = find_info + match + "\n"
    find_info += "========================\n"
    # print(find_info)
else:
    find_info = "未找到\n"

 
# 设置发件人和收件人信息
my_sender='xxxxx@xx.com'  # 自己的邮箱账号
my_pass = 'xxxxxxxx'   # 发件人邮箱密码(邮箱获取的授权码)
my_user='xxxxx@xx.com'    # 自己的邮箱账号
 
def mail():
    ret=True
    try:
        msg=MIMEText(find_info + specific_info,'plain','utf-8')
        msg['From']=formataddr(["IP获取",my_sender])          # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["me",my_user])                 # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="IP地址获取"                           # 邮件的主题，也可以说是标题
        server=smtplib.SMTP("smtp.qq.com", 587)             # 发件人邮箱中的SMTP服务器，端口是587
        server.login(my_sender, my_pass)                   # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret
ret=mail()
if ret:
    print("发送邮件成功")
else:
    print("发送邮件失败")