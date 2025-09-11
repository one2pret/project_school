from odoo import api, fields, models


class Parent(models.Model):
    _name = "malakademik.parent"
    _description = "Parent/Guardian"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, tracking=True)
    relation = fields.Selection(
        [
            ("father", "Father"),
            ("mother", "Mother"),
            ("guardian", "Guardian"),
        ],
        string="Relation",
        tracking=True,
    )
    partner_id = fields.Many2one("res.partner", string="Contact", ondelete="set null")
    email = fields.Char(related="partner_id.email", readonly=False, store=True)
    phone = fields.Char(related="partner_id.phone", readonly=False, store=True)
    address = fields.Char()
    student_ids = fields.Many2many(
        "malakademik.student", string="Students", readonly=True
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
