# D-Safe V36.4.71 — Filter Riwayat Buku Kerja

Filter Tanggal mulai/Tanggal sampai di Riwayat Kegiatan kini memakai satu sumber nilai awal dari Session State. Peringatan Streamlit “The widget ... was created with a default value but also had its value set via the Session State API” tidak muncul saat data baru memperluas rentang riwayat.

Pengujian browser: buka Buku Kerja, simpan Libur bertanggal di luar rentang lama, kembali ke Riwayat Kegiatan; tanggal sampai mencakup data baru dan tidak ada peringatan atau exception. Data uji tidak disertakan dalam paket.
