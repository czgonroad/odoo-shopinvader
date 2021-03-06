# -*- coding: utf-8 -*-
# Copyright 2016 Akretion (http://www.akretion.com)
# Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Shopinvader",
    "summary": "Shopinvader",
    "version": "10.0.1.0.0",
    "category": "e-commerce",
    "website": "https://akretion.com",
    "author": "Akretion",
    "license": "AGPL-3",
    "application": True,
    'installable': True,
    "external_dependencies": {
        "python": ['cerberus', 'unidecode'],
        "bin": [],
    },
    "depends": [
        'base_rest',
        'auth_api_key',
        'base_jsonify',
        "base_sparse_field_list_support",
        "base_url",
        "base_vat",
        "connector_base_product",
        "connector_locomotivecms",
        "sale",
        "onchange_helper",
    ],
    "data": [
        'views/shopinvader_variant_view.xml',
        'views/shopinvader_category_view.xml',
        'views/shopinvader_cart_step_view.xml',
        'views/shopinvader_partner_view.xml',
        'wizards/shopinvader_variant_unbinding_wizard.xml',
        'wizards/shopinvader_variant_binding_wizard.xml',
        'views/product_view.xml',
        'views/backend_view.xml',
        'views/partner_view.xml',
        'views/product_category_view.xml',
        'views/sale_view.xml',
        'security/ir.model.access.csv',
        "data/res_partner.xml",
        "data/ir_export_product.xml",
        "data/ir_export_category.xml",
        "data/cart_step.xml",
    ],
    "demo": [
        "demo/auth_api_key_demo.xml",
        "demo/account_demo.xml",
        "demo/pricelist_demo.xml",
        "demo/backend_demo.xml",
        "demo/partner_demo.xml",
        "demo/sale_demo.xml",
        "demo/email_demo.xml",
        "demo/notification_demo.xml",
    ],
    "qweb": [
    ]
}
