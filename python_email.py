import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



sender = ""
email_password = ""
receiver = [""]
mail_subject = "Email using python"
mail_body = "text in body"



email_object = MIMEMultipart()
email_object["From"] = sender
email_object["To"] = ", ".join(receiver)
email_object["Subject"] = mail_subject
email_object.attach(MIMEText(mail_body, "plain"))

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, email_password)
    server.sendmail(sender, receiver, email_object.as_string())
    print("Mail sent")
    server.quit()
except smtplib.SMTPResponseException as e:
    print("SMTP response exception!", e)
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")