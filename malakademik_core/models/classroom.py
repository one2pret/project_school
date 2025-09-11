from odoo import fields, models


class Classroom(models.Model):
    _name = "malakademik.classroom"
    _description = "Classroom"

    name = fields.Char(required=True)
    grade = fields.Selection(
        [(str(i), str(i)) for i in range(1, 13)], string="Grade"
    )
    homeroom_teacher_id = fields.Many2one("malakademik.teacher", string="Homeroom Teacher")
    active = fields.Boolean(default=True)

