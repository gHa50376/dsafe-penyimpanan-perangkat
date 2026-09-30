# D-Safe PowerPoint Generator V36.4.38

Basis: V36.4.37.

Perubahan V36.4.38:
1. Riwayat Buku Kerja langsung membaca ulang data setelah penyimpanan, sehingga transaksi Pengawasan Langsir baru tidak menunggu refresh browser.
2. Filter Riwayat Buku Kerja otomatis diperluas agar tanggal transaksi yang baru disimpan langsung terlihat.
3. Saat menyimpan Pengawasan Langsir, rentang filter Safety Talk Mingguan otomatis ikut mencakup tanggal baru sehingga beberapa input berurutan langsung terbaca pada periode yang sesuai.
4. Preview Safety Talk Mingguan membaca data Pengawasan Langsir secara fresh dari Buku Kerja berdasarkan filter tanggal aktif, bukan mengandalkan payload session-state lama.
5. Generate PPT memakai sumber data Pengawasan Langsir yang sama persis dengan Preview Safety Talk Mingguan.
6. Pengelompokan tetap 3 transaksi Pengawasan Langsir per lembar; transaksi ke-4 dan seterusnya masuk lembar berikutnya.
7. Template Safety Talk Mingguan tetap menggunakan template baru dengan placeholder {{Hari_Tanggal_Langsir_1..3}} dan {{Foto_Langsir_1..3}} sebelum slide Terima Kasih.

Tidak diubah:
- Satu Hari Satu Pasal.
- Cek Emplasemen Oleh KS.
- Safety Talk / IBPR.
- Pengawasan CCTV.
- Simulasi.
- Struktur Buku Kerja dan Cetak/PDF selain sinkronisasi refresh/filter di atas.
