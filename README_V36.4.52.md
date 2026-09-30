# D-Safe PowerPoint Generator V36.4.52

Fokus versi ini: konsolidasi dan perapihan UI keseluruhan tanpa mengubah logika kegiatan/output.

Perubahan:
- Menghapus tumpukan CSS responsif V36.4.48–V36.4.51 dan menggantinya dengan satu sistem visual desktop/mobile yang konsisten.
- Mobile tidak menggunakan horizontal page scrolling. Baris 2/3/4 kolom tetap berada dalam satu layar; baris 5+ kolom dibungkus maksimal 4 kolom per baris.
- Menata ulang hierarki font, ukuran label, input, tombol, expander, uploader, tab, radio, dan alert.
- Header halaman lebih ringkas; subtitle bantuan disembunyikan; tombol Home diperkecil dan tidak menutupi kontrol.
- Riwayat Buku Kerja dan preview D-Safe/Safety Talk dibuat fit-to-viewport dengan tabel fixed-layout, foto/action lebih kompak, dan tanpa min-width kosong yang memicu overflow.
- Pengaturan Identitas Stasiun dibuat satu baris: input + Simpan.
- Master Kegiatan disederhanakan: label kelompok tanpa simbol tambahan, judul kelompok lebih ringkas.
- Tidak mengubah Dashboard, data, mapping PPT, Cetak/PDF, maupun aturan kegiatan yang sudah stabil.

Pemeriksaan:
- `python -m py_compile app.py` lolos.
- Uji layout sintetis 360, 390, 430, 768, dan 1280 px menunjukkan `scrollWidth == clientWidth` (tidak ada horizontal page overflow).
- Template PPT tetap identik dengan V36.4.51.
