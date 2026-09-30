# D-Safe PowerPoint Generator V36.4.53

Perubahan tampilan:
- Header Buku Kerja menampilkan tombol Download Buku Kerja dan Home; judul lebih besar daripada label tombol.
- Tampilan awal Buku Kerja memuat riwayat dan filter tanggalnya, serta akses Tambah Kegiatan di dekat judul riwayat.
- Klik Download Buku Kerja membuka filter tanggal/jenis kegiatan dan pratinjau halaman PDF yang sama dengan berkas unduhan.
- Form input/edit berada di halaman tersendiri: filter, pratinjau PDF, dan riwayat tidak ditampilkan di dalam form. Simpan/Batal kembali ke riwayat.
- Tombol Home pada kartu lain melayang di sudut kanan bawah, termasuk pada layar HP.
- Logika penyimpanan kegiatan, PDF, dan generator PPT tetap memakai implementasi V36.4.52.

Menjalankan di Windows CMD:
    cd /d "%USERPROFILE%\Downloads\dsafe-ppt-generator-v36.4.53"
    python -m pip install -r requirements.txt
    python -m streamlit run app.py

Ketergantungan baru pypdfium2 merender pratinjau tiap halaman PDF dengan baik pada layar HP.
