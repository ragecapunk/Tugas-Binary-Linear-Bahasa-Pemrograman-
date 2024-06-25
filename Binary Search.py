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
    mobil = ["Toyota", "Honda", "Suzuki", "Mazda", "Angkot", "Nissan", "Ford", "Mitsubishi", "Hyundai", "Kia"]
    harga = [150000, 275000, 180000, 330000, 330000, 150000, 275000, 180000, 180000, 995000]

    target_harga = float(input("Masukkan harga mobil yang akan dicari: "))

    hasil = binary_search(harga, target_harga)

    if len(hasil) > 0:
        print(f"Mobil dengan harga {target_harga} ditemukan pada indeks:")
        for i in hasil:
            print(f"- {mobil[i]} (indeks {i})")
    else:
        print(f"Mobil dengan harga {target_harga} tidak ditemukan dalam daftar")

if __name__ == "__main__":
    main()
