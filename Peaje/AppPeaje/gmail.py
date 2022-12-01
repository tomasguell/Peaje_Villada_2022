import smtplib
import ssl
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase



def enviarMailInforme(password,sender,receiver,pdfpath):
    ctx = ssl.create_default_context()
    #password = "ywjrlngnptcvdelw"    # Your app password goes here
    #sender = "peajevillada@gmail.com"    # Your e-mail address
    #receiver = "tomasguell123@gmail.com" # Recipient's address

    # Create the message
    message = MIMEMultipart("alternative")
    message["Subject"] = "<Informe Peaje Villada>"
    message["From"] = sender
    message["To"] = receiver
    fecha = datetime.today()
    plain = f"""\
    Informe Diario de rendimientos.
    Fecha: {fecha}
    Saludos!
    """
    pdfname = pdfpath
    binary_pdf = open(pdfname, 'rb')    
    payload = MIMEBase('application', 'octate-stream', Name=pdfname)
    payload.set_payload((binary_pdf).read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
    message.attach(MIMEText(plain, "plain"))
    message.attach(payload)
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message.as_string())
    return print("Mail enviado!")

def recibirMailQueja(password,sender,receiver,queja):
    ctx = ssl.create_default_context()
    #password = "ywjrlngnptcvdelw"    # Your app password goes here
    #sender = "peajevillada@gmail.com"    # Your e-mail address
    #receiver = "tomasguell123@gmail.com" # Recipient's address
    print(queja.items())
    # Create the message
    message = MIMEMultipart("alternative")
    message["Subject"] = queja['tituloQueja']
    message["From"] = sender
    message["To"] = receiver
    fecha = datetime.today()
    plain = f"Gmail del protestante: {queja['gmail']}\n Contenido de la queja: \n  {queja['contenidoQueja']}"
    
    
    message.attach(MIMEText(plain, "plain"))
    
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message.as_string())
    return print("Mail enviado!")

