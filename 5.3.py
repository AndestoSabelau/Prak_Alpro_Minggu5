print("Program penghitung IPS Mahasiswa\n=================================")
iJumlahMatkul = int(input("Berapa jumlah mata kuliah :? "))

skor = 0

for i in range (0,iJumlahMatkul):
    Nilai = input("Nilai MK %d: "%(i+1))
    if Nilai == "A":
        nilai = 4
    elif Nilai == "B":
        nilai = 3
    elif Nilai == "C":
        nilai = 2
    elif Nilai == "D":
        nilai = 1
    skor += nilai

ipk = skor / iJumlahMatkul

print("Nilai IPS Anda adalah: %0.2f" %ipk)