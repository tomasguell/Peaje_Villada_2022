import qrcode
import subprocess
from fpdf import FPDF

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




def generarPDFTurnos(nombre, cantidad_emitido,monto_cobrado,cantidad_por_categoria):
	pdf = FPDF()
	pdf.add_page()
	pdf.set_font("Arial", size = 15)
	pdf.cell(200, 10, txt = f"Cantidad de tickets emitida: {cantidad_emitido}",
			 ln = 1,align = 'C')
	pdf.cell(200, 10, txt = f"Monto total cobrado: {monto_cobrado}",
			 ln = 2,align = 'C')
	for i in cantidad_por_categoria:
		print(i)
		pdf.cell(200, 10, txt = f"{i}",
			  ln = 3,	 align = 'C')
        
	pdf.output(f"../Informes/{nombre}.pdf")

def generarPDFTicket(nombre,diccionario):
	pdf = FPDF()
	pdf.add_page()
	a=0	 
	pdf.set_font("Arial", size = 15)
	for i in diccionario:
		a=a+1
		print(i)
		pdf.cell(200, 10, txt = f"{i}",
			  ln = a,	 align = 'C')
        
	pdf.output(f"../Informes/{nombre}.pdf")

