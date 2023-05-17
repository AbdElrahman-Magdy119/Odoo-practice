from odoo import models , fields

class patients(models.Model):

    _name = 'doctorsdata'

    _rec_name = 'firstName'
   

    firstName = fields.Char()

    lastName = fields.Char()

    image = fields.Binary()
