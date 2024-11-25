# Copyright (c) 2024, PAS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AirplaneTicket(Document):
    # def validate(self):
        # t=0
        # for i in self.add_ons:
        #     t += i.amount
        # self.total_amount = self.flight_price + t
        

    def validate(self):
       self.validate_capacity()
       t=0
       for i in self.add_ons:
            t += i.amount
        
       self.total_amount = self.flight_price + t

    def validate_capacity(self):
        # Extract the base airline code from the flight (assuming it is the first part before any hyphen)
        airline_code = self.flight.split('-')[0]

        # Fetch the airplane based on the extracted airline code
        airplane = frappe.db.get_value('Airplane', {'airline': airline_code}, ['capacity', 'airline'], as_dict=True)

        if not airplane:
            frappe.throw(f"Airplane for flight {self.flight} not found.")

        # Count the tickets for this particular flight (linked to the airplane)
        ticket_count = frappe.db.count('Airplane Ticket', {'flight': self.flight})

        # Compare the ticket count with the airplane's capacity
        if ticket_count >= airplane['capacity']:
            frappe.throw(f"Seats are not available for {airplane['airline']} ({self.flight}). Thank you for choosing us!")
