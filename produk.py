def input_nilai():
    nama = input("Masukkan nama mahasiswa: ")
    nilai = float(input("Masukkan nilai: "))

    return nama, nilai

print("Nama mahasiswa dan nilai yang dimasukkan:")
while True:
    nama, nilai = input_nilai()
    print(f"Nama: {nama}, Nilai: {nilai}")

    lagi = input("Apakah Anda ingin memasukkan data lagi? (y/n): ")
    if lagi.lower() != 'y':
        break

print("Terima kasih telah menggunakan program ini.")

print("test branch fitur-produk")