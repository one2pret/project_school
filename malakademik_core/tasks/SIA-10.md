# SIA-10 — Keamanan & Hak Akses (P0)

- ID: SIA-10
- Judul: Matrix Peran, Record Rules, Audit & Backup SOP
- Prioritas: P0
- Deskripsi singkat: Rancang peran (admin, guru, wali kelas, operator), atur ACL/rules, dokumentasi audit & backup.

Acceptance Criteria
- [ ] Grup per peran tersedia; menu sesuai peran.
- [ ] ACL CRUD per model sesuai peran.
- [ ] Record rules pembatasan akses (mis. guru hanya kelasnya; wali kelas kelasnya).
- [ ] Dokumen SOP backup rutin + (opsional) cron job backup.

Perubahan Teknis
- [ ] Security: `security/groups.xml` tambah grup baru; update `ir.model.access.csv`.
- [ ] Record rules (security/*.xml) sesuai kebutuhan per model.
- [ ] Docs: SOP backup di `docs/` atau README.
- [ ] (Opsional) Modul kecil untuk cron backup.

Estimasi
- 8–12 jam

