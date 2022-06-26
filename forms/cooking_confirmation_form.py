from forms.base_form import BaseForm
from pdf_generators.cooking_confirmation import create_pdf

confirmation_form_data = {
    "currency": {
        "label": "Currency",
        "type": "text",
        "default": "USD"
    },
    "cooking_experience_date": {
        "label": "Cooking Experience Date",
        "type": "date"
    },
    "cooking_class_ref_no": {
        "label": "Cooking Class Ref No",
        "type": "text",
        "default": "CCRN#"
    },
    "guest_name": {
        "label": "Guest Name",
        "type": "text",
        "default": ""
    },
    "nationality": {
        "label": "Nationality",
        "type": "text",
        "default": ""
    },
    "rate_per_person": {
        "label": "Rate per person",
        "type": "text",
        "default": ""
    },
    "adults_count": {
        "label": "Number of Adults",
        "type": "text",
        "accepts": "number",
        "default": ""
    },
    "kids_count": {
        "label": "Number of Kids",
        "type": "text",
        "accepts": "number",
        "default": ""
    },
    "babies_count": {
        "label": "Number of Babies",
        "type": "text",
        "accepts": "number",
        "default": ""
    },
    "travel_agent": {
        "label": "Travel Agent",
        "type": "text",
        "default": ""
    },
    "remark": {
        "label": "Remark",
        "type": "textarea",
        "default": ""
    }
}


def call_form(frame):
    base_form = BaseForm(confirmation_form_data)
    base_form.run_pdf_generator(create_pdf)
    base_form.generate_form(frame)
