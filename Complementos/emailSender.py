#https://medium.com/analytics-vidhya/how-to-send-many-custom-emails-with-pdf-attachments-using-python-ba86bfd757f3



import pandas as pd
import smtplib
from email.message import EmailMessage
import test

uploaded = test.upload()


sender = 'SENDEREMAIL'
password = 'yourpassword'

count = 1

receiver = emails[i][0]
msg = EmailMessage()
msg['Subject'] = 'Course Book - GMF Unicamp'
msg['From'] = sender
msg['To'] = receiver
msg.set_content('Good Night, \n Here it is your course book from our investment course. \n Att, \n Team GMF')
file = pdf_file[i][0]
with open(file,'rb') as f:
    file_data = f.read()
    file_name = f.name
    msg.add_attachment(file_data, maintype='application', subtype = 'octet-stream', filename=file_name)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender, password)
    smtp.send_message(msg)
    print(count)
    count = count+1