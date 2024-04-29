# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'project_custom',
    'version': '1.0',
    'summary': "Project custom module",
    'sequence': 15,
    'author': "anand",
    'description': """
Project Custom module
""",
    'category': 'Custom/Project',
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': ['mail', 'project', 'project_team'],
    'data': [
        'security/ir.model.access.csv',
        'views/project_custom_view.xml',
        'wizard/project_custom_pdf_wizard.xml',
        'reports/ir_actions_report.xml',
        'reports/project_custom.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
