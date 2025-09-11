from odoo import fields, models


class Assignment(models.Model):
    _name = "malakademik.assignment"
    _description = "Assignment"

    name = fields.Char(required=True)
    subject_id = fields.Many2one("malakademik.subject", string="Subject", required=True)
    teacher_id = fields.Many2one("malakademik.teacher", string="Teacher", required=True)
    classroom_id = fields.Many2one("malakademik.classroom", string="Classroom")
    due_date = fields.Datetime(string="Due Date")
    description = fields.Text(string="Description")
    submission_ids = fields.One2many("malakademik.assignment.submission", "assignment_id", string="Submissions")


class AssignmentSubmission(models.Model):
    _name = "malakademik.assignment.submission"
    _description = "Assignment Submission"

    assignment_id = fields.Many2one("malakademik.assignment", required=True, ondelete="cascade")
    student_id = fields.Many2one("malakademik.student", string="Student", required=True)
    attachment_ids = fields.Many2many(
        "ir.attachment",
        string="Documents",
        relation="malakademik_submission_attachment_rel",
        column1="submission_id",
        column2="attachment_id",
    )
    score = fields.Float(string="Score")
    feedback = fields.Text(string="Feedback")

