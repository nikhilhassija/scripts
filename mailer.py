import smtplib

user     = "" # email
password = "" # password

# For gmail, need to enable "Allow less secure apps".

# Basic Stuff for email
from_name = ""
from_email = user

to_emails = [""]

subject = ""

message = ""

email_text = "From: {} <{}>\nTo: {}\nSubject: {}\n\n{}".format(
    from_name, from_email,
    ",".join(to_emails),
    subject,
    message)

# Trying to send an email
# Note: For every email to be sent, the whole process needs to be repeated
mail_host = "smtp.gmail.com"
mail_port = 465

try:
    server = smtplib.SMTP_SSL(mail_host, mail_port)

    server.ehlo() # Extended HELlo from the other side

    server.login(user, password)

    server.sendmail(from_email, to_emails, email_text)

    server.close()

    print("Email Sent")

except:
    print("Email Failed. :(")
