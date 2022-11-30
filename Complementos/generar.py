import qrcode
from fpdf import FPDF

def generarQR(nombre, data):
    img = qrcode.make(data)
    type(img)  
    img.save(f"{nombre}.png")

def generarPDF(nombre, data):
	pdf = FPDF()
	pdf.add_page()
	pdf.set_font("Arial", size = 15)
	pdf.cell(200, 10, txt = f"{data}",
			ln = 1, align = 'C')
	pdf.output(f"{nombre}.pdf")

