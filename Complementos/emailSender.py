#https://medium.com/analytics-vidhya/how-to-send-many-custom-emails-with-pdf-attachments-using-python-ba86bfd757f3



import pandas as pd
import smtplib
from email.message import EmailMessage
# Importing all the necessary requirements
from smtplib import SMTP





sender = 'peajevillada@gmail.com'
password = 'dibu1234'
reciever_mail = 'frangiayetto@gmail.com'






















count = 1

receiver = reciever_mail
msg = EmailMessage()
msg['Subject'] = 'TESTING SUBJECT LOLOL'
msg['From'] = sender
msg['To'] = receiver
msg.set_content('TESTING 123 TESTING TESTING LA MAMA DE MONO EN 4 TESTING')
file = 'Complementos/test.pdf'
with open(file,'rb') as f:
    file_data = f.read()
    file_name = f.name
    msg.add_attachment(file_data, maintype='application', subtype = 'octet-stream', filename=file_name)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender, password)
    smtp.send_message(msg)
    print(count)
    count = count+1