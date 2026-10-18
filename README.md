# Sistem Pendukung Keputusan Risiko Diabetes — KNN

Proyek website sederhana untuk tugas kuliah Sistem Pendukung Keputusan (SPK). Website memakai HTML, CSS, dan JavaScript tanpa framework atau database sehingga dapat dijalankan langsung di browser dan dipublikasikan melalui GitHub Pages.

## Fitur
- Form input usia, BMI, glukosa, tekanan darah, dan riwayat diabetes dalam keluarga.
- Klasifikasi K-Nearest Neighbors (KNN) dengan K = 3.
- Normalisasi min–max dan jarak Euclidean.
- Menampilkan kategori hasil dan tiga data pelatihan terdekat.
- Tampilan responsif untuk HP dan desktop dengan tema pink.

## Struktur folder
```text
SPK_Risiko_Diabetes_GitHub/
├── index.html
├── style.css
├── script.js
├── data/
│   └── dataset_pasien.csv
├── README.md
└── LICENSE
```

## Cara menjalankan di komputer atau HP
1. Unduh atau clone repository.
2. Buka `index.html` di browser.
3. Masukkan data pasien lalu tekan **Hitung Prediksi Risiko**.

Tidak perlu menginstal PHP, Node.js, atau database.

## Cara menyimpan ke GitHub
1. Masuk ke GitHub dan buat repository baru, misalnya `spk-risiko-diabetes`.
2. Upload semua file dan folder dari paket ini ke repository.
3. Buka **Settings → Pages**.
4. Pada bagian **Build and deployment**, pilih **Deploy from a branch**.
5. Pilih branch `main` dan folder `/(root)`, lalu tekan **Save**.
6. Tunggu proses publikasi selesai. GitHub akan menampilkan alamat website Pages di bagian Pages; bagikan alamat itu kepada dosen.

## Cara kerja KNN
1. Program menerima lima atribut pasien.
2. Setiap atribut dinormalisasi berdasarkan nilai minimum dan maksimum dataset contoh.
3. Program menghitung jarak Euclidean antara data input dan setiap pasien pelatihan.
4. Tiga pasien dengan jarak terkecil dipilih.
5. Label yang paling banyak muncul menjadi hasil klasifikasi.

## Dataset
File `data/dataset_pasien.csv` memuat 10 baris data contoh dari materi studi kasus yang diberikan. Nilai riwayat keluarga: `0 = Tidak ada`, `1 = Ada`. Kelas target: `Rendah` atau `Tinggi`.

## Catatan penting
Dataset hanya untuk demonstrasi algoritma dan pembelajaran. Prediksi website **bukan diagnosis medis** dan tidak boleh digunakan untuk menentukan pengobatan. Dataset yang kecil juga tidak cukup untuk menyimpulkan akurasi klinis.
