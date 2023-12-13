from email.message import EmailMessage
import ssl
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
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver

    def set_bodyifo(self, info, count):
        self.em['subject'] = self.subject + " " + str(count)
        final_body = self.body
        for depto in info:
            final_body +="""

            """ + depto + """

            """

        self.em.set_content(final_body)

    def SendMail(self):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.email_sender, self.email_password)
            smtp.sendmail(self.email_sender, self.email_receiver, self.em.as_string())






