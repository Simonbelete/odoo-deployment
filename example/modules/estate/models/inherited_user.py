from odoo import fields, models

class InheritedUser(models.Model):
    _inherit = 'res.users'

    nick_name = fields.Char(string = 'Nick Name')
    property_ids = fields.One2many('test.model', 'sales_person', string = "Properties")