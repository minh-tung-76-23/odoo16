from odoo import models, fields

class Company(models.Model):
    _name = 'company.management'
    _description = 'Company Management'

    name = fields.Char(string='Company Name', required=True)
    address = fields.Text(string='Address')
    contact = fields.Char(string='Contact Number')
    request_ids = fields.One2many('company.request', 'company_id', string='Requests')
