# SIA-02 — Manajemen Data Guru & Tendik (P0)

- ID: SIA-02
- Judul: Data Guru/Staff (NIP, Jabatan, Riwayat Sertifikasi/Pendidikan, Tugas Tambahan)
- Prioritas: P0
- Deskripsi singkat: Memperkaya profil guru/tendik, menambah riwayat sertifikasi/pendidikan, dan ekspor PTK dasar.

Acceptance Criteria
- [ ] NIP unik, format valid (angka, panjang sesuai standar).
- [ ] Field jabatan (selection), status kepegawaian (PNS/Non-PNS/dll.).
- [ ] Riwayat sertifikasi (jenis, no, tahun) dan pendidikan terakhir (jenjang, prodi, tahun).
- [ ] Penetapan tugas tambahan (walikelas/kepsek) terdata.
- [ ] Ekspor CSV PTK sesuai kolom dasar Dapodik.

Perubahan Teknis
- [ ] Model: `models/teacher.py`
  - Tambah `nip`, `position`, `employment_status`.
- [ ] Sub-model riwayat: `teacher.cert`, `teacher.education` (models baru) relasi ke teacher.
- [ ] Views: tab Sertifikasi/Pendidikan; input tugas tambahan; filter/pencarian NIP.
- [ ] Security: ACL untuk sub-model riwayat.
- [ ] Export: helper ekspor PTK (CSV) + menu/action.
- [ ] i18n: label baru/selection.

Estimasi
- 10–14 jam

Catatan
- Sinkronisasi `res.partner` tetap dipertahankan.

