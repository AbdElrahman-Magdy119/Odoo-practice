from odoo import models , fields  , api
from odoo.exceptions import ValidationError
from datetime import date
import re

class patientinherit(models.Model):

    _inherit = 'res.partner'

    patient_id = fields.Many2one('patientsdata')
    
    vat = fields.Char(required=True)

    
    @api.constrains('patient_id')
    def create_patient_id(self):
        if self.patient_id:
           self.patient_id.is_available = False
        

    def unlink(self):
        if(self.patient_id):
          raise ValidationError("can't delete this record because this record relates to patient")
        else:
          return super(patientinherit, self).unlink()
    @api.model
    def write(self, vals):
        self.patient_id.is_available=True
        return super(patientinherit,self).write(vals)