from odoo import models, fields

class PropertyOffer(models.Model):
    _name = 'property.offer.model'
    _description = 'Property Offer'

    price = fields.Float(required = True, default = 0)
    status = fields.Selection([('Accepted', 'accepted'), ('Refused', 'refused')])
    partner_id = fields.Many2one('res.partner', required = True)
    property_id = fields.Many2one('test.model', required = True)

    def action_accept(self):
        for record in self:
            record.status = 'Accepted'
        return True

    def action_refused(self):
        for record in self:
            record.status = 'Refused'
        return True