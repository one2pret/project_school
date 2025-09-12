# SIA-06 — Mutasi & Alumni (P1)

- ID: SIA-06
- Judul: Proses Mutasi Masuk/Keluar & Penandaan Alumni
- Prioritas: P1
- Deskripsi singkat: Mendukung proses mutasi antar sekolah dengan riwayat dan penandaan status alumni.

Acceptance Criteria
- [ ] Wizard mutasi masuk/keluar yang memperbarui kelas/status serta menambah entri riwayat.
- [ ] Penandaan siswa sebagai alumni (dengan tahun lulus) dan arsip kelas terkait.
- [ ] Laporan daftar alumni per tahun ajaran.

Perubahan Teknis
- [ ] Wizard mutasi (transient): input jenis, asal/tujuan, tanggal, alasan.
- [ ] Model student: field `alumni:boolean`, `graduation_year:char`.
- [ ] Views: tombol Aksi Mutasi/Alumni pada form siswa; menu laporan alumni.
- [ ] Export: laporan alumni (CSV/PDF) sederhana.
- [ ] i18n label baru; ACL wizard.

Estimasi
- 8–12 jam

