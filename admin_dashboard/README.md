# Admin Dashboard (Odoo 18)

## Ringkasan
- Dashboard administratif untuk modul akademik menampilkan total siswa, guru, dan orang tua.
- Hanya admin/manajer akademik yang dapat mengakses.

## Fitur
- Endpoint JSON /admin_dashboard/stats mengembalikan agregat data utama.
- Komponen OWL menampilkan stat card dan fallback pesan saat akses ditolak.
- Integrasi menu di bawah Academics dengan hak akses Academic Manager.

## Instalasi
1. Pastikan modul berada pada ddons_path.
2. Jalankan odoo-bin -d <db> -u admin_dashboard atau upgrade via Apps.
3. Admin akan melihat menu Admin Dashboard di bawah Academics.

## Penggunaan
- Menu menampilkan kartu statistik (jumlah siswa, guru, orang tua).
- Jika pengguna bukan admin/manajer, dashboard menampilkan pesan akses ditolak.

## Pengembangan
- Lihat step_develope_admin_dashboard.md untuk langkah detail membangun modul.
- Endpoint, component, dan template dapat dikembangkan untuk menambahkan metrik tambahan (grafik, filter).
