#import main
#from main import skala_hesaplama
#db()#
#main dosyasından import edilen fonksiyonlar ile hesaplama yapılması
#farklı hareketler için değerlerde hata oluyor
#dosya okumada dağınıklıklar var
#boş dosyayı okumuyor hata veriyor
#float olması sebebi ile int değerde hata
#yapılması gerekenler:
def ilk():
    soru = input("İlk defa değer giriyorsanız: \n ılk yazın \n Yoksa devam yazın:  ").lower()
    if soru == "ılk":
        mevcut = input("kaç kg ile çalışıyorsunuz:\n")
        with open("db.txt", "a") as dosya:
            dosya.write(mevcut)
def ilk1():
    soru = input("İlk defa değer giriyorsanız: \n ılk yazın \n Yoksa devam yazın:  ").lower()
    if soru == "ılk":
        mevcut = input("kaç kg ile çalışıyorsunuz:")
        with open("bench.txt", "a") as dosya:
            dosya.write(mevcut)
def ilk2():
    soru = input("İlk defa değer giriyorsanız: \n ılk yazın \n Yoksa devam yazın:  ").lower()
    if soru == "ılk":
        mevcut = input("kaç kg ile çalışıyorsunuz:")
        with open("ınc.txt", "a") as dosya:
            dosya.write(mevcut)
def ilk3():
    soru = input("İlk defa değer giriyorsanız: \n ılk yazın \n Yoksa devam yazın:  ").lower()
    if soru == "ılk":
        mevcut = input("kaç kg ile çalışıyorsunuz:")
        with open("cable.txt", "a") as dosya:
            dosya.write(mevcut)
def ilk4():
    soru = input("İlk defa değer giriyorsanız: \n ılk yazın \n Yoksa devam yazın:  ").lower()
    if soru == "ılk":
        mevcut = input("kaç kg ile çalışıyorsunuz:")
        with open("front.txt", "a") as dosya:
            dosya.write(mevcut)
def ilk5():
    soru = input("İlk defa değer giriyorsanız: \n ılk yazın \n Yoksa devam yazın:  ").lower()
    if soru == "ılk":
        mevcut = input("kaç kg ile çalışıyorsunuz:")
        with open("back.txt", "a") as dosya:
            dosya.write(mevcut)
def ilk6():
    soru = input("İlk defa değer giriyorsanız: \n ılk yazın \n Yoksa devam yazın:  ").lower()
    if soru == "ılk":
        mevcut = input("kaç kg ile çalışıyorsunuz:")
        with open("ext.txt", "a") as dosya:
            dosya.write(mevcut)
def ilk7():
    soru = input("İlk defa değer giriyorsanız: \n ılk yazın \n Yoksa devam yazın:  ").lower()
    if soru == "ılk":
        mevcut = input("kaç kg ile çalışıyorsunuz:")
        with open("LC.txt", "a") as dosya:
            dosya.write(mevcut)
def ilk8():
    soru = input("İlk defa değer giriyorsanız: \n ılk yazın \n Yoksa devam yazın:  ").lower()
    if soru == "ılk":
        mevcut = input("kaç kg ile çalışıyorsunuz:")
        with open("ovp.txt", "a") as dosya:
            dosya.write(mevcut)

def g_s():

    ad =input("Hareket adını giriniz:\n 0-Dumbell bench press: \n 1-Bench press \n 2-Inc bench press\n 3-Cable ")

    if ad == "0":


        ilk()
        kg = input("Kiloyu giriniz:")

        with open("db.txt", "r") as dosya:

            last_line = dosya.readlines()[-1]

        girdi = float(last_line)

        bkln = str(girdi + 2.5)

        if kg >= bkln:
            print("Tebrikler")

        else:
            print("hedefinizin gerisinde kaldınız")

        with open("db.txt", "a") as f:
            f.write( kg + "\n")

    if ad == "1":
        ilk1()
        kg = input("Kiloyu giriniz:")
        with open("bench.txt", "r") as dosya:

            last_line = dosya.readlines()[-1]

        girdi = float(last_line)

        bkln = str(girdi + 2.5)

        if kg >= bkln:
            print("Tebrikler")

        else:
            print("hedefinizin gerisinde kaldınız")

        with open("bench.txt", "a") as f:
            f.write(kg + "\n")

    if ad == "2":
        ilk2()
        kg = input("Kiloyu giriniz:")
        with open("ınc.txt", "r") as dosya:

            last_line = dosya.readlines()[-1]

        girdi = float(last_line)

        bkln = str(girdi + 2.5)

        if kg >= bkln:
            print("Tebrikler")

        else:
            print("hedefinizin gerisinde kaldınız")

        with open("ınc.txt", "a") as f:
            f.write(kg + "\n")
    if ad == "3":
        ilk3()
        kg = input("Kiloyu giriniz:")
        with open("cable.txt", "r") as dosya:

            last_line = dosya.readlines()[-1]

        girdi = float(last_line)

        bkln = str(girdi + 2.5)

        if kg >= bkln:
            print("Tebrikler")

        else:
            print("hedefinizin gerisinde kaldınız")

        with open("cable.txt", "a") as f:
            f.write(kg + "\n")
def b_o():

    ad =input("Hareket adını giriniz:\n 0-Front Squat: \n 1-Back Squat \n 2-Leg Extension\n 3-Leg Curl \n 4- Over Head Press ")

    if ad == "0":
        ilk4()
        kg = input("Kiloyu giriniz:")
        with open("front.txt", "r") as dosya:

            last_line = dosya.readlines()[-1]

        girdi = float(last_line)

        bkln = str(girdi + 2.5)

        if kg >= bkln:
            print("Tebrikler")

        else:
            print("hedefinizin gerisinde kaldınız")

        with open("front.txt", "a") as f:
            f.write( kg + "\n")
    if ad == "1":
        ilk5()
        kg = input("Kiloyu giriniz:")
        with open("back.txt", "r") as dosya:

            last_line = dosya.readlines()[-1]

        girdi = float(last_line)

        bkln = str(girdi + 2.5)

        if kg >= bkln:
            print("Tebrikler")

        else:
            print("hedefinizin gerisinde kaldınız")

        with open("back.txt", "a") as f:
            f.write(kg + "\n")
    if ad == "2":
        ilk6()
        kg = input("Kiloyu giriniz:")
        with open("ext.txt", "r") as dosya:

            last_line = dosya.readlines()[-1]

        girdi = float(last_line)

        bkln = str(girdi + 2.5)

        if kg >= bkln:
            print("Tebrikler")

        else:
            print("hedefinizin gerisinde kaldınız")

        with open("ext.txt", "a") as f:
            f.write(kg + "\n")
    if ad == "3":
        ilk7()
        kg = input("Kiloyu giriniz:")
        with open("LC.txt", "r") as dosya:

            last_line = dosya.readlines()[-1]

        girdi = float(last_line)

        bkln = str(girdi + 2.5)

        if kg >= bkln:
            print("Tebrikler")


        else:
            print("hedefinizin gerisinde kaldınız")

        with open("LC.txt", "a") as f:
            f.write(kg + "\n")

    if ad == "4":
        ilk8()
        kg = input("Kiloyu giriniz:")
        with open("ovp.txt", "r") as dosya:

            last_line = dosya.readlines()[-1]

        girdi = float(last_line)

        bkln = str(girdi + 2.5)

        if kg >= bkln:
            print("Tebrikler")

        else:
            print("hedefinizin gerisinde kaldınız")

        with open("ovp.txt", "a") as f:
            f.write( kg + "\n")


while True:
 secim=input(str("Program gününü seçiniz: \n1-Gogus-Sırt: \n2-Bacak-Omuz: \nÇıkmak için Q:")).lower()
 if secim =="q":
     break
 if secim == "1":
     g_s()
     break
 if secim == "2":
     b_o()
     break








