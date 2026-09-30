# D-SAVE PPT Generator V35.1

V35.0 mempertahankan tampilan Home V34.7 yang telah disetujui dan memperbaiki fondasi fungsi:

- Buku Kerja sebagai sumber transaksi tunggal.
- Dashboard Kinerja bersifat read-only terhadap Buku Kerja.
- 12 kegiatan bawaan sistem tetap terkunci.
- 4 kegiatan inti otomatis terhubung ke generator:
  - Safety Talk → Safety Talk IBPR
  - Simulasi Pelayanan Normal & Darurat → D-Safe Simulasi
  - Pengawasan CCTV → D-Safe CCTV
  - Pengawasan Langsir → sheet khusus Safety Talk tepat sebelum slide Terima Kasih
  - Satu Hari Satu Pasal → D-Safe Satu Hari Satu Pasal
  - Cek Emplasemen Oleh KS → D-Safe Cek Emplasemen
- Master Petugas menggunakan Nama + NIPP dengan ID internal stabil.
- Petugas dapat diedit/dihapus tanpa memutus riwayat transaksi.
- Kegiatan baru dapat dibuat dengan target bulanan dan tidak otomatis masuk D-Safe/Safety Talk.
- Riwayat Buku Kerja dapat diedit/dihapus dan dicetak PDF.
- Foto dinormalisasi, duplikat ditolak, maksimal 8 foto per transaksi.
- Draft D-Safe/Safety Talk tetap menggunakan penyimpanan lokal.
- Sinkronisasi Buku Kerja ke generator tidak mengubah snapshot secara acak saat rerun.

## Menjalankan

```cmd
cd C:\Users\User\Downloads\dsafe-ppt-generator-v35.0
python -m pip install -r requirements.txt
python -m streamlit run app.py
```


## Pembaruan V35.1

- Menambahkan **Satu Hari Satu Pasal** sebagai kegiatan sistem tetap di Buku Kerja.
- Menambahkan **Cek Emplasemen Oleh KS** sebagai kegiatan sistem tetap di Buku Kerja.
- Kedua kegiatan tidak dapat diubah atau dihapus dari Master Kegiatan.
- Setiap transaksi Buku Kerja otomatis menjadi lembar pada bagian D-Safe yang sesuai.
- Dokumentasi dari Buku Kerja ikut disinkronkan ke generator (maksimal 8 foto per transaksi).
- Tambah/edit/hapus transaksi tetap dilakukan dari Buku Kerja; D-Safe menggunakan Buku Kerja sebagai sumber data.

### V35.3 — Aturan tanda tangan Buku Kerja
- Canvas/unggah TTD hanya tampil untuk kegiatan: Safety Talk, Diskusi Studi Kasus, Sharing Session Kendala, Pelatihan Mental, Simulasi Pelayanan Normal & Darurat, Coaching Teknis, Penilaian Cara Kerja & Komunikasi, dan Leadership.
- TTD disimpan hanya sebagai bagian dari transaksi Buku Kerja.
- TTD tidak disinkronkan dan tidak dimasukkan ke template PowerPoint D-Safe maupun Safety Talk Mingguan.
- Kegiatan lain tidak menampilkan canvas/kolom TTD.


## V35.4 — Struktur Uraian Buku Kerja mengikuti form generator
- **Safety Talk**: Uraian Buku Kerja dipecah menjadi Potensi Bahaya, Risiko, dan Cara Pengendalian; sinkron ke form Safety Talk IBPR.
- **Simulasi Pelayanan Normal & Darurat**: Uraian Buku Kerja dipecah menjadi Keterangan dan Materi Simulasi; sinkron ke kolom D-Safe Simulasi.
- Kegiatan lain tetap menggunakan Uraian Kegiatan umum.
- Tanda tangan tetap tersimpan hanya di Buku Kerja dan tidak dikirim ke PowerPoint.


## V35.5
- Buku Kerja Satu Hari Satu Pasal diselaraskan dengan kolom form D-Safe: Jabatan, Nama Dinas Pagi, Nama Dinas Siang, Nama Dinas Malam.
- Satu transaksi Buku Kerja Satu Hari Satu Pasal mengisi satu baris D-Safe; baris lain tetap kosong.
- Cek Emplasemen Oleh KS tidak lagi menampilkan kolom Uraian di Buku Kerja karena form D-Safe hanya membutuhkan dokumentasi foto.
- Foto Cek Emplasemen dari Buku Kerja tetap langsung disinkronkan ke D-Safe.

### V36.0 — Pengelompokan Form Buku Kerja

Input Kegiatan kini dibagi menjadi satu kelompok gabungan **D-Safe & Safety Talk**, **Program Keselamatan Kerja**, dan **Kegiatan Lainnya**. Setiap kegiatan hanya muncul pada satu kelompok.
