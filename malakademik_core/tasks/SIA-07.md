# SIA-07 — Layanan Data PTK (P1)

- ID: SIA-07
- Judul: Riwayat Sertifikasi/Pangkat/Pendidikan & Export Layanan
- Prioritas: P1
- Deskripsi singkat: Mencatat riwayat sertifikasi, kepangkatan, dan pendidikan terakhir serta menyediakan exporter layanan.

Acceptance Criteria
- [ ] Riwayat sertifikasi (jenis/no/tanggal), pangkat (golongan/tmt), dan pendidikan terakhir tersimpan per PTK.
- [ ] Export CSV layanan sesuai kolom awal yang disepakati.

Perubahan Teknis
- [ ] Sub-model riwayat: `teacher.rank`, `teacher.cert`, `teacher.education` dengan relasi ke guru.
- [ ] Views: tab riwayat pada teacher; filter pencarian.
- [ ] Export: helper CSV + menu/action.
- [ ] i18n label; ACL sub-model.

Estimasi
- 10–14 jam

