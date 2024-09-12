# -*- coding: utf-8 -*-
from odoo import models


class KxPosSessionInherit(models.Model):
    _inherit = 'pos.session'

    def _pos_ui_models_to_load(self):
        result = super()._pos_ui_models_to_load()
        result += {
            'pos.order', 'pos.order.line'
        }
        return result

    def _loader_params_pos_order(self):
        return {'search_params': {
            'domain': [],
            'fields': ['name', 'date_order', 'pos_reference',
                       'partner_id', 'lines', 'order_status', 'order_reference',
                       'is_preparing']}}

    def _get_pos_ui_pos_order(self, params):
        return self.env['pos.order'].search_read(
            **params['search_params'])

    def _loader_params_pos_order_line(self):
        return {'search_params': {'domain': [],
                                  'fields': ['product_id', 'qty',
                                             'order_status', 'order_reference',
                                             'customer_id',
                                             'price_subtotal', 'total_cost']}}

    def _get_pos_ui_pos_order_line(self, params):
        return self.env['pos.order.line'].search_read(
            **params['search_params'])
