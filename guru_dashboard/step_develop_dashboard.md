# Langkah Pengembangan Guru Dashboard (Odoo 18)

## 1. Setup Modul
- Buat folder `guru_dashboard` dalam `workspace_dev/project_school`.
- Tambahkan `__manifest__.py`, `__init__.py`, struktur `controllers/`, `static/src/{components,scss,xml}`, dan `views/`.
- Isi manifest dengan dependensi `web` dan `malakademik_core`, daftarkan asset JS/SCSS/QWeb serta action client di `views/teacher_dashboard_views.xml`.

## 2. Endpoint Data
- Tambahkan controller `controllers/dashboard.py` dengan route JSON `/guru_dashboard/teacher_stats`.
- Di handler, identifikasi guru aktif berdasarkan user login (atau parameter admin), ambil statistik: jumlah kelas, jadwal hari ini, penilaian pending, notifikasi, ringkasan absensi, nilai rata-rata, dan jadwal mendatang.
- Pastikan record rule di `malakademik_core/security/record_rules.xml` membatasi data sesuai peran.

## 3. Komponen OWL
- Buat `static/src/components/teacher_dashboard.js` yang mendaftarkan action `guru_dashboard.teacher_dashboard`.
- Manfaatkan OWL `Component` + `useState`, akses layanan via `this.env.services`, load Chart.js, dan panggil RPC.
- Tangani fallback ketika service tidak tersedia dan render chart di lifecycle.

## 4. Template QWeb
- Kembangkan `static/src/xml/teacher_dashboard_templates.xml` untuk menampilkan header, stat card, chart `<canvas>`, dan daftar agenda.
- Gunakan ekspresi aman `(state.data.cards && state.data.cards.field) || 0`.

## 5. Styling
- Tambahkan SCSS dark theme di `static/src/scss/teacher_dashboard.scss` (grid stat card, card chart, list agenda).

## 6. Integrasi Menu
- Tambahkan menu `Teacher Dashboard` di `malakademik_core/views/menus.xml` sebagai `ir.actions.client`.

## 7. Pengujian
- Upgrade modul `guru_dashboard` (`-u guru_dashboard`) dan reload assets.
- Gunakan DevTools untuk memastikan `/guru_dashboard/teacher_stats` merespons 200 dan JSON benar.
- uji akses guru vs admin.

## 8. Debugging
- Simpan file dalam UTF-8.
- Hindari `&&` di template; gunakan ternary.
- Pastikan Chart.js termuat sebelum render.

## 9. Pengembangan Lanjutan
- Tambahkan filter periode, selector guru, highlight, eksport.
