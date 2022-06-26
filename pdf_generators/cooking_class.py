import numbers

from pdf_generators.pdf_template import *
import env


def create_pdf(data):
    [currency, demo_price, market_visit, below_6, between_6_12, above_12] = data

    pdf = pdf_header("Cooking Class Rate Sheet")

    pdf.multi_cell(120, line_height, " Cookery Demonstration with Meal (Per Person) ", ln=3, border=1)
    pdf.multi_cell(70, line_height, check_is_a_price(currency, demo_price), ln=1, border=1)

    pdf.multi_cell(120, line_height, " Market Visit Per Tuk ", ln=3, border=1)
    pdf.multi_cell(70, line_height, check_is_a_price(currency, market_visit), ln=1, border=1)

    pdf.multi_cell(120, line_height, " Children Below 6 years ", ln=3, border=1)
    pdf.multi_cell(70, line_height, check_is_a_price(currency, below_6), ln=1, border=1)

    pdf.multi_cell(120, line_height, " Children Between 6 12 years ", ln=3, border=1)
    pdf.multi_cell(70, line_height, check_is_a_price(currency, between_6_12), ln=1, border=1)

    pdf.multi_cell(120, line_height, " Children Above 12 years ", ln=3, border=1)
    pdf.multi_cell(70, line_height, check_is_a_price(currency, above_12), ln=1, border=1)

    pdf.multi_cell(190, line_height, " Please be kind enough to inform us special requests. Ex: Allergies, Vegan,"
                                     " Non veg, Vegetarian, Gluten free ", ln=1, border=1)

    pdf_footer(pdf)

    pdf_output(pdf, "cooking_class")


def check_is_a_price(currency, val):
    # print(val)
    # print(val.isdigit())
    try:
        float(val)
        return f"{currency} {val}"
    except ValueError:
        return val
