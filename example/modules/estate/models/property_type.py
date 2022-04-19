from odoo import models, fields

class PropertyType(models.Model):
    _name = "property.type.model"
    _description = "Property Types"

    name = fields.Char(required = True)