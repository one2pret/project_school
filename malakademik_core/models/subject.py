from odoo import fields, models, _


class Subject(models.Model):
    _name = "malakademik.subject"
    _description = "Subject"

    name = fields.Char(required=True)
    code = fields.Char(string="Code")
    curriculum_id = fields.Many2one("malakademik.curriculum", string="Curriculum")
    active = fields.Boolean(default=True)
    # Smart button counts
    schedule_count = fields.Integer(string="Schedules", compute="_compute_counts")
    assessment_count = fields.Integer(string="Assessments", compute="_compute_counts")
    assignment_count = fields.Integer(string="Assignments", compute="_compute_counts")

    def _compute_counts(self):
        for rec in self:
            rec.schedule_count = rec.assessment_count = rec.assignment_count = 0
        ids = self.ids
        if not ids:
            return
        rg = self.env["malakademik.schedule"].read_group([("subject_id", "in", ids)], ["subject_id"], ["subject_id"])
        sch_map = {d["subject_id"][0]: d["subject_id_count"] for d in rg if d.get("subject_id")}
        rg = self.env["malakademik.assessment"].read_group([("subject_id", "in", ids)], ["subject_id"], ["subject_id"])
        asm_map = {d["subject_id"][0]: d["subject_id_count"] for d in rg if d.get("subject_id")}
        rg = self.env["malakademik.assignment"].read_group([("subject_id", "in", ids)], ["subject_id"], ["subject_id"])
        asg_map = {d["subject_id"][0]: d["subject_id_count"] for d in rg if d.get("subject_id")}
        for rec in self:
            rec.schedule_count = sch_map.get(rec.id, 0)
            rec.assessment_count = asm_map.get(rec.id, 0)
            rec.assignment_count = asg_map.get(rec.id, 0)

    def _act_window(self, name, model, domain):
        return {
            "type": "ir.actions.act_window",
            "name": name,
            "res_model": model,
            "view_mode": "list,form",
            "domain": domain,
            "target": "current",
        }

    def action_view_schedules(self):
        self.ensure_one()
        return self._act_window(_("Schedules"), "malakademik.schedule", [("subject_id", "=", self.id)])

    def action_view_assessments(self):
        self.ensure_one()
        return self._act_window(_("Assessments"), "malakademik.assessment", [("subject_id", "=", self.id)])

    def action_view_assignments(self):
        self.ensure_one()
        return self._act_window(_("Assignments"), "malakademik.assignment", [("subject_id", "=", self.id)])
