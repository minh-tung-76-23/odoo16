from odoo import api, models, fields

class school(models.Model):
    _name = 'school.student'

    name = fields.Many2one('res.partner', string="Student")
    class_id = fields.Integer(string="Class")
    division = fields.Char(string="Division")