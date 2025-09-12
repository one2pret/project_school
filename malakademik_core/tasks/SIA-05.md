# SIA-05 — Absensi Siswa & Guru (P1)

- ID: SIA-05
- Judul: Rekap Absensi & Dashboard Monitoring
- Prioritas: P1
- Deskripsi singkat: Menyediakan rekap kehadiran dan dashboard monitoring sederhana per periode/kelas/guru.

Acceptance Criteria
- [ ] Rekap absensi per siswa/kelas/periode dapat dihasilkan (list/pivot/graph).
- [ ] Filter periode (rentang tanggal), kelas, guru.
- [ ] Ekspor laporan rekap (CSV/PDF) tersedia dari UI.

Perubahan Teknis
- [ ] Model agregasi atau compute stored untuk rekap (opsional: `malakademik.attendance.summary`).
- [ ] Views: menu Laporan Absensi; graph/pivot view pada attendance/summary.
- [ ] Wizard filter periode untuk ekspor.
- [ ] Export: helper CSV/PDF.
- [ ] i18n label baru.

Estimasi
- 10–14 jam

