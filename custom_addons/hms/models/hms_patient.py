from odoo import models , fields  , api
from odoo.exceptions import ValidationError
from datetime import date

import re

class patients(models.Model):

    _name = 'patientsdata'

    _rec_name = 'firstName'
   

    firstName = fields.Char(required=True)

    lastName = fields.Char(required=True)

    birthDate = fields.Date(required=True)

    history = fields.Html()

    CR_Ratio = fields.Float()

    email = fields.Char()

    blood = fields.Selection([('H', 'H'), ('S', 'S'), ('M', 'M')])

    PCR = fields.Boolean()

    image = fields.Binary()

    address = fields.Text()

    age = fields.Integer(compute='compute_age')

    states = fields.Selection([('Undetermined', 'Undetermined'), ('Good', 'Good'), ('Fair', 'Fair') , ('Serious', 'Serious')])

    department_id = fields.Many2one('departmentdata')
    
    department_capacity = fields.Integer(related = 'department_id.Capacity')

    doctors_id = fields.Many2many('doctorsdata')

    history_logs = fields.One2many('history_log' , 'patient_id')

    is_available = fields.Boolean(default=True)


    # customer_id = fields.Many2one('res.partner')





    _sql_constraints = [
        ('Unique_name' , 'UNIQUE(email)' , 'This email is already assigned to another Patient')
    ]
    
    @api.onchange('history')
    def create_log_history(self):
        for rec in self:
            vals = {
                'description' : 'history changed to %s'%(rec.history),
                'patient_id' : rec.id
            }
            rec.env['history_log'].create(vals)

    @api.onchange('states')
    def create_log_states(self):
        for rec in self:
            vals = {
                'description' : 'history changed to %s'%(rec.states),
                'patient_id' : rec.id
            }
            rec.env['history_log'].create(vals)

    @api.onchange('age')
    def change_age(self):
        if self.age < 30:
            self.PCR = True
            return {
                'warning' : {
                    'title' : ('PCR Changed') ,
                    'message' :'PCR is changed'
                }
            }        
        
    

    @api.constrains('email')
    def check_email(self):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex,self.email):
            pass
        else:
            raise ValidationError('invalid email and email must be example@example.com')
        
        
    @api.depends('birthDate')
    def compute_age(self):
        for rec in self:
            if rec.birthDate:
                today = date.today()
                rec.age = today.year - rec.birthDate.year - (
                        (today.month, today.day) < (rec.birthDate.month, rec.birthDate.day))
            else:
                rec.age = 0
            
    

    
        
    

