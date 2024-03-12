def ganjil(Bil1, Bil2):
    if Bil2 > Bil1:
        while Bil2 != Bil1:
            if Bil2 % 2 == 1:
                print(Bil2, end=", ")
            Bil2 = Bil2 - 1
    else:
        while Bil2 != Bil1:
            Bil2 = Bil2 + 1
            if Bil2 % 2 == 1:
                print(Bil2, end=", ")

BatasAtas = int(input("Batas atas : "))
BatasBawah = int(input("Batas bawah : "))
ganjil(BatasBawah,BatasAtas)