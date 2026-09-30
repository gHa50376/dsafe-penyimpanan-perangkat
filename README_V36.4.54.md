# D-Safe PowerPoint Generator V36.4.54

- Halaman awal Buku Kerja langsung menampilkan filter periode/jenis kegiatan, pratinjau PDF, tombol Download PDF Buku Kerja, serta riwayat dengan filter tanggal.
- Tombol Download Buku Kerja pada header dihapus. Tombol PDF di bawah pratinjau tetap ada.
- Header memakai ikon Home; tombol tambah kegiatan di samping judul riwayat menjadi (+).
- Halaman input/edit tetap terpisah dari filter dan riwayat. Panah kembali tersedia pada halaman input.
- Tidak mengubah isi PDF, data kegiatan, atau generator D-Safe/Safety Talk.

Jalankan di Windows CMD:
    cd /d "%USERPROFILE%\Downloads\dsafe-ppt-generator-v36.4.54"
    python -m pip install -r requirements.txt
    python -m streamlit run app.py
