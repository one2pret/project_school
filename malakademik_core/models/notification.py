from odoo import fields, models


class Notification(models.Model):
    _name = "malakademik.notification"
    _description = "Notification"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Subject", required=True, tracking=True)
    message = fields.Text(string="Message", tracking=True)
    recipient_student_ids = fields.Many2many("malakademik.student", string="Students")
    recipient_parent_ids = fields.Many2many("malakademik.parent", string="Parents")
    recipient_teacher_ids = fields.Many2many("malakademik.teacher", string="Teachers")
    state = fields.Selection(
        [("draft", "Draft"), ("sent", "Sent")], default="draft", tracking=True
    )
    scheduled_date = fields.Datetime(string="Scheduled Date")
    sent_date = fields.Datetime(string="Sent Date")

