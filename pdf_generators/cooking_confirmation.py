from datetime import datetime
import env

from pdf_generators.pdf_template import *


def label_text(pdf, w=0, t="", b="TBL", ln=3, f=False, lh=1, a="L", c=": ", tc=True):
    pdf.set_font("Helvetica")
    if tc:
        pdf.set_text_color(80, 80, 80)
    pdf.multi_cell(w, line_height * lh, f" {t} {c}", border=b, ln=ln, fill=f, align=a)


def value_text(pdf, w=0, t="", b="TRB", ln=3, f=False, a="L", tc=True):
    pdf.set_font("Courier")
    if tc:
        pdf.set_text_color(0, 75, 130)
    pdf.multi_cell(w, line_height, f"{t} ", border=b, ln=ln, fill=f, align=a)


def create_pdf(data):
    pdf = pdf_header("Cooking Confirmation Voucher")

    # Data which coming from the form
    [currency, cooking_experience_date, cooking_class_ref_no, guest_name, nationality, rate_per_person, adults_count,
     kids_count,
     babies_count, travel_agent, remarks] = data

    # Row 1
    pdf.set_fill_color(73, 159, 67)
    pdf.set_draw_color(73, 159, 67)
    pdf.set_text_color(255, 255, 255)

    label_text(pdf, 52, "Cooking Experience Date", 1, f=True, tc=False)
    value_text(pdf, 28, cooking_experience_date, 1, f=True, tc=False)

    pdf.set_draw_color(220, 220, 220)
    pdf.set_text_color(27, 39, 51)

    label_text(pdf, 45, "Cooking Class Ref No.")
    value_text(pdf, 65, cooking_class_ref_no, ln=1)

    # Travel Agent
    label_text(pdf, 30, "Travel Agent")
    value_text(pdf, 160, travel_agent, ln=1)

    # Row 3
    label_text(pdf, 30, "Guest name")
    value_text(pdf, 160, guest_name, ln=1)

    # Row 3
    label_text(pdf, 25, "Nationality")
    value_text(pdf, 55, nationality)

    # Variables
    rate_per_person = round(float(rate_per_person), 2)
    number_of_fax = int(adults_count) + (int(kids_count) / 2)
    total = round(float(rate_per_person) * number_of_fax, 2)

    label_text(pdf, 35, "Rate per person")
    value_text(pdf, 26, f"{currency} {rate_per_person}")

    label_text(pdf, 19, "Total")
    value_text(pdf, 30, f"{currency} {total}", ln=1)

    label_text(pdf, 37, "Number of pax", lh=2)
    label_text(pdf, 51, "Adults", a="C", c="")
    label_text(pdf, 51, "Kids 6-12 (Half of charge)", a="C", c="")
    label_text(pdf, 51, "Below 6 (Free)", "LR", a="C", c="", ln=1)

    value_text(pdf, 37, "", 0)
    value_text(pdf, 51, adults_count, "LR", a="C")
    value_text(pdf, 51, kids_count, a="C")
    value_text(pdf, 51, babies_count, a="C", ln=1)

    # Row 9 : Remarks
    label_text(pdf, 25, "Payments")
    value_text(pdf, 165, "Please be kind enough  to settle the bill before check-out", ln=1)

    # Row 9 : Box
    label_text(pdf, 23, "Remarks")
    value_text(pdf, 167, remarks, ln=1)

    pdf.set_font("Helvetica")
    pdf_footer(pdf)

    pdf_output(pdf, cooking_class_ref_no)
