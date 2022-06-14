import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Your Name'
email['to'] = 'your@email.com'
email['subject'] = "If it's free, you are the product"

email.set_content("This is a Python email maker")

with smtplib.SMTP(host="'smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your@email.com', 'your_email_password')
    smtp.send_message(email)
    print("Sent!")
