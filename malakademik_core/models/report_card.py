from odoo import fields, models


class ReportCard(models.Model):
    _name = "malakademik.report.card"
    _description = "Report Card"

    student_id = fields.Many2one("malakademik.student", string="Student", required=True)
    term = fields.Char(string="Term", required=True)
    year = fields.Char(string="Year", required=True)
    line_ids = fields.One2many("malakademik.report.card.line", "report_id", string="Lines")
    average = fields.Float(string="Average", compute="_compute_average", store=True)

    def _compute_average(self):
        for rec in self:
            scores = [l.score for l in rec.line_ids if l.score]
            rec.average = sum(scores) / len(scores) if scores else 0.0


class ReportCardLine(models.Model):
    _name = "malakademik.report.card.line"
    _description = "Report Card Line"

    report_id = fields.Many2one("malakademik.report.card", required=True, ondelete="cascade")
    subject_id = fields.Many2one("malakademik.subject", string="Subject", required=True)
    score = fields.Float(string="Score")
    grade = fields.Char(string="Grade")

