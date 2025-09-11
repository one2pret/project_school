from odoo import fields, models


class Curriculum(models.Model):
    _name = "malakademik.curriculum"
    _description = "Curriculum"

    name = fields.Char(required=True)
    year = fields.Char(string="Year")
    description = fields.Text()
    active = fields.Boolean(default=True)

