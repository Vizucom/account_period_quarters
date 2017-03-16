# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2014- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

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
