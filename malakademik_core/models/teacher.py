from odoo import api, fields, models, _


class Teacher(models.Model):
    _name = "malakademik.teacher"
    _description = "Teacher"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, tracking=True)
    employee_code = fields.Char(string="Employee Code", tracking=True)
    partner_id = fields.Many2one("res.partner", string="Contact", ondelete="set null")
    email = fields.Char(related="partner_id.email", readonly=False, store=True)
    phone = fields.Char(related="partner_id.phone", readonly=False, store=True)
    subject_ids = fields.Many2many(
        "malakademik.subject",
        "malakademik_teacher_subject_rel",
        "teacher_id",
        "subject_id",
        string="Subjects",
    )
    class_ids = fields.Many2many(
        "malakademik.classroom",
        "malakademik_teacher_class_rel",
        "teacher_id",
        "class_id",
        string="Classes",
    )
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
