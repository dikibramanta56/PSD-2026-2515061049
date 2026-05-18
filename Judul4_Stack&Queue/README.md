JUDUL PROGRAM: Sistem Penyimpanan PIN Sementara
DESKRIPSI SINGKAT: Program ini merupakan implementasi struktur data Stack (Array) menggunakan bahasa pemrograman Python dengan tema Sistem Penyimpanan PIN Sementara. Program dibuat untuk mensimulasikan proses penyimpanan data PIN sementara pada sistem keamanan digital menggunakan prinsip Last In First Out (LIFO), yaitu data yang terakhir disimpan akan menjadi data pertama yang dihapus.

Pada program ini pengguna dapat melakukan beberapa operasi dasar stack seperti menambahkan PIN (push), menghapus PIN terakhir (pop), melihat PIN teratas (peek), dan menampilkan seluruh data PIN yang tersimpan (display). Data PIN disimpan menggunakan array/list dengan kapasitas tertentu sehingga program juga dapat melakukan pengecekan kondisi stack penuh maupun stack kosong.

SOURCE CODE: 

<img width="1248" height="4054" alt="tugas akhir 4" src="https://github.com/user-attachments/assets/dcd3df18-0618-43fc-a132-0f9ab1c0a5ca" />

Program diawali dengan class PinStack: yang digunakan untuk membuat sebuah class bernama PinStack. Class ini berfungsi sebagai cetakan atau blueprint untuk membuat sistem penyimpanan PIN sementara menggunakan struktur data stack. Di dalam class inilah seluruh operasi stack seperti menambah data, menghapus data, melihat data teratas, dan menampilkan isi stack dibuat.

Selanjutnya terdapat def __init__(self, max_size=100): yang merupakan constructor atau method otomatis yang dijalankan ketika object dibuat. Constructor ini memiliki parameter self yang digunakan untuk merepresentasikan object itu sendiri, sedangkan max_size=100 digunakan untuk menentukan kapasitas maksimum stack yaitu sebanyak 100 data PIN.

Di dalam constructor terdapat self.MAX = max_size yang berfungsi menyimpan nilai kapasitas maksimum stack ke dalam variabel MAX. Setelah itu terdapat self.stack = [None] * self.MAX yang digunakan untuk membuat list atau array kosong sebanyak kapasitas maksimum stack. Nilai None digunakan sebagai penanda bahwa slot tersebut belum memiliki data. Kemudian self.top = -1 digunakan untuk menandai posisi teratas stack. Nilai -1 menunjukkan bahwa stack masih kosong dan belum memiliki data sama sekali.

Berikutnya terdapat def is_empty(self): yang digunakan untuk membuat method pengecekan apakah stack kosong atau tidak. Pada bagian ini terdapat return self.top == -1 yang berfungsi mengembalikan nilai True jika stack kosong karena posisi top masih berada di -1, dan mengembalikan False jika stack memiliki data.

Selanjutnya terdapat def is_full(self): yang digunakan untuk membuat method pengecekan apakah stack sudah penuh atau belum. Di dalamnya terdapat return self.top == self.MAX - 1 yang berfungsi mengecek apakah posisi top sudah berada pada indeks terakhir array. Karena indeks array dimulai dari 0, maka jika kapasitas stack adalah 100 data, indeks terakhirnya adalah 99. Jika kondisi bernilai benar maka stack dianggap penuh.

Kemudian terdapat def push(self, pin): yang digunakan untuk membuat method penambahan data PIN ke dalam stack. Method ini memiliki parameter pin yang berisi data PIN yang akan disimpan. Di dalam method tersebut terdapat if self.is_full(): yang berfungsi mengecek terlebih dahulu apakah stack sudah penuh. Jika kondisi benar maka program menjalankan print("Penyimpanan PIN penuh!") untuk menampilkan pesan bahwa stack tidak dapat menampung data lagi, lalu return digunakan untuk menghentikan method agar program tidak mengalami error akibat menambah data ke stack penuh.

Jika stack belum penuh maka program menjalankan self.top += 1 yang berfungsi menaikkan posisi top sebanyak satu langkah. Setelah itu self.stack[self.top] = pin digunakan untuk menyimpan data PIN ke posisi top terbaru pada array stack. Kemudian print(f"PIN {pin} berhasil disimpan") digunakan untuk menampilkan pesan bahwa PIN berhasil dimasukkan ke stack.

Berikutnya terdapat def pop(self): yang digunakan untuk membuat method penghapusan data teratas pada stack. Pada method ini terdapat if self.is_empty(): yang digunakan untuk mengecek apakah stack kosong. Jika stack kosong maka program menjalankan print("Tidak ada PIN yang tersimpan!") untuk menampilkan pesan bahwa tidak ada data yang bisa dihapus, kemudian return digunakan untuk menghentikan method.

Jika stack tidak kosong maka program menjalankan print(f"PIN {self.stack[self.top]} berhasil dihapus") yang berfungsi menampilkan data PIN yang akan dihapus dari stack. Setelah itu self.top -= 1 digunakan untuk menurunkan posisi top satu langkah sehingga data paling atas dianggap telah terhapus dari stack.

Selanjutnya terdapat def peek(self): yang digunakan untuk membuat method melihat data PIN teratas tanpa menghapusnya. Pada method ini terdapat if self.is_empty(): yang berfungsi mengecek apakah stack kosong. Jika kosong maka program menjalankan print("Tidak ada PIN yang tersimpan!") untuk menampilkan pesan bahwa tidak ada data yang dapat dilihat, lalu return digunakan untuk menghentikan method.

Jika stack memiliki data maka program menjalankan print(f"PIN terakhir: {self.stack[self.top]}") yang berfungsi menampilkan PIN yang berada pada posisi paling atas stack.

Kemudian terdapat def display(self): yang digunakan untuk membuat method menampilkan seluruh isi stack. Pada bagian ini terdapat if self.is_empty(): yang berfungsi mengecek apakah stack kosong. Jika kosong maka program menjalankan print("Penyimpanan PIN kosong!") untuk menampilkan pesan bahwa tidak ada data di dalam stack, kemudian return digunakan untuk menghentikan method.

Jika stack memiliki data maka program menjalankan print("\nDaftar PIN Tersimpan (Terbaru -> Lama)") untuk menampilkan judul daftar data stack dan print("--------------------------------------") untuk menampilkan garis pemisah tampilan. Setelah itu terdapat for i in range(self.top, -1, -1): yang digunakan untuk melakukan perulangan dari posisi top hingga indeks 0 secara mundur. Perulangan ini membuat data ditampilkan dari PIN terbaru ke PIN terlama sesuai konsep stack. Di dalam perulangan terdapat print(self.stack[i]) yang digunakan untuk menampilkan setiap data PIN pada stack. Setelah seluruh data selesai ditampilkan, program menjalankan print("--------------------------------------") untuk menampilkan garis penutup tampilan.

Berikutnya terdapat def main(): yang digunakan sebagai program utama. Pada bagian ini dibuat object stack menggunakan pin_system = PinStack() yang berfungsi membuat object bernama pin_system dari class PinStack. Setelah itu pilihan = 0 digunakan untuk membuat variabel penyimpan pilihan menu dari user.

Kemudian terdapat while pilihan != 5: yang digunakan untuk membuat perulangan menu program. Perulangan akan terus berjalan selama user belum memilih menu nomor 5 yaitu keluar program. Di dalam perulangan terdapat beberapa print() yang digunakan untuk menampilkan menu program seperti menu simpan PIN, hapus PIN, melihat PIN terakhir, menampilkan semua PIN, dan keluar program.

Selanjutnya terdapat blok try: dan except ValueError: yang digunakan untuk menangani kesalahan input. Pada bagian pilihan = int(input("Pilih menu: ")) program meminta user memasukkan pilihan menu dalam bentuk angka integer. Jika user memasukkan huruf atau simbol maka program akan masuk ke bagian except ValueError: dan menjalankan print("Input harus berupa angka!") untuk menampilkan pesan kesalahan, kemudian continue digunakan untuk mengulang kembali ke menu awal.

Kemudian terdapat if pilihan == 1: yang digunakan untuk menjalankan menu simpan PIN. Pada bagian ini program meminta input PIN menggunakan pin = int(input("Masukkan PIN: ")). Setelah itu terdapat if 1000 <= pin <= 999999: yang berfungsi memvalidasi agar PIN hanya terdiri dari 4 sampai 6 digit angka. Jika valid maka program menjalankan pin_system.push(pin) untuk memanggil method push dan menyimpan PIN ke stack. Namun jika kondisi salah maka program menjalankan print("PIN harus 4 sampai 6 digit!") untuk menampilkan pesan kesalahan. Jika user memasukkan huruf maka bagian except ValueError: dijalankan dan program menampilkan pesan print("PIN harus berupa angka!").

Selanjutnya terdapat elif pilihan == 2: yang digunakan untuk menjalankan menu hapus PIN terakhir. Pada bagian ini program menjalankan pin_system.pop() untuk memanggil method pop dan menghapus data PIN teratas pada stack.

Kemudian terdapat elif pilihan == 3: yang digunakan untuk menjalankan menu melihat PIN terakhir. Program menjalankan pin_system.peek() untuk memanggil method peek dan menampilkan data PIN teratas tanpa menghapusnya.

Berikutnya terdapat elif pilihan == 4: yang digunakan untuk menjalankan menu menampilkan seluruh isi stack. Pada bagian ini program menjalankan pin_system.display() untuk memanggil method display dan menampilkan seluruh data PIN yang tersimpan di dalam stack.

Selanjutnya terdapat elif pilihan == 5: yang digunakan untuk menjalankan menu keluar program. Pada bagian ini program menjalankan print("Program selesai.") untuk menampilkan pesan bahwa program telah selesai dijalankan.

Jika user memasukkan pilihan selain 1 sampai 5 maka bagian else: dijalankan dan print("Pilihan tidak valid!") digunakan untuk menampilkan pesan bahwa menu yang dipilih tidak tersedia.

Terakhir terdapat if __name__ == "__main__": yang digunakan untuk memastikan bahwa file Python dijalankan secara langsung, bukan diimpor dari file lain. Jika kondisi benar maka program menjalankan main() yang berfungsi memanggil dan menjalankan seluruh program utama.

OUTPUT:

<img width="798" height="912" alt="image" src="https://github.com/user-attachments/assets/d6835791-a5a3-4c1b-bb39-e965adebebd6" />

1. Simpan PIN
Pada menu ini pengguna diminta memasukkan PIN berupa angka 4 sampai 6 digit. Jika input valid dan stack belum penuh, program akan menampilkan pesan:

PIN 1234 berhasil disimpan

Output tersebut menunjukkan bahwa data PIN berhasil dimasukkan ke dalam stack dan menjadi data paling atas (top). Jika PIN tidak sesuai ketentuan atau stack penuh, program akan menampilkan pesan kesalahan.

2. Hapus PIN Terakhir
Pada menu ini program akan menghapus data PIN yang berada di posisi paling atas stack sesuai prinsip LIFO (Last In First Out). Setelah berhasil dihapus, program menampilkan output seperti:

PIN 1234 berhasil dihapus

Output tersebut menunjukkan bahwa PIN terakhir berhasil dikeluarkan dari stack. Jika stack kosong maka program akan menampilkan pesan bahwa tidak ada PIN yang tersimpan.

3. Lihat PIN Terakhir

Pada menu ini program menampilkan data PIN yang berada di posisi paling atas stack tanpa menghapusnya. Output yang muncul misalnya:

PIN terakhir: 1234

Output tersebut menunjukkan PIN terbaru yang tersimpan pada stack. Jika stack kosong maka program akan menampilkan pesan bahwa tidak ada PIN yang tersimpan.

4. Tampilkan Semua PIN
Pada menu ini program menampilkan seluruh data PIN yang tersimpan di dalam stack mulai dari PIN terbaru hingga PIN terlama. Contoh output:

Daftar PIN Tersimpan (Terbaru -> Lama)

5678
4321
1234


Output tersebut menunjukkan isi stack dari posisi top hingga data paling bawah sesuai konsep stack.

5. Keluar

Pada menu ini program akan menghentikan seluruh proses dan keluar dari program. Output yang ditampilkan adalah:

Program selesai.

Output tersebut menunjukkan bahwa program telah selesai dijalankan dan perulangan menu dihentikan.

LINK VIDEO YOUTUBE: https://youtu.be/vEmMZUXHHSU?si=4c-IW1Q0DqyCeiWm

