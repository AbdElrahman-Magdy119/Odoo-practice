from odoo import models , fields  , api

class historyLog(models.Model):

    _name = 'history_log'
    description = fields.Text()
    patient_id = fields.Many2one('patientsdata')
