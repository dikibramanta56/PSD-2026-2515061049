JUDUL PROGRAM: Pencarian Nilai Ping Server (ms)
DESKRIPSI SINGKAT: Program ini merupakan aplikasi sederhana bertema jaringan komputer yang digunakan untuk mencari nilai ping server menggunakan metode Sequential Search Sentinel. Data ping server disimpan dalam bentuk list bilangan integer, kemudian pengguna memasukkan nilai ping yang ingin dicari. Program akan melakukan pencarian secara berurutan dari awal hingga data ditemukan. Metode Sentinel digunakan dengan menambahkan sementara nilai target ke akhir list agar proses pencarian menjadi lebih sederhana dan efisien. Setelah pencarian selesai, program akan menampilkan apakah nilai ping ditemukan beserta posisi indeksnya.

SOURCE CODE : 
<img width="1480" height="2116" alt="code sequential search" src="https://github.com/user-attachments/assets/f310b854-843e-4946-b910-a7bf0c01b70c" />
Program diawali dengan def sequential_search_sentinel(data, n, target): yang digunakan untuk membuat fungsi pencarian menggunakan metode Sequential Search Sentinel. Fungsi ini memiliki tiga parameter yaitu data sebagai list yang akan dicari, n sebagai jumlah data asli, dan target sebagai nilai yang ingin dicari. Di dalam fungsi tersebut terdapat data.append(target) yang berfungsi menambahkan target sementara ke akhir list sebagai sentinel atau penanda agar proses pencarian pasti berhenti ketika target ditemukan. Selanjutnya i = 0 digunakan untuk membuat variabel indeks awal pencarian dimulai dari posisi pertama list.

Kemudian terdapat perulangan while data[i] != target: yang akan terus berjalan selama data pada indeks ke-i belum sama dengan target yang dicari. Jika data belum ditemukan maka i += 1 akan dijalankan untuk menambah nilai indeks sehingga pencarian berpindah ke elemen berikutnya. Setelah target ditemukan, program menjalankan data.pop() untuk menghapus kembali sentinel yang sebelumnya ditambahkan agar isi list kembali seperti semula. Selanjutnya kondisi if i < n: digunakan untuk mengecek apakah target ditemukan di dalam data asli atau hanya ditemukan pada sentinel tambahan. Jika indeks i masih lebih kecil dari jumlah data asli n, maka program menjalankan return True, i yang berarti data ditemukan dan mengembalikan posisi indeksnya. Namun jika kondisi salah maka bagian else: dijalankan dan return False, -1 digunakan untuk menandakan bahwa data tidak ditemukan.

Berikutnya terdapat def main(): yang berfungsi sebagai program utama. Pada bagian ini dibuat list ping_server = [12, 25, 8, 45, 67, 30, 90, 15, 55, 40] yang berisi data nilai ping server dalam satuan milisecond (ms). Kemudian n = len(ping_server) digunakan untuk menghitung jumlah data pada list dan menyimpannya ke variabel n. Program lalu menampilkan judul menggunakan print("=== Sistem Monitoring Ping Server ==="), menampilkan keterangan data dengan print("Data ping server (ms):"), dan menampilkan isi list menggunakan print(ping_server).

Selanjutnya terdapat while True: yang digunakan untuk membuat perulangan input agar pengguna terus diminta memasukkan data sampai input yang diberikan benar. Di dalamnya terdapat try: untuk mencoba menjalankan proses input, kemudian target = int(input("\nMasukkan nilai ping yang ingin dicari: ")) digunakan untuk menerima input dari pengguna dan mengubahnya menjadi tipe integer. Jika input berhasil maka break dijalankan untuk menghentikan perulangan. Namun jika pengguna memasukkan selain angka maka except ValueError: akan menangani error tersebut dan program menampilkan pesan print("Input harus berupa angka!").

Setelah input berhasil diterima, program menjalankan found, index = sequential_search_sentinel(ping_server, n, target) untuk memanggil fungsi pencarian dan menyimpan hasilnya ke variabel found dan index. Kemudian kondisi if found: digunakan untuk mengecek apakah data ditemukan. Jika ditemukan maka program menampilkan print(f"\nNilai ping {target} ms ditemukan pada indeks ke-{index}"). Namun jika tidak ditemukan maka bagian else: dijalankan dan program menampilkan print(f"\nNilai ping {target} ms tidak ditemukan").

Terakhir terdapat if __name__ == "__main__": yang berfungsi untuk memastikan program dijalankan secara langsung, kemudian main() dipanggil agar seluruh program dapat dieksekusi.

OUTPUT:
<img width="870" height="265" alt="image" src="https://github.com/user-attachments/assets/0b53c38f-ce02-4389-ae6e-03943d6ad297" />
Ketika program dijalankan ia akan menampilkan list yang telah dibuat [12, 25, 8, 45, 67, 30, 90, 15, 55, 40]
Kemudian pengguna memasukkan nilai yang ingin dicari, misalnya: 30
Program lalu memanggil fungsi sequential_search_sentinel() untuk melakukan proses pencarian menggunakan metode Sequential Search Sentinel. Pada awal proses, nilai 30 ditambahkan sementara ke akhir list sebagai sentinel sehingga data sementara menjadi:

[12, 25, 8, 45, 67, 30, 90, 15, 55, 40, 30]

Selanjutnya program mulai melakukan pencarian dari indeks ke-0 menggunakan perulangan while. Program membandingkan data satu per satu dengan target 30. Pada indeks ke-0 nilai 12 tidak sama dengan 30, lalu indeks bertambah menjadi 1. Pada indeks ke-1 nilai 25 juga tidak sama dengan 30, sehingga pencarian dilanjutkan. Hal yang sama terjadi pada indeks ke-2 dengan nilai 8, indeks ke-3 dengan nilai 45, dan indeks ke-4 dengan nilai 67.

Ketika pencarian mencapai indeks ke-5, program menemukan nilai 30 yang sama dengan target. Karena target ditemukan sebelum mencapai sentinel tambahan, maka kondisi if i < n bernilai benar. Nilai i saat itu adalah 5 dan jumlah data asli n adalah 10, sehingga:

5 < 10

bernilai True. Oleh karena itu fungsi mengembalikan nilai True dan indeks 5. Setelah itu program menampilkan output:

Nilai ping 30 ms ditemukan pada indeks ke-5

Output tersebut menunjukkan bahwa nilai ping 30 ms berhasil ditemukan pada posisi indeks ke-5 dalam list data ping server.

EXTRAS: Menghitung Rumus interpolation secara manual lalu ditulis di kertas
<img width="1086" height="1448" alt="images interpolation" src="https://github.com/user-attachments/assets/f87fa1c1-1b08-4c56-8413-8b029cca29b4" />


LINK VIDEO YOUTUBE: https://youtu.be/ASE5qGAY4qg?si=nckH-gfYVcgRmmbs
