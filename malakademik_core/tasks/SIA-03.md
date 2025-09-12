# SIA-03 — Kelas & Pembelajaran (P0)

- ID: SIA-03
- Judul: Rombel, Kurikulum, Mapel, KD/KI
- Prioritas: P0
- Deskripsi singkat: CRUD kelas/rombel, struktur kurikulum dan Kompetensi Dasar/Inti per mapel/tingkat.

Acceptance Criteria
- [ ] Kelas/rombel dapat dibuat/diarsip; wali kelas terisi.
- [ ] KD/KI terdefinisi per mapel dan tingkat/kelas.
- [ ] Peserta kelas terdaftar; guru pengampu melalui schedule.

Perubahan Teknis
- [ ] Model baru: `malakademik.kd` (kode, deskripsi, subject, grade/kelas, tipe: KD/KI).
- [ ] Views: form/list KD; relasi ke Assessment (opsional untuk rubrik).
- [ ] Wizard assign siswa massal ke kelas.
- [ ] i18n, ACL untuk model KD.

Estimasi
- 10–16 jam

