# D-Safe V36.4.113 — Instalasi baru untuk HP

Paket lengkap ini mulai dengan data kegiatan kosong dan tidak mencari atau menyalin data dari versi sebelumnya. Tampilan dan fungsi kegiatan sama dengan V36.4.110. Pemilih berkas Pulihkan Cadangan menerima pilihan file dari HP tanpa membatasi daftar di file manager; setelah dipilih, aplikasi memeriksa format cadangan ZIP/JSON sebelum menampilkan konfirmasi.

1. Ekstrak ZIP ini ke folder baru. Jangan jalankan peluncur dari dalam ZIP.
2. Klik dua kali `Jalankan_D-Safe_Windows.bat`. Jika Python atau paket belum terpasang, buka Command Prompt di folder aplikasi lalu jalankan `python -m pip install -r requirements.txt` dan coba lagi.
3. Biarkan jendela peluncur terbuka. Di komputer buka `http://localhost:8501`. Di HP yang tersambung ke Wi-Fi yang sama buka `http://IPv4-Wi-Fi-komputer:8501`. Gunakan IPv4 Wi-Fi pada keluaran peluncur, bukan `0.0.0.0` atau `localhost` di HP.
4. Jika Windows meminta izin firewall untuk Python, izinkan pada jaringan Privat. Pengaturan yang sebelumnya berhasil untuk V36.4.111 umumnya tetap dapat dipakai bila Python yang digunakan sama.
5. Untuk memilih ZIP cadangan, buka Pengaturan → Pulihkan Cadangan di aplikasi, lalu pilih file ZIP dari Downloads/Unduhan. ZIP tidak perlu dibuka langsung di file manager.

Folder data akan dibuat otomatis saat aplikasi digunakan. Menutup jendela peluncur menghentikan server.
