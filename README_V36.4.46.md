# D-Safe PowerPoint Generator V36.4.46

Perubahan dari V36.4.45:

1. Perbaikan penyimpanan Buku Kerja di Windows
   - Menghindari crash `PermissionError: [WinError 5]` saat file `buku_kerja_v341.json` sementara sedang dikunci oleh Windows/antivirus/sync/indexer.
   - Penyimpanan tetap mencoba atomic replace terlebih dahulu, kemudian retry direct write.
   - Jika file utama masih terkunci, data disimpan ke `buku_kerja_v341.pending.json` dan otomatis dibaca pada rerun berikutnya sehingga input tidak hilang.
   - Penulisan ulang file pada setiap rerun dikurangi untuk memperkecil peluang file-lock.

2. Master Kegiatan dibuat lebih ringkas
   - Tiga kelompok tetap ditampilkan sebagai tombol: `D-Safe & Safety Talk`, `Program Keselamatan Kerja`, dan `Kegiatan Lainnya`.
   - Daftar kegiatan dan form tambah kegiatan tidak tampil sebelum kelompok dipilih.
   - Setelah tombol kelompok dipilih, hanya isi kelompok tersebut yang ditampilkan.
   - Kegiatan bawaan sistem tetap terkunci.
   - Kegiatan custom tetap dapat ditambah, diubah, dihapus, dan dipindahkan kelompok.
   - Setelah menambah kegiatan, pengguna tetap berada di kelompok yang sama dan field form kembali kosong.

3. Tidak mengubah
   - Mapping PPT D-Safe/Safety Talk.
   - Buku Kerja, Riwayat, Cetak/PDF, Dashboard, serta aturan kegiatan yang sudah dinyatakan sesuai pada V36.4.45.
