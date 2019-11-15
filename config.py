import os

#Insert your email credentials to below to send emails to yourself
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
PASSWORD = os.environ.get('PASSWORD')

print(EMAIL_ADDRESS)
print(PASSWORD)

