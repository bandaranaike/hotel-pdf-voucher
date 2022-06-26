from forms.base_form import BaseForm
from pdf_generators.cooking_class import create_pdf

form_data = {
    "currency": {
        "label": "Currency",
        "type": "text",
        "default": "USD"
    },
    "cooking_demonstration": {
        "label": "Cookery Demonstration with Meal (Per Person)",
        "type": "text",
        "default": ""
    },
    "market_visit": {
        "label": "Market Visit Per Tuk",
        "type": "text",
        "default": ""
    },
    "below_6": {
        "label": "Children Below 6 years",
        "type": "text",
        "default": "Free of Charge"
    },
    "between_6_12": {
        "label": "Children Between 6 12 years",
        "type": "text",
        "default": ""
    },
    "above_12": {
        "label": "Children Above 12 years",
        "type": "text",
        "default": "Considered as an adult"
    }
}


def call_form(frame):
    base_form = BaseForm(form_data)
    base_form.run_pdf_generator(create_pdf)
    base_form.generate_form(frame)
