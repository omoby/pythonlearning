from smtplib import SMTP_SSL
from email.mime.text import MIMEText

with SMTP_SSL(host="smtp.inspur.com") as smtp:
    smtp.login(user='zhangqx02@inspur.com', password='inspur2wx?')

    msg = MIMEText("这是来自Python3的一封测试邮件", _charset="utf8")
    msg["Subject"] = "测试邮件"
    msg["from"] = 'zhangqx02@inspur.com'
    msg["to"] = 'zhangqx02@inspur.com'

    smtp.sendmail(from_addr="zhangqx02@inspur.com", to_addrs="zhangqx02@inspur.com", msg=msg.as_string())