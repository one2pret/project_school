# MalAkademik Core (Odoo 18)

Ringkasan
- Modul inti akademik: jadwal, absensi, penilaian, rapor, tugas, kurikulum, profil siswa/guru/orang tua, dan notifikasi.
- Siap pakai dengan i18n (ID) dan wizard generator data contoh.

Fitur Utama
- Jadwal pelajaran per kelas & guru (Schedule)
- Absensi siswa manual (Attendance + Lines)
- Penilaian dan rapor digital (Assessment/Report Card)
- Tugas & upload dokumen siswa (Assignment/Submission)
- Pengelolaan kurikulum & mata pelajaran (Curriculum/Subject)
- Profil Siswa, Guru, Orang Tua + tautan ke Contacts (`res.partner`)
- Notifikasi akademik & administratif (mail.thread)

Kebutuhan & Dependensi
- Odoo 18
- depends: `base`, `mail`

Instalasi
- Pastikan path module berada dalam `addons_path` di `odoo.conf`.
- Apps > Update Apps List > Install “MalAkademik Core”.

Hak Akses & Menu
- Groups: `Academic User`, `Academic Manager` (lihat `security/groups.xml`).
- Menu Root: “Academics” berisi Master Data, Operations, Communication, Tools.
- Menu dibatasi untuk grup di atas. Beri grup ke user agar menu terlihat.

Model Inti (Overview)
- `malakademik.student` (+ `malakademik.student.history`) — Profil siswa, riwayat akademik.
- `malakademik.teacher` — Profil guru.
- `malakademik.parent` — Orang tua/wali, relasi ke siswa.
- `malakademik.classroom` — Kelas (nama, tingkat, wali kelas).
- `malakademik.curriculum` / `malakademik.subject` — Kurikulum dan mata pelajaran.
- `malakademik.schedule` — Jadwal (kelas, mapel, guru, hari, jam).
- `malakademik.attendance` + `malakademik.attendance.line` — Absensi & detil.
- `malakademik.assessment` + `malakademik.assessment.line` — Penilaian & nilai per siswa.
- `malakademik.report.card` + `malakademik.report.card.line` — Rapor & nilai per mapel.
- `malakademik.assignment` + `malakademik.assignment.submission` — Tugas & pengumpulan (dokumen).
- `malakademik.notification` — Notifikasi, state draft/sent, penerima siswa/orang tua/guru.

Integrasi Contacts
- `student`, `teacher`, `parent` memiliki `partner_id` (M2o ke `res.partner`).
- `email`/`phone` tersinkron via related ke contact.

Berkas Penting
- Manifest: `__manifest__.py`
- Keamanan: `security/groups.xml`, `security/ir.model.access.csv`
- Views:
  - Menus & actions: `views/menus.xml`
  - Student/Teacher/Parent/etc: `views/*_views.xml`
  - Wizard demo: `views/demo_wizard_views.xml`
- Models: `models/*.py`
- Demo wizard: `models/demo_wizard.py`
- Demo data (opsional): `demo/demo.xml`
- Terjemahan: `i18n/id.po`
- Catatan problem solving: `PROBLEM_SOLVING.md`

Demo Data
- Opsi A: Buat DB dengan demo data aktif (atau upgrade dengan `--load-demo=1`) untuk memuat `demo/demo.xml`.
- Opsi B (disarankan): gunakan wizard “Generate Sample Data” (Academics > Tools) — idempotent, bisa diulang.

Terjemahan (i18n)
- File `i18n/id.po` mengikuti pola Odoo (referensi `model_terms` dan `ir.model.fields`).
- Update via Settings > Translations > Load/Update (id_ID) atau upgrade modul.

Pengembangan
- Tambah field: definisikan di model, tambahkan ke views, tambahkan ACL bila perlu, dan lengkapi terjemahan di PO.
- Action/menu: definisikan action lebih dulu (di `menus.xml` blok atas), kemudian tautkan pada `<menuitem action="..."/>`.
- Validasi: jalankan upgrade modul untuk memuat perubahan; gunakan Developer Mode untuk debug UI.

Known Issues & Solusi
- Lihat `PROBLEM_SOLVING.md` untuk ringkasan error dan perbaikannya (load order actions/menus, i18n loader, dsb).

Lisensi
- LGPL-3 (lihat `__manifest__.py`).
