{
    'name': "Module 01", # name module
    'version': '1.0', # version by module
    'depends': ['base'],
    'author': "Mr. Null", # name creater 
    'category': 'Category', 
    'description': """
    Test Create Module 01 
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        #'demo/demo_data.xml',
    ],
}