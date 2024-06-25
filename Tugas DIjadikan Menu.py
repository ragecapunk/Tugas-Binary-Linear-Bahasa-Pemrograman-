def pencarian_linear(harga, target_harga):
    hasil = []
    for i in range(len(harga)):
        if harga[i] == target_harga:
            hasil.append(i)
    return hasil

def binary_search(harga, target_harga):
    low = 0
    high = len(harga) - 1

    while low <= high:
        mid = (low + high) // 2
        if harga[mid] == target_harga:
            hasil = [i for i, x in enumerate(harga) if x == target_harga]
            return hasil
        elif harga[mid] < target_harga:
            low = mid + 1
        else:
            high = mid - 1

    return []

def main():
    while True:
        print("Menu:")
        print("1. Cari harga Buah (Linear Search)")
        print("2. Cari harga Mobil (Binary Search)")
        print("3. Keluar")

        choice = int(input("Pilih menu: "))

        if choice == 1:
            buah = ["Apel", "Mangga", "Jeruk", "Durian", "Strawberry"]
            harga = [5000, 3000, 2000, 4000, 3000]
            print("Jenis Buah: Apel, Mangga, Jeruk, Durian, Strawberry")
            print("Harga Buah: 5000, 3000, 2000, 4000, 3000")
            target_harga = float(input("Masukkan harga buah yang akan dicari: "))

            hasil = pencarian_linear(harga, target_harga)

            if len(hasil) > 0:
                print(f"Buah dengan harga {target_harga} ditemukan pada indeks:")
                for i in hasil:
                    print(f"- {buah[i]} (indeks {i})")
            else:
                print(f"Buah dengan harga {target_harga} tidak ditemukan dalam daftar")

            print("\n1. Kembali ke menu")
            print("2. Keluar")
            back_choice = int(input("Pilih: "))

            if back_choice == 1:
                continue
            elif back_choice == 2:
                print("Terima Kasiiiihhh!")
                break

        elif choice == 2:
            mobil = ["Toyota", "Honda", "Suzuki", "Mazda", "Angkot", "Nissan", "Ford", "Mitsubishi", "Hyundai", "Kia"]
            harga = [150000, 275000, 180000, 330000, 330000, 150000, 275000, 180000, 180000, 995000]
            print("Jenis Mobil: Toyota, Honda, Suzuki, Mazda, Angkot, Nissan, Ford, Mitsubishi, Hyundai, Kia" )
            print("Harga Mobil: 150000, 275000, 180000, 330000, 330000, 150000, 275000, 180000, 180000, 995000")
            target_harga = float(input("Masukkan harga mobil yang akan dicari: "))

            hasil = binary_search(harga, target_harga)

            if len(hasil) > 0:
                print(f"Mobil dengan harga {target_harga} ditemukan pada indeks:")
                for i in hasil:
                    print(f"- {mobil[i]} (indeks {i})")
            else:
                print(f"Mobil dengan harga {target_harga} tidak ditemukan dalam daftar")

            print("\n1. Kembali ke menu")
            print("2. Keluar")
            back_choice = int(input("Pilih: "))

            if back_choice == 1:
                continue
            elif back_choice == 2:
                print("Terima Kasiiiihhh!")
                break

        elif choice == 3:
            print("Terima Kasiiiihhh!")
            break

if __name__ == "__main__":
    main()