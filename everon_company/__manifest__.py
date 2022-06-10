# -*- coding: utf-8 -*-
{
    'name': "everon_company",

    'summary': """
        Matchea pagos de clientes con facturas""",

    'description': """
        Extiende y agrega numero de comercio en Empresa
    """,

    'author': "Devoogroup",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'payment'],

    # always loaded
    'data': [
        'views/everon_company_view.xml',
    ],
}
