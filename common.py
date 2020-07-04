# coding: utf-8
'''
共通クラス
'''
import os
import datetime
from email.mime.text import MIMEText
from email.utils import formatdate
import logging.config
import smtplib


class Common:

    # logging設定
    logging.config.fileConfig(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logging.conf'))
    __logger = logging.getLogger()

    # SMTPメール設定
    __smtp_addr = "from_example_address@gmail.com"
    __smtp_addr_pass = "your_pass"

    @classmethod
    def get_now(cls):
        '''現在の日付時刻を返す

        Return:
            str：'YYYY-MM-DD HH:MI:SS.MIS'
        '''
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

    @classmethod
    def error(cls, message):
        Common.__logger.error(message)

    @classmethod
    def warning(cls, message):
        Common.__logger.warning(message)

    @classmethod
    def info(cls, message):
        Common.__logger.info(message)

    @classmethod
    def send_mail(cls, to_addr, subject, body):
        # create message
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = Common.__smtp_addr
        msg['To'] = to_addr
        msg['Date'] = formatdate()
        # send mail
        smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.ehlo()
        smtpobj.login(Common.__smtp_addr, Common.__smtp_addr_pass)
        smtpobj.sendmail(Common.__smtp_addr, to_addr, msg.as_string())
        smtpobj.close()