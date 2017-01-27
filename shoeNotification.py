# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 13:41:09 2016

@author: Ian Yake

This file will become a function to be imported into the main.py
"""

import smtplib, Settings

def notify(recipient):
    FROM = Settings.botuser
    TO = recipient # Your email
    MSG = """\
 Subject: Your shoes are here\n
 
 
 Your nike shoe order has been added to wishlist. Check it out: http://swoo.sh/2kyzrET
"""

    #Connect to SMTP server [Server domain name, Port]
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()

    smtpObj.starttls() #TLS encryption for connection

    smtpObj.login(FROM, Settings.botpassw) #enter the password

    smtpObj.sendmail(FROM, TO, MSG)

    smtpObj.quit()
