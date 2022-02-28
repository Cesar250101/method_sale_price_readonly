# -*- coding: utf-8 -*-
from odoo import http

# class MethodSalePriceReadonly(http.Controller):
#     @http.route('/method_sale_price_readonly/method_sale_price_readonly/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_sale_price_readonly/method_sale_price_readonly/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_sale_price_readonly.listing', {
#             'root': '/method_sale_price_readonly/method_sale_price_readonly',
#             'objects': http.request.env['method_sale_price_readonly.method_sale_price_readonly'].search([]),
#         })

#     @http.route('/method_sale_price_readonly/method_sale_price_readonly/objects/<model("method_sale_price_readonly.method_sale_price_readonly"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_sale_price_readonly.object', {
#             'object': obj
#         })