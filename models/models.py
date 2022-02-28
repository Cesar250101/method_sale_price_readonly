# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order.line'

    price_unit_readonly = fields.Float(string='Precio Unitario',compute="_compute_price_unit_readonly")

    @api.depends('price_unit')
    def _compute_price_unit_readonly(self):
        self.price_unit_readonly=self.price_unit
    
    