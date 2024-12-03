# Copyright (c) 2024, PAS and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
# from frappe.model.document import Document


class AirportShops(WebsiteGenerator):
   def before_save(self):
        
        shop_config = frappe.get_doc("Shop Configurations")

        if self.rent_amount == 0:
            self.rent_amount = shop_config.default_rent_amount
