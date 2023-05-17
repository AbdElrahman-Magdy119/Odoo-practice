from odoo import models , fields

class patients(models.Model):

    _name = 'departmentdata'


    
    name = fields.Char()
    Capacity = fields.Integer() 
    Is_opened = fields.Boolean() 
   
    patient_ids = fields.One2many('patientsdata','department_id')
   
    
   