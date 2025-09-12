# SIA-01 — Manajemen Data Peserta Didik (P0)

- ID: SIA-01
- Judul: Manajemen Data Peserta Didik (Profil, Riwayat, Ekspor Dapodik)
- Prioritas: P0
- Deskripsi singkat: Tambahkan field wajib (NISN, TTL, foto, status), riwayat masuk/keluar, dan ekspor data siswa format Dapodik.

Acceptance Criteria
- [ ] NISN 10 digit, unik, numerik; validasi saat create/write.
- [ ] Field TTL: `birth_place`, `birth_date`; `image_1920` untuk foto; `status` (aktif/nonaktif).
- [ ] Riwayat di `malakademik.student.history`: event masuk/keluar, sekolah asal/tujuan, tanggal.
- [ ] Ekspor CSV siswa dengan kolom minimal Dapodik (NISN, Nama, JK, TTL, Alamat, Status, Kelas).
- [ ] Label/terjemahan ID tersedia di `i18n/id.po`.

Perubahan Teknis
- [ ] Model: `models/student.py`
  - Tambah fields: `nisn = fields.Char(...)`, `birth_place = fields.Char(...)`, `image_1920 = fields.Image(...)`, `status = fields.Selection([('active','Active'),('inactive','Inactive')], ...)`.
  - Constraint unik `nisn`; python constraint validasi digit/length.
  - `malakademik.student.history`: tambah `event_type` (masuk/keluar), `school_name`, `date`.
- [ ] Views: `views/student_views.xml`
  - Tampilkan field baru di form; tambahkan `image_1920` widget image.
  - Smart button ke riwayat atau tab notebook “Riwayat”.
- [ ] Security: pastikan ACL student/history sudah tepat (sudah ada), update jika ada model/field baru.
- [ ] i18n: tambahkan label baru ke `i18n/id.po` (fields & selection values).
- [ ] Export: helper python + server action/menu “Export Siswa (Dapodik)” atau wizard sederhana.
- [ ] Demo/Test: update wizard generator opsional buat contoh NISN valid.

Dampak & Risiko
- Migrasi data: untuk DB yang sudah ada, `nisn` boleh nullable awalnya; constraint unik diterapkan saat field terisi.

Estimasi
- 8–12 jam

Catatan
- Rujukan kolom Dapodik terbaru untuk mapping ekspor.

