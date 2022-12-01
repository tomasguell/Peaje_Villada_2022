import qrcode
import subprocess
from fpdf import FPDF
from .gmail import enviarMailInforme

def generarQR(nombre, data):
    img = qrcode.make(f'{data}')
    type(img)  
    img.save(f"{nombre}.png")

def generarPDF(nombre, data):
	pdf = FPDF()
	pdf.add_page()
	print(data)
	pdf.set_font("Arial", size = 15)
	for i in data:
     
		pdf.cell(200, 10, txt = f"{data[str(i)]}",
			ln = i)
	pdf.output(f"{nombre}.pdf")

def imprimir(archivo):
	lpr =  subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
	lpr.stdin.write(archivo)




def generarPDFTurnos(nombre, cantidad_emitido,monto_cobrado,cantidad_por_categoria, user, date):
	pdf = FPDF()
	pdf.add_page()
	pdf.set_font("Arial", size = 20)
	pdf.cell(200, 10, txt = f"Informe Turno {user}",
			 ln =1 ,align = 'C')
	pdf.cell(200, 10, txt = f"Fecha y hora: {date}",
			 ln = 2,align = 'C')
	pdf.set_font("Arial", size = 15)
	pdf.cell(200, 10, txt = f"Cantidad de tickets emitida: {cantidad_emitido}",
			 ln = 4,align = 'C')
	pdf.cell(200, 10, txt = f"Monto total cobrado: {monto_cobrado}",
			 ln = 5,align = 'C')
	for i in cantidad_por_categoria:
		print(i)
		pdf.cell(200, 10, txt = f"{i}",
			  ln = 6,	 align = 'C')
        
	output_path = f"../Informes/{nombre}.pdf"
	pdf.output(output_path)
	enviarMailInforme("ywjrlngnptcvdelw","peajevillada@gmail.com", "peajevillada@gmail.com",output_path, f"Informe del turno de {nombre}" )

def generarPDFTicket(nombre,diccionario):
	pdf = FPDF()
	pdf = FPDF('P', 'mm', 'a4')
	pdf.add_page()
	a=0	 
	pdf.set_font("Arial", size = 15)
	for i in diccionario:
		a=a+1
		print(str(i))
		pdf.cell(200, 10, txt = f"{i}",
			  ln = a)
	
	pdf.image("QR.png", x=90, y=0)
	output_path = f"../Informes/{nombre}.pdf"
	pdf.output(output_path)
	#enviarMailInforme("ywjrlngnptcvdelw","peajevillada@gmail.com", "peajevillada@gmail.com",output_path, f"Ticket emitido por {nombre}" )
    
