# -*- coding: utf-8 -*-
{
    "name": 'POS Kitchen Display Food Order Management',
    "summary": """The kitchen screen quickly sends orders to the kitchen 
                and lets cooks see what to make. Cooks can choose 
                what information they see.""",
    "description": """Odoo 17's kitchen screen boosts efficiency by providing
                    real-time order updates and customizable views for kitchen 
                    staff.""",
    "version": "17.0.0.0",
    "author": "KoderXpert Technologies LLP",
    "company": "KoderXpert Technologies LLP",
    "maintainer": "KoderXpert Technologies LLP",
    "website": "https://koderxpert.com",
    "category": "Point Of Sale",
    "depends": ['pos_restaurant'],
    "data": [
        'security/pos_kitchen_screen_groups.xml',
        "security/ir.model.access.csv",
        'data/order_sequence_data.xml',
        "views/kitchen_display_views.xml",
        "views/menu_pos_kitchen_display.xml",
        "views/pos_order_inherit_views.xml",
    ],
    "assets": {
        'point_of_sale._assets_pos': [
            'kx_pos_food_order_management/static/src/js/data_binding.js',
            'kx_pos_food_order_management/static/src/js/order_payment_detail.js',
            'kx_pos_food_order_management/static/src/js/checkout_button.js',
        ],
        'web.assets_backend': [
            'kx_pos_food_order_management/static/src/css/kitchen_screen.css',
            'kx_pos_food_order_management/static/src/js/kitchen_screen.js',
            'kx_pos_food_order_management/static/src/xml/kitchen_management_display_templates.xml',
            'https://code.jquery.com/jquery-1.10.2.min.js',
            'https://unpkg.com/scrollreveal@4.0.0/dist/scrollreveal.min.js',
            'https://fonts.googleapis.com',
            'https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js',
            'https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js',
        ],
    },

    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
    "images":['static/description/pos_kitchen.gif'],
}
