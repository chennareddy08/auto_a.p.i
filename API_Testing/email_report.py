from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import unittest,time,os,re
import sys
from email.mime.base import MIMEBase
from email.utils import COMMASPACE,formatdate
from email import encoders
import os
import string
import random
from datetime import datetime

stamp = datetime.now().strftime("%d/%m/%Y%  %H:%m:%S %p")
dir = os.getcwd()
fromaddr = "chenna@handstandapp.com"
recipients=['sri@handstandapp.com', 'tiffany@handstandapp.com', 'jhicks@science-inc.com','rupam@handstandapp.com','kartik@science-inc.com','polina@handstandapp.com','fareeth@handstandapp.com','channareddy.biradar@science-inc.com','sebi@handstandapp.com']

#recipients=['chennareddy.biradar@gmail.com','channareddy.biradar@science-inc.com']

class Email(unittest.TestCase):

    def test_email(self):
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = msg['To'] = ", ".join(recipients)
        msg['Subject'] = "Handstand Daily API Automation Test Report for " + stamp
        body = "Hi All,<br/><br/>Please find attached API Automation Test Report:<br/><br/><b>Note</b>:To view clear report,Please download in your desktop and open <br/><br/>Thanks,<br/>Channareddy"

        msg.attach(MIMEText(body, 'html'))
        filename = "report.html"
        attachment = open(dir + "/report.html", "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, 'jyoti1989')
        text = msg.as_string()
        server.sendmail(fromaddr, recipients, text)
        server.quit()


if __name__ == "__main__":
    unittest.main()



