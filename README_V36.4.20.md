# D-Safe PowerPoint Generator V36.4.20

## Perubahan
- Basis: V36.4.19.
- Memperbaiki mapping **Pengawasan CCTV** dari Buku Kerja ke D-Safe:
  - Hari/Tanggal
  - Nama/NIPP/Petugas
  - Hasil Pengawasan
  - Tindak Lanjut
  - Dokumentasi
- Memperbaiki sumber CCTV untuk **Safety Talk Mingguan** agar mengambil data CCTV dari Buku Kerja melalui snapshot D-Safe.
- Pada halaman Safety Talk Mingguan, periode CCTV yang tersedia dari Buku Kerja otomatis terpilih pada kondisi awal; pengguna tetap dapat menghapus periode yang tidak ingin dimasukkan.
- **Template PPT tidak diubah.**
- Mapping Safety Talk, Buku Kerja, Riwayat, dan Cetak/PDF V36.4.19 tidak diubah.

## Verifikasi
- `app.py` berhasil melewati `py_compile`.
- Placeholder CCTV pada kedua template diverifikasi dapat terisi dengan mapping terstruktur.
