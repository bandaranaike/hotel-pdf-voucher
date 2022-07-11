from forms.base_form import BaseForm
from pdf_generators.cooking_confirmation import create_pdf

confirmation_form_data = {
    "cc_currency": {
        "label": "Currency",
        "type": "text",
        "default": "USD"
    },
    "cc_cooking_experience_date": {
        "label": "Cooking Experience Date",
        "type": "date"
    },
    "cc_cooking_class_ref_no": {
        "label": "Cooking Class Ref No",
        "type": "text",
        "default": "CCRN#"
    },
    "cc_guest_name": {
        "label": "Guest Name",
        "type": "text",
        "default": ""
    },
    "cc_nationality": {
        "label": "Nationality",
        "type": "text",
        "default": ""
    },
    "cc_rate_per_person": {
        "label": "Rate per person",
        "type": "text",
        "default": ""
    },
    "cc_adults_count": {
        "label": "Number of Adults",
        "type": "text",
        "accepts": "number",
        "default": ""
    },
    "cc_kids_count": {
        "label": "Number of Kids",
        "type": "text",
        "accepts": "number",
        "default": ""
    },
    "cc_babies_count": {
        "label": "Number of Babies",
        "type": "text",
        "accepts": "number",
        "default": ""
    },
    "cc_travel_agent": {
        "label": "Travel Agent",
        "type": "text",
        "default": ""
    },
    "cc_remark": {
        "label": "Remark",
        "type": "text",
        "default": ""
    },
    "cc_total": {
        "label": "Total",
        "type": "text",
        "default": ""
    }
}


def call_form(frame):
    base_form = BaseForm(confirmation_form_data)
    base_form.run_pdf_generator(create_pdf)
    base_form.generate_form(frame)
