from odoo import models, fields

class Company(models.Model):
    _name = 'company.management'
    _description = 'Company Management'

    name = fields.Char(string='Company Name', required=True)
    manager = fields.Char(string='Manager Name')  
    address = fields.Text(string='Address')
    business_info = fields.Text(string='Business Information') 
    employer = fields.Char(string='Employers')  
    contact = fields.Char(string='Contact')
    request_ids = fields.One2many('company.request', 'company_id', string='Requests')
