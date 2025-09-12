from odoo import api, fields, models, _


class MalAkademikDemoWizard(models.TransientModel):
    _name = "malakademik.demo.wizard"
    _description = "Generate Sample Academic Data"

    generate_students = fields.Boolean(string="Students/Parents", default=True)
    generate_teachers = fields.Boolean(string="Teachers", default=True)
    generate_schedule = fields.Boolean(string="Schedules & Attendance", default=True)
    generate_assessment = fields.Boolean(string="Assessments & Report Cards", default=True)
    generate_assignments = fields.Boolean(string="Assignments & Notifications", default=True)

    def _get_or_create(self, model, search_domain, create_vals):
        rec = self.env[model].search(search_domain, limit=1)
        if rec:
            return rec
        return self.env[model].create(create_vals)

    def action_generate(self):
        self.ensure_one()
        env = self.env

        # Curriculum
        curriculum = self._get_or_create(
            "malakademik.curriculum",
            [("name", "=", "Kurikulum 2024")],
            {"name": "Kurikulum 2024", "year": "2024", "description": "Kurikulum contoh tahun 2024"},
        )

        # Subjects
        sub_mat = self._get_or_create(
            "malakademik.subject", [("code", "=", "MAT")], {"name": "Matematika", "code": "MAT", "curriculum_id": curriculum.id}
        )
        sub_sci = self._get_or_create(
            "malakademik.subject", [("code", "=", "SCI")], {"name": "IPA", "code": "SCI", "curriculum_id": curriculum.id}
        )
        sub_ind = self._get_or_create(
            "malakademik.subject", [("code", "=", "IND")], {"name": "Bahasa Indonesia", "code": "IND", "curriculum_id": curriculum.id}
        )

        # Classes
        cls_7a = self._get_or_create("malakademik.classroom", [("name", "=", "Kelas 7A")], {"name": "Kelas 7A", "grade": "7"})
        cls_7b = self._get_or_create("malakademik.classroom", [("name", "=", "Kelas 7B")], {"name": "Kelas 7B", "grade": "7"})

        # Teachers
        tch_andika = None
        tch_sri = None
        if self.generate_teachers:
            tch_andika = self._get_or_create(
                "malakademik.teacher",
                [("employee_code", "=", "T001")],
                {
                    "name": "Andika Pratama",
                    "employee_code": "T001",
                    "email": "andika@example.com",
                    "phone": "0811111111",
                    "subject_ids": [(6, 0, [sub_mat.id, sub_sci.id])],
                },
            )
            tch_sri = self._get_or_create(
                "malakademik.teacher",
                [("employee_code", "=", "T002")],
                {
                    "name": "Sri Wahyuni",
                    "employee_code": "T002",
                    "email": "sri@example.com",
                    "phone": "0822222222",
                    "subject_ids": [(6, 0, [sub_ind.id])],
                },
            )
            # Homeroom
            if not cls_7a.homeroom_teacher_id:
                cls_7a.homeroom_teacher_id = tch_sri.id
            if not cls_7b.homeroom_teacher_id:
                cls_7b.homeroom_teacher_id = tch_andika.id
            # Link teachers to classes
            if tch_andika:
                tch_andika.class_ids = [(4, cls_7a.id), (4, cls_7b.id)]
            if tch_sri:
                tch_sri.class_ids = [(4, cls_7a.id)]

        # Parents and Students
        if self.generate_students:
            par_budi = self._get_or_create(
                "malakademik.parent",
                [("name", "=", "Budi Santoso")],
                {"name": "Budi Santoso", "relation": "father", "phone": "0813333333"},
            )
            par_ani = self._get_or_create(
                "malakademik.parent",
                [("name", "=", "Ani Lestari")],
                {"name": "Ani Lestari", "relation": "mother", "phone": "0814444444"},
            )
            stu_ahmad = self._get_or_create(
                "malakademik.student",
                [("student_id", "=", "S001")],
                {
                    "name": "Ahmad Fauzi",
                    "student_id": "S001",
                    "class_id": cls_7a.id,
                    "gender": "male",
                    "parent_ids": [(6, 0, [par_budi.id, par_ani.id])],
                },
            )
            stu_siti = self._get_or_create(
                "malakademik.student",
                [("student_id", "=", "S002")],
                {
                    "name": "Siti Nurhaliza",
                    "student_id": "S002",
                    "class_id": cls_7a.id,
                    "gender": "female",
                    "parent_ids": [(6, 0, [par_budi.id])],
                },
            )
            stu_eko = self._get_or_create(
                "malakademik.student",
                [("student_id", "=", "S003")],
                {"name": "Eko Prasetyo", "student_id": "S003", "class_id": cls_7b.id, "gender": "male"},
            )
        else:
            stu_ahmad = env["malakademik.student"].search([("student_id", "=", "S001")], limit=1)
            stu_siti = env["malakademik.student"].search([("student_id", "=", "S002")], limit=1)

        # Schedules
        if self.generate_schedule and (tch_andika or env["malakademik.teacher"].search([("employee_code", "=", "T001")], limit=1)):
            tch_andika = tch_andika or env["malakademik.teacher"].search([("employee_code", "=", "T001")], limit=1)
            tch_sri = tch_sri or env["malakademik.teacher"].search([("employee_code", "=", "T002")], limit=1)
            self._get_or_create(
                "malakademik.schedule",
                [("classroom_id", "=", cls_7a.id), ("subject_id", "=", sub_mat.id), ("day_of_week", "=", "mon"), ("start_time", "=", 8.0)],
                {"classroom_id": cls_7a.id, "subject_id": sub_mat.id, "teacher_id": tch_andika.id, "day_of_week": "mon", "start_time": 8.0, "end_time": 9.5},
            )
            self._get_or_create(
                "malakademik.schedule",
                [("classroom_id", "=", cls_7a.id), ("subject_id", "=", sub_ind.id), ("day_of_week", "=", "tue"), ("start_time", "=", 9.5)],
                {"classroom_id": cls_7a.id, "subject_id": sub_ind.id, "teacher_id": tch_sri.id, "day_of_week": "tue", "start_time": 9.5, "end_time": 11.0},
            )

            # Attendance example (if students exist)
            if stu_ahmad and stu_siti:
                att = self._get_or_create(
                    "malakademik.attendance",
                    [("date", "=", "2024-09-10"), ("classroom_id", "=", cls_7a.id)],
                    {"date": "2024-09-10", "classroom_id": cls_7a.id},
                )
                # lines
                existing_ahmad = env["malakademik.attendance.line"].search([("attendance_id", "=", att.id), ("student_id", "=", stu_ahmad.id)], limit=1)
                if not existing_ahmad:
                    env["malakademik.attendance.line"].create({"attendance_id": att.id, "student_id": stu_ahmad.id, "status": "present"})
                existing_siti = env["malakademik.attendance.line"].search([("attendance_id", "=", att.id), ("student_id", "=", stu_siti.id)], limit=1)
                if not existing_siti:
                    env["malakademik.attendance.line"].create({"attendance_id": att.id, "student_id": stu_siti.id, "status": "late", "remarks": "Terlambat karena hujan"})

        # Assessment & Report Card
        if self.generate_assessment and (tch_andika or env["malakademik.teacher"].search([("employee_code", "=", "T001")], limit=1)):
            tch_andika = tch_andika or env["malakademik.teacher"].search([("employee_code", "=", "T001")], limit=1)
            asm = self._get_or_create(
                "malakademik.assessment",
                [("name", "=", "Ulangan Tengah Semester - Matematika"), ("classroom_id", "=", cls_7a.id)],
                {"name": "Ulangan Tengah Semester - Matematika", "date": "2024-10-01", "subject_id": sub_mat.id, "teacher_id": tch_andika.id, "classroom_id": cls_7a.id},
            )
            # add lines if not exists
            if stu_ahmad:
                if not env["malakademik.assessment.line"].search([("assessment_id", "=", asm.id), ("student_id", "=", stu_ahmad.id)], limit=1):
                    env["malakademik.assessment.line"].create({"assessment_id": asm.id, "student_id": stu_ahmad.id, "score": 85, "notes": "Baik"})
            if stu_siti:
                if not env["malakademik.assessment.line"].search([("assessment_id", "=", asm.id), ("student_id", "=", stu_siti.id)], limit=1):
                    env["malakademik.assessment.line"].create({"assessment_id": asm.id, "student_id": stu_siti.id, "score": 92, "notes": "Sangat baik"})

            # Report card for Ahmad
            if stu_ahmad:
                rc = self._get_or_create(
                    "malakademik.report.card",
                    [("student_id", "=", stu_ahmad.id), ("term", "=", "Ganjil"), ("year", "=", "2024")],
                    {"student_id": stu_ahmad.id, "term": "Ganjil", "year": "2024"},
                )
                if not env["malakademik.report.card.line"].search([("report_id", "=", rc.id), ("subject_id", "=", sub_mat.id)], limit=1):
                    env["malakademik.report.card.line"].create({"report_id": rc.id, "subject_id": sub_mat.id, "score": 86, "grade": "B+"})
                if not env["malakademik.report.card.line"].search([("report_id", "=", rc.id), ("subject_id", "=", sub_ind.id)], limit=1):
                    env["malakademik.report.card.line"].create({"report_id": rc.id, "subject_id": sub_ind.id, "score": 88, "grade": "A-"})

        # Assignment & Notification
        if self.generate_assignments and (tch_andika or env["malakademik.teacher"].search([("employee_code", "=", "T001")], limit=1)):
            tch_andika = tch_andika or env["malakademik.teacher"].search([("employee_code", "=", "T001")], limit=1)
            asg = self._get_or_create(
                "malakademik.assignment",
                [("name", "=", "PR Matematika Bab 1"), ("classroom_id", "=", cls_7a.id)],
                {"name": "PR Matematika Bab 1", "subject_id": sub_mat.id, "teacher_id": tch_andika.id, "classroom_id": cls_7a.id, "due_date": "2024-10-05 17:00:00", "description": "Kerjakan soal 1-10 di buku paket."},
            )
            self._get_or_create(
                "malakademik.notification",
                [("name", "=", "Pengumuman Jadwal Ujian")],
                {
                    "name": "Pengumuman Jadwal Ujian",
                    "message": "Ujian tengah semester akan dimulai tanggal 1 Oktober.",
                    "recipient_student_ids": [(6, 0, env["malakademik.student"].search([("class_id", "=", cls_7a.id)]).ids)],
                    "state": "draft",
                    "scheduled_date": "2024-09-25 08:00:00",
                },
            )

        # Notify user (webclient notification)
        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": _("Success"),
                "message": _("Sample data generated (idempotent)."),
                "type": "success",
                "sticky": False,
            },
        }
