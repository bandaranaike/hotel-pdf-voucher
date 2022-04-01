from pdf_template import *

pdf_header("Cooking Class Rate Sheet")



pdf.multi_cell(120, line_height, " Cookery Demonstration with Meal (Per Person) ", ln=3, border=1)
pdf.multi_cell(70, line_height, " LKR 5500 ", ln=1, border=1)

pdf.multi_cell(120, line_height, " Market Visit Per Tuk ", ln=3, border=1)
pdf.multi_cell(70, line_height, " LKR 1500 ", ln=1, border=1)

pdf.multi_cell(120, line_height, " Children Below 6 years ", ln=3, border=1)
pdf.multi_cell(70, line_height, " Free of Charge ", ln=1, border=1)

pdf.multi_cell(120, line_height, " Children Between 6 12 years ", ln=3, border=1)
pdf.multi_cell(70, line_height, " LKR 2750 ", ln=1, border=1)

pdf.multi_cell(120, line_height, " Children Above 12 years ", ln=3, border=1)
pdf.multi_cell(70, line_height, " Considered as an adult ", ln=1, border=1)

pdf_footer()

pdf.output("../cooking_class.pdf")
