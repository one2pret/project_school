# SIA-04 — Nilai & Rapor (P0)

- ID: SIA-04
- Judul: Tipe Penilaian, Perhitungan Nilai Akhir, Cetak Rapor
- Prioritas: P0
- Deskripsi singkat: Tambah tipe penilaian (harian/PTS/PAS) & bobot; hitung nilai akhir; cetak rapor QWeb.

Acceptance Criteria
- [ ] Tipe penilaian (harian/PTS/PAS) dan bobot per mapel/kelas.
- [ ] Nilai akhir per mapel dihitung dari bobot dan nilai komponen.
- [ ] Cetak rapor (PDF) sesuai template nasional dasar.

Perubahan Teknis
- [ ] Model: `assessment.type` (atau selection di `assessment`), field `weight` dan compute agregasi ke report card.
- [ ] Report: QWeb untuk rapor; action print pada report card dan batch kelas.
- [ ] Views: tombol “Generate Report Card” per kelas/semester.
- [ ] i18n.

Estimasi
- 16–24 jam

