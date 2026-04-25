def menu():
    print("\n PENGELUARAN HARIAN")
    print("1. Tampilkan address list")
    print("2. Tampilkan address setiap data")
    print("3. Input pengeluaran harian")
    print("4. Tampilkan pengeluaran harian")
    print("5. Hitung total pengeluaran")
    print("6. Keluar")                                                                         


def main():
    pengeluaran = [0] * 5
    running = True

    while running:
        menu()

        try:
            pilihan = int(input("Masukkan pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if pilihan == 1:
            print("Address list:", id(pengeluaran))

        elif pilihan == 2:
            for i in range(len(pengeluaran)):
                print(f"Address pengeluaran[{i}] = {id(pengeluaran[i])}")

        elif pilihan == 3:
            print("Masukkan pengeluaran 5 hari:")
            for i in range(len(pengeluaran)):
                while True:
                    try:
                        pengeluaran[i] = int(input(f"Hari ke-{i+1}: Rp "))
                        break
                    except ValueError:
                        print("Harus berupa angka!")

        elif pilihan == 4:
            print("\nData pengeluaran:")
            for i in range(len(pengeluaran)):
                print(f"Hari {i+1}: Rp {pengeluaran[i]}")

        elif pilihan == 5:
            total = sum(pengeluaran)
            print("Total pengeluaran: Rp", total)

        elif pilihan == 6:
            running = False
            print("Program selesai")

        else:
            print("Pilihan tersebut tidak tersedia")


if __name__ == "__main__":
    main()