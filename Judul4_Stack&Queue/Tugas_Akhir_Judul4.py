class PinStack:
    def __init__(self, max_size=100):
        self.MAX = max_size
        self.stack = [None] * self.MAX
        self.top = -1


    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.MAX - 1

    def push(self, pin):
        if self.is_full():
            print("Penyimpanan PIN penuh!")
            return

        self.top += 1
        self.stack[self.top] = pin
        print(f"PIN {pin} berhasil disimpan")

    def pop(self):
        if self.is_empty():
            print("Tidak ada PIN yang tersimpan!")
            return

        print(f"PIN {self.stack[self.top]} berhasil dihapus")
        self.top -= 1

    def peek(self):
        if self.is_empty():
            print("Tidak ada PIN yang tersimpan!")
            return

        print(f"PIN terakhir: {self.stack[self.top]}")

    def display(self):
        if self.is_empty():
            print("Penyimpanan PIN kosong!")
            return

        print("\nDaftar PIN Tersimpan (Terbaru -> Lama)")
        print("--------------------------------------")

        for i in range(self.top, -1, -1):
            print(self.stack[i])

        print("--------------------------------------")


def main():
    pin_system = PinStack()
    pilihan = 0

    while pilihan != 5:
        print("\n=== Sistem Penyimpanan PIN sementara ===")
        print("1. Simpan PIN")
        print("2. Hapus PIN Terakhir")
        print("3. Lihat PIN Terakhir")
        print("4. Tampilkan Semua PIN")
        print("5. Keluar")

        try:
            pilihan = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus berupa angka!")
            continue

        if pilihan == 1:
            try:
                pin = int(input("Masukkan PIN: "))

                if 1000 <= pin <= 999999:
                    pin_system.push(pin)
                else:
                    print("PIN harus 4 sampai 6 digit")

            except ValueError:
                print("PIN harus berupa angka!")

        elif pilihan == 2:
            pin_system.pop()

        elif pilihan == 3:
            pin_system.peek()

        elif pilihan == 4:
            pin_system.display()

        elif pilihan == 5:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()