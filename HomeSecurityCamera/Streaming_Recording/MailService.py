import json
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class eMailService(object):
    def __init__(self):
        self.smtpConnect()
    
    def SendMail(self, img1, subject):
        while(True):
            try:
                emailMessage = MIMEMultipart('alternative')
                emailMessage['From'] = self.fromAddress
                emailMessage['To'] = self.toAddress
                emailMessage['Subject'] = subject

                mailBody = MIMEText('<strong>Movimento Rilevato!<strong><br>' + '<img src="cid:image1">', 'html')
                emailMessage.attach(mailBody)

                image = open(img1, 'rb')
                mailImage = MIMEImage(image.read())
                image.close()
                mailImage.add_header('Content-ID', '<image1>')

                emailMessage.attach(mailImage)

                self.smtpServer.send_message(emailMessage)
                
                return
            except:
                self.smtpConnect()

    def smtpConnect(self):
        with open('mail_service.json', 'r') as email_data:
            self.emailData = json.loads(email_data.read())
        
        self.smtpServer = smtplib.SMTP(host=str(self.emailData['host']) , port=str(self.emailData['port']))
        self.smtpServer.starttls()
        self.smtpServer.login(str(self.emailData['username']), str(self.emailData['password']))

        self.fromAddress = str(self.emailData['fromAdress'])
        self.toAddress = str(self.emailData['toAddress'])