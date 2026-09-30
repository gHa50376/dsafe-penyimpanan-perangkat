# D-Safe PowerPoint Generator V36.4.35

Perbaikan terbatas dari V36.4.34:

- Memperbaiki error `AttributeError: 'str' object has no attribute 'weekday'` pada Preview Safety Talk Mingguan bagian Pengawasan Langsir.
- Tanggal Pengawasan Langsir yang tersimpan sebagai string ISO dinormalisasi menjadi objek `date` sebelum diformat.
- Tidak mengubah struktur input, Buku Kerja, Cetak/PDF, kegiatan lain, maupun template PPT.
