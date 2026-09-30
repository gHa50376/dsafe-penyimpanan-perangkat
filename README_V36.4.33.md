# V36.4.33

Perbaikan khusus Cek Emplasemen Oleh KS pada Cetak/PDF Buku Kerja.

- Maksimal 8 foto Cek Emplasemen tidak lagi ditumpuk vertikal.
- Foto disusun dalam grid ringkas 4 foto per baris, maksimal 2 baris, di kolom KETERANGAN.
- Rasio foto tetap dipertahankan.
- Perubahan ini mencegah `reportlab.platypus.doctemplate.LayoutError` pada halaman A5 landscape.
- Tidak mengubah fungsi Satu Hari Satu Pasal, kegiatan lain, Riwayat, maupun template PPT.
