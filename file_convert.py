import os
from docx2pdf import convert #you need microsoft word for this to work
from fpdf import FPDF
import textwrap
from PIL import Image


def pdf(file):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.add_page()
    pdf.set_font("Courier", size=10)
    pt_to_mm=0.35 
    fontsize=10
    width_text=int(210/2.45) #textwrap expects int
    for line in file.split('\n'):
        lines=textwrap.wrap(line, width_text)
        if len(lines) == 0:
            pdf.ln()
        for wrap in lines:
            pdf.cell(0, fontsize*pt_to_mm, wrap, ln=1)
    pdf.output('converted.pdf', 'F')

def png(file):
    im=Image.open(file)
    im.save('converted.png')
file = input("Enter the path to your file including the file extension: ")
file_and_ext = os.path.splitext(file)
extension = file_and_ext[1].lower()


if extension == '.docx':
    convert(file, "converted.pdf")
elif extension == '.txt':
    with open(file, 'r') as f:
        content = f.read()
        pdf(content)
elif extension in ['.jpg', '.jpeg']: #same logic for both file types
    png(file)


