Judul Program: Pencacatan Harian
Deskripsi Singkat: Program ini berfungsi untuk mencatat pengeluaran harian pengguna selama 5 hari dengan menggunakan list 1 dimensi sebagai media penyimpanan data. Setiap data pengeluaran disimpan dalam satu index list, sehingga pengguna dapat memasukkan nilai pengeluaran, melihat data yang tersimpan, mengetahui alamat memori list, serta menghitung total seluruh pengeluaran melalui menu interaktif.
Struktur data yang diterapkan pada program ini adalah list 1 dimensi, yaitu struktur data linear yang menyimpan elemen secara berurutan dalam satu baris. Algoritma yang digunakan adalah traversal, yaitu proses menelusuri seluruh elemen list untuk menampilkan data dan menghitung total nilai pengeluaran.

SOURCE CODE:
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
<img width="1404" height="406" alt="code pilihan kedua ph" src="https://github.com/user-attachments/assets/f4d6ece9-66ce-43a8-a69b-e1a3f5f2fbb1" />
for i in range(len(pengeluaran)):
Menelusuri semua elemen list.
print(id(pengeluaran[i]))
Menampilkan alamat memori setiap elemen.
<img width="1448" height="672" alt="code pilihan ketiga ph" src="https://github.com/user-attachments/assets/8b4e0144-48fb-4d53-8df5-e1af458d8224" />
pengeluaran[i] = int(input())
Mengisi nilai pengeluaran ke setiap index list.
<img width="1158" height="482" alt="code pilihan keempat ph" src="https://github.com/user-attachments/assets/4b13b942-6e8b-4ea7-91c5-1ba8e1f5663d" />
print(pengeluaran)
Menampilkan seluruh isi list.
<img width="1034" height="444" alt="code pilihan kelima ph" src="https://github.com/user-attachments/assets/3274d37d-e183-4354-ba0c-0a78607166cd" />
total = sum(pengeluaran)
Menjumlahkan semua isi list.
print(total)
Menampilkan total pengeluaran.
<img width="834" height="444" alt="code pilihan keenam ph" src="https://github.com/user-attachments/assets/37dc6c27-3313-40dc-a69c-3114f9026e74" />
running = False
Menghentikan program.
<img width="1096" height="520" alt="code pengkondisian lain dan main()" src="https://github.com/user-attachments/assets/5ec6967d-64a4-4404-9800-c0908b8d4a19" />
else: print("Pilihan tersebut tidak tersedia") pengkondisian lain jika user menginput angka int selain 1-6 
if __name__ == "__main__":
    main()
    Menjalankan fungsi utama saat program dibuka.
OUTPUT:
<img width="1920" height="1080" alt="Screenshot (5)" src="https://github.com/user-attachments/assets/6871e50c-c892-4c6d-a68c-c4578fe99f41" />
<img width="1920" height="1080" alt="Screenshot (6)" src="https://github.com/user-attachments/assets/6e18357c-b430-497b-80e4-cfbed5f11ad3" />
Pilihan 1
Address list: 140234567890
Artinya program menunjukkan lokasi list disimpan di memori.
pilihan 2
Address pengeluaran[0] = 140234500001
Address pengeluaran[1] = 140234500002
Artinya setiap nilai dalam list memiliki alamat memori tersendiri.
pilihan 3
Hari ke-1: Rp 10000
Hari ke-2: Rp 15000
Nilai yang dimasukkan akan disimpan ke dalam list.
pilihan 4
Output menampilkan seluruh data pengeluaran yang sudah disimpan.
pilhan 5
Total pengeluaran: Rp 50000
Output menampilkan jumlah seluruh pengeluaran.
pilihan 6
Program selesai
Output menampilkan pesan bahwa program selesai.
Program berhenti dijalankan.

LINK YOUTUBE: https://youtu.be/Y6eOMLdVMfM?si=gcbvKZjmwpDrCuhx


