{
    "name": "Admin Dashboard",
    "version": "18.0.1.0.0",
    "summary": "Dashboard administratif untuk Akademik",
    "category": "Education",
    "author": "mochwawankurnia@gmail.com",
    "license": "LGPL-3",
    "depends": ["web", "malakademik_core"],
    "data": [
        "views/admin_dashboard_views.xml"
    ],
    "assets": {
        "web.assets_backend": [
            "admin_dashboard/static/src/scss/admin_dashboard.scss",
            "admin_dashboard/static/src/components/admin_dashboard.js",
            "admin_dashboard/static/src/xml/admin_dashboard_templates.xml"
        ],
        "web.assets_qweb": []
    },
    "installable": True,
    "application": False,
}
