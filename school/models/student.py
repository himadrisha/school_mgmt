# -*- coding: utf-8 -*-

from datetime import date

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class StudentInformation(models.Model):
    _name = 'student.student'
    _description = 'student_information'

    name = fields.Char(string="Name")
    l_name = fields.Char(string="Last_Name")
    include_last_name = fields.Boolean('Include Last name')
    division = fields.Char(string="Division" , readonly=True)
    date = fields.Date(string='Join Birth')
    mail = fields.Char(string="Email")
    phone = fields.Char(string="Phone Number")
    role = fields.Integer(string="Roll_Number")
    department_id = fields.Many2one('department.department', string="Department_id")
    birth_date = fields.Date(string='Date of Birth')
    age = fields.Integer(string="Age", compute='_compute_age')
    status = fields.Selection([("padding", "Padding"), ("success", "Success")], string="fee_Status",
                              compute='_compute_status', store=True, readonly=True)
    fee_ids = fields.One2many("fee.fee", "student_id", string="fee")
    all_success = fields.Boolean(string='All Success', compute='_compute_all_success', store=True)
    number = fields.Integer(string="Number Of Fee", compute="number_count")
    sequence_number = fields.Char(string='sequence_number', required=True,
                                  readonly=True, copy=False, default='New')

    # active = fields.Boolean(string='Active Student')

    @api.onchange('name')
    def capitalize_first_letter(self):
        for record in self:
            if record.name:
                capitalized_value = record.name.title()
                record.name = capitalized_value

    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.birth_date:
                rec.age = today.year - rec.birth_date.year
            else:
                rec.age = 0

    def fee_payment(self):
        self.write({'status': 'success'})

    @api.depends('fee_ids.status')
    def _compute_status(self):
        for student in self:
            if student.all_success:
                student.status = 'success'
            else:
                student.status = 'padding'

    @api.depends('fee_ids.status')
    def _compute_all_success(self):
        for student in self:
            student.all_success = all(fee.status == 'success' for fee in student.fee_ids)

    @api.constrains('phone')
    def _check_phone_number(self):
        for record in self:
            if record.phone and not record.phone.isdigit():
                raise ValidationError(" Phone number only should contain digits.")
            if record.phone and len(record.phone) != 10:
                raise ValidationError("Phone number should be 10 digits only.")

    def action_confirm(self):
        for _ in self:
            student = self.env['student.student'].search([('name', '=', 'Himadri')])
            # print("this is ", student)
            browse = self.env['student.student'].browse(4)
            print("this is", browse)

    def action_create(self):
        for rec in self:
            vals = {
                'name': 'Sweetu',
                'phone': '9734129832'

            }
            new_student = self.env['student.student'].create(vals)
            # print("this is ", new_student)

    def action_browse(self):
        for rec in self:
            browse = self.env['student.student'].browse(4)
            print("this is", browse)

    # def name_get(self):
    #     student_list = []
    #     for record in self:
    #         name = record.division + record.name
    #         student_list.append((record.id, name))
    #
    #     return student_list
    #
    # def name_search(self, name='', args=None, operator='ilike', limit=100):
    #     if args is None:
    #         args = []
    #
    #         domain = [('name', operator, name)]
    #
    #         record = self.search(domain + args, limit=limit)
    #         print("this is..........", record)
    #         return record.name_get()

    def view_student(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Fee',
            'view_mode': 'tree',
            'res_model': 'fee.fee',
            'domain': [('student_id', '=', self.name)],
            'context': "{'create' : False}"

        }

    @api.depends('fee_ids')
    def number_count(self):
        for record in self:
            record.number = len(record.fee_ids)

    @api.model
    def create(self, vals):
        if vals.get('sequence_number', 'New') == 'New':
            vals['sequence_number'] = self.env['ir.sequence'].next_by_code('student.student.sequence') or 'New'
            result = super(StudentInformation, self).create(vals)
            return result
