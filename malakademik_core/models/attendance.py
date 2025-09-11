from odoo import fields, models


class Attendance(models.Model):
    _name = "malakademik.attendance"
    _description = "Attendance"

    name = fields.Char(string="Name", compute="_compute_name", store=True)
    date = fields.Date(required=True)
    classroom_id = fields.Many2one("malakademik.classroom", string="Classroom", required=True)
    schedule_id = fields.Many2one("malakademik.schedule", string="Schedule")
    line_ids = fields.One2many("malakademik.attendance.line", "attendance_id", string="Lines")

    def _compute_name(self):
        for rec in self:
            parts = [rec.date and rec.date.strftime('%Y-%m-%d') or '', rec.classroom_id.name or '']
            rec.name = " - ".join([p for p in parts if p]) or "Attendance"


class AttendanceLine(models.Model):
    _name = "malakademik.attendance.line"
    _description = "Attendance Line"

    attendance_id = fields.Many2one("malakademik.attendance", required=True, ondelete="cascade")
    student_id = fields.Many2one("malakademik.student", string="Student", required=True)
    status = fields.Selection(
        [
            ("present", "Present"),
            ("absent", "Absent"),
            ("late", "Late"),
            ("excused", "Excused"),
        ],
        string="Status",
        required=True,
        default="present",
    )
    remarks = fields.Char(string="Remarks")

