{
    'name': 'Motorbike Registration',
    'version': '1.0',
    'category': 'Management',
    'summary': 'Module for registering motorbikes and customers',
    'license': 'LGPL-3', 
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/motorbike_views.xml',
        'views/customer_views.xml',
    ],
    'installable': True,
    'application': True,
}
