def perkalian (Bil1,Bil2):
    result = 0
    print(str(Bil1)+"x"+str(Bil2)+":", end="")
    for i in range (Bil2):
        if i == Bil2-1:
            print(str(Bil1)+" = ",end= "")
        else:
            print(str(Bil1)+" + ",end= "")
        result = result + Bil1
    return result
iBil1 = int(input("Bilangan pertama: "))
iBil2 = int(input("Bilangan kedua: "))
print(perkalian(iBil1,iBil2))