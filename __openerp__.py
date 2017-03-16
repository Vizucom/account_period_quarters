# -*- coding: utf-8 -*-
{
    'name': 'Account Period Quarters',
    'author': 'Vizucom Oy',
    'website': '',
    # Categories can be used to filter modules in module listing
    'category': 'Account',
    'version': '0.1',
    # Any module necessary for this one to work correctly
    'depends': ['account'],
    'data': [
        # security/ir.model.access.csv,
        'views/period.xml',
        # data/
    ],
    'description': """
* Adds yearly quarter attribute to period object.
    """,
}
