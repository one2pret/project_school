from odoo import fields, models


class Assessment(models.Model):
    _name = "malakademik.assessment"
    _description = "Assessment"

    name = fields.Char(required=True)
    date = fields.Date(required=True)
    subject_id = fields.Many2one("malakademik.subject", string="Subject", required=True)
    teacher_id = fields.Many2one("malakademik.teacher", string="Teacher", required=True)
    classroom_id = fields.Many2one("malakademik.classroom", string="Classroom")
    line_ids = fields.One2many("malakademik.assessment.line", "assessment_id", string="Lines")


class AssessmentLine(models.Model):
    _name = "malakademik.assessment.line"
    _description = "Assessment Line"

    assessment_id = fields.Many2one("malakademik.assessment", required=True, ondelete="cascade")
    student_id = fields.Many2one("malakademik.student", string="Student", required=True)
    score = fields.Float(string="Score")
    notes = fields.Char(string="Notes")

