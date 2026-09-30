# D-Safe PowerPoint Generator V36.4.30

Basis: V36.4.29.

Perubahan terkontrol hanya untuk alur **Satu Hari Satu Pasal -> D-Safe**:

- Data Buku Kerja Satu Hari Satu Pasal sekarang dipaketkan sesuai kapasitas template D-Safe: **3 kegiatan per lembar**.
- Kegiatan ke-1 sampai ke-3 masuk lembar 1, kegiatan ke-4 sampai ke-6 masuk lembar 2, dan seterusnya.
- Setiap baris tetap membawa Tanggal, Jabatan, Dinas Pagi, Dinas Siang, Dinas Malam, serta foto Pagi/Siang/Malam milik kegiatan yang sama.
- Nama petugas tetap menggunakan format **Nama / NIPP** dari Master Data.
- Baris template yang belum terisi ditampilkan sebagai `-` dan tidak pernah diberi tanggal hari ini secara otomatis.
- Jika tidak ada data Satu Hari Satu Pasal pada periode yang dipilih, tabel Satu Hari Satu Pasal tidak ditampilkan pada review/generasi.
- Tidak mengubah Safety Talk, CCTV, Simulasi, Cek Emplasemen, Riwayat Kegiatan, TTD, atau template PPT.

Validasi: `python -m py_compile app.py` berhasil.
