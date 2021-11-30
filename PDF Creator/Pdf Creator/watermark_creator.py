from typing import Text
from fpdf import FPDF

#Crear el Pdf 
pdf = FPDF('P', 'mm', 'Letter')
# Layout -  P (portrait) L 
# Unit - mm cm in
# Format -  A3 A4 A5 Letter Legal or custom(width, height)

# Añadir Pagina
pdf.add_page()

# Editar fuente
pdf.set_font('helvetica','',16)
# Indicar Fuente
# fonts ('times','courier','helvetica','symbol')
# 'B' (bold), 'U' (underline), I (italics), "" (regular), combined (i.e, ('BU))

# Añadir texto
pdf.cell(50,10,'Important File', ln=True, align='C' ) # ln= True empieza en la sig. linea cuando acaba
# w = width
# h = height
pdf.cell(50,10,'DO NOT LEAK',ln=True, border=True , align='C')


# Guardar archivo
pdf.output('pdf_1.pdf')