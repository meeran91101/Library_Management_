# Copyright (c) 2025, Meeran and contributors
# For license information, please see license.txt

# import frappe


import frappe
from frappe import _
 
 
def execute(filters=None):
    columns, data = get_columns(), get_values(filters or {})
    return columns, data
   
def get_columns():
    columns = [
        {
            'fieldname': 'article',
            'fieldtype': 'Link',
            'label': _('Article'),
            'options': 'Article',
        },
 
        {
            'fieldname': 'library_member',
            'fieldtype': 'Link',
            'label': _('Library Member'),
            'options': 'Library Member',
        },
 
        {
            "fieldname": "type",
            "label": _("Type"),
            "fieldtype": "Data",
        },
        {
            "fieldname": "date",
            "label": _("Date"),
            "fieldtype": "Date",
        },
		 {
            "fieldname": "from_date",
            "label": _("Membership From Date"),
            "fieldtype": "Date",
        },
		{
            "fieldname": "to_date",
            "label": _("Membership To Date"),
            "fieldtype": "Date",
        }
    ]
    return columns
 
def get_values(filters):
    condition = "1=1"
    if filters.get("article"):
        condition += f" AND L.article = '{filters.get('article')}'"
    if filters.get("library_member"):
        condition += f" AND L.library_member = '{filters.get('library_member')}'"
    if filters.get("type"):
        condition += f" AND L.`type` = '{filters.get('type')}'"
    if filters.get("date"):
        condition += f" AND L.date = '{filters.get('date')}'"
    if filters.get("from_date"):
        condition += f" AND LM.from_date >= '{filters.get('from_date')}'"
    if filters.get("to_date"):
        condition += f" AND LM.to_date <= '{filters.get('to_date')}'"

    query = f"""
        SELECT
            L.article,
            L.library_member,
            L.`type`,
            L.date,
            LM.from_date,
            LM.to_date
        FROM
            `tabLibrary Transaction` L
        JOIN
            `tabLibrary Membership` LM
            ON L.library_member = LM.library_member
        WHERE
            {condition}
        ORDER BY L.date DESC
    """

    return frappe.db.sql(query, as_dict=True)