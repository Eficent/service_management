# -*- coding: utf-8 -*-
# © 2015 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from openerp import api, fields, models
from openerp.exceptions import ValidationError, Warning
from openerp.tools.translate import _


class PartnerExternalReferenceOrigin(models.Model):
    _name = "partner.external.reference.origin"

    code = fields.Char(
        string="Code", required=True)
    name = fields.Char(
        string="Name", required=True)
