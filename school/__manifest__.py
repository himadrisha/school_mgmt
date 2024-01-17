# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'School Management',
    'version': '16.0',
    'summary': 'School Management',
    'sequence': 1,
    'description': """
Invoicing & Payments
====================
managing the affairs of a school. School management means running the school along the desired educational policies. 
It takes into account all aspects of the school 
 and integrates them into a fruitful whole.    """,
    'category': 'School',
    # 'website': 'https://www.odoo.com/app/invoicing',

    'depends': ['base', 'sale', 'product'],
    'data': [
        'security/ir.model.access.csv',
        # 'security/security.xml',

        'views/student.xml',
        'views/department.xml',
        'views/faculty.xml',
        'views/fee.xml',
        'data/contract_data.xml',
        'report/student_fee_report.xml',
        'report/list_student.xml',
        'data/ir_sequence_data.xml',





    ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',



}
