// Copyright (c) 2024, PAS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        // Check if the website field is not empty
        if (frm.doc.website) {
            // Add the website link using frm.add_web_link
            frm.add_web_link(frm.doc.website,"Visit Website");
        }
    }
});

