from odoo import fields, models


class Subject(models.Model):
    _name = "malakademik.subject"
    _description = "Subject"

    name = fields.Char(required=True)
    code = fields.Char(string="Code")
    curriculum_id = fields.Many2one("malakademik.curriculum", string="Curriculum")
    active = fields.Boolean(default=True)

