from odoo import fields, models, _


class Classroom(models.Model):
    _name = "malakademik.classroom"
    _description = "Classroom"

    name = fields.Char(required=True)
    grade = fields.Selection(
        [(str(i), str(i)) for i in range(1, 13)], string="Grade"
    )
    homeroom_teacher_id = fields.Many2one("malakademik.teacher", string="Homeroom Teacher")
    active = fields.Boolean(default=True)
    # Smart button counts
    student_count = fields.Integer(compute="_compute_counts", string="Students")
    schedule_count = fields.Integer(compute="_compute_counts", string="Schedules")
    attendance_count = fields.Integer(compute="_compute_counts", string="Attendance")
    assessment_count = fields.Integer(compute="_compute_counts", string="Assessments")
    assignment_count = fields.Integer(compute="_compute_counts", string="Assignments")

    def _compute_counts(self):
        for rec in self:
            rec.student_count = rec.schedule_count = rec.attendance_count = rec.assessment_count = rec.assignment_count = 0
        ids = self.ids
        if not ids:
            return
        # Students in class
        rg = self.env["malakademik.student"].read_group([("class_id", "in", ids)], ["class_id"], ["class_id"])
        stu_map = {d["class_id"][0]: d["class_id_count"] for d in rg if d.get("class_id")}
        # Schedules
        rg = self.env["malakademik.schedule"].read_group([("classroom_id", "in", ids)], ["classroom_id"], ["classroom_id"])
        sch_map = {d["classroom_id"][0]: d["classroom_id_count"] for d in rg if d.get("classroom_id")}
        # Attendance
        rg = self.env["malakademik.attendance"].read_group([("classroom_id", "in", ids)], ["classroom_id"], ["classroom_id"])
        att_map = {d["classroom_id"][0]: d["classroom_id_count"] for d in rg if d.get("classroom_id")}
        # Assessments
        rg = self.env["malakademik.assessment"].read_group([("classroom_id", "in", ids)], ["classroom_id"], ["classroom_id"])
        asm_map = {d["classroom_id"][0]: d["classroom_id_count"] for d in rg if d.get("classroom_id")}
        # Assignments
        rg = self.env["malakademik.assignment"].read_group([("classroom_id", "in", ids)], ["classroom_id"], ["classroom_id"])
        asg_map = {d["classroom_id"][0]: d["classroom_id_count"] for d in rg if d.get("classroom_id")}
        for rec in self:
            rec.student_count = stu_map.get(rec.id, 0)
            rec.schedule_count = sch_map.get(rec.id, 0)
            rec.attendance_count = att_map.get(rec.id, 0)
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

    def action_view_students(self):
        self.ensure_one()
        return self._act_window(_("Students"), "malakademik.student", [("class_id", "=", self.id)])

    def action_view_schedules(self):
        self.ensure_one()
        return self._act_window(_("Schedules"), "malakademik.schedule", [("classroom_id", "=", self.id)])

    def action_view_attendance(self):
        self.ensure_one()
        return self._act_window(_("Attendance"), "malakademik.attendance", [("classroom_id", "=", self.id)])

    def action_view_assessments(self):
        self.ensure_one()
        return self._act_window(_("Assessments"), "malakademik.assessment", [("classroom_id", "=", self.id)])

    def action_view_assignments(self):
        self.ensure_one()
        return self._act_window(_("Assignments"), "malakademik.assignment", [("classroom_id", "=", self.id)])
