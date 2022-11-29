import smtplib
import ssl
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase

# Define the transport variables
ctx = ssl.create_default_context()
password = "ywjrlngnptcvdelw"    # Your app password goes here
sender = "peajevillada@gmail.com"    # Your e-mail address
receiver = "tomasguell123@gmail.com" # Recipient's address

# Create the message
message = MIMEMultipart("alternative")
message["Subject"] = "<Informe Peaje Villada>"
message["From"] = sender
message["To"] = receiver

# HTML version
#T1BaseDeDatos.pdf

# Plain text alternative version

fecha = datetime.today()
plain = f"""\
Informe Diario de rendimientos.
Fecha: {fecha}
Saludos!
"""

pdfname = 'T1BaseDeDatos.pdf'
 
# open the file in bynary
binary_pdf = open(pdfname, 'rb')
 
payload = MIMEBase('application', 'octate-stream', Name=pdfname)
payload.set_payload((binary_pdf).read())
 
# enconding the binary into base64
encoders.encode_base64(payload)
 
# add header with pdf name
payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)













# Add the different alternative parts in order of increasing complexity
# starting with the simplest first, i.e. the plain text version first.
message.attach(MIMEText(plain, "plain"))
message.attach(payload)

#message.attach(MIMEText(html, "html"))

# Connect with server and send the message
with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message.as_string())