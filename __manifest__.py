{
    'name': 'Confirmación de Credito',
    'version': '1.0',
    'category': 'Accounting',
    'description': """
        Modulo para la confrimación de pago de los creditos
    """,
    'author': 'Your Name',
    'depends': ['base', 'account'],  
    'data': [
        'views/credit_view.xml', 
    ],
    
    'installable': True,
    'application': True,
}
