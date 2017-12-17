#! /usr/bin/env python3
# This program sends an email
# Reference: https://automatetheboringstuff.com/chapter16/
# Use configparser for creds: https://docs.python.org/2/library/configparser.html
import smtplib, sys, creds

SMTP_EMAIL = 'smtp.gmail.com'
MY_EMAIL = creds.login['email']
MY_P = creds.login['p']
price = '$13.37'

to_email = MY_EMAIL
from_email = MY_EMAIL
subject = 'Price check'
msg_body = 'The price for that item is '+ price + '.'
msg = 'Subject: ' + subject + '\n' + msg_body

#if a price was supplied, store it, otherwise use demo price
if len(sys.argv) > 1:
    price = sys.argv[1]

smtpObj = smtplib.SMTP(SMTP_EMAIL, 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(MY_EMAIL, MY_P)
smtpObj.sendmail(from_email, to_email, msg)
smtpObj.quit()
