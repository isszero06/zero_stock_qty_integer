# -*- coding: utf-8 -*-
#################################################################################
# Author      : Zero For Information Systems (<www.erpzero.com>)
# Copyright(c): 2016-Zero For Information Systems
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################

{
    "name": "Stock Move Quantity Must Integer",
    'version': '7.0.5',
    'category': 'Warehouse',
    "author": 'Zero Systems',
    "company": 'Zero for Information Systems',
    "website": "https://www.erpzero.com",
    'live_test_url': 'https://youtu.be/bnf1K0Fgndw',
    "email": "sales@erpzero.com",
    "sequence": 0,
    'license': 'OPL-1',
    "summary": "Stock Move Quntity Must Integer.",
    "data": [
        "views/view.xml",
         ],
    "depends": ['stock'],
    "price": 1.0,
    "currency": 'EUR',
    'installable': True,
    'auto_install': False,
    "application": True,
    'images': ['static/description/integer.jpg'],
    'pre_init_hook': 'pre_init_check',
}
