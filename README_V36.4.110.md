# D-Safe V36.4.110 — Pembersihan setelah periode terakhir

Filter cadangan tetap **Tanggal, Bulan, Tahun**. Bila reset suatu periode masih menyisakan kegiatan di periode lain, ZIP hanya memuat kegiatan terpilih dan cadangan/draf lama tetap di aplikasi.

Bila periode yang direset merupakan periode terakhir yang tersimpan, ZIP juga memuat salinan cadangan dan draf lama di folder terpisah. Setelah pengguna memastikan ZIP tersimpan dan mengonfirmasi, sesi periode terpilih serta salinan lokal itu dibersihkan dari aplikasi. Data master tetap ada. Bila sesi sudah kosong tetapi salinan cadangan/draf lama masih ada, tombol yang sama dapat mengarsipkannya dan membersihkannya.

Pemulihan ZIP periode menambahkan sesi tanpa duplikat. Draf yang terdapat pada ZIP akan dipulihkan bila belum ada draf aktif, sehingga draf yang baru tidak tertimpa. Salinan cadangan lama dapat diambil dari folder `cadangan_terdahulu` di dalam ZIP.
