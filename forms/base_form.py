import re
from tkinter import *
from pdf_generators.booking_confirmation import create_pdf
from tkcalendar import DateEntry
from execption_handler import run


class BaseForm:
    form_fields = {}
    string_vars = {}
    form_values = []
    form_items = {}

    def __init__(self, form_items):
        self.form_items = form_items

    @staticmethod
    def clean_text(text):
        return re.sub("[^A-Za-z0-9 ]+", '', text)

    def generate_pdf(self):
        for label, form_item in self.form_items.items():
            field_type = form_item.get('type')
            if field_type == "dropdown":
                self.form_values.append(self.string_vars[label].get())
                self.string_vars[label].initialize('')
            elif field_type == "textarea":
                cleaned_text = self.clean_text(self.form_fields[label].get("1.0", END))
                self.form_values.append(cleaned_text)
                self.form_fields[label].delete("1.0", END)
            else:
                accepts = field_type_1 = form_item.get('accepts')
                if accepts and accepts == "number" and self.form_fields[label].get() == "":
                    self.form_values.append(0)
                else:
                    self.form_values.append(self.form_fields[label].get())
                # form_fields[label].delete(0, END)
        run(create_pdf, self.form_values)
        self.form_values.clear()

    # Driver code
    def generate_form(self, form_items):
        self.form_items = form_items
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

        for label, form_item in self.form_items.items():
            field_type = form_item.get('type')
            Label(root, text=form_item.get("label") + " :  ", anchor='se').grid(row=row, column=0, sticky="E")
            if field_type == "date":
                self.form_fields[label] = DateEntry(root, selectmode='day', date_pattern='yyyy-MM-dd')
            elif field_type == "textarea":
                self.form_fields[label] = Text(root, width=15, height=4)
            elif field_type == "dropdown":
                self.string_vars[label] = StringVar(root)
                self.form_fields[label] = OptionMenu(root, self.string_vars[label], *form_item.get('options'))
            elif field_type == "text":
                self.form_fields[label] = Entry(root)

            self.form_fields[label].bind("<Return>", self.form_fields[label].focus_set())
            self.form_fields[label].grid(row=row, column=1, ipadx=120, sticky="W")
            # if label == "booking_number":
            #     self.form_fields[label].insert(END, "BK#")
            row = row + 1

        # create a Submit Button and place into the root window
        submit = Button(root, text="Create the Confirmation Voucher", fg="White", bg="Green",
                        command=self.generate_pdf)
        submit.grid(row=row, column=1)

        # start the GUI
        root.mainloop()


print("base_form ran")
