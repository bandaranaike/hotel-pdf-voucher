import json


def run(cursor, connection):
    booking_confirmation_form_items = [
        {
            "hash": "booking_confirm_date",
            "label": "Booking Confirmed Date",
            "type": "date"
        },
        {
            "hash": "tr_ref_no",
            "label": "TR Reference Number",
            "type": "text"
        },
        {
            "hash": "tour_number",
            "label": "Tour Number",
            "type": "text"
        },
        {
            "hash": "checking_date",
            "label": "Checking Date",
            "type": "date"
        },
        {
            "hash": "checkout_date",
            "label": "Checkout Date",
            "type": "date"
        },
        {
            "hash": "guest_name",
            "label": "Guest Name",
            "type": "text"
        },
        {
            "hash": "nationality",
            "label": "Nationality",
            "type": "text",
        },
        {
            "hash": "rate_per_night",
            "label": "Rate per Night",
            "type": "text"
        },
        {
            "hash": "ro",
            "label": "Room Only",
            "type": "dropdown",
            "options": {"Yes", "No"}
        },
        {
            "hash": "bb",
            "label": "Bed and Breakfast",
            "type": "dropdown",
            "options": {"Yes", "No"}
        },
        {
            "hash": "hb",
            "label": "Half Board",
            "type": "dropdown",
            "options": {"Yes", "No"}
        },
        {
            "hash": "fb",
            "label": "Full Board",
            "type": "dropdown",
            "options": {"Yes", "No"}
        },
        {
            "hash": "adults",
            "label": "Number of Adults",
            "type": "text",
            "accepts": "number"
        },
        {
            "hash": "kids",
            "label": "Number of Kids",
            "type": "text",
            "accepts": "number"
        },
        {
            "hash": "baby",
            "label": "Number of Babies",
            "type": "text",
            "accepts": "number"
        },
        {
            "hash": "room_category",
            "label": "Room Category",
            "type": "text"
        },
        {
            "hash": "single",
            "label": "Number of Single Rooms",
            "type": "text",
            "accepts": "number"
        },
        {
            "hash": "double",
            "label": "Number of Double Rooms",
            "type": "text",
            "accepts": "number"
        },
        {
            "hash": "triple",
            "label": "Number of Triple Rooms",
            "type": "text",
            "accepts": "number"
        },
        {
            "hash": "quad",
            "label": "Number of Quad Rooms",
            "type": "text",
            "accepts": "number"
        },
        {
            "hash": "family",
            "label": "Number of Family Rooms",
            "type": "text",
            "accepts": "number"
        },
        {
            "hash": "cooking_demo",
            "label": "Cooking Demo",
            "type": "dropdown",
            "options": {"Yes", "No"}
        },
        {
            "hash": "market_visit",
            "label": "Market Visit",
            "type": "dropdown",
            "options": {"Yes", "No"}
        },
        {
            "hash": "driver_accommodation",
            "label": "  Driver Accommodation Required",
            "type": "dropdown",
            "options": {"Yes", "No"}
        },
        {
            "hash": "travel_agent",
            "label": "Travel Agent",
            "type": "text"
        },
        {
            "hash": "remark",
            "label": "Remark",
            "type": "textarea"
        }
    ]
    print(type(booking_confirmation_form_items))
    structure = json.dumps(list(booking_confirmation_form_items))

    cursor.execute(
        f"INSERT INTO form_values (structure, status, id, hash) VALUES  ('{structure}',1,1,'booking-confirmation')")

    connection.commit()


print("form seeder ran")
