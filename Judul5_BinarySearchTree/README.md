JUDUL PROGRAM: Sistem Registrasi ID Player Game Menggunakan Binary Search Tree (BST)

DEKSRIPSI SINGKAT: Program ini dibuat untuk mengelola data ID player dalam sebuah game menggunakan struktur data Binary Search Tree (BST). Program memungkinkan pengguna untuk melakukan registrasi ID player, mencari ID player tertentu, menampilkan data player dengan metode traversal inorder, preorder, dan postorder, serta mengetahui ID player terkecil, ID player terbesar, jumlah player, dan total seluruh ID player yang tersimpan di dalam BST. Struktur BST digunakan agar proses pencarian dan pengelolaan data dapat dilakukan secara lebih teratur dan efisien.

SOURCE CODE:

<img width="1202" height="2230" alt="code BST 1" src="https://github.com/user-attachments/assets/bce2b22a-2555-44b3-9a6f-b8e7167db345" />

Program diawali dengan class Node: yang digunakan untuk membuat sebuah class bernama Node. Class ini berfungsi sebagai representasi satu buah node pada Binary Search Tree (BST). Di dalam node nantinya akan disimpan data berupa ID player beserta cabang kiri dan kanan.

Selanjutnya terdapat def __init__(self, key): yang merupakan constructor dari class Node. Constructor ini otomatis dijalankan ketika object node baru dibuat. Parameter self digunakan untuk merepresentasikan object itu sendiri, sedangkan key digunakan untuk menerima nilai data yang akan disimpan pada node.

Di dalam constructor terdapat self.key = key yang berfungsi menyimpan nilai data atau ID player ke dalam node. Nilai inilah yang nantinya digunakan pada proses pencarian maupun traversal BST.

Berikutnya terdapat self.left = None yang digunakan untuk membuat pointer atau cabang kiri node. Nilai awalnya adalah None karena node baru belum memiliki anak kiri.

Kemudian terdapat self.right = None yang digunakan untuk membuat pointer atau cabang kanan node. Nilai awal None menunjukkan bahwa node baru belum memiliki anak kanan.

Selanjutnya program memiliki class BSTPlayer: yang digunakan untuk membuat class utama Binary Search Tree. Class ini berfungsi untuk mengatur seluruh operasi BST seperti insert, search, traversal, mencari nilai minimum, maksimum, menghitung node, dan menjumlahkan seluruh nilai node.

Di dalam class tersebut terdapat def __init__(self): yang merupakan constructor class BSTPlayer. Constructor ini dijalankan ketika object BST dibuat.

Kemudian terdapat self.root = None yang digunakan untuk membuat root atau akar BST. Nilai awal None menunjukkan bahwa tree masih kosong dan belum memiliki node.

Selanjutnya terdapat def insert_node(self, root, key): yang digunakan untuk membuat fungsi memasukkan node baru ke dalam BST secara rekursif. Parameter root merepresentasikan posisi node saat ini, sedangkan key merupakan data baru yang ingin dimasukkan.

Di dalam fungsi insert terdapat if root is None: yang digunakan untuk mengecek apakah posisi node saat ini masih kosong.

Jika kondisi tersebut benar maka program menjalankan return Node(key) yang berfungsi membuat node baru menggunakan nilai key. Node baru tersebut kemudian dikembalikan ke posisi tree yang kosong tadi.

Selanjutnya terdapat if key < root.key: yang digunakan untuk membandingkan apakah nilai yang dimasukkan lebih kecil daripada node saat ini.

Jika nilai lebih kecil maka program menjalankan root.left = self.insert_node(root.left, key) yang berfungsi memasukkan data ke cabang kiri BST secara rekursif. Program akan terus bergerak ke kiri sampai menemukan posisi kosong.

Kemudian terdapat elif key > root.key: yang digunakan untuk mengecek apakah nilai yang dimasukkan lebih besar daripada node saat ini.

Jika kondisi tersebut benar maka program menjalankan root.right = self.insert_node(root.right, key) yang berfungsi memasukkan data ke cabang kanan BST secara rekursif sampai ditemukan posisi kosong.

Setelah proses insert selesai terdapat return root yang digunakan untuk mengembalikan root BST agar struktur tree tetap tersusun dengan benar.

Selanjutnya terdapat def insert(self, key): yang digunakan sebagai fungsi sederhana untuk memanggil proses insert dari root utama BST.

Di dalamnya terdapat self.root = self.insert_node(self.root, key) yang berfungsi memasukkan data baru ke BST dimulai dari root utama.

Berikutnya terdapat def search_node(self, root, key): yang digunakan untuk membuat fungsi pencarian data pada BST secara rekursif.

Di dalam fungsi search terdapat if root is None: yang digunakan untuk mengecek apakah node saat ini kosong.

Jika kosong maka program menjalankan return False yang menandakan bahwa data tidak ditemukan di BST.

Selanjutnya terdapat if root.key == key: yang digunakan untuk mengecek apakah nilai node saat ini sama dengan nilai yang dicari.

Jika sama maka program menjalankan return True yang menandakan bahwa data berhasil ditemukan.

Kemudian terdapat if key < root.key: yang digunakan untuk mengecek apakah nilai yang dicari lebih kecil dari node saat ini.

Jika lebih kecil maka program menjalankan return self.search_node(root.left, key) yang berfungsi melanjutkan pencarian ke cabang kiri BST secara rekursif.

Jika kondisi sebelumnya tidak terpenuhi maka program menjalankan return self.search_node(root.right, key) yang digunakan untuk melanjutkan pencarian ke cabang kanan BST.

Selanjutnya terdapat def search(self, key): yang digunakan sebagai fungsi sederhana untuk memulai proses pencarian data dari root utama BST.

Di dalamnya terdapat return self.search_node(self.root, key) yang berfungsi memanggil fungsi pencarian rekursif dimulai dari root utama.

Berikutnya terdapat def inorder(self, root): yang digunakan untuk membuat traversal inorder pada BST. Traversal inorder memiliki urutan kiri → root → kanan sehingga data akan tampil terurut dari kecil ke besar.

Di dalam fungsi inorder terdapat if root is None: yang digunakan untuk mengecek apakah node kosong.

Jika node kosong maka program menjalankan return yang berfungsi menghentikan proses traversal pada cabang tersebut.

Selanjutnya terdapat self.inorder(root.left) yang digunakan untuk menelusuri seluruh cabang kiri terlebih dahulu secara rekursif.

Kemudian terdapat print(root.key, end=" ") yang digunakan untuk mencetak nilai node saat ini ke layar.

Setelah itu terdapat self.inorder(root.right) yang digunakan untuk menelusuri seluruh cabang kanan BST secara rekursif.

<img width="956" height="2268" alt="code BST 2" src="https://github.com/user-attachments/assets/99469973-f39b-4f72-abec-abe2a8bcd52b" />

Selanjutnya terdapat def preorder(self, root): yang digunakan untuk membuat traversal preorder pada BST. Traversal preorder memiliki urutan root → kiri → kanan, sehingga node induk akan ditampilkan terlebih dahulu sebelum cabang kiri dan kanan.

Di dalam fungsi preorder terdapat if root is None: yang digunakan untuk mengecek apakah node saat ini kosong.

Jika node kosong maka program menjalankan return yang berfungsi menghentikan proses traversal pada cabang tersebut.

Kemudian terdapat print(root.key, end=" ") yang digunakan untuk mencetak nilai node saat ini terlebih dahulu ke layar.

Setelah itu terdapat self.preorder(root.left) yang digunakan untuk menelusuri seluruh cabang kiri BST secara rekursif.

Lalu terdapat self.preorder(root.right) yang digunakan untuk menelusuri seluruh cabang kanan BST secara rekursif.

Traversal preorder biasa digunakan untuk melihat struktur awal tree karena root selalu ditampilkan terlebih dahulu.

Berikutnya terdapat def postorder(self, root): yang digunakan untuk membuat traversal postorder pada BST. Traversal postorder memiliki urutan kiri → kanan → root sehingga node induk ditampilkan paling akhir.

Di dalam fungsi postorder terdapat if root is None: yang digunakan untuk mengecek apakah node kosong.

Jika node kosong maka program menjalankan return yang berfungsi menghentikan traversal pada cabang tersebut.

Selanjutnya terdapat self.postorder(root.left) yang digunakan untuk menelusuri seluruh cabang kiri BST terlebih dahulu secara rekursif.

Kemudian terdapat self.postorder(root.right) yang digunakan untuk menelusuri seluruh cabang kanan BST secara rekursif.

Setelah cabang kiri dan kanan selesai ditelusuri maka program menjalankan print(root.key, end=" ") yang digunakan untuk mencetak nilai node saat ini.

Traversal postorder sering digunakan ketika proses penghapusan tree karena node anak diproses lebih dahulu dibanding node induk.

Selanjutnya terdapat def find_min(self, root): yang digunakan untuk membuat fungsi pencarian nilai terkecil pada BST.

Di dalam fungsi tersebut terdapat if root is None: yang digunakan untuk mengecek apakah BST kosong.

Jika BST kosong maka program menjalankan return -1 yang berfungsi mengembalikan nilai -1 sebagai penanda bahwa data tidak tersedia.

Kemudian terdapat current = root yang digunakan untuk membuat variabel sementara bernama current. Variabel ini digunakan untuk menelusuri node BST dimulai dari root.

Setelah itu terdapat while current.left is not None: yang digunakan untuk melakukan perulangan selama node masih memiliki anak kiri.

Hal ini dilakukan karena pada BST nilai terkecil selalu berada di posisi paling kiri.

Di dalam perulangan terdapat current = current.left yang digunakan untuk memindahkan posisi current ke node sebelah kiri secara terus-menerus.

Ketika node paling kiri ditemukan maka perulangan berhenti dan program menjalankan return current.key yang digunakan untuk mengembalikan nilai node terkecil dalam BST.

Berikutnya terdapat def find_max(self, root): yang digunakan untuk membuat fungsi pencarian nilai terbesar pada BST.

Di dalam fungsi tersebut terdapat if root is None: yang digunakan untuk mengecek apakah BST kosong.

Jika kosong maka program menjalankan return -1 sebagai tanda bahwa tidak ada data di dalam tree.

Kemudian terdapat current = root yang digunakan untuk membuat variabel sementara guna menelusuri node BST.

Setelah itu terdapat while current.right is not None: yang digunakan untuk melakukan perulangan selama node masih memiliki anak kanan.

Hal ini dilakukan karena pada BST nilai terbesar selalu berada di posisi paling kanan.

Di dalam perulangan terdapat current = current.right yang digunakan untuk memindahkan posisi current ke node kanan secara terus-menerus.

Jika node paling kanan telah ditemukan maka program menjalankan return current.key yang digunakan untuk mengembalikan nilai terbesar dalam BST.

Selanjutnya terdapat def count_nodes(self, root): yang digunakan untuk menghitung jumlah seluruh node yang ada di dalam BST.

Di dalam fungsi tersebut terdapat if root is None: yang digunakan untuk mengecek apakah node kosong.

Jika node kosong maka program menjalankan return 0 yang berarti jumlah node pada cabang tersebut adalah nol.

<img width="910" height="672" alt="code BST 3" src="https://github.com/user-attachments/assets/5d8ddcdc-559d-4796-889b-c83bf53de8b3" />

Selanjutnya terdapat def sum_nodes(self, root): yang digunakan untuk membuat fungsi penjumlahan seluruh nilai node yang ada di dalam BST. Fungsi ini berguna untuk menghitung total semua ID player yang tersimpan pada tree.

Di dalam fungsi tersebut terdapat if root is None: yang digunakan untuk mengecek apakah node saat ini kosong.

Jika node kosong maka program menjalankan return 0 yang berarti cabang tersebut tidak memiliki nilai untuk dijumlahkan.

Bagian ini digunakan untuk menjumlahkan seluruh nilai node BST secara rekursif. root.key merepresentasikan nilai node saat ini, kemudian ditambahkan dengan hasil penjumlahan seluruh node pada cabang kiri melalui self.sum_nodes(root.left) dan seluruh node pada cabang kanan melalui self.sum_nodes(root.right).

Proses ini akan terus dilakukan sampai seluruh node pada BST selesai ditelusuri. Setelah semua nilai dijumlahkan, fungsi akan mengembalikan total keseluruhan nilai node yang ada di dalam tree.

<img width="1048" height="1204" alt="code BST 4" src="https://github.com/user-attachments/assets/24d3c9ff-b9ca-496f-986c-b5fc67f8008d" />

Selanjutnya terdapat def main(): yang digunakan sebagai fungsi utama program. Seluruh proses interaksi pengguna seperti menampilkan menu, menerima input, dan menjalankan operasi BST dilakukan di dalam fungsi ini.

Di dalam fungsi main terdapat bst = BSTPlayer() yang digunakan untuk membuat object BST baru dari class BSTPlayer. Object ini nantinya dipakai untuk menjalankan seluruh operasi Binary Search Tree pada data ID player.

Kemudian terdapat pilih = 0 yang digunakan untuk membuat variabel bernama pilih. Variabel ini berfungsi menyimpan pilihan menu dari pengguna. Nilai awal dibuat 0 agar program dapat masuk ke dalam perulangan menu.

Selanjutnya terdapat while pilih != 10: yang digunakan untuk membuat perulangan menu program. Perulangan akan terus berjalan selama pengguna belum memilih menu 10 yaitu keluar dari program.

Di dalam perulangan terdapat beberapa perintah print() yang digunakan untuk menampilkan tampilan menu program ke layar. Menu tersebut berisi daftar operasi BST seperti registrasi player, pencarian player, traversal BST, pencarian nilai minimum dan maksimum, menghitung jumlah node, serta menjumlahkan seluruh nilai node.

Setelah menu ditampilkan, program menggunakan try: untuk menangani kemungkinan kesalahan input dari pengguna. Di dalamnya terdapat pilih = int(input("Pilih menu: ")) yang digunakan untuk meminta pengguna memasukkan pilihan menu. Input yang diterima masih berupa string sehingga harus diubah menjadi integer menggunakan int() agar dapat diproses sebagai angka.

Kemudian terdapat except ValueError: yang digunakan untuk menangkap error apabila pengguna memasukkan data selain angka, misalnya huruf atau simbol.

Jika error terjadi maka program menjalankan print("Input tidak valid!") yang digunakan untuk menampilkan pesan kesalahan bahwa input yang dimasukkan tidak sesuai.

Setelah itu terdapat continue yang digunakan untuk menghentikan iterasi saat ini dan kembali ke awal perulangan menu. Dengan demikian program akan menampilkan menu kembali tanpa menjalankan operasi BST lainnya ketika terjadi kesalahan input.

<img width="1294" height="1622" alt="code BST 5" src="https://github.com/user-attachments/assets/9e91701a-e60f-4886-97bc-b5227c3ad32d" />

Selanjutnya terdapat if pilih == 1: yang digunakan untuk mengecek apakah pengguna memilih menu 1 yaitu registrasi ID player baru ke dalam BST.

Di dalam kondisi tersebut program kembali menggunakan try: untuk menangani kemungkinan kesalahan input dari pengguna.

Kemudian terdapat player = int(input("Masukkan ID Player: ")) yang digunakan untuk meminta pengguna memasukkan ID player. Input yang diterima diubah menjadi tipe data integer menggunakan int() agar dapat disimpan sebagai data numerik di dalam BST.

Setelah pengguna memasukkan ID player, program menjalankan bst.insert(player) yang digunakan untuk memasukkan ID player tersebut ke dalam Binary Search Tree. Proses insert dilakukan sesuai aturan BST, yaitu nilai yang lebih kecil ditempatkan di kiri dan nilai yang lebih besar ditempatkan di kanan.

Kemudian terdapat print(f"ID Player {player} berhasil diregistrasi.") yang digunakan untuk menampilkan pesan bahwa ID player berhasil ditambahkan ke dalam sistem BST.

Jika pengguna memasukkan data selain angka maka program akan masuk ke bagian except ValueError: yang digunakan untuk menangkap kesalahan input.

Di dalamnya terdapat print("Input harus berupa angka!") yang digunakan untuk menampilkan pesan bahwa ID player harus berupa angka.

Selanjutnya terdapat elif pilih == 2: yang digunakan untuk mengecek apakah pengguna memilih menu 2 yaitu mencari ID player di dalam BST.

Di dalam kondisi tersebut program kembali menggunakan try: untuk menangani kemungkinan kesalahan input.

Kemudian terdapat player = int(input("Masukkan ID Player yang dicari: ")) yang digunakan untuk meminta pengguna memasukkan ID player yang ingin dicari. Input tersebut diubah menjadi integer agar dapat dibandingkan dengan data di BST.

Setelah itu program menjalankan if bst.search(player): yang digunakan untuk memanggil fungsi pencarian pada BST. Fungsi search akan menelusuri BST mulai dari root hingga data ditemukan atau tidak ditemukan.

Jika data ditemukan maka program menjalankan print(f"ID Player {player} ditemukan.") yang digunakan untuk menampilkan pesan bahwa ID player tersedia di dalam BST.

Namun jika data tidak ditemukan maka program menjalankan print(f"ID Player {player} tidak ditemukan.") yang digunakan untuk menampilkan pesan bahwa ID player tidak ada di dalam BST.

Jika pengguna memasukkan input selain angka maka program akan masuk ke bagian except ValueError:.

Di dalamnya terdapat print("Input harus berupa angka!") yang digunakan untuk menampilkan pesan kesalahan bahwa input pencarian harus berupa angka.

<img width="1034" height="1318" alt="code BST 6" src="https://github.com/user-attachments/assets/e5d62151-84a2-4ebf-a765-f8f0a1576bab" />

Selanjutnya terdapat elif pilih == 3: yang digunakan untuk mengecek apakah pengguna memilih menu 3 yaitu menampilkan seluruh ID player secara terurut menggunakan traversal inorder.

Di dalam kondisi tersebut program menjalankan print("ID Player Terurut: ", end="") yang digunakan untuk menampilkan teks pembuka sebelum data BST dicetak. Parameter end="" digunakan agar hasil traversal dicetak pada baris yang sama.

Kemudian program menjalankan bst.inorder(bst.root) yang digunakan untuk memanggil fungsi traversal inorder dimulai dari root BST. Traversal inorder memiliki urutan kiri → root → kanan sehingga seluruh ID player akan ditampilkan dari nilai terkecil ke terbesar.

Setelah traversal selesai terdapat print() yang digunakan untuk membuat baris baru agar tampilan output menjadi lebih rapi.

Selanjutnya terdapat elif pilih == 4: yang digunakan untuk mengecek apakah pengguna memilih menu 4 yaitu menampilkan traversal preorder BST.

Di dalam kondisi tersebut program menjalankan print("Preorder: ", end="") yang digunakan untuk menampilkan teks pembuka sebelum hasil traversal preorder dicetak.

Kemudian terdapat bst.preorder(bst.root) yang digunakan untuk memanggil fungsi traversal preorder dimulai dari root BST. Traversal preorder memiliki urutan root → kiri → kanan sehingga node induk akan ditampilkan terlebih dahulu sebelum cabang kiri dan kanan.

Setelah traversal selesai program menjalankan print() untuk membuat baris baru agar tampilan output lebih rapi.

Selanjutnya terdapat elif pilih == 5: yang digunakan untuk mengecek apakah pengguna memilih menu 5 yaitu menampilkan traversal postorder BST.

Di dalam kondisi tersebut program menjalankan print("Postorder: ", end="") yang digunakan untuk menampilkan teks pembuka sebelum hasil traversal postorder dicetak.

Kemudian program menjalankan bst.postorder(bst.root) yang digunakan untuk memanggil fungsi traversal postorder dimulai dari root BST. Traversal postorder memiliki urutan kiri → kanan → root sehingga node induk akan ditampilkan paling akhir setelah seluruh cabang selesai ditelusuri.

Setelah traversal selesai terdapat print() yang digunakan untuk membuat baris baru agar hasil output terlihat lebih rapi.

<img width="1018" height="1926" alt="code BST 7" src="https://github.com/user-attachments/assets/07f17f5b-49fc-4180-9ae6-22eed305426a" />

Selanjutnya terdapat elif pilih == 6: yang digunakan untuk mengecek apakah pengguna memilih menu 6 yaitu mencari ID player terkecil di dalam BST.

Di dalam kondisi tersebut program menjalankan bst.find_min(bst.root) yang digunakan untuk memanggil fungsi pencarian nilai minimum dimulai dari root BST. Fungsi ini bekerja dengan terus menelusuri cabang kiri BST sampai node paling kiri ditemukan karena pada BST nilai terkecil selalu berada di posisi paling kiri.

Hasil dari fungsi tersebut kemudian ditampilkan menggunakan print() sehingga pengguna dapat melihat ID player terkecil yang tersimpan di dalam BST.

Selanjutnya terdapat elif pilih == 7: yang digunakan untuk mengecek apakah pengguna memilih menu 7 yaitu mencari ID player terbesar di dalam BST.

Di dalam kondisi tersebut program menjalankan bst.find_max(bst.root) yang digunakan untuk memanggil fungsi pencarian nilai maksimum dimulai dari root BST. Fungsi ini bekerja dengan terus bergerak ke cabang kanan sampai node paling kanan ditemukan karena pada BST nilai terbesar selalu berada di posisi paling kanan.

Hasil nilai maksimum tersebut kemudian ditampilkan ke layar menggunakan print().

Selanjutnya terdapat elif pilih == 8: yang digunakan untuk mengecek apakah pengguna memilih menu 8 yaitu menghitung jumlah seluruh player yang ada di dalam BST.

Di dalam kondisi tersebut program menjalankan bst.count_nodes(bst.root) yang digunakan untuk menghitung total node BST secara rekursif. Fungsi akan menelusuri seluruh cabang kiri dan kanan kemudian menjumlahkan seluruh node yang ditemukan.

Hasil perhitungan tersebut kemudian ditampilkan menggunakan print() sehingga pengguna dapat mengetahui jumlah total ID player yang tersimpan di BST.

Berikutnya terdapat elif pilih == 9: yang digunakan untuk mengecek apakah pengguna memilih menu 9 yaitu menghitung total seluruh nilai ID player di dalam BST.

Di dalam kondisi tersebut program menjalankan bst.sum_nodes(bst.root) yang digunakan untuk menjumlahkan seluruh nilai node pada BST secara rekursif. Fungsi akan menambahkan nilai node saat ini dengan seluruh nilai pada cabang kiri dan cabang kanan.

Hasil penjumlahan tersebut kemudian ditampilkan menggunakan print() sehingga pengguna dapat mengetahui total seluruh nilai ID player yang ada di BST.

Selanjutnya terdapat elif pilih == 10: yang digunakan untuk mengecek apakah pengguna memilih menu 10 yaitu keluar dari program.

Di dalam kondisi tersebut program menjalankan print("Program selesai.") yang digunakan untuk menampilkan pesan bahwa program telah selesai dijalankan.

Karena nilai pilih sudah sama dengan 10 maka perulangan while pilih != 10 akan berhenti sehingga program berakhir.

Terakhir terdapat else: yang digunakan untuk menangani kondisi apabila pengguna memasukkan pilihan menu di luar angka 1 sampai 10.

Di dalam kondisi tersebut program menjalankan print("Pilihan tidak valid!") yang digunakan untuk menampilkan pesan bahwa menu yang dipilih tidak tersedia di dalam sistem.

Di bagian paling akhir program terdapat if __name__ == "__main__": yang digunakan untuk memastikan bahwa fungsi main() hanya dijalankan ketika file program dijalankan secara langsung, bukan ketika file diimport dari program lain.

Kemudian terdapat main() yang digunakan untuk memanggil fungsi utama program sehingga seluruh sistem BST dapat dijalankan.

OUTPUT:

<img width="838" height="973" alt="image" src="https://github.com/user-attachments/assets/0f5811be-6e05-46e4-b39b-f7cd73d3ac1a" />

Pada saat pengguna memasukkan data 122, 256, dan 983 ke dalam BST, maka struktur Binary Search Tree akan terbentuk sesuai aturan BST. Nilai 122 menjadi root karena dimasukkan pertama kali. Kemudian 256 ditempatkan di sebelah kanan 122 karena nilainya lebih besar. Setelah itu 983 ditempatkan di sebelah kanan 256 karena nilainya juga lebih besar dari node sebelumnya.

Ketika pengguna memilih menu 4 yaitu preorder traversal, program akan menampilkan data dengan urutan root → kiri → kanan. Karena struktur BST hanya memiliki cabang kanan, maka output yang muncul adalah 122 256 983. Hal ini terjadi karena program mencetak node induk terlebih dahulu sebelum menelusuri cabang lainnya.

Selanjutnya ketika pengguna memilih menu 5 yaitu postorder traversal, program akan menampilkan data dengan urutan kiri → kanan → root. Karena tree hanya memiliki cabang kanan, maka program akan bergerak ke node paling kanan terlebih dahulu lalu kembali ke node induk. Oleh sebab itu output yang dihasilkan adalah 983 256 122.

Kemudian ketika pengguna memilih menu 9 yaitu sum nodes, program akan menjumlahkan seluruh nilai node yang ada di BST. Nilai 122, 256, dan 983 akan dijumlahkan sehingga menghasilkan total 1361. Output ini menunjukkan total seluruh ID player yang tersimpan di dalam BST.

Setelah seluruh proses selesai dan pengguna memilih menu keluar, program akan menampilkan pesan “Program selesai.” yang menandakan bahwa sistem BST telah berhenti dijalankan dan seluruh proses input maupun operasi tree telah selesai dilakukan.


LINK VIDEO YOUTUBE: https://youtu.be/k1a8h4FOIbY?si=MBN2JfDxXY_J0y8x




