{
    'name': 'Sale Expiration Date Reminder',
    'version': '13',
    'category': 'Sales',
    'license': 'OPL-1',
    'author': 'ERP Technologies',
    'website': 'https://salesexpirationreminder.blogspot.com/2021/07/blog-post.html',
    'maintainer': 'ERP Technologies',
    'summary': 'Sale Expiration Date Reminder',
    'depends': [
        'base',
        'sale_management'
    ],
    'data': [
        'data/validity_due_reminder_email.xml',
		'data/validity_due_reminder_sheduler.xml',
    ],
    'images': ['images/main.png'],
    'installable': True,
    'auto_install': False,
    'price':26,
    'currency':'USD',

}