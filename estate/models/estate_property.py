# -*- coding: utf-8 -*-
from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char(default="Unknown", required = True)
    id = fields.Integer(required = True)
    expected_price = fields.Float(required = True)
    create_uid = fields.Integer()
    description = fields.Char()
    postcode = fields.Char()
    active = fields.Boolean(default = False)
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())