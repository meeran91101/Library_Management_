# Copyright (c) 2025, Meeran and contributors

import frappe
from frappe import _
 
def execute(filters=None):
    columns = get_columns()
    data = get_values(filters or {})

    # Breakdown of counts
    status_counts = {
        "Booking": 0,
        "Vacating": 0
    }
    type_counts = {
        "A/C": 0,
        "NON A/C": 0
    }

    for row in data:
        status = row.get("status")
        room_type = row.get("type")
        if status in status_counts:
            status_counts[status] += 1
        if room_type in type_counts:
            type_counts[room_type] += 1

    labels = ["Booking", "Vacating", "A/C", "NON A/C"]

    chart = {
        "data": {
            "labels": labels,
            "datasets": [
                {
                    "name": "Status",
                    "values": [
                        status_counts["Booking"],
                        status_counts["Vacating"],
                        0,
                        0
                    ]
                },
                {
                    "name": "Room Type",
                    "values": [
                        0,
                        0,
                        type_counts["A/C"],
                        type_counts["NON A/C"]
                    ]
                }
            ]
        },
        "type": "bar",
        "height": 300
    }

    return columns, data, None, chart


def get_columns():
    columns = [
        { 
                'fieldname': 'name1',
                'label': _('Name'),
                'fieldtype': 'Data',
                'width':150,
            },
 
            {
                'fieldname': 'mobile_number',
                'label': _('Mobile Number'),
                'fieldtype': 'Data',
                'width':150,
            },  
 
            {
                'fieldname': 'aadhar_number',
                'label': _('Aadhar Number'),
                'fieldtype': 'Data',
                'width':150,
            },
			 {
                'fieldname': 'nationality',
                'label': _('Nationality'),
                'fieldtype': 'Select',
                'options': ['', 'IND'],
                'width':150,
            },
			{ 
                'fieldname': 'city',
                'label': _('City'),
                'fieldtype': 'Data',
                'width':150,
            },
 
            {
                'fieldname': 'type',
                'label': _('Type'),
                'fieldtype': 'Select',
                'options': ['', 'A/C','NON A/C'],
                'width':150,

            },  
 
            {
                'fieldname': 'status',
                'label': _('Status'),
                'fieldtype': 'Select',
                'options': ['', 'Booking','Vacating'],
                'width':150,
            },
			 {
                'fieldname': 'amount',
                'label': _('Amount'),
                'fieldtype': 'Data',
                'width':150,
				
            },
			{
                'fieldname': 'custom_paid',
                'label': _('Paid'),
                'fieldtype': 'Check',
                'width':150,
				
            },

    ]
    return columns
 
def get_values(filters):
    conditions = ["1=1"] 

    if filters.get("name1"):
        conditions.append(f"name1 LIKE '%{filters.get('name1')}%'")
    if filters.get("nationality"):
        conditions.append(f"nationality = '{filters.get('nationality')}'")
    if filters.get("city"):
        conditions.append(f"city LIKE '%{filters.get('city')}%'")
    if filters.get("type") == "A/C":
        conditions.append("type LIKE 'A/C%'")
    elif filters.get("type") == "NON A/C":
        conditions.append("type LIKE 'NON A/C%'")
    if filters.get("status"):
        conditions.append(f"status = '{filters.get('status')}'")
    if filters.get("paid"):
        conditions.append(f"paid = '{filters.get('paid')}'")

    condition_str = " AND ".join(conditions)

    query = f"""
        SELECT
            name1,
            mobile_number,
            aadhar_number,
            nationality,
            city,
            type,
            status,
            paid,
            amount
        FROM
            `tabResort Booking`
        WHERE
            {condition_str}
        ORDER BY name1 DESC
    """

    return frappe.db.sql(query, as_dict=True)