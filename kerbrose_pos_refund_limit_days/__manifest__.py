{
    'name': "POS Refund Days",
    'summary': "return allowance",
    'description': """
        number of days to allow returns
    """,
    'author': 'Khaled Said',
    "website": "https://kerbrose.github.io/",
    'category': 'Sales/Point of Sale',
    'version': '17.0.0.0.1',
    'depends': [
        'base',
        'point_of_sale',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'kerbrose/static/src/js/ticket_screen.js',
        ],
    },
    'data': [
        'views/res_config_settings.xml',
    ],
    'demo': [],
    'images':['static/description/icon.png'],
    "license": "LGPL-3",
    "currency ": "USD",
    "price": 13,
}
