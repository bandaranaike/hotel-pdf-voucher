# import tkinter module
import re
from tkinter import *
from main import create_pdf
from tkcalendar import DateEntry

# Creating Labels
form_items = {
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
        "type": "dropdown",
        "options": {"Sri Lankan", "French", "Australia", "America"}
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
        "label": "Bed adn Breakfast",
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

form_fields = {}
string_vars = {}
form_values = []


def clean_text(text):
    return re.sub("[^A-Za-z0-9 ]+", '', text)


def generate_pdf():
    for label_1, form_item_1 in form_items.items():
        field_type_1 = form_item_1.get('type')
        if field_type_1 == "dropdown":
            form_values.append(string_vars[label_1].get())
            string_vars[label_1].initialize('')
        elif field_type_1 == "textarea":
            cleaned_text = clean_text(form_fields[label_1].get("1.0", END))
            form_values.append(cleaned_text)
            form_fields[label_1].delete("1.0", END)
        else:
            accepts = field_type_1 = form_item_1.get('accepts')
            if accepts and accepts == "number" and form_fields[label_1].get() == "":
                form_values.append(0)
            else:
                form_values.append(form_fields[label_1].get())
            # form_fields[label_1].delete(0, END)
    create_pdf(form_values)
    form_values.clear()


# Driver code
if __name__ == "__main__":
    # create a GUI window
    root = Tk()

    # set the background colour of GUI window
    root.configure(background='#efefef')

    # set the title of GUI window
    root.title("Booking Confirmation Voucher")

    # set the configuration of GUI window
    root.geometry("700x900")

    # create a Form label
    heading = Label(root, text="Fill the Form")
    heading.grid(row=0, column=1)

    row = 1

    for label, form_item in form_items.items():
        field_type = form_item.get('type')
        Label(root, text=form_item.get("label") + " :  ", anchor='se').grid(row=row, column=0, sticky="E")
        if field_type == "date":
            form_fields[label] = DateEntry(root, selectmode='day', date_pattern='yyyy-MM-dd')
        elif field_type == "textarea":
            form_fields[label] = Text(root, width=15, height=4)
        elif field_type == "dropdown":
            string_vars[label] = StringVar(root)
            form_fields[label] = OptionMenu(root, string_vars[label], *form_item.get('options'))
        elif field_type == "text":
            form_fields[label] = Entry(root)
        form_fields[label].config(validate='focusout')
        form_fields[label].bind("<Return>", form_fields[label].focus_set())
        form_fields[label].grid(row=row, column=1, ipadx=120, sticky="W")
        # if label == "booking_number":
        #     form_fields[label].insert(END, "BK#")
        row = row + 1

    # create a Submit Button and place into the root window
    submit = Button(root, text="Create the Confirmation Voucher", fg="White", bg="Green", command=generate_pdf)
    submit.grid(row=row, column=1)

    # start the GUI
    root.mainloop()
