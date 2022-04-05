from pdf_template import *
import env


def add_header(header_text):
    pdf.set_text_color(255, 255, 255)
    pdf.set_font_size(11)
    pdf.multi_cell(0, line_height, header_text, ln=1, fill=True)
    pdf.ln(3)
    pdf.set_text_color(80, 80, 80)
    pdf.set_font_size(10)


def add_li(li_text):
    pdf.multi_cell(5, line_height / 1.2, "º", ln=3)
    pdf.multi_cell(185, line_height / 1.5, li_text, ln=1)
    pdf.ln(3)


def create_pdf(data):
    pdf_header("Our Company Policies")

    pdf.set_fill_color(120, 120, 120)
    pdf.set_draw_color(220, 220, 220)

    add_header(" Please Note: COVID-19 Policy Updates ")
    pdf.write(5.5,
              "In light of the COVID-19 pandemic, we have amended our policies to ensure the safety of our guests and "
              "team... Understandably, our policies and practices are subject to change in light of new information "
              "and recommendations from local health authorities and new orders and restrictions that may be put in"
              " place by various governmental entities. Prior to your arrival, Thotupola Residence will make every "
              "reasonable effort to keep you informed of service changes that may impact your stay. Summary of policy "
              "updates in response to COVID-19:")
    pdf.ln(10)

    add_li("Face masks and distancing are required. All guests are required to wear a face mask while in the indoor "
           "community spaces of the hotel, including the lobby. You must wear a mask to enter our building. If you do not"
           " bring a mask, you may purchase a mask at check in. Employees are required to wear a mask at all times. Face"
           " masks, hand sanitizer, and COVID-19 information are available.")

    add_li(
        "Health checks: All staff have received extensive training on COVID-19 mitigation and are monitored for health "
        "conditions before starting each shift. Guests are required to confirm that they are not ill, do not have a "
        "temperature over 100 degrees, and do not have reason to believe they have been exposed to COVID-19.")

    add_li(
        "Enhanced cleaning and operational procedures: Our team uses approved veridical and antibacterial cleaning and"
        " laundry processes to keep you safe.")

    add_li("Daily housekeeping is temporarily suspended. In accordance with our updated COVID-19 related procedures and"
           " policies, no staff will enter your guest room during your stay unless explicitly approved by management. For "
           "stays of 5 nights or longer, we will contact you prior to arrival to discuss extended-stay housekeeping "
           "options.")

    add_li(
        "Early check-ins by appointment only. Due to our stringent and lengthy housekeeping procedures, reduced desk "
        "hours, and limited space for safely storing luggage, early check-ins must be pre-arranged. If you plan to"
        " arrive before 3:00pm, please let us know at least 24 hours in advance so we can indicate if an early check "
        "in is possible.")

    pdf.ln(5)

    add_header("Cancellation and Change Policy")

    pdf.write(5.5,
              "As a small, independent property, we ask for your understanding in respecting our cancellation, change and"
              " no-show policy. Please read carefully. If you must change, shorten or cancel your reservation, do so within "
              "the timeframe indicated below for a full refund minus the specified change/cancellation fee (per room). If a"
              " reservation is cancelled or shortened after the cancellation period expires, the guest is responsible for full"
              " payment of the original reservation unless the room(s) is re-booked. Changes or cancellations must be made via"
              " phone or by email, and you must receive a confirmation email from Thotupola Residence. There are no refunds "
              "for early departure.")

    pdf.ln(12)

    add_header("Cancellation periods and fees")

    pdf.write(5.5,
              "Cancellation should be received 14 days prior to arrival date. In the event of no-show or late cancellation"
              " within 14 days, the value of the entire stay will be charged.")
    pdf.ln(10)

    add_header("Child Policies")

    add_li("FOC for children under 5 years and below.")
    add_li("Children between 6 to 11 years will be charged Rs.2500 of the room rate.")
    add_li("Children 12 years and above are considered as an adult & will be charged the full rate.")

    pdf.ln(5)

    add_header("Driver Accommodation")

    pdf.write(5.5,
              "Moving forward, we want be able to provide driver accommodations with respect to the current situation.")

    pdf.ln(6)

    pdf_footer()

    pdf.output(f"{env.dirname}/policies.pdf")
