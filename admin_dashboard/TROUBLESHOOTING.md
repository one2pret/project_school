# Dokumentasi Troubleshooting Modul Admin Dashboard

Dokumen ini merangkum serangkaian masalah yang ditemui selama pengembangan modul `admin_dashboard` dan solusi yang diterapkan.

## Masalah Awal: Komponen Gagal Dimuat

Komponen dasbor pada awalnya sama sekali tidak berfungsi dan menampilkan berbagai error di konsol browser.

### Problem 1: `Uncaught Promise > Error: Service rpc is not available`

- **Gejala**: Komponen OWL crash saat proses `setup()` karena tidak dapat menemukan `rpc` service.
- **Analisis**: File template XML komponen (`admin_dashboard_templates.xml`) terdaftar di dua bundel aset pada `__manifest__.py`: `web.assets_backend` dan `web.assets_qweb`. Pendaftaran di `web.assets_qweb` menyebabkan Odoo mencoba menginisialisasi komponen di lingkungan "statis" yang tidak memiliki akses ke service inti seperti `rpc`.
- **Solusi**: Menghapus path template dari bundel `web.assets_qweb` di `__manifest__.py`, dan hanya menyisakannya di `web.assets_backend`.

### Problem 2: `odoo.exceptions.AccessError`

- **Gejala**: Setelah masalah `rpc` teratasi, frontend menerima error hak akses dari backend.
- **Analisis**:
    1.  Controller di backend tidak memiliki pemeriksaan untuk memastikan hanya pengguna yang berwenang (manajer akademik) yang dapat meminta data statistik.
    2.  Menu "Admin Dashboard" terlihat oleh semua pengguna, yang menyebabkan pengalaman pengguna yang buruk bagi mereka yang tidak memiliki akses.
- **Solusi**:
    1.  Menambahkan pemeriksaan `if not request.env.user.has_group(...)` di awal metode controller `admin_stats`.
    2.  Menambahkan atribut `groups="malakademik_core.group_malakademik_manager"` pada `menuitem` di `views/admin_dashboard_views.xml` untuk menyembunyikan menu dari pengguna yang tidak berhak.

### Problem 3: Perubahan Kode Python Tidak Berdampak

- **Gejala**: Error yang seharusnya sudah diperbaiki (seperti `400 Bad Request`) terus muncul meskipun kode Python sudah diubah.
- **Analisis**: Proses server Odoo tidak dimatikan dan dimulai ulang dengan benar. Akibatnya, server masih menjalankan kode Python versi lama yang ada di memori, bukan kode baru dari file yang telah diubah.
- **Solusi**: Menetapkan alur kerja yang benar untuk pengembangan Odoo:
    1.  **Hentikan Server**: Gunakan `Ctrl+C` atau paksa berhenti melalui **Task Manager** di Windows untuk memastikan proses `python.exe` Odoo benar-benar mati.
    2.  **Mulai Ulang dengan Perintah yang Tepat**:
        *   Gunakan flag `-u nama_modul` untuk memperbarui modul.
        *   Gunakan flag `-i nama_modul` untuk melakukan install/reinstall bersih, yang lebih kuat dari `-u`.
        *   Gunakan flag `--workers=0` saat melakukan debugging dengan `pdb` untuk memaksa Odoo berjalan dalam mode single-process.

### Problem 4: `TypeError: <function> returns an invalid value`

- **Gejala**: Setelah semua masalah di atas teratasi, backend menghasilkan `TypeError` saat mencoba mengembalikan data.
- **Analisis**: Karena frontend menggunakan `http.post` (sebagai solusi untuk masalah `rpc` service yang hilang secara misterius dari environment), mekanisme otomatis `type="json"` pada dekorator `@http.route` tidak berfungsi seperti yang diharapkan. Framework tidak tahu cara mengubah dictionary Python menjadi respons HTTP JSON.
- **Solusi (Final)**: Membuat objek respons HTTP secara manual di dalam controller.
    1.  Mengubah tipe route menjadi `type="http"`.
    2.  Mengimpor `json` dan `odoo.http.Response`.
    3.  Mengubah pernyataan `return` menjadi:
        ```python
        return Response(
            json.dumps(data_dictionary),
            content_type='application/json',
            status=200,
        )
        ```
    Ini memberikan kontrol penuh atas output dan memastikan respons yang dikirim ke frontend memiliki format JSON yang benar.
