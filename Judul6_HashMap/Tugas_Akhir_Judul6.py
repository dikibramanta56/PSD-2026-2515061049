class Komputer:
    def __init__(self):
        self.nomor = None
        self.status = None

class RentalWarnet:
    def __init__(self, ukuran=10):
        self.ukuran = ukuran
        self.data = [None] * ukuran

    def hash(self, nomor):
        return nomor % self.ukuran

    def tambah(self, nomor, status):
        i = self.hash(nomor)

        while self.data[i] is not None:
            if self.data[i].nomor == nomor:
                self.data[i].status = status
                return
            i = (i + 1) % self.ukuran

        komputer = Komputer()
        komputer.nomor = nomor
        komputer.status = status
        self.data[i] = komputer

    def cari(self, nomor):
        i = self.hash(nomor)

        while self.data[i] is not None:
            if self.data[i].nomor == nomor:
                return self.data[i]
            i = (i + 1) % self.ukuran

        return None

    def tampil(self):
        print("\nDAFTAR KOMPUTER")

        for i in range(self.ukuran):
            if self.data[i]:
                print(
                    f"{i} → Komputer {self.data[i].nomor}"
                    f" ({self.data[i].status})"
                )
            else:
                print(f"{i} → Kosong")


def main():

    warnet = RentalWarnet()

    warnet.tambah(1, "Tersedia")
    warnet.tambah(11, "Digunakan")
    warnet.tambah(21, "Tersedia")

    warnet.tampil()

    hasil = warnet.cari(11)

    if hasil:
        print(
            f"\nKomputer {hasil.nomor}"
            f" status {hasil.status}"
        )

    warnet.tambah(11, "Tersedia")

    print("\nSetelah dikembalikan:")
    warnet.tampil()


main()