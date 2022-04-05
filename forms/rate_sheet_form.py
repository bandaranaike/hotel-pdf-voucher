from forms.base_form import BaseForm
from pdf_generators.rate_sheet import create_pdf
from tkinter import *

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

form_fields = dict()


def call_form(frame):
    create_multi_col_form(frame)


def generate_pdf():
    create_pdf(form_fields)


def create_multi_col_form(frame):
    row = 1
    col = 0
    Label(frame, text="Room Type", anchor="se").grid(row=row, column=0, sticky="N")
    for meal_plan in meal_plans:
        col = col + 1
        Label(frame, text=meal_plan, anchor="se").grid(row=row, column=col, sticky="N")

    Label(frame, text=" Currency ").grid(row=row, column=5, sticky="N")
    form_fields['currency'] = Entry(frame, width=3)
    form_fields['currency'].grid(row=row, column=6, ipadx=40, sticky="W")
    form_fields['currency'].insert(END, "USD")

    for price_item_index, price_item in price_items.items():
        row = row + 1
        Label(frame, text=f'   {price_item.get("name")} ', anchor="se", font="Helvetica 9 bold", foreground="#525",
              ).grid(row=row, column=0, columnspan=4,
                     sticky="W")

        if price_item_index not in form_fields:
            form_fields[price_item_index] = {}

        for room_abb in price_item.get("rooms"):
            row = row + 1
            Label(frame, text=room_names[room_abb]).grid(row=row, column=0, sticky="E")

            if room_abb not in form_fields[price_item_index]:
                form_fields[price_item_index][room_abb] = {}

            for meal_plan in meal_plans:
                col = (col % len(meal_plans)) + 1
                form_fields[price_item_index][room_abb][meal_plan] = Entry(frame, width=4)
                form_fields[price_item_index][room_abb][meal_plan].grid(row=row, column=col, ipadx=40, sticky="W")

    row = row + 3
    Button(frame, text="  Create Rate Sheet  ", fg="White", bg="Green", command=generate_pdf).grid(row=row, column=1)
