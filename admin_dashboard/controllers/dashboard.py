import json
from odoo import http
from odoo.http import request, Response
import logging

_logger = logging.getLogger(__name__)


class AdminDashboardController(http.Controller):
    @http.route("/admin_dashboard/stats", type="http", website=True, auth="user", csrf=False)
    def admin_stats(self):
        # import pdb
        # pdb.set_trace()
        _logger.info(
            "--- PYTHON CONTROLLER: admin_stats() method is being executed (CSRF-FIX VERSION) ---")
        env = request.env
        Student = env["malakademik.student"]
        Teacher = env["malakademik.teacher"]
        Parent = env["malakademik.parent"]

        student_count = Student.sudo().search_count([])
        teacher_count = Teacher.sudo().search_count([])
        parent_count = Parent.sudo().search_count([])

        _logger.info(
            "Admin dashboard stats => students: %s, teachers: %s, parents: %s | context=%s",
            student_count,
            teacher_count,
            parent_count,
            env.context,
        )

        response_data = {
            "cards": {
                "student_count": student_count,
                "teacher_count": teacher_count,
                "parent_count": parent_count,
            },
        }
        return Response(
            json.dumps(response_data),
            content_type='application/json',
            status=200,
        )
