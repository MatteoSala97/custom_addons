{
    'name': 'User Table',
    'version': '1.0',
    'summary': 'A module to create a user table',
    'description': 'This module adds a simple user table with name, email, and username fields.',
    'author': 'Matteo',
    'depends': ['base'],
    'data': [
        'views/user_table_view.xml',
        'security/ir.model.access.csv'        
        ],
    'installable': True,
    'application': True,
}
