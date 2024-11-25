# Copyright (c) 2024, PAS and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ShopConfigurations(Document):
	def before_save(self):
		if self.rent_amount == 0:
			self.rent_amount = self.default_rent_amount

             
