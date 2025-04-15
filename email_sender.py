import smtplib
from email.message import EmailMessage
from string import Template # allows us to subsitute strings with the template using $ sign
from pathlib import Path # same as os.path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Karthik Nair'
email['to'] = 'knair1229@gmail.com'
email['subject'] = 'You won a million dollars!'

email.set_content(html.substitute(name = 'Karthik'), 'html')

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls() # encryption mechanism that lets us connect to the server securely
    # google disabled directly logging in using password, need to use google generated app pwd
    smtp.login('knair1229@gmail.com', 'ecyk hget fzmd ktnb')
    smtp.send_message(email)
    print("all good boss!")

