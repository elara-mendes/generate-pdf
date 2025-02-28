from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)


for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", size=24, style="B")
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10,20, 200, 20)

    pdf.ln(255)

    pdf.set_font(family="Times", size=8, style="B")
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for page in range(row["Pages"] - 1):
        pdf.add_page()

        pdf.ln(268)

        pdf.set_font(family="Times", size=8, style="B")
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
pdf.output("teste.pdf")