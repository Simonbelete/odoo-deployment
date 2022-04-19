from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

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
    status = fields.Selection([('New', 'new'), ('Canceled', 'canceled'), ('Sold', 'sold')], default ='')
    # last_seen = fields.DateTime("Last Seen", default = lambda self: fields.Datetime.now())
    active = fields.Boolean(default = True)
    # Dosen't have odoo account
    buyer = fields.Many2one('res.partner', string='Estate Buyer', required = True)
    sales_person = fields.Many2one('res.users', string='Estate Employee', required = True, default = lambda self: self.env.user)

    tag_ids = fields.Many2many('property.tag.model', string = 'Tags')
    offer_ids = fields.One2many('property.offer.model', "property_id", string = "Offers")

    total_area = fields.Float(compute="_compute_total_area")
    best_price = fields.Float(compute="_compute_best_price")

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        # Fix for compute failed for create
        self.best_price = 0
        for record in self:
            if(len(record.mapped('offer_ids.price')) > 0):
                record.best_price = max(record.mapped('offer_ids.price'), 0)

    def action_sold(self):
        for record in self:
            if(record.status == 'Canceled'):
                raise UserError('Canceled property cannot be sold')
            else:
                record.status = 'Sold'
        return True

    def action_cancel(self):
        for record in self:
            record.status = 'Canceled'
        return True

    @api.constrains('name')
    def _check_name(self):
        for record in self:
            if(len(record.name) < 3):
                raise ValidationError('Name Char must be at least more than 2 char long')