from odoo import models , fields

class p(models.Model):

    _name = 'hsm'

    _rec_name = 'firstName'

    firstName = fields.Char()

    lastName = fields.Char()

    birthDate = fields.Date()

    history = fields.Html()

    CR_Ratio = fields.Float()

    blood = fields.Selection([('H', 'H'), ('S', 'S'), ('M', 'M')])

    PCR = fields.Boolean()

    image = fields.Binary()

    address = fields.Text()

    age = fields.Integer()
