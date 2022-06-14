from odoo import models, fields, api, _
from datetime import datetime,date
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, float_round

class BillofMaterial(models.Model):
    _inherit = "mrp.bom"

    bom_total_cost = fields.Float(compute='_amount_all', string='Total Cost', store=True)

    @api.depends('bom_line_ids.subtotal_cost')
    def _amount_all(self):
        """
        Compute the total amounts of the SO.
        """
        for bom in self:
            amount = 0.0
            for line in bom.bom_line_ids:
                amount += line.subtotal_cost
            bom.update({
                'bom_total_cost': amount,
            })

class BillofMaterialLine(models.Model):
    _inherit = "mrp.bom.line"

    bom_cost = fields.Float(compute='_compute_cost', string='Product Cost', store=True)
    subtotal_cost = fields.Float(compute='_compute_cost', string='Subtotal Cost', store=True)

    @api.depends('product_qty',)
    def _compute_cost(self):
            """
            Compute the Costs of the BOM line.
            """
            for line in self:
                cost = line.product_id.standard_price
                subtotal_cost = line.product_id.standard_price * line.product_qty
                line.update({
                    'bom_cost': cost,
                    'subtotal_cost':subtotal_cost,
                })
