print("""
**************************
Tokalaşma Sayacı Programı

1. Tokalaşma sayısını bulun
2. Tokalaşan kişi sayısını bulun
3. Çıkış
**************************
""")

while True:
    işlem = input("İşlem seçiniz:")

    if (işlem == "1"):

        kişi_sayısı = int(input("Tokalaşan kişi sayısı:"))

        kişi_işlem = int(kişi_sayısı * (kişi_sayısı - 1) / 2)

        print("{} kişi arasında {} tokalaşma olmuştur." .format(kişi_sayısı, kişi_işlem))

    elif (işlem == "2"):

        tokalaşma = (input("Tokalaşma sayısı:"))

        t2 = int(tokalaşma) * 2

        for i in range(1, t2):

            if (t2 == i * (i - 1)):
                a = i
                print("{} tokalaşma {} kişi arasında olmuştur." .format(tokalaşma, a))
                break

        if (a != i):
            print("Geçersiz sayı. Bir daha deneyin.")
    elif ( işlem == "3"):
        print("Bye bye...")
        break

    else:
        print("Geçersiz seçenek")
