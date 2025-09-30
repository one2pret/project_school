/** @odoo-module */

import { registry } from "@web/core/registry";
import { Component, useState, onWillStart, onMounted, onPatched, onWillUnmount } from "@odoo/owl";
import { _t } from "@web/core/l10n/translation";
import { loadJS } from "@web/core/assets";

const actionRegistry = registry.category("actions");

class TeacherDashboard extends Component {
    setup() {
        const services = this.env.services || {};
        this.rpc = services.rpc;
        this.notification = services.notification;
        this.state = useState({
            loading: true,
            data: this._emptyData(),
            teacherOptions: [],
            selectedTeacherId: false,
        });
        this.charts = {};

        onWillStart(async () => {
            await this._ensureChartLoaded();
            await this._loadData();
        });

        onMounted(() => this._renderCharts());
        onPatched(() => this._renderCharts());
        onWillUnmount(() => this._destroyCharts());
    }

    _emptyData() {
        return {
            teacher: { name: "", subjects: [], classes: [] },
            cards: { class_count: 0, today_lessons: 0, pending_grading: 0, unread_notifications: 0 },
            attendance: { labels: [], present: [], absent: [] },
            scores: { labels: [], data: [] },
            upcoming: [],
        };
    }

    async _ensureChartLoaded() {
        if (typeof window.Chart === "undefined") {
            await loadJS("/web/static/lib/Chart/Chart.js");
        }
    }

    async _loadData(teacherId) {
        this.state.loading = true;
        try {
            const payload = this.rpc
                ? await this.rpc("/guru_dashboard/teacher_stats", teacherId ? { teacher_id: teacherId } : {})
                : {};
            const data = payload || {};
            this.state.data = Object.assign(this._emptyData(), data);
            this.state.teacherOptions = data.teacher_options || [];
            this.state.selectedTeacherId = data.selected_teacher_id || (data.teacher && data.teacher.id) || false;
        } catch (error) {
            console.error("Failed to load teacher dashboard", error);
            if (this.notification) {
                this.notification.add(_t("Tidak dapat memuat data dashboard guru."), { type: "danger" });
            }
        } finally {
            this.state.loading = false;
        }
    }

    _destroyCharts() {
        Object.values(this.charts).forEach((chart) => {
            if (chart) {
                chart.destroy();
            }
        });
        this.charts = {};
    }

    _renderCharts() {
        if (this.state.loading || typeof Chart === "undefined" || !this.el) {
            return;
        }
        const attendanceCanvas = this.el.querySelector("#attendanceChart");
        const scoreCanvas = this.el.querySelector("#scoreChart");

        if (attendanceCanvas) {
            this._renderAttendanceChart(attendanceCanvas);
        }
        if (scoreCanvas) {
            this._renderScoreChart(scoreCanvas);
        }
    }

    _renderAttendanceChart(canvas) {
        this._destroyChart("attendance");
        const attendance = this.state.data.attendance || {};
        const labels = attendance.labels || [];
        const present = attendance.present || [];
        const absent = attendance.absent || [];
        this.charts.attendance = new Chart(canvas, {
            type: "line",
            data: {
                labels,
                datasets: [
                    {
                        label: _t("Hadir"),
                        data: present,
                        borderColor: "#5be7a9",
                        backgroundColor: "rgba(91, 231, 169, 0.2)",
                        tension: 0.45,
                        fill: true,
                        pointRadius: 4,
                        pointHoverRadius: 6,
                    },
                    {
                        label: _t("Tidak Hadir"),
                        data: absent,
                        borderColor: "#ff7b7f",
                        backgroundColor: "rgba(255, 123, 127, 0.2)",
                        tension: 0.45,
                        fill: true,
                        pointRadius: 4,
                        pointHoverRadius: 6,
                    },
                ],
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        ticks: { color: "#9fb3c8" },
                        grid: { color: "rgba(80, 110, 140, 0.15)" },
                    },
                    y: {
                        ticks: { color: "#9fb3c8" },
                        grid: { color: "rgba(80, 110, 140, 0.12)" },
                        beginAtZero: true,
                    },
                },
                plugins: {
                    legend: {
                        labels: { color: "#dbe6f4" },
                    },
                },
            },
        });
    }

    _renderScoreChart(canvas) {
        this._destroyChart("score");
        const scores = this.state.data.scores || {};
        const labels = scores.labels || [];
        const data = scores.data || [];
        this.charts.score = new Chart(canvas, {
            type: "bar",
            data: {
                labels,
                datasets: [
                    {
                        label: _t("Nilai Rata-rata"),
                        data,
                        backgroundColor: labels.map((_, index) => `rgba(${75 + index * 20}, 125, 255, 0.65)`),
                        borderRadius: 12,
                        borderSkipped: false,
                    },
                ],
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        ticks: { color: "#9fb3c8" },
                        grid: { display: false },
                    },
                    y: {
                        ticks: { color: "#9fb3c8" },
                        grid: { color: "rgba(80, 110, 140, 0.12)" },
                        beginAtZero: true,
                        suggestedMax: 100,
                    },
                },
                plugins: {
                    legend: {
                        labels: { color: "#dbe6f4" },
                    },
                },
            },
        });
    }

    _destroyChart(name) {
        if (this.charts[name]) {
            this.charts[name].destroy();
            this.charts[name] = undefined;
        }
    }

    _onTeacherChange(ev) {
        const value = ev.target.value ? parseInt(ev.target.value, 10) : false;
        this.state.selectedTeacherId = value;
        this._loadData(value);
    }

    get greeting() {
        const hours = new Date().getHours();
        if (hours < 11) {
            return _t("Selamat pagi");
        }
        if (hours < 15) {
            return _t("Selamat siang");
        }
        if (hours < 18) {
            return _t("Selamat sore");
        }
        return _t("Selamat malam");
    }

    get currentDate() {
        return new Intl.DateTimeFormat(undefined, {
            weekday: "long",
            day: "numeric",
            month: "long",
            year: "numeric",
        }).format(new Date());
    }
}

TeacherDashboard.template = "guru_dashboard.TeacherDashboard";
actionRegistry.add("guru_dashboard.teacher_dashboard", TeacherDashboard);

export default TeacherDashboard;
