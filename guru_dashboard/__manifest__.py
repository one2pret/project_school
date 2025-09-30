{
    "name": "Guru Dashboard",
    "version": "18.0.1.0.0",
    "summary": "Dashboard modern untuk guru dengan OWL dan Chart.js",
    "category": "Education",
    "author": "mochwawankurnia@gmail.com",
    "license": "LGPL-3",
    "depends": ["web", "malakademik_core"],
    "data": [
        "views/teacher_dashboard_views.xml"
    ],
    "assets": {
        "web.assets_backend": [
            "guru_dashboard/static/src/scss/teacher_dashboard.scss",
            "guru_dashboard/static/src/components/teacher_dashboard.js",
            "guru_dashboard/static/src/xml/teacher_dashboard_templates.xml"
        ],
        "web.assets_qweb": [
            "guru_dashboard/static/src/xml/teacher_dashboard_templates.xml"
        ]
    },
    "installable": True,
    "application": False,
}
