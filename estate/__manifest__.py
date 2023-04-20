# -*- coding: utf-8 -*-
{
    'name': 'Real Estate',
    'version': '1.0',
    'category': 'estate',
    'sequence': 15,
    'depends': [
        'base_setup'
       
    ],
   
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml'
    ],

    'installable': True,
    'application': True,
   
    'license': 'LGPL-3',
}
