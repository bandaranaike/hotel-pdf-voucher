import re
from tkinter import *
from tkcalendar import DateEntry
from execption_handler import run


class BaseForm:
    form_fields = {}
    string_vars = {}
    form_values = []
    form_items = {}
    pdf_gen_method = None

    def __init__(self, form_items):
        self.form_items = form_items
        # self.generate_form()

    @staticmethod
    def clean_text(text):
        return re.sub("[^A-Za-z0-9 ]+", '', text)

    def run_pdf_generator(self, pdf_gen_method):
        self.pdf_gen_method = pdf_gen_method

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
                accepts = form_item.get('accepts')
                if accepts and accepts == "number" and self.form_fields[label].get() == "":
                    self.form_values.append(0)
                else:
                    self.form_values.append(self.form_fields[label].get())
                # form_fields[label].delete(0, END)
        run(self.pdf_gen_method, self.form_values)
        self.form_values.clear()

    # Driver code
    def generate_form(self, frame):

        row = 1

        for label, form_item in self.form_items.items():
            field_type = form_item.get('type')
            Label(frame, text=form_item.get("label") + " :  ", anchor='se').grid(row=row, column=0, sticky="E")
            if field_type == "date":
                self.form_fields[label] = DateEntry(frame, selectmode='day', date_pattern='yyyy-MM-dd')
            elif field_type == "textarea":
                self.form_fields[label] = Text(frame, width=15, height=4)
            elif field_type == "dropdown":
                self.string_vars[label] = StringVar(frame)
                self.form_fields[label] = OptionMenu(frame, self.string_vars[label], *form_item.get('options'))
            elif field_type == "text":
                self.form_fields[label] = Entry(frame)

            self.form_fields[label].bind("<Return>", self.form_fields[label].focus_set())
            self.form_fields[label].grid(row=row, column=1, ipadx=120, sticky="W")
            if form_item.get('default'):
                if field_type == "text" or field_type == "textarea":
                    self.form_fields[label].insert(END, form_item.get('default'))
                elif field_type == "dropdown":
                    self.string_vars[label].set(form_item.get('default'))
            row = row + 1

        # create a Submit Button and place into the root window
        submit = Button(frame, text="Create the Confirmation Voucher", fg="White", bg="Green",
                        command=self.generate_pdf)
        submit.grid(row=row, column=1)

