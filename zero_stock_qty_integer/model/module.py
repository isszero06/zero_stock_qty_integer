# -*- coding: utf-8 -*-
#################################################################################
# Author      : Zero For Information Systems (<www.erpzero.com>)
# Copyright(c): 2016-Zero For Information Systems
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################


from collections import defaultdict

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools import float_is_zero, float_round, float_compare, OrderedSet

import logging
_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = "product.template"


    is_int = fields.Boolean(string="Stock move must integer number?",default=True)

class StockMove(models.Model):
    _inherit = 'stock.move'

    def _action_done(self, cancel_backorder=False):
        res = super(StockMove, self)._action_done(cancel_backorder=cancel_backorder)
        for move in self:
            quantity_int = (int(float_round(move.quantity, precision_digits=0,precision_rounding=1, rounding_method='DOWN')))       
            if move.product_id.is_int and move.quantity != quantity_int:
                raise UserError(_('You cannot perform the move of Quantity Not Integer!.(Product: %s)', move.name))
        for move_line in self.move_line_ids:
            move_line._qty_integer_product()
        return res            

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    @api.onchange('quantity','lot_id')
    def _qty_integer_product(self):
        for move_line in self:
            quantity_int = (int(float_round(move_line.quantity, precision_digits=0,precision_rounding=1, rounding_method='DOWN')))       
            if move_line.product_id.is_int and move_line.quantity != quantity_int:
                raise UserError(_('You cannot perform the move of Quantity Not Integer!.(Product: %s)', move_line.product_id.name))
