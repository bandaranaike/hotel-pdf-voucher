from forms.base_form import BaseForm
from pdf_generators.booking_confirmation import create_pdf

confirmation_form_data = {
    "currency": {
        "label": "Currency",
        "type": "text",
        "default": "USD"
    },
    "booking_confirm_date": {
        "label": "Booking Confirmed Date",
        "type": "date"
    },
    "tr_ref_no": {
        "label": "TR Reference Number",
        "type": "text",
        "default": "TRN#"
    },
    "tour_number": {
        "label": "Tour Number",
        "type": "text",
        "default": "TN#"
    },
    "checking_date": {
        "label": "Checking Date",
        "type": "date"
    },
    "checkout_date": {
        "label": "Checkout Date",
        "type": "date"
    },
    "guest_name": {
        "label": "Guest Name",
        "type": "text"
    },
    "nationality": {
        "label": "Nationality",
        "type": "text",
    },
    "rate_per_night": {
        "label": "Rate per Night",
        "type": "text",
        "default": ""
    },
    "ro": {
        "label": "Room Only",
        "type": "dropdown",
        "options": {"Yes", "No"},
        "default": "No"
    },
    "bb": {
        "label": "Bed and Breakfast",
        "type": "dropdown",
        "options": {"Yes", "No"},
        "default": "No"
    },
    "hb": {
        "label": "Half Board",
        "type": "dropdown",
        "options": {"Yes", "No"},
        "default": "No"
    },
    "fb": {
        "label": "Full Board",
        "type": "dropdown",
        "options": {"Yes", "No"},
        "default": "No"
    },
    "adults": {
        "label": "Number of Adults",
        "type": "text",
        "accepts": "number"
    },
    "kids": {
        "label": "Number of Kids",
        "type": "text",
        "accepts": "number"
    },
    "baby": {
        "label": "Number of Babies",
        "type": "text",
        "accepts": "number"
    },
    "room_category": {
        "label": "Room Category",
        "type": "text"
    },
    "single": {
        "label": "Number of Single Rooms",
        "type": "text",
        "accepts": "number"
    },
    "double": {
        "label": "Number of Double Rooms",
        "type": "text",
        "accepts": "number"
    },
    "triple": {
        "label": "Number of Triple Rooms",
        "type": "text",
        "accepts": "number"
    },
    "quad": {
        "label": "Number of Quad Rooms",
        "type": "text",
        "accepts": "number"
    },
    "family": {
        "label": "Number of Family Rooms",
        "type": "text",
        "accepts": "number"
    },
    "cooking_demo": {
        "label": "Cooking Demo",
        "type": "dropdown",
        "options": {"Yes", "No"},
        "default": "No"
    },
    "cooking_demo_rate": {
        "label": "Cooking Demo Rate",
        "type": "text",
        "accepts": "number"
    },
    "market_visit": {
        "label": "Market Visit",
        "type": "dropdown",
        "options": {"Yes", "No"},
        "default": "No"
    },
    "total_cost": {
        "label": "Total Cost",
        "type": "text"
    },
    "travel_agent": {
        "label": "Travel Agent",
        "type": "text"
    },
    "remarks": {
        "label": "Remark",
        "type": "text",
        "default": ""
    }
}


def call_form(frame):
    base_form = BaseForm(confirmation_form_data)
    base_form.run_pdf_generator(create_pdf)
    base_form.generate_form(frame)
