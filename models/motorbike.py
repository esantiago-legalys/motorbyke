from odoo import models, fields

class Motorbike(models.Model):
    _name = 'motorbike.registration'
    _description = 'Motorbike Registration'

    name = fields.Char(string='Model', required=True)
    brand = fields.Char(string='Brand', required=True)
    year = fields.Integer(string='Year', required=True)
    vin = fields.Char(string='VIN', required=True)
    owner_id = fields.Many2one('res.partner', string='Owner')
