# import tkinter module
from tkinter import *
from main import create_pdf
from tkcalendar import DateEntry

# Creating Labels
labels = ["Booking Confirmed Date", "Booking Number", "Guest Name", "Guest Family Name", "Nationality",
          "Rate per Night",
          "Meal Plan", "Adults 18+", "Teens 12-17", "Kids 5-11", "Baby 0-5", "Checking Date", "Checkout Date",
          "Number of Delux Rooms", "Number of River View Rooms", "Driver Accommodation Required"]
form_fields = {}
form_values = []


def generate_pdf():
    for label_1 in labels:
        form_values.append(form_fields[label_1].get())
        form_fields[label_1].delete(0, END)
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
    root.geometry("600x400")

    # create a Form label
    heading = Label(root, text="Fill the Form")
    heading.grid(row=0, column=1)

    row = 1

    for label in labels:
        Label(root, text=label, anchor='se').grid(row=row, column=0)
        if label == "Checking Date" or label == "Checkout Date" or label == "Booking Confirmed Date":
            form_fields[label] = DateEntry(root, selectmode='day', date_pattern='yyyy-MM-dd')
        else:
            form_fields[label] = Entry(root)
        form_fields[label].bind("<Return>", form_fields[label].focus_set())
        form_fields[label].grid(row=row, column=1, ipadx=100)
        row = row + 1

    # create a Submit Button and place into the root window
    submit = Button(root, text="Create the Confirmation Voucher", fg="White", bg="Blue", command=generate_pdf)
    submit.grid(row=row, column=1)

    # start the GUI
    root.mainloop()
