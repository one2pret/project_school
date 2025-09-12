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
    # Smart button counts
    schedule_count = fields.Integer(compute="_compute_counts", string="Schedules")
    assessment_count = fields.Integer(compute="_compute_counts", string="Assessments")
    assignment_count = fields.Integer(compute="_compute_counts", string="Assignments")

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

    def _compute_counts(self):
        for rec in self:
            rec.schedule_count = rec.assessment_count = rec.assignment_count = 0
        ids = self.ids
        if not ids:
            return
        rg = self.env["malakademik.schedule"].read_group([("teacher_id", "in", ids)], ["teacher_id"], ["teacher_id"])
        sch_map = {d["teacher_id"][0]: d["teacher_id_count"] for d in rg if d.get("teacher_id")}
        rg = self.env["malakademik.assessment"].read_group([("teacher_id", "in", ids)], ["teacher_id"], ["teacher_id"])
        asm_map = {d["teacher_id"][0]: d["teacher_id_count"] for d in rg if d.get("teacher_id")}
        rg = self.env["malakademik.assignment"].read_group([("teacher_id", "in", ids)], ["teacher_id"], ["teacher_id"])
        asg_map = {d["teacher_id"][0]: d["teacher_id_count"] for d in rg if d.get("teacher_id")}
        for rec in self:
            rec.schedule_count = sch_map.get(rec.id, 0)
            rec.assessment_count = asm_map.get(rec.id, 0)
            rec.assignment_count = asg_map.get(rec.id, 0)

    def action_view_schedules(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": _("Schedules"),
            "res_model": "malakademik.schedule",
            "view_mode": "list,form",
            "domain": [("teacher_id", "=", self.id)],
            "context": {"default_teacher_id": self.id},
        }

    def action_view_assessments(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": _("Assessments"),
            "res_model": "malakademik.assessment",
            "view_mode": "list,form",
            "domain": [("teacher_id", "=", self.id)],
            "context": {"default_teacher_id": self.id},
        }

    def action_view_assignments(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": _("Assignments"),
            "res_model": "malakademik.assignment",
            "view_mode": "list,form",
            "domain": [("teacher_id", "=", self.id)],
            "context": {"default_teacher_id": self.id},
        }
