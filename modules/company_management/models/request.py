from odoo import models, fields

class Request(models.Model):
    _name = 'company.request'
    _description = 'Company Request'

    name = fields.Char(string='Request Name', required=True)
    quantity_intern = fields.Integer("Quantity Intern")
    request = fields.Text(string='Request')
    company_id = fields.Many2one('company.management', string='Company', required=True)
