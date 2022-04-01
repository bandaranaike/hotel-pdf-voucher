import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Thotupola PDF Generator")
tabController = ttk.Notebook(root, width=800, height=700)

rateSheetTab = ttk.Frame(tabController)
policiesTab = ttk.Frame(tabController)

tabController.add(rateSheetTab, text="  Rate Sheet  ")
tabController.add(policiesTab, text="  Policies  ")
tabController.pack(expand=1, fill="both",)

ttk.Label(rateSheetTab, text="Rate Sheet tab").grid(column=0, row=0, padx=30, pady=30)
ttk.Label(policiesTab, text="Policies tab").grid(column=0, row=0, padx=30, pady=30)

root.mainloop()
