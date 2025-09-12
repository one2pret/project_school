# Roadmap & TODO — Sistem Informasi Akademik (SIA)

Tujuan
- Menyelaraskan pengembangan MalAkademik Core dengan regulasi nasional (Dapodik, Permendikbud, Diknas).
- Menyediakan checklist implementasi bertahap beserta kriteria penerimaan (acceptance criteria).

Legenda Status
- [x] Selesai (basis/fondasi tersedia)
- [~] Parsial (fitur dasar ada, perlu pengayaan/penyesuaian regulasi)
- [ ] Belum dikerjakan

Prioritas
- P0: Kritis/regulasi/P1 integrasi utama
- P1: Wajib operasional semester berjalan
- P2: Peningkatan kualitas & pelaporan

1) Manajemen Data Peserta Didik (P0)
- [~] Profil siswa (NISN, nama, alamat, TTL, status, foto)
  - Acceptance: Field NISN (unik, validasi panjang), TTL, alamat, status aktif, foto (image) tersedia di form siswa.
  - Implement: model `malakademik.student` (tambahkan `nisn`, `image_1920`, `birth_place`, `status`).
- [ ] Riwayat sekolah masuk/keluar (mutasi internal/eksternal)
  - Acceptance: Riwayat tersimpan di `malakademik.student.history` dengan tipe peristiwa (masuk/keluar), asal/tujuan.
- [ ] Validasi dan formatter NISN + mapping Dapodik
  - Acceptance: Constraint NISN numerik 10 digit; export template sesuai Dapodik.
  - Task: `tasks/SIA-01.md`

2) Manajemen Data Guru & Tendik (P0)
- [~] Profil guru/pegawai (NIP, nama, jabatan, kepegawaian)
  - Acceptance: Field NIP unik, jabatan (selection), status kepegawaian.
- [ ] Rekam sertifikasi, pendidikan terakhir, tugas tambahan (walikelas/kepsek)
  - Acceptance: Tab riwayat sertifikasi/pendidikan; relasi tugas tambahan.
- [ ] Link Dapodik/Verval PTK (ekspor siap unggah)
  - Acceptance: Export CSV sesuai spesifikasi; validasi data wajib.
  - Task: `tasks/SIA-02.md`

3) Kelas & Pembelajaran (P0)
- [x] Rombel/kelas (create/edit/archive) dan guru walikelas
- [~] Kurikulum, mapel, KD/KI (standar isi)
  - Acceptance: Struktur KD/KI per mapel/kelas; relasi ke penilaian.
- [x] Peserta kelas dan guru pengampu mapel (melalui schedule & M2M guru-kelas)
  - Task: `tasks/SIA-03.md`

4) Nilai & Rapor (P0)
- [~] Input nilai harian/mid/akhir semester oleh guru
  - Acceptance: Tipe penilaian (harian/PTS/PAS) + bobot.
- [~] Hitung dan cetak rapor (format nasional, PDF)
  - Acceptance: Report QWeb rapor per siswa per semester (template nasional dasar).
- [ ] Rekap & pelaporan hasil belajar (format Dapodik)
  - Acceptance: Export nilai mapel per kelas sesuai kolom Dapodik.
  - Task: `tasks/SIA-04.md`

5) Absensi Siswa & Guru (P1)
- [x] Input absensi harian per kelas
- [ ] Rekap kehadiran dan pelaporan absensi untuk dinas (format standar)
- [ ] Dashboard monitoring absensi (filter periode/kelas/guru)

6) Mutasi & Alumni (P1)
- [ ] Proses mutasi masuk/keluar (antar sekolah) dengan dokumen pendukung
- [ ] Penandaan status alumni dan data ringkas pasca lulus

7) Layanan Data Pendidik & Kependidikan (P1)
- [ ] Data sertifikasi/pangkat/pendidikan terakhir guru/staf (riwayat)
- [ ] Integrasi layanan (Dapodik/API Simpadu) — starter exporter

8) Laporan & Rekap (P1)
- [ ] Laporan siswa/guru/kelas (excel/pdf) — daftar dan rekap
- [ ] Laporan nilai/absensi/alumni — filter akademik (tahun/semester/kelas)

9) Pelaporan Dapodik/Diknas (P0)
- [ ] Ekspor data siap upload (CSV/XLSX) — siswa, PTK, rombel, nilai, absensi
- [ ] Validator kesesuaian format sebelum sinkronisasi
  - Task: `tasks/SIA-09.md`

10) Keamanan & Hak Akses (P0)
- [x] Sistem login multi-user (Odoo default) dan grup: User/Manager Akademik
- [ ] Matrix peran detail (admin, guru, wali kelas, operator sekolah)
  - Acceptance: Akses CRUD sesuai peran; menu dibatasi grup.
- [ ] Audit trail & log kegiatan (mail.thread + chatter, plus auditlog opsional)
- [ ] SOP backup data (dokumentasi + jadwal cron backup jika diperlukan)
  - Task: `tasks/SIA-10.md`

Tambahan Teknis (Penunjang)
- [ ] Penomoran dokumen (sequence) untuk rapor/penilaian
- [ ] Constraint jadwal (deteksi bentrok kelas/guru)
- [ ] Wizard impor siswa/guru dari Excel (template)
- [ ] Generator data contoh (sudah ada) — tambah opsi rentang tanggal/kelas

Dokumen & I18n
- [x] README, Developer Guide, Problem Solving
- [x] i18n Bahasa Indonesia untuk menu/field utama
- [ ] Lengkapi i18n untuk seluruh view/field setelah stabil (export translation lalu edit)

Catatan Implementasi
- Model & Views saat ini: fondasi CRUD tersedia untuk siswa/guru/orangtua/kelas/mapel/kurikulum/jadwal/absensi/penilaian/rapor/tugas/notifikasi.
- Integrasi `res.partner`: sinkron nama/email/telepon; pertimbangkan sinkron dua arah untuk perubahan nama.
- Pelaporan & ekspor Dapodik: butuh spesifikasi kolom terbaru — susun mapping dan template ekspor.

Rencana Iterasi (saran)
- Iterasi 1 (P0): NISN/NIP + validator, struktur KD/KI, tipe penilaian, role matrix, ekspor dasar siswa/PTK/rombel.
- Iterasi 2 (P1): dashboard absensi, rekap laporan excel/pdf, mutasi & alumni, sertifikasi/pangkat.
- Iterasi 3 (P2): validasi Dapodik lanjutan, auditlog, SOP backup, impor excel, sequence dokumen.

\

Format Tugas (Template)
- ID: SIA-<no>
- Judul: <singkat, padat>
- Prioritas: P0/P1/P2
- Deskripsi singkat: <1–2 kalimat>
- Acceptance Criteria:
  - [ ] …
  - [ ] …
- Perubahan Teknis (ceklist):
  - [ ] Model: … (file: models/…)
  - [ ] Views: … (file: views/…)
  - [ ] Security: ACL/Groups/Rules (file: security/…)
  - [ ] i18n: tambah entri PO (file: i18n/id.po)
  - [ ] Export/Report: CSV/XLSX/QWeb (file: report/… | export/…)
  - [ ] Demo/Test: wizard/demo data/unit manual
- Dampak & Risiko: <opsional>
- Estimasi: <xx jam>
- Catatan: link spesifikasi/regulasi (Dapodik/Permendikbud)

Breakdown Tugas Per Item

SIA-01 Manajemen Data Peserta Didik (P0)
- Acceptance:
  - [ ] NISN 10 digit unik, validasi numerik.
  - [ ] TTL (tempat/tanggal lahir), alamat, status aktif, foto.
  - [ ] Riwayat masuk/keluar tercatat.
  - [ ] Ekspor siswa (CSV) format Dapodik (minimal kolom wajib).
- Perubahan Teknis:
  - [ ] Model: `malakademik.student` tambah `nisn:char`, `birth_place:char`, `image_1920:binary`, `status:selection` (aktif/nonaktif). (models/student.py)
  - [ ] Constraint: SQL/py constraint unik `nisn`, validator panjang/numeric. (models/student.py)
  - [ ] Views: tampilkan field baru, gambar, smart button ke history. (views/student_views.xml)
  - [ ] Student History: tambah `event_type` (masuk/keluar), `school_name`, `date`. (models/student.py + views)
  - [ ] Export: action server ekspor CSV “Export Siswa (Dapodik)”. (actions + python helper/export)
  - [ ] i18n: label baru.
  - [ ] Demo/Test: generator wizard opsi buat nisn acak valid.
- Estimasi: 8–12 jam.

SIA-02 Manajemen Data Guru & Tendik (P0)
- Acceptance:
  - [ ] NIP unik, jabatan, status kepegawaian.
  - [ ] Riwayat sertifikasi, pendidikan terakhir, tugas tambahan (wali/ks).
  - [ ] Ekspor PTK (CSV) dasar Dapodik.
- Perubahan Teknis:
  - [ ] Model: `malakademik.teacher` tambah `nip`, `position`, `employment_status`. (models/teacher.py)
  - [ ] Sub-model: `teacher.cert`, `teacher.education` (riwayat). (models/new)
  - [ ] Views: tab Sertifikasi/Pendidikan; penugasan wali kelas refer ke classroom. (views/teacher_views.xml)
  - [ ] Export: CSV PTK sederhana. (export)
  - [ ] i18n, ACL.
- Estimasi: 10–14 jam.

SIA-03 Kelas & Pembelajaran (P0)
- Acceptance:
  - [ ] CRUD kelas/rombel, homeroom.
  - [ ] Struktur kurikulum, mapel, KD/KI per kelas/mapel.
  - [ ] Peserta kelas terdaftar.
- Perubahan Teknis:
  - [ ] Model: tambah `malakademik.kd` (kompetensi dasar) relasi subject+grade. (models/new)
  - [ ] Views: formulir KD/KI, relasi ke Assessment. (views/new)
  - [ ] Wizard assign siswa ke kelas massal. (wizard/new)
  - [ ] i18n, ACL.
- Estimasi: 10–16 jam.

SIA-04 Nilai & Rapor (P0)
- Acceptance:
  - [ ] Tipe penilaian: Harian/PTS/PAS dengan bobot.
  - [ ] Perhitungan nilai akhir per mapel/rapor.
  - [ ] Cetak rapor (QWeb) format nasional dasar (PDF).
- Perubahan Teknis:
  - [ ] Model: `malakademik.assessment` tambah `type` (harian/pts/pas), `weight` dan compute agregasi. (models/assessment.py)
  - [ ] Report: QWeb rapor; action cetak di report card. (report/qweb + server action)
  - [ ] Views: tombol “Generate Report Card” per kelas/semester. (views/report_card_views.xml)
  - [ ] i18n.
- Estimasi: 16–24 jam.

SIA-05 Absensi Siswa & Guru (P1)
- Acceptance:
  - [ ] Rekap absensi per siswa/kelas/periode.
  - [ ] Dashboard monitoring sederhana.
- Perubahan Teknis:
  - [ ] Model: agregasi attendance -> rekap. (compute/stored model)
  - [ ] Views: kanban/dashboard, graph/pivot untuk analitik. (views)
  - [ ] Export: laporan rekap CSV/PDF.
- Estimasi: 10–14 jam.

SIA-06 Mutasi & Alumni (P1)
- Acceptance: proses mutasi masuk/keluar; penandaan alumni.
- Perubahan Teknis:
  - [ ] Wizard mutasi (masuk/keluar) ubah class/status & history event. (wizard)
  - [ ] Student: status alumni + tahun lulus. (models)
  - [ ] Views tombol Mutasi/Alumni. (views)
- Estimasi: 8–12 jam.

SIA-07 Layanan Data PTK (P1)
- Acceptance: riwayat sertifikasi/pangkat/pendidikan; exporter layanan.
- Perubahan Teknis:
  - [ ] Tambah sub-model & views riwayat. (models/views)
  - [ ] Export CSV sesuai spesifikasi awal. (export)
- Estimasi: 10–14 jam.

SIA-08 Laporan & Rekap (P1)
- Acceptance: laporan siswa/guru/kelas/nilai/absensi/alumni (Excel/PDF) dengan filter akademik.
- Perubahan Teknis:
  - [ ] XLSX export helpers; QWeb PDF untuk beberapa laporan. (report/export)
  - [ ] Menu Laporan & wizard filter. (views/wizard)
- Estimasi: 12–18 jam.

SIA-09 Pelaporan Dapodik/Diknas (P0)
- Acceptance: paket ekspor siap unggah; validator format.
- Perubahan Teknis:
  - [ ] Modul kecil `malakademik_dapodik_export` terpisah (opsional) untuk format spesifik. (addon terpisah)
  - [ ] Validator schema (csv header/kolom wajib). (python helper)
- Estimasi: 16–24 jam (bergantung spesifikasi terbaru).

SIA-10 Keamanan & Hak Akses (P0)
- Acceptance: matrix peran (admin, guru, wali kelas, operator); audit & backup SOP.
- Perubahan Teknis:
  - [ ] Tambah groups per peran & ACL per model. (security)
  - [ ] Record rules bila perlu (pembatasan per kelas/guru). (security)
  - [ ] Dokumen SOP backup + (opsional) cron skrip backup. (docs/cron)
- Estimasi: 8–12 jam.
