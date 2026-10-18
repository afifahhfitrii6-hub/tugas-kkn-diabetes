# SPK Risiko Diabetes — Python + Streamlit

Aplikasi Sistem Pendukung Keputusan untuk simulasi klasifikasi risiko diabetes menggunakan algoritma K-Nearest Neighbors (KNN). Tampilan bertema pink dan responsif untuk HP/laptop.

## Struktur
- `app.py` — kode aplikasi Python dan perhitungan KNN.
- `requirements.txt` — pustaka yang dibutuhkan.
- `data/dataset_pasien.csv` — 10 data pasien contoh.

## Jalankan di komputer
1. Install Python.
2. Buka terminal pada folder proyek.
3. Jalankan `pip install -r requirements.txt`.
4. Jalankan `streamlit run app.py`.
5. Buka alamat lokal yang ditampilkan Streamlit.

## Upload ke GitHub
Buat repository publik, lalu upload `app.py`, `requirements.txt`, `README.md`, dan folder `data`.

## Publikasikan agar dosen bisa membuka link
1. Buka https://share.streamlit.io/ dan login dengan GitHub.
2. Pilih Create app.
3. Pilih repository, branch `main`, dan file utama `app.py`.
4. Klik Deploy. Setelah selesai, Streamlit akan memberi URL publik.

## Cara kerja
1. Membaca lima atribut pasien: usia, BMI, glukosa, tekanan darah, dan riwayat keluarga.
2. Melakukan normalisasi min-max berdasarkan rentang data pelatihan.
3. Menghitung jarak Euclidean.
4. Memilih tiga tetangga terdekat (K=3).
5. Memilih kelas mayoritas: Rendah atau Tinggi.

**Peringatan:** dataset adalah contoh untuk pembelajaran, bukan alat diagnosis medis.
