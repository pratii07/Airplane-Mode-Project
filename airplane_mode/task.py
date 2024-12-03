import frappe

def log_cron_message():
    """
    A simple task to log a message into the system log daily.
    """
    frappe.log("Hello from Cron! This is a daily task.")
    frappe.log_error("Cron Job Not Executed")
