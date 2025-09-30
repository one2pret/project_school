# Guru Dashboard (Odoo 18)

Ringkasan
- Dashboard interaktif untuk guru dengan tampilan modern bertema gelap.
- Dibangun menggunakan OWL (Odoo Web Library) dan Chart.js.
- Menyajikan statistik kelas, jadwal hari ini, tugas yang perlu dinilai, notifikasi, tren kehadiran, rata-rata nilai, dan agenda mengajar mendatang.

Fitur
- Widget OWL sebagai client action (`guru_dashboard.teacher_dashboard`).
- Konsumsi data via endpoint JSON `/guru_dashboard/teacher_stats` dengan agregasi dari modul `malakademik_core`.
- Dua grafik Chart.js (line dan bar) + kartu statistik responsif.
- Styling khusus melalui SCSS untuk nuansa dark mode yang konsisten.

Instalasi
1. Pastikan modul berada di `addons_path` Odoo.
2. Update daftar aplikasi lalu instal "Guru Dashboard".
3. Menu baru "Teacher Dashboard" akan muncul di bawah menu Academics.

Cara Pakai
- Pastikan pengguna login terhubung ke record `malakademik.teacher` (relasi partner).
- Buka menu Academics > Teacher Dashboard untuk melihat widget.
- Data otomatis tersinkron berdasarkan jadwal, absensi, penilaian, dan notifikasi yang ada di `malakademik_core`.

Catatan Pengembangan
- Asset bundle dimuat melalui `web.assets_backend` (Chart.js, JS OWL, SCSS, QWeb template).
- Endpoint controller berada di `controllers/dashboard.py` dan berjalan dengan `sudo()` untuk konsistensi data.
- Bila menambah metrik baru, perluas struktur payload di controller, komponen OWL, dan template QWeb secara sinkron.
- Gunakan `actionRegistry.add("guru_dashboard.teacher_dashboard", ...)` untuk mendaftarkan widget aksi.

Lisensi
- Mengikuti lisensi modul induk: LGPL-3.
