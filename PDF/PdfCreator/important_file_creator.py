from typing import Text
from fpdf import FPDF

#Crear el Pdf 
pdf = FPDF('P', 'mm', 'Letter')
# Layout -  P (portrait) L 
# Unit - mm cm in
# Format -  A3 A4 A5 Letter Legal or custom(width, height)

# Añadir Pagina
pdf.add_page()

# Indicar Fuente
pdf.set_font('helvetica','',16)
# fonts ('times','courier','helvetica','symbol')
# 'B' (bold), 'U' (underline), I (italics), "" (regular), combined (i.e, ('BU))

# Añadir texto
pdf.cell(0,10,'Company File',ln=True, border=True, align='C') 


pdf.cell(0,10,'This is a very important file that contains a lot of details about the company.',ln=True, align='C') 

pdf.cell(0,10,'We will work with this relevant information',ln=True, align='C')

 

# Guardar archivo
pdf.output('pdf_1.pdf')