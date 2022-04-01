from pdf_template import *

pdf_header(title="Summer Rate Sheet")

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
            pdf.multi_cell(45, line_height, f" {meal_plan} ", border=1, ln=3, align="C")
        pdf.ln()

pdf_footer()

pdf.output("../summer-rate-sheet.pdf")

#
# def rates(title, triple="", double="", single=""):
#
