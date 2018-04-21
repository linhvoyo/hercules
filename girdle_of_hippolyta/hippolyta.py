import smtplib
import sys
import imaplib
import email

def send_email():
    """
    Use smtplib to send email
    http://stackabuse.com/how-to-send-emails-with-gmail-using-python/
    """
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.ehlo()
    server.starttls()
    server.login(sys.argv[2], sys.argv[3])
    print sys.argv[4]
    server.sendmail(sys.argv[2], sys.argv[4], 'Subject: help?!?!?!\nhelp me plox')

def read_mail():
    """
    check inbox
    https://yuji.wordpress.com/2011/06/22/python-imaplib-imap-example-with-gmail
    http://www.vineetdhanawat.com/blog/2012/06/how-to-extract-email-gmail-contents-as-text-using-imaplib-via-imap-in-python-3/
    """
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(sys.argv[2], sys.argv[3])
    mail.select("inbox")
    result, data = mail.search(None, "ALL")
    latest = data[0].split()[-1]
    result, data = mail.fetch(latest, "(RFC822)")
    raw_email_string = data[0][1].decode('utf-8')
    msg = email.message_from_string(raw_email_string)
    for part in msg.walk():
        if part.get_content_type() == "text/plain":
            print part.get_payload(decode=True)


if len(sys.argv) < 2:
	print "\nusage: python hippolyta.py <option> <you@gmail.com> <your_pass> " \
	+ "<to@email.com>\n\noptions:\n\t--send\n\t--read\n"
elif sys.argv[1] == '--send' and len(sys.argv) > 4:
    	print "sending mail to ...\n"
    	send_email()
elif sys.argv[1] == '--read' and len(sys.argv) > 3:
    	print "reading latest email ...\n"
    	read_mail()
else:
	print "\nusage: python hippolyta.py <option> <you@gmail.com> <your_pass> " \
	+ "<to@email.com>\n\noptions:\n\t--send\n\t--read\n"
