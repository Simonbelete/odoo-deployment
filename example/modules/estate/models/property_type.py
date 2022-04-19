from odoo import models, fields

class PropertyType(models.Model):
    _name = "property.type.model"
    _description = "Property Types"

    name = fields.Char(required = True)
    # property_ids = fields.One2many('test.model', 'property_type_id', string = "Property")