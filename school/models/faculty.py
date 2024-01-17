# -*- coding: utf-8 -*-
import re

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from datetime import date


class FacultyInformation(models.Model):
    _name = 'faculty.faculty'
    _description = 'faculty_information'

    name = fields.Char(string="Name")
    date = fields.Date(string='Join Birth')
    phone = fields.Char(string="Phone Number")

    department_id = fields.Many2one("department.department", string="Department Name")
    student_id = fields.Many2one("student.student", string="student Name")
    birth_date = fields.Date(string='Date of Birth')
    age = fields.Integer(string="Age")  # , compute='_compute_age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    sequence_number = fields.Char(string='sequence_number', required=True,
                                  readonly=True, copy=False, default='New')

    # mail = fields.Char(string="Email")

    def funtion(self):
        pass

    # @api.onchange('name')
    # def capitalize_first_letter(self):
    #     for record in self:
    #         if record.name:
    #             capitalized_value = record.name.title()
    #             record.name = capitalized_value

    # def _compute_age(self):
    #     for rec in self:
    #         today = date.today()
    #         if rec.birth_date:
    #             rec.age = today.year - rec.birth_date.year
    #         else:
    #             rec.age = 0
    #
    # @api.constrains('name')
    # def _check_name(self):
    #     for record in self:
    #         if record.name and not record.name[0].isupper():
    #             raise ValidationError("Name should start with a capital letter.")
    #         if record.name:
    #             record.name = record.name.capitalize()
    #
    # @api.constrains('age')
    # def _check_age(self):
    #     # for rec in self:
    #     if self.age < 20:
    #         raise ValidationError("Age must be up to 20 years.")

    # @api.constrains('mail')
    # def _check_mail(self):
    #
    #     if self.mail:
    #         match = re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', self.mail)
    #     if match is None:
    #         raise ValidationError("this is not valid Email ID")

    # @api.model
    # def send_email_to_students(self):
    #     faculties = self.env['faculty.faculty'].search([('department', '=', True)])
    #
    #     for faculty in faculties:
    #         students = faculty.student_id
    #
    #         for student in students:
    #             email_subject = "Fee Payment"
    #             email_body = " your payment is successfully pay"
    #             student.email_field.send_email(email_body, email_subject)

    # def action_confirm(self):
    #     for rec in self:
    #         # this is for the search
    #         faculty = self.env['faculty.faculty'].search([])
    #         print('faculty.....', faculty)
    #         # this is the for the query search
    #         female = self.env['faculty.faculty'].search([('gender', '=', 'female')])
    #         print("gender...", female)
    #         # this is browse
    #         browse = self.env['faculty.faculty'].browse(50)
    #         print("this is browse", browse)
    #         # this is for the if the record is in the model or not  using exists
    #         if browse.exists():
    #             print("this record is in the model...")
    #         else:
    #             print("this record is not in the model...")
    #
    #             email_subject = "Your Subject"
    #             email_body = "Your email body"
    #             student.email_field.send_email(email_subject, email_body)

    # @api.model_create_multi
    # def create(self, vals_list):
    #     print("value ------------------", vals_list)
    #     res = super(FacultyInformation, self).create(vals_list)
    #     # print("res......", res)
    #     # print("res......", res.name)
    #     res.name = "Mittal"
    #     print("this is value", vals_list)
    #     return res

    @api.model
    def create(self, vals):
        if vals.get('sequence_number', 'New') == 'New':
            vals['sequence_number'] = self.env['ir.sequence'].next_by_code('faculty.faculty.sequence') or 'New'
            result = super(FacultyInformation, self).create(vals)
            return result

    # def write(self, vals):
    #     print('this is', vals)
    #     res = super(FacultyInformation, self).write(vals)
    #     if vals.get('name'):
    #         self.student_id.name()
    #     return res

    # def write(self, vals):
    #     res = super(Channel, self).write(vals)
    #     if vals.get('subscription_department_ids'):
    #         self._subscribe_users_automatically()
    #     return res

    # @api.model_create_multi
    #     def create(self, vals_list):
    #         # TDE note: auto-subscription of manager done by hand, because currently
    #         # the tracking allows to track+subscribe fields linked to a res.user record
    #         # An update of the limited behavior should come, but not currently done.
    #         departments = super(Department, self.with_context(mail_create_nosubscribe=True)).create(vals_list)
    #         for department, vals in zip(departments, vals_list):
    #             manager = self.env['hr.employee'].browse(vals.get("manager_id"))
    #             if manager.user_id:
    #                 department.message_subscribe(partner_ids=manager.user_id.partner_id.ids)
    #         return departments

    @api.model
    def send_email_to_students(self):
        print("this is the cron job.....")
