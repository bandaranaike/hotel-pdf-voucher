import tkinter as tk
from tkinter import ttk
import forms.booking_confirmation_form as confirmation_form
import forms.cooking_confirmation_form as cooking_confirmation_form
import forms.cooking_class_form as cooking_form
import forms.rate_sheet_form as rate_form
from forms.policies_form import PolicyForm

root = tk.Tk()
root.title("Thotupola PDF Generator")
tab_controller = ttk.Notebook(root, width=900, height=700)

confirmation_voucher_tab = ttk.Frame(tab_controller)
cooking_class_voucher_tab = ttk.Frame(tab_controller)
rate_sheet_tab = ttk.Frame(tab_controller)
cooking_class_tab = ttk.Frame(tab_controller)
policies_tab = ttk.Frame(tab_controller)

# Confirmation voucher
tab_controller.add(confirmation_voucher_tab, text="  Confirmation Voucher  ")
confirmation_form.call_form(confirmation_voucher_tab)

# Cooking class voucher
tab_controller.add(cooking_class_voucher_tab, text="  Cooking class Voucher  ")
cooking_confirmation_form.call_form(cooking_class_voucher_tab)

# Rate sheet
tab_controller.add(rate_sheet_tab, text="  Rate Sheet  ")
rate_form.call_form(rate_sheet_tab)

# Cooking class
tab_controller.add(cooking_class_tab, text="  Cooking Class  ")
cooking_form.call_form(cooking_class_tab)

# Policies
tab_controller.add(policies_tab, text="  Policies  ")
policy_form = PolicyForm(policies_tab)
policy_form.create_form()

tab_controller.pack(expand=1, fill="both", )

ttk.Label(confirmation_voucher_tab, text="Confirmation Voucher").grid(column=0, row=0, padx=30, pady=30)
ttk.Label(cooking_class_voucher_tab, text="Cooking class Voucher").grid(column=0, row=0, padx=30, pady=30)
ttk.Label(rate_sheet_tab, text="Rate Sheet").grid(column=0, row=0, padx=30, pady=30)
ttk.Label(cooking_class_tab, text="Cooking Class").grid(column=0, row=0, padx=30, pady=30)
ttk.Label(policies_tab, text="Policies").grid(column=0, row=0, padx=30, pady=30)

root.mainloop()
