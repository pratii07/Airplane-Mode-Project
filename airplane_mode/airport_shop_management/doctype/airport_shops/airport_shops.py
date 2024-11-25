# Copyright (c) 2024, PAS and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
# from frappe.model.document import Document


class AirportShops(WebsiteGenerator):
    def before_save(self):
        if self.rent_amount == 0:

            default_rent_amount = frappe.db.get_single_value("Shop Configurations", "default_rent_amount")
            
            if default_rent_amount:
                self.rent_amount = default_rent_amount



# import frappe

# def get_context(context):
#     # Get the document name from the route parameter
#     docname = frappe.form_dict.get("docname")
#     if not docname:
#         frappe.throw("Document not found")
#     # Fetch the specific document
#     context.doc = frappe.get_doc("Airport Shops", docname)
#     return context
