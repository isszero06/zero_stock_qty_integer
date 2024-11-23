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
from datetime import timedelta
from operator import itemgetter
from re import findall as regex_findall

from odoo import _, api, Command, fields, models
from odoo.exceptions import UserError,ValidationError
from odoo.osv import expression
from odoo.osv.expression import OR
from odoo.tools.float_utils import float_compare, float_is_zero, float_round
from odoo.tools.misc import clean_context, OrderedSet, groupby


class StockMove(models.Model):
    _inherit = 'stock.move'

    quantity_int = fields.Float('Quantity Integer')


    def _action_done(self, cancel_backorder=False):
        res = super(StockMove, self)._action_done(cancel_backorder=cancel_backorder)
        for move in self:
            moves_error = move.quantity_int != move.quantity
            if move.quantity !=0:
                move.quantity_int = (int(float_round(move.quantity, precision_digits=0,precision_rounding=1, rounding_method='DOWN')))
                if moves_error:
                    raise ValidationError(_('You cannot perform the move because the Quantity Not Integer!. (Product Name: %s)', move.product_id.name))
        return res            
