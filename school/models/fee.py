from odoo import fields, models


class FeeInformation(models.Model):
    _name = 'fee.fee'
    _description = 'fee information'
    _rec_name = 'status'

    status = fields.Selection([('success', 'Success'), ('padding', 'Padding')], string='Statuses')
    amount = fields.Integer(string='Amount')
    payment = fields.Selection([('online', 'Online'), ('cash', 'Cash')], string='Payment_type')
    student_id = fields.Many2one("student.student", string="Student Name")
    month = fields.Date(string="Month")

    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'very High')], string="Priority")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('cancel', 'cancelled')], default='draft', string="State", required=True)

    # def fee_status(self):
    #     for record in self:
    #         if record.status == 'success':
    #             record.student_id.status = 'success'
    #         else:
    #             record.student_id.status = 'padding'

    # def onchange_fee_status(self):
    #     for record in self:
    #         if record.status == 'success':
    #             record.student_id.status = 'success'
    #         else:
    #             record.student_id.status = 'padding'

    def default_get(self, fields_list):
        print("this is the", fields_list)
        defaults = super(FeeInformation, self).default_get(fields_list)

        defaults['amount'] = 20000
        print("this is value", fields_list)
        return defaults

    def action_done(self):
        self.write({'state': 'draft'})

    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_cancel(self):
        self.write({'state': 'cancel'})
