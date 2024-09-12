# -*- coding: utf-8 -*-
from odoo import api, fields, models


class KxKitchenScreen(models.Model):
    _name = 'kitchen.screen'
    _description = 'Pos Kitchen Display'
    _rec_name = 'sequence'

    def _pos_store_id(self):
        kitchen = self.search([])
        if kitchen:
            return [('module_pos_restaurant', '=', True),
                    (
                    'id', 'not in', [rec.id for rec in kitchen.pos_config_id])]
        else:
            return [('module_pos_restaurant', '=', True)]

    sequence = fields.Char(readonly=True, default='New',
                           copy=False, tracking=True)
    pos_config_id = fields.Many2one('pos.config', string='Authorized POS',
                                    domain=_pos_store_id)
    pos_categ_ids = fields.Many2many('pos.category',
                                     string='Authorized product category')
    store_number = fields.Integer(related='pos_config_id.id', string='Customer')

    def kitchen_screen(self):
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': '/pos/kitchen?pos_config_id= %s' % self.pos_config_id.id,
        }

    @api.model
    def create(self, vals):
        if vals.get('sequence', 'New') == 'New':
            vals['sequence'] = self.env['ir.sequence'].next_by_code(
                'kitchen.screen')
        result = super(KxKitchenScreen, self).create(vals)
        return result
