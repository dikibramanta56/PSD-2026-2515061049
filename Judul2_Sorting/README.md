Judul Program: Program Mengurutkan Kecepatan Internet(Mbps)
Deskripsi Singkat: Program ini dibuat untuk mengurutkan data kecepatan internet yang dimasukkan oleh pengguna, dari yang paling lambat hingga yang paling cepat. Pengguna diminta memasukkan jumlah data, lalu mengisi nilai kecepatan internet satu per satu dalam satuan Mbps. Setelah semua data dimasukkan, program akan menampilkan data sebelum diurutkan dan setelah diurutkan.

Algoritma yang digunakan adalah Bubble Sort, yaitu metode pengurutan sederhana yang bekerja dengan cara membandingkan dua elemen yang bersebelahan, lalu menukarnya jika urutannya salah. Proses ini dilakukan berulang-ulang sampai seluruh data tersusun dengan benar.

Source Code:
<img width="875" height="998" alt="image" src="https://github.com/user-attachments/assets/c79c942b-3e13-48ce-bad6-479a962e0de3" />
Baris pertama def tukar(data, x, y): adalah pembuatan sebuah fungsi bernama tukar. Fungsi ini bertugas untuk menukar posisi dua data dalam sebuah list. Parameter data adalah list yang berisi angka, sedangkan x dan y adalah posisi (index) dari dua elemen yang ingin ditukar. Di dalam fungsi ini terdapat data[x], data[y] = data[y], data[x] yang artinya nilai pada posisi x dan y ditukar secara langsung tanpa menggunakan variabel sementara.

Selanjutnya ada def bubble_sort(data): yang merupakan fungsi utama untuk melakukan pengurutan menggunakan algoritma Bubble Sort. Di dalamnya, n = len(data) digunakan untuk menghitung jumlah elemen dalam list. Kemudian terdapat perulangan for i in range(n - 1): yang berfungsi untuk menentukan berapa kali proses pengulangan dilakukan. Pengulangan ini berjalan sebanyak jumlah data dikurangi satu, karena setiap iterasi akan menempatkan satu elemen terbesar di posisi akhir.

Di dalam perulangan pertama, terdapat perulangan kedua yaitu for j in range(n - i - 1):. Perulangan ini digunakan untuk membandingkan elemen yang bersebelahan. Bagian n - i - 1 bertujuan agar setiap iterasi tidak perlu mengecek elemen yang sudah berada di posisi benar di bagian akhir list.

Kemudian ada kondisi if data[j] > data[j + 1]: yang berarti jika elemen saat ini lebih besar dari elemen berikutnya, maka posisinya harus ditukar agar urutan menjadi benar (dari kecil ke besar). Jika kondisi ini terpenuhi, maka fungsi tukar(data, j, j + 1) akan dipanggil untuk menukar kedua elemen tersebut.

Setelah itu masuk ke fungsi main() yang menjadi pusat jalannya program. Pada bagian try: program mencoba membaca input jumlah data dari pengguna dengan n = int(input(...)). Jika pengguna memasukkan sesuatu yang bukan angka, maka akan terjadi error dan ditangani oleh except ValueError: yang akan menampilkan pesan "Input salah!" lalu menghentikan program dengan return.

Kemudian dibuat list kosong bernama kecepatan = [] untuk menyimpan data kecepatan internet yang akan dimasukkan pengguna.

Selanjutnya terdapat perulangan for i in range(n): yang berfungsi untuk meminta input sebanyak jumlah data yang sudah ditentukan. Di dalamnya ada perulangan while True: yang digunakan agar program terus meminta input sampai pengguna memasukkan angka yang benar. Pada bagian try: program mencoba mengubah input menjadi tipe float dengan nilai = float(input(...)). Jika berhasil, nilai tersebut dimasukkan ke dalam list kecepatan menggunakan append(), lalu perulangan dihentikan dengan break. Jika gagal (misalnya pengguna memasukkan huruf), maka akan masuk ke except ValueError: dan menampilkan pesan "Masukkan angka!".

Setelah semua data dimasukkan, program mencetak data awal dengan print("Sebelum:", kecepatan).

Kemudian fungsi bubble_sort(kecepatan) dipanggil untuk mengurutkan data tersebut.

Setelah proses pengurutan selesai, program mencetak hasilnya dengan print("Setelah (terlambat → tercepat):", kecepatan).

Terakhir, bagian if __name__ == "__main__": digunakan untuk memastikan bahwa fungsi main() hanya dijalankan ketika file ini dijalankan secara langsung, bukan ketika diimpor sebagai modul.

Output:
<img width="834" height="273" alt="image" src="https://github.com/user-attachments/assets/aca0d146-1188-434a-9cc0-798a4d46b3e9" />
Output dari program ini terdiri dari tiga bagian utama yang muncul secara berurutan saat program dijalankan.

Pertama, program akan meminta pengguna memasukkan jumlah data dengan tampilan seperti “Jumlah data kecepatan internet:”. Setelah itu, program akan meminta input kecepatan internet satu per satu, misalnya “Kecepatan ke-1 (Mbps):”, “Kecepatan ke-2 (Mbps):”, dan seterusnya sesuai jumlah yang dimasukkan. Jika pengguna memasukkan nilai yang bukan angka, program akan menampilkan pesan “Masukkan angka!” dan meminta input ulang sampai benar.

Setelah semua data berhasil dimasukkan, program akan menampilkan output pertama yaitu data sebelum diurutkan, dengan format seperti:
Sebelum: [20.5, 5.2, 10.0, 3.8]

Ini menunjukkan urutan data masih sama seperti yang dimasukkan oleh pengguna.
Kemudian program akan memproses data menggunakan algoritma Bubble Sort tanpa menampilkan prosesnya ke layar.

Setelah proses selesai, program akan menampilkan output kedua yaitu data setelah diurutkan, dengan format seperti:
Setelah (terlambat → tercepat): [3.8, 5.2, 10.0, 20.5]

Artinya data sudah diurutkan dari nilai terkecil (internet paling lambat) ke nilai terbesar (internet paling cepat).
Jadi secara keseluruhan, output program memperlihatkan perbandingan antara data sebelum dan sesudah diurutkan, sehingga pengguna bisa melihat perubahan urutan yang terjadi akibat proses sorting.

LINK VIDEO YOUTUBE: https://youtu.be/jgAUgFkQsbY?si=Lino6fxkd4rQCEWD
