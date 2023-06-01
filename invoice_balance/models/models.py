# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
from odoo.exceptions import UserError
logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _create_invoices(self, grouped=False, final=False, date=None):
        res = super(SaleOrder, self)._create_invoices(grouped=grouped, final=final, date=date)

        total_debit = sum([line.debit for line in res.line_ids])
        total_credit = sum([line.credit for line in res.line_ids])

        diff = total_credit - total_debit
        if total_debit > total_credit:
            for line in res.line_ids:
                if line.debit == 0:
                    line.sudo().write({
                        'credit': line.credit + diff
                    })
                    return res
                
        elif total_debit < total_credit:
            for line in res.line_ids:
                if line.credit == 0:
                    line.sudo().write({
                        'debit': line.debit + diff
                    })
                    return res

        return res


