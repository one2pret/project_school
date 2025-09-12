# MalAkademik Core — Developer Guide (Odoo 18)

Tujuan
- Panduan singkat untuk kontribusi dan pemeliharaan modul `malakademik_core`.
- Fokus: gaya penulisan, pola views/actions, i18n, keamanan, dan tips upgrade.

Struktur Modul (ringkas)
- Manifest: `__manifest__.py` — depends, data load order, demo, icon.
- Models: `models/*.py` — logika bisnis.
- Views: `views/*_views.xml`, `views/menus.xml` — daftar/form, actions, menus.
- Security: `security/groups.xml`, `security/ir.model.access.csv`.
- i18n: `i18n/id.po` — terjemahan.
- Demo: `demo/demo.xml` (opsional) dan wizard `models/demo_wizard.py`.

Gaya Penulisan (Python)
- Penamaan model: gunakan prefix `malakademik.` (contoh: `malakademik.student`).
- Field naming: snake_case, deskriptif (contoh: `employee_code`, `homeroom_teacher_id`).
- Related fields: gunakan `related="model.field"`, `store=True` bila perlu disaring/diurutkan.
- Compute fields: beri `compute="_compute_x"`, `store` sesuai kebutuhan; gunakan `@api.depends`.
- Create/write override: jaga idempotensi, hindari side-effect berat, panggil `super()`.
- Konstanta/selection: definisikan dekat field; gunakan nilai stabil (mon, tue, ...).

Pola Views (Odoo 18)
- Gunakan `<list>` menggantikan `<tree>` untuk list view.
- Simpan satu file per model: `*_views.xml` (list+form). Pola minimal:
  - List: kolom ringkas, field yang dapat disortir/difilter.
  - Form: kelompokkan field dalam `<group>`; gunakan `notebook` untuk one2many.
- One2many inline: gunakan `<list editable="bottom">`.
- Definisikan actions di satu tempat (saat ini bagian atas `views/menus.xml`).

Actions & Menus
- Definisikan semua `ir.actions.act_window` lebih dulu (di bagian atas `views/menus.xml`).
- Tautkan menu memakai atribut `action="action_xmlid"` pada `<menuitem>`.
- Urutan load di manifest: views (dengan actions) sebelum `views/menus.xml`.
- Gunakan `groups` di `<menuitem>` untuk kontrol visibilitas menu.

Keamanan
- Groups: definisikan kategori dan grup di `security/groups.xml`.
- ACL: setiap model wajib punya baris di `security/ir.model.access.csv` untuk user/manager sesuai kebutuhan CRUD.
- Pertimbangkan record rules jika diperlukan pembatasan per-record.

i18n (Terjemahan)
- Ikuti pola Odoo: referensi `model_terms:ir.ui.view`, `model:ir.model.fields`, `model:ir.ui.menu`, dll.
- Disarankan generate PO via Settings > Translations > Export Translation (pilih modul ini), lalu edit hasilnya.
- Simpan sebagai `i18n/id.po`, lalu upgrade modul untuk memuat terjemahan.

Demo Data
- `demo/demo.xml` dimuat jika DB dibuat dengan demo atau upgrade dengan `--load-demo=1`.
- Wizard idempotent: `malakademik.demo.wizard` (Academics > Tools > Generate Sample Data).
- Saat menambah contoh baru di wizard, cari dulu (search), buat jika belum ada (idempotent).

Tips Upgrade / Pengembangan
- Upgrade modul:
  - UI: Apps > Upgrade pada modul, atau
  - CLI: `-u malakademik_core` (tambahkan `--load-demo=1` bila ingin memuat demo).
- Cache assets UI: hard refresh; bila perlu Clear Asset Cache (Developer Mode).
- Perubahan views/actions: jaga XMLID stabil, pastikan actions tersedia sebelum menus.
- Migrasi data: tambah kolom dengan default aman; gunakan compute/store sesuai kebutuhan.

Quality & Debugging
- Aktifkan Developer Mode untuk inspeksi views, menus, actions, fields.
- Naikkan log level bila menelusuri isu instalasi/upgrade.
- Dokumentasikan isu/solusi di `PROBLEM_SOLVING.md`.

Konvensi Tambahan
- Jangan menghapus/rename XMLID publik tanpa migrasi.
- Ikuti struktur file yang ada; buat perubahan terfokus per fitur.
- Perbarui README/guide saat ada fitur yang memengaruhi pengguna/developer.

Referensi Cepat
- README: gambaran fitur dan struktur.
- PROBLEM_SOLVING.md: isu yang pernah terjadi dan solusinya.
