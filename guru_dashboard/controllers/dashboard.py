from odoo import http, fields
from odoo.http import request


class TeacherDashboardController(http.Controller):
    @http.route("/guru_dashboard/teacher_stats", type="json", auth="user")
    def teacher_stats(self, teacher_id=None):
        env = request.env
        user = env.user
        Teacher = env["malakademik.teacher"]

        teacher = False
        if teacher_id and user.has_group("malakademik_core.group_malakademik_manager"):
            teacher = Teacher.search([("id", "=", teacher_id)], limit=1)

        if not teacher and user.partner_id:
            teacher = Teacher.search([("partner_id", "=", user.partner_id.id)], limit=1)

        if not teacher and user.has_group("malakademik_core.group_malakademik_manager"):
            teacher = Teacher.search([], limit=1)

        if not teacher:
            return {
                "teacher": {"name": user.name},
                "cards": {
                    "class_count": 0,
                    "today_lessons": 0,
                    "pending_grading": 0,
                    "unread_notifications": 0,
                },
                "attendance": {"labels": [], "present": [], "absent": []},
                "scores": {"labels": [], "data": []},
                "upcoming": [],
                "teacher_options": [],
                "selected_teacher_id": False,
            }

        Schedule = env["malakademik.schedule"]
        Submission = env["malakademik.assignment.submission"]
        Notification = env.get("malakademik.notification")
        AttendanceLine = env["malakademik.attendance.line"]
        today = fields.Date.today()

        weekday_short = today.strftime("%a").lower()[:3]
        schedules_today = Schedule.search_count([
            ("teacher_id", "=", teacher.id),
            ("day_of_week", "=", weekday_short),
        ])
        pending_submissions = Submission.search_count([
            ("assignment_id.teacher_id", "=", teacher.id),
            ("score", "=", False),
        ])

        notifications_count = 0
        if Notification:
            notifications_count = Notification.search_count([
                ("recipient_teacher_ids", "in", teacher.ids),
                ("state", "=", "draft"),
            ])

        class_count = len(teacher.class_ids)

        attendance_domain = [
            ("attendance_id.classroom_id", "in", teacher.class_ids.ids),
        ]
        attendance_records = AttendanceLine.search(attendance_domain, limit=200, order="attendance_id.date desc")
        attendance_map = {}
        for line in attendance_records:
            if not line.attendance_id.date:
                continue
            date_key = line.attendance_id.date.strftime("%Y-%m-%d")
            day_data = attendance_map.setdefault(date_key, {"present": 0, "absent": 0, "late": 0, "excused": 0})
            day_data[line.status] += 1

        attendance_labels = sorted(attendance_map.keys())[-7:]
        attendance_present = [attendance_map[day]["present"] for day in attendance_labels]
        attendance_absent = [attendance_map[day]["absent"] for day in attendance_labels]

        AssessmentLine = env["malakademik.assessment.line"]
        lines = AssessmentLine.search([
            ("assessment_id.teacher_id", "=", teacher.id),
        ], limit=500)
        score_map = {}
        count_map = {}
        for line in lines:
            subject = line.assessment_id.subject_id.display_name or "Unnamed"
            if subject not in score_map:
                score_map[subject] = 0
                count_map[subject] = 0
            if line.score is not None:
                score_map[subject] += line.score
                count_map[subject] += 1
        score_labels = list(score_map.keys())
        score_values = [round(score_map[name] / count_map[name], 2) if count_map[name] else 0 for name in score_labels]

        weekday_order = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
        schedule_records = Schedule.search([
            ("teacher_id", "=", teacher.id),
        ])
        upcoming = sorted(
            schedule_records,
            key=lambda rec: (
                weekday_order.index(rec.day_of_week) if rec.day_of_week in weekday_order else 0,
                rec.start_time or 0,
            ),
        )[:5]
        upcoming_info = [
            {
                "title": f"{s.subject_id.name or ''} - {s.classroom_id.name or ''}",
                "day": dict(Schedule._fields["day_of_week"].selection).get(s.day_of_week, s.day_of_week.title()),
                "time": f"{int(s.start_time):02d}:{int((s.start_time % 1) * 60):02d} - {int(s.end_time):02d}:{int((s.end_time % 1) * 60):02d}",
            }
            for s in upcoming
        ]

        teacher_options = []
        if user.has_group("malakademik_core.group_malakademik_manager"):
            teacher_options = [
                {"id": t.id, "name": t.name}
                for t in Teacher.search([], order="name")
            ]

        return {
            "teacher": {
                "id": teacher.id,
                "name": teacher.name,
                "subjects": [sub.name for sub in teacher.subject_ids[:6]],
                "classes": [cls.name for cls in teacher.class_ids[:6]],
            },
            "cards": {
                "class_count": class_count,
                "today_lessons": schedules_today,
                "pending_grading": pending_submissions,
                "unread_notifications": notifications_count,
            },
            "attendance": {
                "labels": attendance_labels,
                "present": attendance_present,
                "absent": attendance_absent,
            },
            "scores": {
                "labels": score_labels,
                "data": score_values,
            },
            "upcoming": upcoming_info,
            "teacher_options": teacher_options,
            "selected_teacher_id": teacher.id,
        }
