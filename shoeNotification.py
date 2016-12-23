# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 13:41:09 2016

@author: Ian

This file will become a function to be imported into the main.py
"""

import smtplib

FROM = 'shoebot3000@gmail.com'
TO = 'iangyake@gmail.com' # Your email
MSG = """\
Subject: Your shoes are here!

Your nike shoe order has been added to cart. Check it out: https://goo.gl/8gtuWN
"""

#Connect to SMTP server [Server domain name, Port]
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()

smtpObj.starttls() #TLS encryption for connection

smtpObj.login(FROM, '2kZf7njz')



smtpObj.sendmail(FROM, TO, MSG)

smtpObj.quit()