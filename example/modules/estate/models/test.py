from odoo import models, fields

class TestModel(models.Model):
    _name = "test.model"
    _description = "Test Model"

    name = fields.Char(required = True, default = "Unknown")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required = True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Boolean()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([('x', 'X'), ('y', 'Y')])
    # last_seen = fields.DateTime("Last Seen", default = lambda self: fields.Datetime.now())
    active = fields.Boolean(default = True)
    # Dosen't have odoo account
    buyer = fields.Many2one('res.partner', string='Estate Buyer', required = True)
    sales_person = fields.Many2one('res.users', string='Estate Employee', required = True, default = lambda self: self.env.user)

    tag_ids = fields.Many2many('property.tag.model', string = 'Tags')
    offer_ids = fields.One2many('property.offer.model', "property_id", string = "Offers")