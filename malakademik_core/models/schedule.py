from odoo import fields, models


class Schedule(models.Model):
    _name = "malakademik.schedule"
    _description = "Schedule"

    classroom_id = fields.Many2one("malakademik.classroom", string="Classroom", required=True)
    subject_id = fields.Many2one("malakademik.subject", string="Subject", required=True)
    teacher_id = fields.Many2one("malakademik.teacher", string="Teacher", required=True)
    day_of_week = fields.Selection(
        [
            ("mon", "Monday"),
            ("tue", "Tuesday"),
            ("wed", "Wednesday"),
            ("thu", "Thursday"),
            ("fri", "Friday"),
            ("sat", "Saturday"),
            ("sun", "Sunday"),
        ],
        string="Day of Week",
        required=True,
    )
    start_time = fields.Float(string="Start Time", required=True)
    end_time = fields.Float(string="End Time", required=True)

