import qrcode

def generar(nombre, data):
    img = qrcode.make(data)
    type(img)  
    img.save(f"{nombre}.png")
