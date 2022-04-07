from pdf_generators.plicies import create_pdf
from tkinter import *


class PolicyForm:
    form_items = {}
    form_fields = {}
    frame = None

    def __init__(self, frame):
        self.frame = frame

    def add_new_field(self):
        dynamic_item_count = len(self.form_items)
        self.form_items[f"dynamic_item_{dynamic_item_count}"] = {
            "title": "",
            "text": ""
        }

        self.create_form()

    def create_policy_pdf(self):
        create_pdf(self.form_fields)

    def create_form(self):
        row = 1

        Button(self.frame, text="  + Add extra field  ", fg="White", bg="Orange", command=self.add_new_field).grid(
            row=row, column=1)
        Button(self.frame, text="  Create Policies PDF  ", fg="White", bg="Green", command=self.create_policy_pdf).grid(
            row=row, column=2)
        row = row + 1

        for form_item_index, form_item in self.form_items.items():
            row = row + 1
            Label(self.frame, text="Title", anchor="se", font="Helvetica 9 bold", foreground=form_item.get('color')) \
                .grid(row=row, column=0, columnspan=4, sticky="W")
            self.form_fields[f"{form_item_index}_title"] = Entry(self.frame, width=40)
            self.form_fields[f"{form_item_index}_title"].grid(row=row, column=1, ipadx=40, sticky="W")

            row = row + 1

            Label(self.frame, text="Text", anchor="se", font="Helvetica 9 bold",
                  foreground=form_item.get('color')).grid(
                row=row, column=0, columnspan=4, sticky="W")
            self.form_fields[f"{form_item_index}_text"] = Text(self.frame, width=30, height=3)
            self.form_fields[f"{form_item_index}_text"].grid(row=row, column=1, ipadx=40, sticky="W")
