# -*- coding: utf-8 -*-
{
    'name': '銷售訂單日期編輯',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'summary': '允許使用者編輯銷售訂單日期',
    'description': '''
        odoo17銷售訂單日期編輯模組
        ==================
        
        允許具有特定權限的使用者編輯銷售訂單日期，
        包括已確認的訂單，便於導入舊資料。
        
        功能：
        • 編輯銷售訂單日期
        • 權限控制管理  
        • 支援已確認訂單編輯
        • 自動變更記錄追蹤

    ''',
    'author': 'Roy',
    'website': 'https://rdfarm.net',
    'depends': ['sale'],
    'data': [
        'security/sale_security.xml',
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
