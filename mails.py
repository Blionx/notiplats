from email.message import EmailMessage
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from decouple import config

class MailApi:
    
    email_sender = config('MAILUSR')
    email_password = config('MAILPASSWD')
    email_receiver = config('RECEIVERLIST')
    subject ="Hay nuevos deptos publicados hoy APURATE A REVISAR"
    body = """
    estos son los nuevos deptos:

    """
    em  = MIMEMultipart("alternative")
    em['From'] = email_sender
    em['To'] = ", " + email_receiver
    em['subject'] = subject

    def set_bodyifo(self, info, count):
        final_body = self.body
        htmlbodytext=""
        for depto in info:
            final_body +="""

            """ + depto + """

            """
            htmlbodytext += "<p>" + depto + "</p> </br>"

        htmlbodytext += "<a href='localhost'> hola mundo </a>"
        part1 = MIMEText(final_body, "plain")
        part2 = MIMEText(htmlbodytext, "html")

        #self.em.set_content(final_body)
        self.em.attach(part1)
        self.em.attach(part2)

    def SendMail(self):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.email_sender, self.email_password)
            smtp.sendmail(self.email_sender, list(self.email_receiver.split(", ")), self.em.as_string())






