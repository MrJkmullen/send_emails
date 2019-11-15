import smtplib
import config

def send_email(subject,msg):
    try:
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n \n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
        server.quit()
        print('Email Sent')
    except:
        print('Something went wrong')
subject = "test subject"
msg = "Hey baby I love you Mariana"

send_email(subject,msg)