// Copyright (c) 2025, Meeran and contributors
// For license information, please see license.txt


frappe.query_reports["Script Report Library"] = {
        "filters": [
            { 
                'fieldname': 'article',
                'label': __('Article'),
                'fieldtype': 'Link',
                'options': 'Article',
            },
 
            {
                'fieldname': 'library_member',
                'label': __('Library Member'),
                'fieldtype': 'Link',
                'options': 'Library Member',
            },
 
            {
                'fieldname': 'type',
                'label': __('Type'),
                'fieldtype': 'Select',
                'options': ['', 'Issue', 'Return'],
            },
			 {
                'fieldname': 'date',
                'label': __('Date'),
                'fieldtype': 'Date',
           
            },
           
            {
                'fieldname': 'from_date',
                'label': __('Membership From Date'),
                'fieldtype': 'Date',
           
            },
            {
                'fieldname': 'to_date',
                'label': __('Membership To Date'),
                'fieldtype': 'Date',
           
            },
 
        ]
    };