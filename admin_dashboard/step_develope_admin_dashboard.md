# Step by Step: Pengembangan Admin Dashboard

1. **Siapkan Struktur Modul**
   - Buat folder dmin_dashboard beserta subdirektori controllers/, static/src/{components,scss,xml}, dan iews/.
   - Tambahkan __init__.py dan __manifest__.py dengan dependensi web dan malakademik_core.

2. **Endpoint Data**
   - Implementasi controllers/dashboard.py dengan route /admin_dashboard/stats.
   - Batasi akses hanya pengguna yang memiliki grup malakademik_core.group_malakademik_manager.
   - Hitung jumlah record siswa, guru, orang tua dan kembalikan JSON.

3. **Komponen OWL**
   - Buat static/src/components/admin_dashboard.js.
   - Gunakan 	his.env.services.rpc untuk memanggil endpoint.
   - Simpan hasil ke state (llowed, cards) dan tampilkan notifikasi jika gagal/ditolak.

4. **Template & Styling**
   - Buat static/src/xml/admin_dashboard_templates.xml menampilkan header, stat card, dan pesan akses ditolak.
   - Tambahkan SCSS (static/src/scss/admin_dashboard.scss) untuk gaya dark-theme sederhana.

5. **Integrasi UI**
   - Definisikan action client dmin_dashboard.admin_dashboard dan menu menu_admin_dashboard di iews/admin_dashboard_views.xml.
   - Menu ditempatkan di bawah malakademik_core.menu_malakademik_root dengan sequence="5" sehingga tampil pertama.

6. **Registrasi Asset**
   - Pastikan manifest memasukkan file JS/SCSS/XML ke web.assets_backend dan web.assets_qweb.

7. **Pengujian**
   - Jalankan odoo-bin -c odoo.conf -d <db> -u admin_dashboard --stop-after-init.
   - Reload asset (Ctrl+Shift+R) dan login sebagai admin untuk melihat dashboad.
   - Uji gunakan akun bukan admin untuk memastikan pesan akses ditolak muncul.

8. **Pengembangan Lanjutan**
   - Tambahkan metrik tambahan (mis. jumlah kelas, jadwal aktif).
   - Integrasi chart jika diperlukan (mis. distribusi siswa per kelas).
   - Buat endpoint parameterized untuk filter tahun ajaran.
