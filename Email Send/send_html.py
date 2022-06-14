import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Your Name'
email['to'] = 'your@email.com'
email['subject'] = "If it's free, you are the product"

#Primer argumento, todas las variables
#Segundo argumento, tipo de archivo html
email.set_content(html.substitute({'name':'Your Name',}), 'html')

with smtplib.SMTP(host="'smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your@email.com', 'your_email_password')
    smtp.send_message(email)
    print("Sent!")
