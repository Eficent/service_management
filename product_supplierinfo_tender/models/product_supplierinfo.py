# -*- coding: utf-8 -*-
# © 2015 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from openerp import _, api, fields, models

_STATES = [('draft', 'Draft'), ('open', 'Call for Bids'),
           ('selection', 'Bid Selection'), ('done', 'Completed'),
           ('cancel', 'Cancelled')]


class ProductSupplierinfo(models.Model):
    _inherit = "product.supplierinfo"

    bid_id = fields.Many2one(string='Bid',
                             comodel_name='product.supplierinfo.bid',
                             copy=False)
    tender_id = fields.Many2one(string='Tender',
                                comodel_name='product.supplierinfo.tender',
                                related='bid_id.tender_id',
                                store=True,
                                readonly=True)
    tender_state = fields.Selection(_STATES,
                                    string='Tender State',
                                    related='tender_id.state',
                                    readonly=True)
    approved_tender = fields.Boolean(string='Approved in Tender',
                                     default=False)

    @api.multi
    def button_approve_tender(self):
        for rec in self:
            rec.approved_tender = True

    @api.multi
    def button_unapprove_tender(self):
        for rec in self:
            rec.approved_tender = False
