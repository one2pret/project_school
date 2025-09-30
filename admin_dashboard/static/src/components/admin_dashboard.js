
/** @odoo-module */

import { registry } from "@web/core/registry"
import { Component, useState, onWillStart } from "@odoo/owl"
import { useService } from "@web/core/utils/hooks"
import { _t } from "@web/core/l10n/translation"

const actionRegistry = registry.category("actions")

class AdminDashboard extends Component {
    static props = {
        action: { type: Object, optional: true },
        actionId: { type: Number, optional: true },
        updateActionState: { type: Function, optional: true },
        className: { type: String, optional: true },
    }

    setup() {
        // Rpc service is not available, using http as a workaround
        this.http = useService("http")
        this.notification = useService("notification")

        this.state = useState({
            loading: true,
            cards: {
                student_count: 0,
                teacher_count: 0,
                parent_count: 0,
            },
        })

        onWillStart(this._loadData.bind(this))
    }

    async _loadData() {
        this.state.loading = true
        try {
            // Using http.post as a workaround for missing rpc service
            const data = await this.http.post("/admin_dashboard/stats", {})
            const cards = data.cards || {};
            Object.assign(this.state.cards, {
                student_count: cards.student_count || 0,
                teacher_count: cards.teacher_count || 0,
                parent_count: cards.parent_count || 0,
            })
        } catch (error) {
            console.error("Failed to load admin dashboard", error)
            this._notify(_t("Gagal memuat data Admin Dashboard."), "danger")
        } finally {
            this.state.loading = false
        }
    }

    _notify(message, type) {
        if (this.notification) {
            this.notification.add(message, { type })
        } else if (type === "danger") {
            console.error(message)
        } else {
            console.warn(message)
        }
    }
}

AdminDashboard.template = "admin_dashboard.AdminDashboard"
actionRegistry.add("admin_dashboard.admin_dashboard", AdminDashboard)

export default AdminDashboard
