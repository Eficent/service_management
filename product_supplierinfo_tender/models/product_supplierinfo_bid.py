# -*- coding: utf-8 -*-
# © 2015 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from openerp import api, fields, models

READONLY_STATES = {
    'accept': [('readonly', True)],
    'approve': [('readonly', True)],
    'cancel': [('readonly', True)],
}


class ProductSupplierinfoBid(models.Model):
    _name = "product.supplierinfo.bid"
    _description = "Supplier Pricelist Bid"
    _inherit = ['mail.thread', 'ir.needaction_mixin']

    name = fields.Char(string='Reference', required=True, copy=False,
                       default='New', readonly=True)
    state = fields.Selection([('draft', 'Draft'),
                              ('accept', 'Accept'),
                              ('approve', 'Approved'),
                              ('cancel', 'Cancelled')],
                             string='Status', select=True,
                             copy=False, default='draft',
                             track_visibility='onchange')
    tender_id = fields.Many2one(comodel_name='product.supplierinfo.tender',
                                string='Tender', required=True,
                                states=READONLY_STATES,
                                domain=[('state', 'in', ['draft',
                                                         'in_progress'])],
                                track_visibility='always')
    partner_id = fields.Many2one('res.partner', string='Vendor', required=True,
                                 states=READONLY_STATES, change_default=True,
                                 track_visibility='always')
    date_received = fields.Datetime('Received on', states=READONLY_STATES)
    currency_id = fields.Many2one('res.currency', 'Currency', required=True,
                                  states=READONLY_STATES,
                                  default=lambda self:
                                  self.env.user.company_id.currency_id.id)
    description = fields.Text(string='Description')
    company_id = fields.Many2one(
        'res.company', 'Company', required=True,
        select=1, states=READONLY_STATES,
        default=lambda self: self.env.user.company_id.id)
    line_ids = fields.One2many(
        comodel_name='product.supplierinfo',
        inverse_name='bid_id',
        string='Supplier Pricelists',
        states=READONLY_STATES,
        copy=False)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'product.supplierinfo.bid') or '/'
        return super(ProductSupplierinfoBid, self).create(vals)
