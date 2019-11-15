import os
#I used environment variables for the below but feel free to replace them with your real email and password to test

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
PASSWORD = os.environ.get('PASSWORD')

print(EMAIL_ADDRESS)
print(PASSWORD)

