def pencarian_linear(harga, target_harga):
    hasil = []
    for i in range(len(harga)):
        if harga[i] == target_harga:
            hasil.append(i)
    return hasil

def main():
    buah = ["Apel", "Mangga", "Jeruk", "Durian", "Strawberry"]
    harga = [5000, 3000, 2000, 4000, 3000]
    target_harga = float(input("Masukkan harga buah yang akan dicari: "))

    hasil = pencarian_linear(harga, target_harga)

    if len(hasil) > 0:
        print(f"Buah dengan harga {target_harga} ditemukan pada indeks:")
        for i in hasil:
            print(f"- {buah[i]} (indeks {i})")
    else:
        print(f"Buah dengan harga {target_harga} tidak ditemukan dalam daftar")

if __name__ == "__main__":
    main()
