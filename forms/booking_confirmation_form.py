from base_form import BaseForm

confirmation_form_data = {
    "booking_confirm_date": {
        "label": "Booking Confirmed Date",
        "type": "date"
    },
    "tr_ref_no": {
        "label": "TR Reference Number",
        "type": "text"
    },
    "tour_number": {
        "label": "Tour Number",
        "type": "text"
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
        "type": "text"
    },
    "ro": {
        "label": "Room Only",
        "type": "dropdown",
        "options": {"Yes", "No"}
    },
    "bb": {
        "label": "Bed and Breakfast",
        "type": "dropdown",
        "options": {"Yes", "No"}
    },
    "hb": {
        "label": "Half Board",
        "type": "dropdown",
        "options": {"Yes", "No"}
    },
    "fb": {
        "label": "Full Board",
        "type": "dropdown",
        "options": {"Yes", "No"}
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
        "options": {"Yes", "No"}
    },
    "market_visit": {
        "label": "Market Visit",
        "type": "dropdown",
        "options": {"Yes", "No"}
    },
    "driver_accommodation": {
        "label": "  Driver Accommodation Required",
        "type": "dropdown",
        "options": {"Yes", "No"}
    },
    "travel_agent": {
        "label": "Travel Agent",
        "type": "text"
    },
    "remark": {
        "label": "Remark",
        "type": "textarea"
    }
}

base_form = BaseForm(confirmation_form_data)

base_form.generate_form(confirmation_form_data)
