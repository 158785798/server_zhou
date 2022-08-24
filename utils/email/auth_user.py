import smtplib
from email.header import Header
from email.mime.text import MIMEText

import settings


def sendmail(receiver, mail_msg):
    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['From'] = Header(f'CandyCats<{settings.EMAIL_HOST_USER}>')
    message['To'] = Header(receiver, 'utf-8')
    subject = 'Welcome to CandyCats'
    message['Subject'] = Header(subject, 'utf-8')

    smtpObj = smtplib.SMTP_SSL(host=settings.EMAIL_HOST, port=settings.EMAIL_PORT)
    # smtpObj.connect(host=settings.EMAIL_HOST, port=settings.EMAIL_PORT)
    smtpObj.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    res = smtpObj.sendmail(settings.EMAIL_HOST_USER, [receiver], message.as_string())
    smtpObj.close()
    return res


def sent_user_register():
    receiver = '1587857985@qq.com'
    sendmail(receiver, '1587857985@qq.com')


if __name__ == '__main__':
    sent_user_register()
