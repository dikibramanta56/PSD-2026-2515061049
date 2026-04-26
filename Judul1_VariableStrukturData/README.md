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
<img width="1140" height="748" alt="code def main" src="https://github.com/user-attachments/assets/4c0043f1-1e9f-4dfc-9682-6aca0f54c0a4" />
def main():
Membuat fungsi utama program.
pengeluaran = [0] * 5
Membuat list berisi 5 elemen bernilai 0.
running = True
Variabel agar program terus berjalan.
while running:
Perulangan selama program masih aktif.
menu()
Menampilkan menu.
pilihan = int(input("Masukkan pilihan: "))
Menerima input pilihan user.
<img width="1080" height="406" alt="code pilihan pertama ph" src="https://github.com/user-attachments/assets/a048cdd6-e3d0-468f-984d-87ff54d7c583" />
print(id(pengeluaran))
Menampilkan alamat memori list.
