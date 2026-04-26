Judul Program: Pencacatan Harian
Deskripsi Singkat: Program ini berfungsi untuk mencatat pengeluaran harian pengguna selama 5 hari dengan menggunakan list 1 dimensi sebagai media penyimpanan data. Setiap data pengeluaran disimpan dalam satu index list, sehingga pengguna dapat memasukkan nilai pengeluaran, melihat data yang tersimpan, mengetahui alamat memori list, serta menghitung total seluruh pengeluaran melalui menu interaktif.
Struktur data yang diterapkan pada program ini adalah list 1 dimensi, yaitu struktur data linear yang menyimpan elemen secara berurutan dalam satu baris. Algoritma yang digunakan adalah traversal, yaitu proses menelusuri seluruh elemen list untuk menampilkan data dan menghitung total nilai pengeluaran.

<img width="1758" height="634" alt="code menu" src="https://github.com/user-attachments/assets/51ce5933-a8a6-445e-b5c9-c5149f06b749" />
def menu():
Membuat fungsi untuk menampilkan menu pilihan.
print("1. Lihat address list")
Menampilkan pilihan pertama untuk melihat alamat list.
print("2. Lihat address setiap data")
Menampilkan pilihan kedua untuk melihat alamat tiap elemen.
print("3. Input pengeluaran")
Menampilkan pilihan ketiga untuk mengisi data.
print("4. Tampilkan pengeluaran")
Menampilkan pilihan keempat untuk melihat isi list.
print("5. Hitung total pengeluaran")
Menampilkan pilihan kelima untuk menjumlahkan data.
print("6. Keluar")
Menampilkan pilihan keenam untuk keluar.
