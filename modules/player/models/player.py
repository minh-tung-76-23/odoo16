from odoo import fields, models

class Player(models.Model):
    _name = 'player'
    _description = 'Player'
    
    name = fields.Char('Name', required=True)
    image = fields.Binary('Image', attachment=True)
    country = fields.Char('Country')
    gender = fields.Selection([
        ('Male', 'Male'),
        ('Female', 'Female')
    ], string='Gender', default='Male')  
    date_of_birth = fields.Datetime('Date of Birth')
    position = fields.Char('Position', group="mo_football.group_player_manager")
    height = fields.Float('Height')
    weight = fields.Float('Weight')
