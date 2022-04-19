{

    'name': 'estate',
    'version': '0.1',
    'category': 'Sales/CRM',
    'description': 'Sale and Buy Real Estates',
    'depends': ['base'],
    'author': "Author Name",
    'data': [
        'security/ir.model.access.csv',

        'views/estate_property_views.xml',
        'views/estate_menus.xml',

        'views/property_type_views.xml',
        'views/property_type_menus.xml',

        'views/inherit_user_view.xml'
    ]
}