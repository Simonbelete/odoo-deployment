from odoo import models, fields

class PropertyTag(models.Model):
    _name = 'property.tag.model'
    _description = 'Property Tag'

    name = fields.Char(required = True)