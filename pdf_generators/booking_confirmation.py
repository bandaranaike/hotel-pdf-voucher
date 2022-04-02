from datetime import datetime
import env

from pdf_generators.pdf_template import *


def number_of_days(start, end):
    first_date = datetime.strptime(start, "%Y-%m-%d")
    last_date = datetime.strptime(end, "%Y-%m-%d")
    return abs((last_date - first_date).days)


def label_text(w=0, t="", b="TBL", ln=3, f=False, lh=1, a="L", c=": "):
    pdf.set_font("Helvetica")
    pdf.multi_cell(w, line_height * lh, f" {t} {c}", border=b, ln=ln, fill=f, align=a)


def value_text(w=0, t="", b="TRB", ln=3, f=False, a="L"):
    pdf.set_font("Courier")
    pdf.multi_cell(w, line_height, f"{t} ", border=b, ln=ln, fill=f, align=a)


def create_pdf(data):
    pdf_header("Booking Confirmation Voucher")

    # Data which coming from the form
    [booking_confirm_date, tr_ref_no, booking_number, checking_date, checkout_date, guest_name, nationality,
     rate_per_night, ro, bb, hb, fb, adults, kids, baby, room_category, single, double,
     triple, quad, family, cooking_demo, market_visit, driver_accommodation, travel_agent, remarks] = data

    # Row 1
    pdf.set_fill_color(64, 157, 120)
    pdf.set_draw_color(64, 157, 120)
    pdf.set_text_color(255, 255, 255)
    label_text(42, "Booking Confirmed On", 1, f=True)
    value_text(28, booking_confirm_date, 1, f=True)

    pdf.set_draw_color(220, 220, 220)
    pdf.set_text_color(27, 39, 51)

    label_text(25, "TR Ref No.")
    value_text(35, tr_ref_no)

    label_text(21, "Tour No.")
    value_text(39, booking_number, ln=1)

    # Travel Agent
    label_text(30, "Travel Agent")
    value_text(160, travel_agent, ln=1)

    # Row 2 : Dates
    # pdf.multi_cell(72, line_height, f"  : {}", border=1, ln=3)
    label_text(30, "Checking Date")
    value_text(42, checking_date)

    label_text(30, "Checkout Date")
    value_text(42, checkout_date)

    nu_of_nights = number_of_days(checking_date, checkout_date)
    label_text(34, "Number of nights")
    value_text(12, nu_of_nights, ln=1)

    # Row 3
    label_text(30, "Guest name")
    value_text(160, guest_name, ln=1)

    # Row 3
    # pdf.multi_cell(80, line_height, f"  : {}", border=1, ln=3)
    label_text(25, "Nationality")
    value_text(55, nationality)

    # pdf.multi_cell(55, line_height, f"  : {}", border=1, ln=3)
    label_text(30, "Rate per night")
    value_text(25, rate_per_night)

    total = round(float(rate_per_night) * nu_of_nights, 2)
    # pdf.multi_cell(55, line_height, f"  : {}", border=1, ln=1)
    label_text(25, "Total")
    value_text(30, total, ln=1)

    # Row 4
    # pdf.multi_cell(43, line_height * 2, " Meal plan :", border=1, ln=3)
    label_text(43, "Meal plan", lh=2)
    # pdf.multi_cell(37, line_height, f" ", border=1, ln=3, align="C")
    label_text(37, "RO", a="C", c="")
    # pdf.multi_cell(37, line_height, f" ", border=1, ln=3, align="C")
    label_text(37, "BB", a="C", c="")
    # pdf.multi_cell(37, line_height, f" ", border=1, ln=3, align="C")
    label_text(37, "HB", a="C", c="")
    # pdf.multi_cell(36, line_height, f" ", border=1, ln=1, align="C")
    label_text(36, "FB", "LR", a="C", c="", ln=1)

    # pdf.multi_cell(43, line_height, "", ln=3)
    value_text(43, "", 0)
    # pdf.multi_cell(37, line_height, f" {} ", border=1, ln=3, align="C")
    value_text(37, ro, "LR", a="C")
    # pdf.multi_cell(37, line_height, f" {} ", border=1, ln=3, align="C")
    value_text(37, bb, a="C")
    # pdf.multi_cell(37, line_height, f" {} ", border=1, ln=3, align="C")
    value_text(37, hb, a="C")
    # pdf.multi_cell(36, line_height, f" {} ", border=1, ln=1, align="C")
    value_text(36, fb, a="C", ln=1)

    # Number of pax
    number_of_fax = int(adults) + int(kids) + int(baby)
    # pdf.multi_cell(43, line_height * 2, f"  : {number_of_fax}", border=1, ln=3)
    label_text(43, "Number of pax", lh=2)
    # pdf.multi_cell(49, line_height, " ", border=1, ln=3, align="C")
    label_text(49, "Adults 12+", a="C", c="")
    # pdf.multi_cell(49, line_height, " ", border=1, ln=3, align="C")
    label_text(49, "Kids 5-11", a="C", c="")
    # pdf.multi_cell(49, line_height, " ", border=1, ln=1, align="C")
    label_text(49, "Infants 0-4", "LR", a="C", c="", ln=1)

    # pdf.multi_cell(43, line_height, "", border=0, ln=3)
    value_text(43, "", 0)
    # pdf.multi_cell(49, line_height, f" {}", border=1, ln=3, align="C")
    value_text(49, adults, "LR", a="C")
    # pdf.multi_cell(49, line_height, f" {}", border=1, ln=3, align="C")
    value_text(49, kids, a="C")
    # pdf.multi_cell(49, line_height, f" {}", border=1, ln=1, align="C")
    value_text(49, baby, a="C", ln=1)

    # Room category
    # pdf.multi_cell(0, line_height, f"  : {}", border=1, ln=1)
    label_text(35, "Room category")
    value_text(155, room_category, ln=1)

    # Rooms
    number_of_rooms = int(single) + int(double) + int(triple) + int(quad) + int(family)
    # pdf.multi_cell(43, line_height * 2, f"  : {number_of_rooms}", border=1, ln=3)
    label_text(43, "Number of rooms", lh=2)
    # pdf.multi_cell(30, line_height, "  ", border=1, ln=3, align="C")
    label_text(30, "SIN", a="C", c="")
    # pdf.multi_cell(30, line_height, "  ", border=1, ln=3, align="C")
    label_text(30, "DBL", a="C", c="")
    # pdf.multi_cell(29, line_height, "  ", border=1, ln=3, align="C")
    label_text(29, "TRI", a="C", c="")
    # pdf.multi_cell(29, line_height, "  ", border=1, ln=3, align="C")
    label_text(29, "QUD", a="C", c="")
    # pdf.multi_cell(29, line_height, "  ", border=1, ln=1, align="C")
    label_text(29, "FAM", "LR", a="C", c="", ln=1)

    # pdf.multi_cell(43, line_height, "", border=0, ln=3)
    value_text(43, "", 0)
    # pdf.multi_cell(30, line_height, f" {}", border=1, ln=3, align="C")
    value_text(30, single, "LR", a="C")
    # pdf.multi_cell(30, line_height, f" {}", border=1, ln=3, align="C")
    value_text(30, double, a="C")
    # pdf.multi_cell(29, line_height, f" {}", border=1, ln=3, align="C")
    value_text(29, triple, a="C")
    # pdf.multi_cell(29, line_height, f" {}", border=1, ln=3, align="C")
    value_text(29, quad, a="C")
    # pdf.multi_cell(29, line_height, f" {}", border=1, ln=1, align="C")
    value_text(29, family, a="C", ln=1)

    # Extra activities
    # pdf.multi_cell(43, line_height * 2, "  ", border=1, ln=3)
    label_text(43, "Extra Activities", lh=2)
    # pdf.multi_cell(73, line_height, "  ", border=1, ln=3, align="C")
    label_text(73, "Cooking Demo", a="C", c="")
    # pdf.multi_cell(74, line_height, "  ", border=1, ln=1, align="C")
    label_text(74, "Market Visit", "LR", a="C", c="", ln=1)

    # pdf.multi_cell(43, line_height, "", ln=3)
    value_text(43, "", 0)
    # pdf.multi_cell(73, line_height, f" {} ", border=1, ln=3, align="C")
    value_text(73, cooking_demo, "LR", a="C")
    # pdf.multi_cell(74, line_height, f" {} ", border=1, ln=1, align="C")
    value_text(74, market_visit, a="C", ln=1)

    # Driver
    # pdf.multi_cell(0, line_height, f"  : {}", border=1, ln=1)
    label_text(60, "Driver accommodation required")
    value_text(130, driver_accommodation, ln=1)

    # Row 9 : Remarks
    # pdf.multi_cell(0, line_height, " ",
    #                border=1, ln=1)
    label_text(25, "Payments")
    value_text(165, "Please be kind enough  to settle the bill before check-out", ln=1)

    # Row 9 : Box
    # pdf.multi_cell(page_width - 55, line_height / 1.8, f" : {}", ln=3)
    label_text(23, "Remarks")
    value_text(167, remarks, ln=1)

    pdf.set_font("Helvetica")
    pdf_footer()

    pdf.output(f"{env.dirname}/{booking_number}.pdf")
