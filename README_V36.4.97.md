# D-Safe V36.4.97 — Satu Pengawasan Langsir

Kegiatan terkunci `Pengawas langsir` pada **Program Keselamatan Kerja** dihapus dari pilihan karena merupakan duplikat yang tidak memakai form otomatisasi PPT. `Pengawasan Langsir` pada **D-Safe & Safety Talk** tetap menjadi kegiatan utama yang mengisi PPT Safety Talk Mingguan.

Jika ada riwayat lama dengan ID duplikat (`keg_15`), aplikasi memindahkannya ke ID utama (`keg_10`) saat data dibuka. ID sesi, tanggal, catatan, foto, dan tanda tangan dipertahankan. Data lain, nama file unduhan, fungsi, dan tampilan V36.4.96 tidak diubah.

Pemeriksaan pada data uji dengan kedua ID memastikan hanya satu kegiatan Langsir yang dapat dipilih, dua catatan lama dan baru tetap ada, dan keduanya muncul dalam satu slide Pengawasan Langsir pada PPT Safety Talk.

Ekstrak ZIP, pasang dependensi yang tercantum pada `requirements.txt` dan `packages.txt` bila diperlukan, lalu jalankan `streamlit run app.py`.
