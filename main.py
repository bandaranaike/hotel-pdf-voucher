from datetime import datetime

from fpdf import FPDF

from os.path import exists

import qrcode_gen


def create_pdf(data):

        page_width = 210
        page_height = 297

        # Contact details
        address = "162/1, Panasara Mw, Halloluwa"
        email = "info@thotupolaresidence.lk"
        mobile = "0773389665 / 0777802093"
        tele_phone = "0812492754"

        # Data which coming from the form
        [booking_confirm_date, tr_ref_no, booking_number, checking_date, checkout_date, guest_name, nationality,
         rate_per_night, ro, bb, hb, fb, adults, kids, baby, room_category, single, double,
         triple, quad, family, cooking_demo, market_visit, driver_accommodation, travel_agent, remarks] = data

        # Generate QR code for website
        qrcode_gen.generate_qr(booking_number, "https://thotupolaresidence.lk")
        # Generate QR code for contact details
        qrcode_gen.generate_qr(booking_number + "-1", f"A:{address}, E:{email}, M:{mobile}, T:{tele_phone}")

        # Config
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica", size=20)

        col_width = pdf.epw / 4  # distribute content evenly

        # Top Line
        pdf.set_draw_color(255, 159, 53)
        pdf.set_fill_color(255, 159, 53)
        pdf.rect(0, 0, page_width, 0.5, style="FD")

        # Logo
        if exists('logo.png'):
            pdf.image('logo.png', 10, 10, 40)
        else:
            pdf.multi_cell(1, ln=3)

        # Header
        pdf.set_text_color(0, 55, 129)
        pdf.multi_cell(page_width - 20, 10, "Booking Confirmation Voucher", align="R", ln=1)
        pdf.ln(8)

        # Body style config
        pdf.set_draw_color(220, 220, 220)
        pdf.set_line_width(0.4)
        pdf.set_font_size(10)
        line_height = pdf.font_size * 2.5

        # Details
        pdf.set_font_size(10)
        pdf.set_text_color(80, 80, 80)
        pdf.multi_cell(190, line_height / 6, "", ln=1, border="0")
        pdf.multi_cell(28, line_height / 1.6, "Email Address", ln=3, border="0")
        pdf.multi_cell(page_width - 55, line_height / 1.6, f" : {email}", ln=1, border="0")
        pdf.multi_cell(28, line_height / 1.6, "Hotel Tel", ln=3, border="0")
        pdf.multi_cell(page_width - 55, line_height / 1.6, f" : {tele_phone}", ln=1, border="0")
        pdf.multi_cell(28, line_height / 1.6, "Mobile", ln=3, border="0")
        pdf.multi_cell(page_width - 55, line_height / 1.6, f" : {mobile}", ln=1, border="0")
        pdf.multi_cell(28, line_height / 1.6, "Address", ln=3, border="0")
        pdf.multi_cell(page_width - 55, line_height / 1.6, f" : {address}", ln=1, border="0")
        pdf.multi_cell(190, line_height / 6, "", ln=1, border="0")
        # QR
        pdf.image(f'{booking_number}-1.png', page_width - 38, 26, w=28)

        pdf.ln(10)

        # Table
        pdf.set_font_size(10)

        # Row 1
        pdf.set_fill_color(64, 157, 120)
        pdf.set_draw_color(64, 157, 120)
        pdf.set_text_color(255, 255, 255)
        pdf.multi_cell(63, line_height, f" Booking Confirmed On : {booking_confirm_date}", border=1, ln=3, fill=True)

        pdf.set_draw_color(220, 220, 220)
        pdf.set_text_color(27, 39, 51)
        pdf.multi_cell(63, line_height, f" TR Ref No. : {tr_ref_no} ", border=1, ln=3)
        pdf.multi_cell(64, line_height, f" Tour No. : {booking_number} ", border=1, ln=1)

        # Travel Agent
        pdf.multi_cell(0, line_height, f" Travel Agent : {travel_agent}", border=1, ln=1)

        # Row 2 : Dates
        pdf.multi_cell(72, line_height, f" Checking Date : {checking_date}", border=1, ln=3)
        pdf.multi_cell(72, line_height, f" Checkout Date : {checkout_date}", border=1, ln=3)
        nu_of_nights = number_of_days(checking_date, checkout_date)
        pdf.multi_cell(46, line_height, f" Number of nights : {nu_of_nights}", border=1, ln=1)

        # Row 3
        pdf.multi_cell(0, line_height, f" Guest name : {guest_name}", border=1, ln=1)

        # Row 3
        pdf.multi_cell(80, line_height, f" Nationality : {nationality}", border=1, ln=3)
        pdf.multi_cell(55, line_height, f" Rate per night : {rate_per_night}", border=1, ln=3)
        total = round(float(rate_per_night) * nu_of_nights, 2)
        pdf.multi_cell(55, line_height, f" Total : {total}", border=1, ln=1)

        # Row 4
        pdf.multi_cell(43, line_height * 2, " Meal plan :", border=1, ln=3)
        pdf.multi_cell(37, line_height, f" RO", border=1, ln=3, align="C")
        pdf.multi_cell(37, line_height, f" BB", border=1, ln=3, align="C")
        pdf.multi_cell(37, line_height, f" HB", border=1, ln=3, align="C")
        pdf.multi_cell(36, line_height, f" FB", border=1, ln=1, align="C")

        pdf.multi_cell(43, line_height, "", ln=3)
        pdf.multi_cell(37, line_height, f" {ro} ", border=1, ln=3, align="C")
        pdf.multi_cell(37, line_height, f" {bb} ", border=1, ln=3, align="C")
        pdf.multi_cell(37, line_height, f" {hb} ", border=1, ln=3, align="C")
        pdf.multi_cell(36, line_height, f" {fb} ", border=1, ln=1, align="C")

        # Number of pax
        number_of_fax = int(adults) + int(kids) + int(baby)
        pdf.multi_cell(43, line_height * 2, f" Number of pax : {number_of_fax}", border=1, ln=3)
        pdf.multi_cell(49, line_height, " Adults 12+", border=1, ln=3, align="C")
        pdf.multi_cell(49, line_height, " Kids 5-11", border=1, ln=3, align="C")
        pdf.multi_cell(49, line_height, " Infants 0-4", border=1, ln=1, align="C")

        pdf.multi_cell(43, line_height, "", border=0, ln=3)
        pdf.multi_cell(49, line_height, f" {adults}", border=1, ln=3, align="C")
        pdf.multi_cell(49, line_height, f" {kids}", border=1, ln=3, align="C")
        pdf.multi_cell(49, line_height, f" {baby}", border=1, ln=1, align="C")

        # Room category
        pdf.multi_cell(0, line_height, f" Room category : {room_category}", border=1, ln=1)

        # Rooms
        number_of_rooms = int(single) + int(double) + int(triple) + int(quad) + int(family)
        pdf.multi_cell(43, line_height * 2, f" Number of rooms : {number_of_rooms}", border=1, ln=3)
        pdf.multi_cell(30, line_height, " SIN ", border=1, ln=3, align="C")
        pdf.multi_cell(30, line_height, " DBL ", border=1, ln=3, align="C")
        pdf.multi_cell(29, line_height, " TRI ", border=1, ln=3, align="C")
        pdf.multi_cell(29, line_height, " QUD ", border=1, ln=3, align="C")
        pdf.multi_cell(29, line_height, " FAM ", border=1, ln=1, align="C")

        pdf.multi_cell(43, line_height, "", border=0, ln=3)
        pdf.multi_cell(30, line_height, f" {single}", border=1, ln=3, align="C")
        pdf.multi_cell(30, line_height, f" {double}", border=1, ln=3, align="C")
        pdf.multi_cell(29, line_height, f" {triple}", border=1, ln=3, align="C")
        pdf.multi_cell(29, line_height, f" {quad}", border=1, ln=3, align="C")
        pdf.multi_cell(29, line_height, f" {family}", border=1, ln=1, align="C")

        # Extra activities
        pdf.multi_cell(43, line_height * 2, " Extra Activities ", border=1, ln=3)
        pdf.multi_cell(73, line_height, " Cooking Demo ", border=1, ln=3, align="C")
        pdf.multi_cell(74, line_height, " Market Visit ", border=1, ln=1, align="C")

        pdf.multi_cell(43, line_height, "", ln=3)
        pdf.multi_cell(73, line_height, f" {cooking_demo} ", border=1, ln=3, align="C")
        pdf.multi_cell(74, line_height, f" {market_visit} ", border=1, ln=1, align="C")

        # Driver
        pdf.multi_cell(0, line_height, f" Driver accommodation required : {driver_accommodation}", border=1, ln=1)

        # Row 9 : Remarks
        pdf.multi_cell(0, line_height, " Payments : Please be kind enough  to settle the bill before check-out",
                       border=1, ln=1)
        pdf.ln(3)
        # Row 9 : Box
        pdf.multi_cell(page_width - 55, line_height / 1.8, f"Remarks : {remarks}", ln=3)
        pdf.multi_cell(5, line_height, "", ln=3)
        # QR
        pdf.image(f'{booking_number}.png', page_width - 40, w=30)
        pdf.ln(5)

        # Message
        pdf.set_font_size(9)
        pdf.set_text_color(100, 100, 100)
        pdf.multi_cell(page_width - 20, line_height / 1.8, "Thank you for being our valued customer. We are so grateful for serving you and hope we met your expectations. Always happy to hear from you.", ln=1)

        # Bottom info
        pdf.set_font_size(8)
        pdf.set_text_color(150, 150, 150)
        pdf.multi_cell(95, line_height, "Generated by Thotupola Residence", ln=3)
        pdf.multi_cell(95, line_height, "https://thotupolaresidence.lk", link="https://thotupolaresidence.lk", ln=1,
                       align="R")
        pdf.image('7sb.png', 11, w=8, link="https://sevensbay.com")

        # Output
        pdf.output(f'{booking_number}.pdf')

        # Delete generated QR code image
        qrcode_gen.delete_qr(booking_number)
        qrcode_gen.delete_qr(booking_number + "-1")




def number_of_days(start, end):
    first_date = datetime.strptime(start, "%Y-%m-%d")
    last_date = datetime.strptime(end, "%Y-%m-%d")
    return abs((last_date - first_date).days)
