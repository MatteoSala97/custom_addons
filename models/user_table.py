from odoo import models, fields

class UserTable(models.Model):
    _name = 'user.table'
    _description = 'Modulo di test con tabella'
    
    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    username = fields.Char(string='Username', required=True)