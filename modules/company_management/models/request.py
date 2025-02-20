from odoo import models, fields

class Request(models.Model):
    _name = 'company.request'
    _description = 'Company Request'

    name = fields.Char(string='Request Name', required=True)
    quantity_intern = fields.Integer("Quantity Intern")
    request = fields.Text(string='Request')
    job_description = fields.Text(string='Job description')
    benefits = fields.Text(string='Benefits')
    work_time = fields.Text(string='Working time')
    note = fields.Text(string='Note') 
    request_state = fields.Selection(  
        [('insufficient', 'Insufficient'), 
         ('submitted', 'Submitted'), 
         ('approved', 'Approved'), 
         ('rejected', 'Rejected')],
        string='Request State', 
        default='insufficient'
    )
    company_id = fields.Many2one('company.management', string='Company', required=True)
