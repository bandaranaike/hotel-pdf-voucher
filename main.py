from fpdf import FPDF

import qrcode_gen


def create_pdf(data):
    try:
        page_width = 210
        page_height = 297

        # Contact details
        address = "162/1, Panasara Mw, Halloluwa"
        email = "info@thotupolaresidence.lk"
        mobile = "0773389665 / 0777802093"
        tele_phone = "0812492754"

        # Data which coming from the form
        [booking_confirm_date, booking_number, guest_name, guest_family_name, nationality, rate_per_night, meal_plan,
         adults_count, teen_count, kids_count, baby_count, checking_date, checkout_date, number_of_delux_rooms,
         number_of_river_view_rooms, driver_accommodation] = data

        # Generate QR code for booking number
        qrcode_gen.generate_qr(booking_number)
        # Generate QR code for contact details
        qrcode_gen.generate_qr(booking_number + "-1", f"A:{address}, E:{email}, M:{mobile}, T:{tele_phone}")

        # Config
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica", size=20)

        col_width = pdf.epw / 4  # distribute content evenly

        # Top Line
        pdf.set_draw_color(209, 103, 0)
        pdf.set_fill_color(209, 103, 0)
        pdf.rect(0, 0, page_width, 0.5, style="FD")

        # Logo
        pdf.image('logo.png', 10, 10, 40)

        # Header
        pdf.set_text_color(209, 103, 0)
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
        pdf.multi_cell(28, line_height / 1.6, " Email Address", ln=3, border="0")
        pdf.multi_cell(page_width - 55, line_height / 1.6, f" : {email}", ln=1, border="0")
        pdf.multi_cell(28, line_height / 1.6, " Hotel Tel", ln=3, border="0")
        pdf.multi_cell(page_width - 55, line_height / 1.6, f" : {tele_phone}", ln=1, border="0")
        pdf.multi_cell(28, line_height / 1.6, " Mobile", ln=3, border="0")
        pdf.multi_cell(page_width - 55, line_height / 1.6, f" : {mobile}", ln=1, border="0")
        pdf.multi_cell(28, line_height / 1.6, " Address", ln=3, border="0")
        pdf.multi_cell(page_width - 55, line_height / 1.6, f" : {address}", ln=1, border="0")
        pdf.multi_cell(190, line_height / 6, "", ln=1, border="0")
        # QR
        pdf.image(f'{booking_number}-1.png', page_width - 37, 26, w=28)

        pdf.ln(10)

        # Table
        pdf.set_font_size(10)
        pdf.set_fill_color(238, 253, 242)
        pdf.set_text_color(44, 132, 83)

        # Row 1
        pdf.multi_cell(63, line_height, f" Booking Confirmed On : {booking_confirm_date}", border=1, ln=3, fill=True)
        pdf.set_text_color(60, 60, 60)
        pdf.multi_cell(63, line_height, f"TR Ref No. : {booking_number} ", border=1, ln=3)
        pdf.multi_cell(64, line_height, f"Tour No. : {booking_number} ", border=1, ln=1)

        # Row 2 : Dates
        pdf.multi_cell(72, line_height, f" Checking Date : {checking_date}", border=1, ln=3)
        pdf.multi_cell(72, line_height, f" Checkout Date : {checkout_date}", border=1, ln=3)
        pdf.multi_cell(46, line_height, " Number of nights : 4", border=1, ln=1)

        # Row 3
        pdf.multi_cell(0, line_height, f" Guest name : {guest_name}", border=1, ln=1)

        # Row 3
        pdf.multi_cell(95, line_height, f" Nationality : {nationality}", border=1, ln=3)
        pdf.multi_cell(95, line_height, f" Rate per night : {rate_per_night}", border=1, ln=1)

        # Row 4

        pdf.multi_cell(43, line_height * 2, f" Meal plan : {meal_plan}", border=1, ln=3)
        pdf.multi_cell(37, line_height, f" RO", border=1, ln=3)
        pdf.multi_cell(37, line_height, f" BB", border=1, ln=3)
        pdf.multi_cell(37, line_height, f" HB", border=1, ln=3)
        pdf.multi_cell(36, line_height, f" FB", border=1, ln=1)

        pdf.multi_cell(43, line_height, "", ln=3)
        pdf.multi_cell(37, line_height, f" {meal_plan} ", border=1, ln=3)
        pdf.multi_cell(37, line_height, f" {meal_plan} ", border=1, ln=3)
        pdf.multi_cell(37, line_height, f" {meal_plan} ", border=1, ln=3)
        pdf.multi_cell(36, line_height, f" {meal_plan} ", border=1, ln=1)

        # Row 5 : Number of pax
        pdf.multi_cell(43, line_height * 2, " Number of pax : 10", border=1, ln=3)
        pdf.multi_cell(49, line_height, " Adults 12+", border=1, ln=3)
        pdf.multi_cell(49, line_height, " Kids 5-11", border=1, ln=3)
        pdf.multi_cell(49, line_height, " Infants 0-4", border=1, ln=1)

        pdf.multi_cell(43, line_height, "", border=0, ln=3)
        pdf.multi_cell(49, line_height, f" {adults_count}", border=1, ln=3)
        pdf.multi_cell(49, line_height, f" {kids_count}", border=1, ln=3)
        pdf.multi_cell(49, line_height, f" {baby_count}", border=1, ln=1)

        # Row 7 : Rooms
        pdf.multi_cell(43, line_height * 2, " Number of rooms : 4", border=1, ln=3)
        pdf.multi_cell(30, line_height, " SIN ", border=1, ln=3)
        pdf.multi_cell(30, line_height, " DBL ", border=1, ln=3)
        pdf.multi_cell(29, line_height, " TRI ", border=1, ln=3)
        pdf.multi_cell(29, line_height, " QUD ", border=1, ln=3)
        pdf.multi_cell(29, line_height, " FAM ", border=1, ln=1)

        pdf.multi_cell(43, line_height, "", border=0, ln=3)
        pdf.multi_cell(30, line_height, " 1", border=1, ln=3)
        pdf.multi_cell(30, line_height, " 2", border=1, ln=3)
        pdf.multi_cell(29, line_height, " 2", border=1, ln=3)
        pdf.multi_cell(29, line_height, " 2", border=1, ln=3)
        pdf.multi_cell(29, line_height, " 3", border=1, ln=1)

        # Extra activities
        pdf.multi_cell(43, line_height * 2, " Extra Activities ", border=1, ln=3)
        pdf.multi_cell(73, line_height, " Cooking Demo ", border=1, ln=3)
        pdf.multi_cell(74, line_height, " Market Visit ", border=1, ln=1)

        pdf.multi_cell(43, line_height, "", ln=3)
        pdf.multi_cell(73, line_height, " Yes ", border=1, ln=3)
        pdf.multi_cell(74, line_height, " No ", border=1, ln=1)

        # Row 8 : Driver
        pdf.multi_cell(0, line_height, f" Driver accommodation required : {driver_accommodation}", border=1, ln=1)

        # Row 9 : Remarks
        pdf.multi_cell(0, line_height, " Payments : Please be kind enough  to settle the bill before the checkout",
                       border=1, ln=1)
        pdf.ln(3)
        # Row 9 : Box
        pdf.multi_cell(page_width - 50, line_height / 1.8,
                       "Remarks : Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                       ln=3)
        # QR
        pdf.image(f'{booking_number}.png', page_width - 40, w=30)
        pdf.ln(line_height)

        # Bottom info
        pdf.set_font_size(8)
        pdf.set_text_color(150, 150, 150)
        pdf.multi_cell(95, line_height, "Generated by Thotupola Residence", ln=3)
        pdf.multi_cell(95, line_height, "https://thotupolaresidence.lk", link="https://thotupolaresidence.lk", ln=1,
                       align="R")

        # Output
        pdf.output(f'{booking_number}.pdf')

        # Delete generated QR code image
        qrcode_gen.delete_qr(booking_number)
        qrcode_gen.delete_qr(booking_number + "-1")

    except AssertionError:
        log_message("AssertionError")
    except AttributeError:
        log_message("AttributeError")
    except EOFError:
        log_message("EOFError")
    except FloatingPointError:
        log_message("FloatingPointError")
    except GeneratorExit:
        log_message("GeneratorExit")
    except ImportError:
        log_message("ImportError")
    except IndexError:
        log_message("IndexError")
    except KeyError:
        log_message("KeyError")
    except KeyboardInterrupt:
        log_message("KeyboardInterrupt")
    except MemoryError:
        log_message("MemoryError")
    except NameError:
        log_message("NameError")
    except NotImplementedError:
        log_message("NotImplementedError")
    except OSError as er:
        log_message(str(er))
    except OverflowError:
        log_message("OverflowError")
    except ReferenceError:
        log_message("ReferenceError")
    except RuntimeError:
        log_message("RuntimeError")
    except StopIteration:
        log_message("StopIteration")
    except SyntaxError:
        log_message("SyntaxError")
    except IndentationError:
        log_message("IndentationError")
    except TabError:
        log_message("TabError")
    except SystemError:
        log_message("SystemError")
    except SystemExit:
        log_message("SystemExit")
    except TypeError:
        log_message("TypeError")
    except UnboundLocalError:
        log_message("UnboundLocalError")
    except UnicodeError:
        log_message("UnicodeError")
    except UnicodeEncodeError:
        log_message("UnicodeEncodeError")
    except UnicodeDecodeError:
        log_message("UnicodeDecodeError")
    except UnicodeTranslateError:
        log_message("UnicodeTranslateError")
    except ValueError:
        log_message("ValueError")
    except ZeroDivisionError:
        log_message("ZeroDivisionError")
    except Exception as e:
        log_message(str(e))


def log_message(message):
    with open('log.txt', 'w') as f:
        print("Something went wrong", message, file=f)
