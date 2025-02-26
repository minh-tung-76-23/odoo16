from odoo import models, fields

class UniversityStudentInfo(models.Model):
    _name = 'university.student.info'
    _description = 'University Student Information'

    name = fields.Char(string="Student Name", required=True)
    student_id = fields.Char(string="Student ID", required=True)
    email = fields.Char(string="Email", required=True)
    university_id = fields.Many2one('university', string="University")
