from datetime import datetime
import env

from pdf_generators.pdf_template import *


def number_of_days(start, end):
    first_date = datetime.strptime(start, "%Y-%m-%d")
    last_date = datetime.strptime(end, "%Y-%m-%d")
    return abs((last_date - first_date).days)


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
    pdf = pdf_header("Booking Confirmation Voucher")

    # Data which coming from the form
    [currency, booking_confirm_date, tr_ref_no, booking_number, checking_date, checkout_date, guest_name, nationality,
     rate_per_night, ro, bb, hb, fb, adults, kids, baby, room_category, single, double,
     triple, quad, family, cooking_demo, cooking_demo_rate, market_visit, total_cost, travel_agent, remarks] = data

    # Row 1
    pdf.set_fill_color(73, 159, 67)
    pdf.set_draw_color(73, 159, 67)
    pdf.set_text_color(255, 255, 255)
    label_text(pdf, 42, "Booking Confirmed On", 1, f=True, tc=False)
    value_text(pdf, 28, booking_confirm_date, 1, f=True, tc=False)

    pdf.set_draw_color(220, 220, 220)
    pdf.set_text_color(27, 39, 51)

    label_text(pdf, 25, "TR Ref No.")
    value_text(pdf, 35, tr_ref_no)

    label_text(pdf, 21, "Tour No.")
    value_text(pdf, 39, booking_number, ln=1)

    # Travel Agent
    label_text(pdf, 30, "Travel Agent")
    value_text(pdf, 160, travel_agent, ln=1)

    # Row 2 : Dates
    label_text(pdf, 30, "Checking Date")
    value_text(pdf, 42, checking_date)

    label_text(pdf, 30, "Checkout Date")
    value_text(pdf, 42, checkout_date)

    nu_of_nights = number_of_days(checking_date, checkout_date)
    label_text(pdf, 34, "Number of nights")
    value_text(pdf, 12, nu_of_nights, ln=1)

    # Row 3
    label_text(pdf, 30, "Guest name")
    value_text(pdf, 160, guest_name, ln=1)

    # Row 3
    # pdf.multi_cell(80, line_height, f"  : {}", border=1, ln=3)
    label_text(pdf, 25, "Nationality")
    value_text(pdf, 55, nationality)

    # rate_per_night = round(float(rate_per_night), 2)
    label_text(pdf, 30, "Rate per night")
    value_text(pdf, 25, f"{currency} {rate_per_night}")

    label_text(pdf, 25, "Total")
    value_text(pdf, 30, f"{currency} {total_cost}", ln=1)

    # Row 4
    label_text(pdf, 43, "Meal plan", lh=2)
    label_text(pdf, 37, "RO", a="C", c="")
    label_text(pdf, 37, "BB", a="C", c="")
    label_text(pdf, 37, "HB", a="C", c="")
    label_text(pdf, 36, "FB", "LR", a="C", c="", ln=1)


    value_text(pdf, 43, "", 0)
    value_text(pdf, 37, ro, "LR", a="C")
    value_text(pdf, 37, bb, a="C")
    value_text(pdf, 37, hb, a="C")
    value_text(pdf, 36, fb, a="C", ln=1)

    # Number of pax
    label_text(pdf, 43, "Number of pax", lh=2)
    label_text(pdf, 49, "Adults 12+", a="C", c="")
    label_text(pdf, 49, "Kids 5-11", a="C", c="")
    label_text(pdf, 49, "Infants 0-4", "LR", a="C", c="", ln=1)

    value_text(pdf, 43, "", 0)
    value_text(pdf, 49, adults, "LR", a="C")
    value_text(pdf, 49, kids, a="C")
    value_text(pdf, 49, baby, a="C", ln=1)

    # Room category
    label_text(pdf, 35, "Room category")
    value_text(pdf, 155, room_category, ln=1)

    # Rooms
    number_of_rooms = int(single) + int(double) + int(triple) + int(quad) + int(family)
    label_text(pdf, 43, "Number of rooms", lh=2)
    label_text(pdf, 30, "SIN", a="C", c="")
    label_text(pdf, 30, "DBL", a="C", c="")
    label_text(pdf, 29, "TRI", a="C", c="")
    label_text(pdf, 29, "QUD", a="C", c="")
    label_text(pdf, 29, "FAM", "LR", a="C", c="", ln=1)

    value_text(pdf, 43, "", 0)
    value_text(pdf, 30, single, "LR", a="C")
    value_text(pdf, 30, double, a="C")
    value_text(pdf, 29, triple, a="C")
    value_text(pdf, 29, quad, a="C")
    value_text(pdf, 29, family, a="C", ln=1)

    # Extra activities
    label_text(pdf, 43, "Extra Activities", lh=2)
    label_text(pdf, 49, "Cooking Demo", a="C", c="")
    label_text(pdf, 49, "Cooking Demo Rate", a="C", c="")
    label_text(pdf, 49, "Market Visit", "LR", a="C", c="", ln=1)

    value_text(pdf, 43, "", 0)
    value_text(pdf, 49, cooking_demo, "LR", a="C")
    value_text(pdf, 49, f"{currency} {cooking_demo_rate}", "LR", a="C")
    value_text(pdf, 49, market_visit, a="C", ln=1)

    # Driver
    label_text(pdf, 60, "Driver accommodation")
    value_text(pdf, 130, "Not Available", ln=1)

    # Row 9 : Remarks
    label_text(pdf, 25, "Payments")
    value_text(pdf, 165, "Please be kind enough  to settle the bill before check-out", ln=1)

    # Row 9 : Box
    label_text(pdf, 23, "Remarks")
    value_text(pdf, 167, remarks, ln=1)

    pdf.set_font("Helvetica")
    pdf_footer(pdf)

    pdf_output(pdf, booking_number)
