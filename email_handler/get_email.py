#! /usr/bin/env python3
# This program retrieves email from the pi account
# Use pip install pyzmail36
# Reference: https://automatetheboringstuff.com/chapter16/
# Use configparser for creds: https://docs.python.org/2/library/configparser.html
import imapclient, pyzmail, os, creds

IMAP_EMAIL = 'imap.gmail.com'
MY_EMAIL = creds.login['email']
MY_P = creds.login['p']
EMAIL_FILTER = ['unseen']
GET_PRICE_SCRIPT = 'get_price.py'

imapObj = imapclient.IMAPClient(IMAP_EMAIL, ssl=True)
imapObj.login(MY_EMAIL, MY_P)
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(EMAIL_FILTER)

#for every email
for email in UIDs:
    rawMessages = imapObj.fetch([email], ['BODY[]', 'FLAGS'])
    message = pyzmail.PyzMessage.factory(rawMessages[email][b'BODY[]'])

    #email parts
    subject = message.get_subject()
    from_name, from_email = message.get_addresses('from')[0]
    to_info = message.get_addresses('to')
    #cc_emails = message.get_addresses('cc')
    #bcc_emails = bcc.get_addresses('bcc')

    #plain text in the email body
    body_plain_text = ''
    if (message.text_part != None):
        #wont work encoding = message.text_part.charset
        encoding = 'utf-8'
        body_plain_text = message.text_part.get_payload().decode(encoding)
        print(body_plain_text.find('href='))
        #os.system(GET_PRICE_SCRIPT + ' ' + )

    #html in the email body
    body_html = ''
    if (message.html_part != None):
        #wont work encoding = message.html_part.charset
        encoding = 'utf-8'
        body_html = message.html_part.get_payload().decode(encoding)

        #get rid of everything before the href
        href_blob = body_html.split('href="')[1]

        #get rid of everything after the href
        href = href_blob[:href_blob.find('"')]
        print(href)
imapObj.logout()
