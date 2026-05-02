def tukar(data, x, y):
    data[x], data[y] = data[y], data[x]


def bubble_sort(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                tukar(data, j, j + 1)


def main():
    try:
        n = int(input("Jumlah data kecepatan internet: "))
    except ValueError:
        print("Input salah!")
        return

    kecepatan = []

    for i in range(n):
        while True:
            try:
                nilai = float(input(f"Kecepatan ke-{i+1} (Mbps): "))
                kecepatan.append(nilai)
                break
            except ValueError:
                print("Masukkan angka!")

    print("Sebelum:", kecepatan)

    bubble_sort(kecepatan)

    print("Setelah (terlambat → tercepat):", kecepatan)


if __name__ == "__main__":
    main()