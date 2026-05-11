# Program Sequential Search Sentinel
# Nama Program: Pencarian Nilai Ping Server (ms)

def sequential_search_sentinel(data, n, target):
    # Menambahkan target sebagai sentinel
    data.append(target)

    i = 0

    # Proses pencarian
    while data[i] != target:
        i += 1
# Sentinel dihapus kembali
    data.pop()

    # Mengecek apakah data ditemukan
    if i < n:
        return True, i
    else:
        return False, -1


def main():
    # Data ping server dalam milisecond (ms)
    ping_server = [12, 25, 8, 45, 67, 30, 90, 15, 55, 40]

    n = len(ping_server)

    print("Data ping server (ms):")
    print(ping_server)

    # Input pengguna
    while True:
        try:
            target = int(input("\nMasukkan nilai ping yang ingin dicari: "))
            break
        except ValueError:
            print("Input harus berupa angka!") 

    # Memanggil fungsi sequential search sentinel
    found, index = sequential_search_sentinel(ping_server, n, target)

    # Menampilkan hasil pencarian
    if found:
        print(f"\nNilai ping {target} ms ditemukan pada indeks ke-{index}")
    else:
        print(f"\nNilai ping {target} ms tidak ditemukan")


if __name__ == "__main__":
    main()