from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Student(models.Model):
    _name = "malakademik.student"
    _description = "Student"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, tracking=True)
    nisn = fields.Char(string="NISN", tracking=True, index=True)
    student_id = fields.Char(string="Student ID", tracking=True)
    class_id = fields.Many2one("malakademik.classroom", string="Class", tracking=True)
    parent_ids = fields.Many2many("malakademik.parent", string="Parents")
    image_1920 = fields.Image(string="Photo")
    birth_place = fields.Char(string="Birth Place")
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
    status = fields.Selection([
        ("active", "Active"),
        ("inactive", "Inactive"),
    ], string="Status", default="active", tracking=True)
    active = fields.Boolean(default=True)
    history_ids = fields.One2many("malakademik.student.history", "student_id", string="History")
    history_count = fields.Integer(string="History Count", compute="_compute_history_count")
    submission_count = fields.Integer(string="Submissions", compute="_compute_related_counts")
    assessment_count = fields.Integer(string="Assessments", compute="_compute_related_counts")
    attendance_count = fields.Integer(string="Attendance", compute="_compute_related_counts")
    report_card_count = fields.Integer(string="Report Cards", compute="_compute_related_counts")

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

    @api.constrains("nisn")
    def _check_nisn(self):
        for rec in self:
            if rec.nisn:
                if not rec.nisn.isdigit() or len(rec.nisn) != 10:
                    raise ValidationError(_("NISN must be 10 digits (numeric)."))

    _sql_constraints = [
        ("malakademik_student_nisn_uniq", "unique(nisn)", "NISN must be unique."),
    ]

    def _compute_history_count(self):
        for rec in self:
            rec.history_count = len(rec.history_ids)

    def action_view_history(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": _("History"),
            "res_model": "malakademik.student.history",
            "view_mode": "list,form",
            "domain": [("student_id", "=", self.id)],
            "context": {"default_student_id": self.id},
            "target": "current",
        }

    def _compute_related_counts(self):
        # Initialize
        for rec in self:
            rec.submission_count = 0
            rec.assessment_count = 0
            rec.attendance_count = 0
            rec.report_card_count = 0
        ids = self.ids
        if not ids:
            return
        # Submissions
        data = self.env["malakademik.assignment.submission"].read_group(
            [("student_id", "in", ids)], ["student_id"], ["student_id"]
        )
        sub_map = {d["student_id"][0]: d["student_id_count"] for d in data if d.get("student_id")}
        # Assessments
        data = self.env["malakademik.assessment.line"].read_group(
            [("student_id", "in", ids)], ["student_id"], ["student_id"]
        )
        asm_map = {d["student_id"][0]: d["student_id_count"] for d in data if d.get("student_id")}
        # Attendance lines
        data = self.env["malakademik.attendance.line"].read_group(
            [("student_id", "in", ids)], ["student_id"], ["student_id"]
        )
        att_map = {d["student_id"][0]: d["student_id_count"] for d in data if d.get("student_id")}
        # Report cards
        data = self.env["malakademik.report.card"].read_group(
            [("student_id", "in", ids)], ["student_id"], ["student_id"]
        )
        rep_map = {d["student_id"][0]: d["student_id_count"] for d in data if d.get("student_id")}
        for rec in self:
            rec.submission_count = sub_map.get(rec.id, 0)
            rec.assessment_count = asm_map.get(rec.id, 0)
            rec.attendance_count = att_map.get(rec.id, 0)
            rec.report_card_count = rep_map.get(rec.id, 0)

    def action_view_submissions(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": _("Submissions"),
            "res_model": "malakademik.assignment.submission",
            "view_mode": "list,form",
            "domain": [("student_id", "=", self.id)],
            "context": {"default_student_id": self.id},
            "target": "current",
        }

    def action_view_assessments(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": _("Assessments"),
            "res_model": "malakademik.assessment.line",
            "view_mode": "list,form",
            "domain": [("student_id", "=", self.id)],
            "context": {"default_student_id": self.id},
            "target": "current",
        }

    def action_view_attendance(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": _("Attendance"),
            "res_model": "malakademik.attendance.line",
            "view_mode": "list,form",
            "domain": [("student_id", "=", self.id)],
            "context": {"default_student_id": self.id},
            "target": "current",
        }

    def action_view_report_cards(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": _("Report Cards"),
            "res_model": "malakademik.report.card",
            "view_mode": "list,form",
            "domain": [("student_id", "=", self.id)],
            "context": {"default_student_id": self.id},
            "target": "current",
        }


class StudentHistory(models.Model):
    _name = "malakademik.student.history"
    _description = "Student Academic History"

    student_id = fields.Many2one("malakademik.student", required=True, ondelete="cascade")
    year = fields.Char(required=True, string="Academic Year")
    event_type = fields.Selection([
        ("in", "Admission In"),
        ("out", "Transfer Out"),
    ], string="Event Type")
    school_name = fields.Char(string="School Name")
    date = fields.Date(string="Date")
    notes = fields.Text()
