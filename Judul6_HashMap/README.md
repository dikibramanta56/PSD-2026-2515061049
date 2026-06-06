JUDUL: Sistem Penyewaan Komputer(Warnet) 

DESKRIPSI SINGKAT: Program ini dibuat untuk mensimulasikan sistem penyewaan komputer pada warnet menggunakan struktur data Hash Map Open Addressing dengan metode Linear Probing. Program dapat digunakan untuk menambahkan data komputer beserta statusnya (tersedia atau sedang digunakan), mencari data komputer berdasarkan nomor komputer, memperbarui status komputer, serta menampilkan seluruh daftar komputer yang tersimpan di dalam sistem. Jika terjadi tabrakan posisi penyimpanan (collision), program akan menggunakan metode Linear Probing yaitu mencari slot berikutnya secara berurutan sampai menemukan tempat kosong untuk menyimpan data.

SOURCE CODE:
<img width="1202" height="3142" alt="code komputer" src="https://github.com/user-attachments/assets/cae53acc-2085-4dbf-9bc8-7078058a66a9" />

Program diawali dengan class Komputer: yang digunakan untuk membuat class bernama Komputer. Class ini berfungsi sebagai cetakan untuk menyimpan data satu komputer di warnet, seperti nomor komputer dan status komputer tersebut.

Selanjutnya terdapat def init(self): yang merupakan constructor dari class Komputer. Constructor ini otomatis dijalankan ketika object Komputer baru dibuat. Parameter self digunakan untuk mewakili object Komputer itu sendiri.

Di dalam constructor terdapat self.nomor = None yang digunakan untuk menyiapkan tempat penyimpanan nomor komputer. Nilai awalnya None karena saat object baru dibuat, nomor komputer belum diisi.

Kemudian terdapat self.status = None yang digunakan untuk menyiapkan tempat penyimpanan status komputer. Status ini nantinya bisa berisi keterangan seperti “Tersedia” atau “Digunakan”.

Selanjutnya terdapat class RentalWarnet: yang digunakan untuk membuat class utama sistem rental warnet. Class ini berfungsi untuk mengatur data komputer, seperti menambah komputer, mencari komputer, dan menampilkan daftar komputer.

Berikutnya terdapat def init(self, ukuran=10): yang merupakan constructor dari class RentalWarnet. Constructor ini otomatis dijalankan ketika object RentalWarnet dibuat. Parameter ukuran=10 berarti jumlah slot penyimpanan data komputer secara default adalah 10.

Di dalam constructor terdapat self.ukuran = ukuran yang digunakan untuk menyimpan ukuran atau jumlah slot data yang tersedia. Jadi, kalau ukuran bernilai 10, maka sistem memiliki 10 tempat penyimpanan data komputer.

Selanjutnya terdapat self.data = [None] * ukuran yang digunakan untuk membuat list kosong sebanyak ukuran yang sudah ditentukan. Karena ukurannya 10, maka akan dibuat 10 slot kosong yang awalnya berisi None.

Kemudian terdapat def hash(self, nomor): yang digunakan untuk membuat fungsi hash. Fungsi ini bertugas menentukan posisi awal penyimpanan data berdasarkan nomor komputer.

Di dalam fungsi hash terdapat return nomor % self.ukuran. Baris ini berarti nomor komputer akan dibagi dengan ukuran tabel, lalu sisa baginya dijadikan posisi slot. Misalnya nomor komputer 11 dan ukuran tabel 10, maka 11 % 10 hasilnya 1, jadi data awalnya akan diarahkan ke slot indeks 1.

Selanjutnya terdapat def tambah(self, nomor, status): yang digunakan untuk menambahkan data komputer ke dalam sistem rental warnet. Fungsi ini menerima nomor komputer dan status komputer.

Di dalam fungsi tambah terdapat i = self.hash(nomor). Baris ini digunakan untuk menentukan slot awal tempat data komputer akan disimpan. Jadi program bertanya, “Nomor komputer ini cocoknya masuk ke indeks berapa?”

Kemudian terdapat while self.data[i] is not None: yang berarti selama slot tersebut sudah terisi, program akan terus mencari slot lain yang kosong.

Di dalam perulangan terdapat if self.data[i].nomor == nomor: yang digunakan untuk mengecek apakah nomor komputer yang dimasukkan ternyata sudah ada di dalam data.

Jika nomor komputer sudah ada, maka self.data[i].status = status akan dijalankan. Baris ini digunakan untuk memperbarui status komputer tanpa membuat data baru. Contohnya komputer 11 awalnya “Digunakan”, lalu bisa diubah menjadi “Tersedia”.

Setelah status diperbarui, terdapat return yang digunakan untuk menghentikan fungsi tambah karena data sudah berhasil diperbarui.

Jika slot sudah terisi tetapi nomornya berbeda, maka i = (i + 1) % self.ukuran akan dijalankan. Baris ini digunakan untuk pindah ke slot berikutnya. Jika sudah sampai slot terakhir, program akan kembali lagi ke slot awal karena menggunakan simbol %.

Setelah menemukan slot kosong, terdapat komputer = Komputer() yang digunakan untuk membuat object baru dari class Komputer.

Selanjutnya komputer.nomor = nomor digunakan untuk mengisi nomor komputer ke dalam object komputer yang baru dibuat.

Kemudian komputer.status = status digunakan untuk mengisi status komputer ke dalam object tersebut.

Setelah itu self.data[i] = komputer digunakan untuk menyimpan object komputer ke dalam slot list data pada indeks yang sudah ditemukan.

Selanjutnya terdapat def cari(self, nomor): yang digunakan untuk mencari data komputer berdasarkan nomor komputer.

Di dalam fungsi cari terdapat i = self.hash(nomor) yang digunakan untuk menentukan posisi awal pencarian berdasarkan nomor komputer.

Kemudian terdapat while self.data[i] is not None: yang berarti selama slot yang dicek tidak kosong, program akan terus melakukan pencarian.

Di dalam perulangan terdapat if self.data[i].nomor == nomor: yang digunakan untuk mengecek apakah nomor komputer pada slot tersebut sama dengan nomor yang dicari.

Jika nomor komputer ditemukan, maka return self.data[i] akan mengembalikan data komputer tersebut.

Jika belum ditemukan, maka i = (i + 1) % self.ukuran digunakan untuk pindah ke slot berikutnya.

Jika pencarian berhenti karena bertemu slot kosong, maka return None akan dijalankan. Artinya komputer dengan nomor tersebut tidak ditemukan.

Selanjutnya terdapat def tampil(self): yang digunakan untuk menampilkan seluruh daftar slot komputer di dalam sistem.

Di dalam fungsi tampil terdapat print("\nDAFTAR KOMPUTER") yang digunakan untuk mencetak judul daftar komputer. Simbol \n digunakan agar output turun ke baris baru terlebih dahulu.

Kemudian terdapat for i in range(self.ukuran): yang digunakan untuk mengulang dari indeks 0 sampai indeks terakhir sesuai ukuran tabel.

Di dalam perulangan terdapat if self.data[i]: yang digunakan untuk mengecek apakah slot pada indeks tersebut berisi data komputer.

Jika slot berisi data, maka print(...) akan menampilkan indeks slot, nomor komputer, dan status komputer.

Bagian f"{i} → Komputer {self.data[i].nomor}" digunakan untuk menampilkan nomor indeks dan nomor komputer.

Bagian f" ({self.data[i].status})" digunakan untuk menampilkan status komputer, misalnya “Tersedia” atau “Digunakan”.

Jika slot kosong, maka else akan dijalankan.

Di dalam else terdapat print(f"{i} → Kosong") yang digunakan untuk menampilkan bahwa slot tersebut belum memiliki data komputer.

Selanjutnya terdapat def main(): yang digunakan sebagai fungsi utama tempat program dijalankan.

Di dalam fungsi main terdapat warnet = RentalWarnet() yang digunakan untuk membuat object dari class RentalWarnet. Object ini nantinya dipakai untuk mengelola data komputer warnet.

Kemudian terdapat warnet.tambah(1, "Tersedia") yang digunakan untuk menambahkan komputer nomor 1 dengan status Tersedia.

Selanjutnya terdapat warnet.tambah(11, "Digunakan") yang digunakan untuk menambahkan komputer nomor 11 dengan status Digunakan.

Kemudian terdapat warnet.tambah(21, "Tersedia") yang digunakan untuk menambahkan komputer nomor 21 dengan status Tersedia.

Ketiga nomor tersebut yaitu 1, 11, dan 21 akan menghasilkan nilai hash yang sama jika ukuran tabelnya 10, karena 1 % 10, 11 % 10, dan 21 % 10 sama-sama mengarah ke indeks 1. Karena itulah program menggunakan open addressing untuk mencari slot kosong berikutnya.

Selanjutnya terdapat warnet.tampil() yang digunakan untuk menampilkan daftar komputer yang sudah dimasukkan ke dalam sistem.

Kemudian terdapat hasil = warnet.cari(11) yang digunakan untuk mencari data komputer dengan nomor 11. Hasil pencariannya disimpan ke dalam variabel hasil.

Selanjutnya terdapat if hasil: yang digunakan untuk mengecek apakah komputer nomor 11 berhasil ditemukan.

Jika ditemukan, maka print(...) akan menampilkan nomor komputer dan status komputer tersebut.

Bagian f"\nKomputer {hasil.nomor}" digunakan untuk menampilkan nomor komputer yang ditemukan.

Bagian f" status {hasil.status}" digunakan untuk menampilkan status komputer tersebut.

Kemudian terdapat warnet.tambah(11, "Tersedia") yang digunakan untuk mengubah status komputer nomor 11 dari “Digunakan” menjadi “Tersedia”. Karena nomor 11 sudah ada, program tidak menambah data baru, tetapi hanya memperbarui statusnya.

Selanjutnya terdapat print("\nSetelah dikembalikan:") yang digunakan untuk menampilkan keterangan bahwa data setelah komputer dikembalikan akan ditampilkan.

Kemudian terdapat warnet.tampil() yang digunakan untuk menampilkan kembali daftar komputer setelah status komputer nomor 11 diperbarui.

Terakhir terdapat main() yang digunakan untuk menjalankan fungsi utama. Tanpa baris ini, program hanya berisi class dan fungsi saja, tetapi tidak akan benar-benar berjalan.

OUTPUT:
<img width="882" height="731" alt="image" src="https://github.com/user-attachments/assets/c3a7b38b-21bc-4678-92d6-5496af41ef84" />

Saat program dijalankan, sistem pertama kali menambahkan 3 data komputer ke dalam rental warnet yaitu komputer nomor 1 dengan status Tersedia, komputer nomor 11 dengan status Digunakan, dan komputer nomor 21 dengan status Tersedia.

Karena program menggunakan Hash Map Open Addressing (Linear Probing) dengan ukuran tabel 10, maka ketiga nomor tersebut memiliki hasil hash yang sama:

1 % 10 = 1
11 % 10 = 1
21 % 10 = 1

Akibatnya:

Komputer 1 masuk ke slot 1
Komputer 11 mencoba masuk slot 1, tetapi sudah terisi → pindah ke slot 2
Komputer 21 mencoba slot 1 dan 2, keduanya penuh → pindah ke slot 3

Maka daftar awal yang ditampilkan kira-kira menjadi:

DAFTAR KOMPUTER
0 → Kosong
1 → Komputer 1 (Tersedia)
2 → Komputer 11 (Digunakan)
3 → Komputer 21 (Tersedia)
4 → Kosong
5 → Kosong
6 → Kosong
7 → Kosong
8 → Kosong
9 → Kosong

Setelah itu program melakukan pencarian komputer nomor 11 menggunakan fungsi cari(). Karena ditemukan, program menampilkan:

Komputer 11 status Digunakan

Berikutnya program menjalankan:

warnet.tambah(11, "Tersedia")

Karena nomor 11 sudah ada, program tidak menambah komputer baru, tetapi hanya mengubah statusnya dari Digunakan menjadi Tersedia.

Output akhir menjadi:

Setelah dikembalikan:

DAFTAR KOMPUTER
0 → Kosong
1 → Komputer 1 (Tersedia)
2 → Komputer 11 (Tersedia)
3 → Komputer 21 (Tersedia)
...

Artinya komputer nomor 11 yang sebelumnya sedang dipakai berhasil dikembalikan dan statusnya berubah menjadi tersedia kembali.

LINK VIDEO YOUTUBE: https://youtu.be/A3x3x5aWfAA?si=4YCyZsskyjhhUtzC
