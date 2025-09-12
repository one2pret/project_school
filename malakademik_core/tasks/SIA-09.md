# SIA-09 — Pelaporan Dapodik/Diknas (P0)

- ID: SIA-09
- Judul: Ekspor Data Dapodik + Validator
- Prioritas: P0
- Deskripsi singkat: Menyediakan ekspor data siap unggah (CSV/XLSX) dan validator kesesuaian format.

Acceptance Criteria
- [ ] Export siswa, PTK, rombel, nilai, absensi (minimal kolom wajib Dapodik).
- [ ] Validator header & tipe data; laporan error sebelum sinkronisasi.

Perubahan Teknis
- [ ] Addon opsional `malakademik_dapodik_export` (terpisah) untuk menjaga modularitas.
- [ ] Helper ekspor per entitas; mapping kolom; wizard ekspor per modul.
- [ ] Validator schema (header, required fields) + UI hasil validasi.
- [ ] i18n; menu Laporan/Ekspor.

Estimasi
- 16–24 jam (bergantung spesifikasi kolom Dapodik terbaru)

