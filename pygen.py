import os
import pandas as pd
from fpdf import FPDF

FILEPATH = "topics.csv"
df = pd.read_csv(FILEPATH)


def pdfgen(data):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_font('Arial', 'B', size=24)
    pdf.set_text_color(100, 100, 100)
    for index, row in data.iterrows():
        pdf.add_page()
        pdf.cell(txt=row["Topic"], w=10, h=10, ln=1, align='L', border=0)
        pdf.line(10,20,200,20)
    pdf.output("pdf.pdf")

pdfgen(df)


