from odoo import api, fields, models, _


class Student(models.Model):
    _name = "malakademik.student"
    _description = "Student"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, tracking=True)
    student_id = fields.Char(string="Student ID", tracking=True)
    class_id = fields.Many2one("malakademik.classroom", string="Class", tracking=True)
    parent_ids = fields.Many2many("malakademik.parent", string="Parents")
    birth_date = fields.Date()
    gender = fields.Selection([
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ], tracking=True)
    partner_id = fields.Many2one("res.partner", string="Contact", ondelete="set null")
    email = fields.Char(related="partner_id.email", readonly=False, store=True)
    phone = fields.Char(related="partner_id.phone", readonly=False, store=True)
    address = fields.Char()
    active = fields.Boolean(default=True)

    @api.model_create_multi
    def create(self, vals_list):
        partners_to_create = []
        for vals in vals_list:
            if not vals.get("partner_id"):
                partners_to_create.append({
                    "name": vals.get("name"),
                    "email": vals.get("email"),
                    "phone": vals.get("phone"),
                    "type": "contact",
                })
        created_partners = self.env["res.partner"].create(partners_to_create) if partners_to_create else self.env["res.partner"]
        idx = 0
        for vals in vals_list:
            if not vals.get("partner_id"):
                vals["partner_id"] = created_partners[idx].id
                idx += 1
        return super().create(vals_list)


class StudentHistory(models.Model):
    _name = "malakademik.student.history"
    _description = "Student Academic History"

    student_id = fields.Many2one("malakademik.student", required=True, ondelete="cascade")
    year = fields.Char(required=True, string="Academic Year")
    notes = fields.Text()
