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
        return res            
