// Copyright (c) 2025, Meeran and contributors
// For license information, please see license.txt

frappe.query_reports["Resort Booking Report"] = {
	"filters": [
		{ 
                'fieldname': 'name1',
                'label': __('Name'),
                'fieldtype': 'Data',
            },
 
            {
                'fieldname': 'mobile_number',
                'label': __('Mobile Number'),
                'fieldtype': 'Data',
            },  
 
            {
                'fieldname': 'aadhar_number',
                'label': __('Aadhar Number'),
                'fieldtype': 'Data',
            },
			 {
                'fieldname': 'nationality',
                'label': __('Nationality'),
                'fieldtype': 'Select',
                'options': ['', 'IND'],
            },
			{ 
                'fieldname': 'city',
                'label': __('City'),
                'fieldtype': 'Data',
            },
 
            {
                'fieldname': 'type',
                'label': __('Type'),
                'fieldtype': 'Select',
                'options': ['', 'A/C','NON A/C'],

            },  
 
            {
                'fieldname': 'status',
                'label': __('Status'),
                'fieldtype': 'Select',
                'options': ['', 'Booking','Vacating'],
            },
			 {
                'fieldname': 'amount',
                'label': __('Amount'),
                'fieldtype': 'Data',
				
            },
			{
                'fieldname': 'custom_paid',
                'label': __('Paid'),
                'fieldtype': 'Check',
				
            },

	]
};
