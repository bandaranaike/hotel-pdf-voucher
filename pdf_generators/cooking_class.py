from pdf_generators.pdf_template import *
import env


def create_pdf(data):
    [demo_price, market_visit, below_6, between_6_12, above_12] = data

    pdf = pdf_header("Cooking Class Rate Sheet")

    pdf.multi_cell(120, line_height, " Cookery Demonstration with Meal (Per Person) ", ln=3, border=1)
    pdf.multi_cell(70, line_height, f" {demo_price} ", ln=1, border=1)

    pdf.multi_cell(120, line_height, " Market Visit Per Tuk ", ln=3, border=1)
    pdf.multi_cell(70, line_height, f" {market_visit} ", ln=1, border=1)

    pdf.multi_cell(120, line_height, " Children Below 6 years ", ln=3, border=1)
    pdf.multi_cell(70, line_height, f" {below_6} ", ln=1, border=1)

    pdf.multi_cell(120, line_height, " Children Between 6 12 years ", ln=3, border=1)
    pdf.multi_cell(70, line_height, f" {between_6_12} ", ln=1, border=1)

    pdf.multi_cell(120, line_height, " Children Above 12 years ", ln=3, border=1)
    pdf.multi_cell(70, line_height, f" {above_12} ", ln=1, border=1)

    pdf_footer(pdf)

    pdf_output(pdf, "cooking_class")
