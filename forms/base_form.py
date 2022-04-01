import re
from tkinter import *
from pdf_generators.booking_confirmation import create_pdf
from tkcalendar import DateEntry
from execption_handler import run

form_fields = {}
string_vars = {}
form_values = []


def clean_text(text):
    return re.sub("[^A-Za-z0-9 ]+", '', text)


def generate_pdf(form_items):
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
    run(create_pdf, form_values)
    form_values.clear()


# Driver code
def generate_form(form_items):
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
