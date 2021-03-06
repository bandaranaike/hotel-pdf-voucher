from pdf_generators.pdf_template import *
import env


def create_pdf(data):
    # [] = data

    pdf = pdf_header(title="Summer Rate Sheet")

    price_items = {
        "suit": {
            "name": "Suit with A/C",
            "rooms": ["d", "t"],
            "color": [224, 155, 62]
        },
        "supper-deluxe": {
            "name": "Super Deluxe with A/C",
            "rooms": ["s", "d", "t"],
            "color": [62, 108, 174]
        },
        "standard": {
            "name": "Standard room with A/C",
            "rooms": ["s", "d"],
            "color": [197, 94, 53]
        },
        "tree-house": {
            "name": "Tree House",
            "rooms": ["s", "d"],
            "color": [51, 110, 139]
        },
        "suit-cottage": {
            "name": "Suite cottage with A/C",
            "rooms": ["d", "t", "q"],
            "color": [71, 60, 58]
        },
        "family": {
            "name": "Family suite with river view and A/C",
            "rooms": ["d", "t", "q"],
            "color": [139, 121, 109]
        }
    }

    meal_plans = ["BB", "HB", "FB"]

    room_names = {
        "s": "Single",
        "d": "Double",
        "t": "Triple",
        "q": "Quaternary"
    }

    pdf.set_fill_color(240, 240, 240)
    pdf.set_text_color(70, 70, 70)
    pdf.multi_cell(55, line_height, " Room Type ", border=1, ln=3, fill=True)
    for meal_plan in meal_plans:
        pdf.multi_cell(45, line_height, f" {meal_plan} ", border=1, ln=3, align="C", fill=True)
    pdf.ln(line_height)

    for price_item_index, price_item in price_items.items():
        color = price_item.get("color")
        pdf.set_text_color(255, 255, 255)
        pdf.set_fill_color(color[0], color[1], color[2])
        pdf.set_draw_color(color[0], color[1], color[2])
        pdf.multi_cell(0, line_height, f" {price_item.get('name')} ", border=1, ln=1, fill=True)
        pdf.set_text_color(27, 39, 51)
        pdf.set_fill_color(255, 255, 255)
        pdf.set_draw_color(220, 220, 220)
        for room_abb in price_item.get("rooms"):
            pdf.multi_cell(55, line_height, f" {room_names[room_abb]} ", border=1, ln=3)
            for meal_plan in meal_plans:
                price = data[price_item_index][room_abb][meal_plan].get()
                if price:
                    price_str = f" {data['currency'].get()} {price} "
                else:
                    price_str = " - "
                pdf.multi_cell(45, line_height, price_str, border=1, ln=3, align="C")
            pdf.ln()

    pdf.ln(4)

    if len(data['special_note'].get('1.0', 'end-1c')) != 0:
        pdf.multi_cell(0, line_height / 1.5, f"{data['special_note'].get('1.0', 'end')} ", border=0, ln=1)

    pdf_footer(pdf)

    pdf_output(pdf, "summer-rate-sheet")
