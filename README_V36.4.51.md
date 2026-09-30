# D-Safe PowerPoint Generator V36.4.51

Fokus versi ini adalah perbaikan menyeluruh tampilan mobile tanpa mengubah fungsi data/output yang sudah stabil.

Perubahan:
- Semua baris `st.columns` pada layar HP dipaksa tetap berada di dalam lebar layar, tanpa perlu geser horizontal.
- Kolom horizontal mengecil proporsional; tidak lagi memakai minimum width yang memaksa halaman melebar.
- Tombol, input, select, tanggal, uploader, radio, expander, dan teks dipadatkan khusus mobile.
- Label input dibuat bisa membungkus dengan aman dan tidak saling menumpuk.
- Tombol Home dipindah ke area header dan diperkecil agar tidak menutupi tombol Input/Cetak.
- Toolbar/Deploy Streamlit disembunyikan pada viewport HP untuk menambah ruang kerja.
- Caption/petunjuk sekunder disembunyikan pada HP; instruksi uploader yang tidak penting juga disembunyikan.
- Master Petugas: form tambah dibuat satu baris (Nama Petugas | NIPP | Tambah), tanpa judul/petunjuk berulang.
- Master Kegiatan: form tambah dibuat satu baris (Nama Kegiatan | Tambah); edit kegiatan custom menampilkan Nama + Kelompok secara horizontal.
- Buku Kerja: Form Kegiatan + Sub Kegiatan dibuat satu baris.
- Satu Hari Satu Pasal: Jabatan + Dinas Pagi + Dinas Siang + Dinas Malam dibuat satu baris.
- Judul filter dipersingkat menjadi Periode D-Safe / Periode Safety Talk Mingguan.
- Riwayat Buku Kerja dan preview HTML tetap dipaksa berada di dalam viewport HP.
- Image/canvas/custom component dibatasi maksimum lebar viewport agar tidak memicu horizontal scroll.

Tidak diubah:
- Logika Buku Kerja, Riwayat, Edit/Hapus, penyimpanan data.
- Cetak/PDF.
- Dashboard.
- Mapping dan template D-Safe / Safety Talk Mingguan.
- Aturan kegiatan yang sudah dinyatakan sesuai.
