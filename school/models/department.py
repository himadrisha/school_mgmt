# -*- coding: utf-8 -*-
from odoo import fields, models, api


class DepartmentInformation(models.Model):
    _name = 'department.department'
    _description = 'department information'


    name = fields.Char(string="Name")
    number = fields.Integer(string="Number Faculty", compute='_cumpute_data')
    student_ids = fields.One2many("student.student", "department_id", string="Student_Name")
    related_model = fields.Char(string="faculty__name", compute="_compute_related")
    faculty_ids = fields.One2many("faculty.faculty", "department_id", string="Faculty_Name")
    model_related = fields.Char(string="student_name", compute="_compute_related")
    snumber = fields.Integer(string="Number Student", compute="_cumpute_data")




    @api.depends('related_model')
    def _compute_related(self):
        for record in self:
            name = ','.join(record.faculty_ids.mapped('name'))
            record.related_model = name

        for record1 in self:
            name1 = ','.join(record1.student_ids.mapped('name'))
            record1.model_related = name1

    def create_data(self):
        for _ in self:
            new_department = self.env['department.department'].create({'name': 'MUSIC'})

        for _ in self:
            vals = {
                'name': 'Tadu',
                'department_id': new_department.id
            }
        new_student = self.env['student.student'].create(vals)

    @api.depends('faculty_ids')
    def _cumpute_data(self):
        for record in self:
            record.number = len(record.faculty_ids)
        for record in self:
            record.snumber = len(record.student_ids)


    def action_view_faculty(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Faculty',
            'view_mode': 'tree',
            'res_model': 'faculty.faculty',
            'domain': [('department_id', '=', self.name)],
            'context': "{'create' : False}"
        }

    def action_view_student(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Faculty',
            'view_mode': 'tree',
            'res_model': 'student.student',
            'domain': [('department_id', '=', self.name)],
            'context': "{'create' : False}"
        }

    def create_custom_login(self):
        vals = {
            'name': self.name,
            'number': self.number,
        }
        login = self.env['student.student'].create(vals)
        return login
