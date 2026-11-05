jumlah = int(input("Jumlah mahasiswa (5-10): "))

if jumlah < 5 or jumlah > 10:
    print("Jumlah tidak valid")
else:
    daftar_nilai = []
    for i in range(jumlah):
        nilai = int(input(f"Nilai mahasiswa {i+1}: "))
        daftar_nilai.append(nilai)
    print("Daftar nilai mahasiswa:", daftar_nilai)
    print("Rata-rata nilai mahasiswa:", sum(daftar_nilai) / jumlah)