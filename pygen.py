import os
import pandas as pd
from fpdf import FPDF

FILEPATH = "topics.csv"
df = pd.read_csv(FILEPATH)


def pdfgen(data):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    for index, row in data.iterrows():
        pdf.set_auto_page_break(False, margin=0)
        pdf.set_font('Arial', 'B', size=24)
        pdf.set_text_color(100, 100, 100)
        pdf.add_page()
        pdf.cell(txt=row["Topic"], w=10, h=10, ln=1, align='L', border=0)
        pdf.line(10,20,200,20)
        y1=20
        while y1 < 270:
            y1 +=10
            pdf.line(10, y1, 200, y1)
        #footer
        pdf.ln(260)
        pdf.set_font('Times', 'I', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=0, ln=1, align='R', border=0, txt=row["Topic"])
        for i in range(int(row["Pages"])-1):
            pdf.add_page()
            y1 = 10
            while y1 < 280:
                y1 += 10
                pdf.line(10, y1, 200, y1)
            #footer
            pdf.ln(277)
            pdf.set_font('Times', 'I', size=8)
            pdf.set_text_color(180, 180, 180)
            pdf.cell(w=0, h=0, ln=1, align='R', border=0, txt=row["Topic"])

    pdf.output("pdf.pdf")

pdfgen(df)


