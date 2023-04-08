def hesap(x,y):
    return x+(x/100*y)

def vadeli(x,y,z):
    return x+((x/100*y/12)*z)

def bilesik():
    para = int(input("Ana parayı giriniz:"))
    faiz = int(input("Faiz oranını giriniz:"))
    Vade = int(input("Vade süresini giriniz(ay cinsinden):"))
    i = 0
    while i < Vade:
        Tanim = hesap(para, faiz)
        print(Tanim)
        i += 1
        para = int(Tanim)

def bilesik1():
    para = int(input("Ana parayı giriniz:"))
    faiz = int(input("Faiz oranını giriniz:"))
    Vade = int(input("Vade süresini giriniz(ay cinsinden):"))
    i = 0
    while i < Vade:
        Tanim = hesap(para, faiz)
        i += 1
        para = int(Tanim)
    return para

def vadelihes():

    para = int(input("Ana parayı giriniz:"))
    faiz = int(input("Faiz oranını giriniz:"))
    Vade = int(input("Vade süresini giriniz(ay cinsinden):"))
    tanim1 = str(vadeli(para, faiz, Vade))
    print("Vade sonu paranız" + " " + tanim1 + " " + "kadardır.")
    quit()

def vadelihes1():
    print("Vadeli hesap ")
    para = int(input("Ana parayı giriniz:"))
    faiz = int(input("Faiz oranını giriniz:"))
    Vade = int(input("Vade süresini giriniz(ay cinsinden):"))
    tanim1 = vadeli(para, faiz, Vade)
    return tanim1

def tek():
    para = int(input("Ana parayı giriniz:"))
    faiz = int(input("Faiz oranını giriniz:"))
    Vade = int(input("Vade süresini giriniz(ay cinsinden):"))
    tanim1 = vadeli(para, faiz, Vade)
    i = 0
    while i < Vade:
        Tanim = hesap(para, faiz)
        i += 1
        para = int(Tanim)
    tanim2=para
    print(tanim2-tanim1)




girdi=input("Yapmak istediğiniz işlemi seçiniz:\n -1-Bileşke faiz:\n-2-Vadeli faiz:\n-3-Bileşke-Vadeli farkı:\n-4-Aynı miktar para için faiz farkı hesaplamak :\n-5-Çıkmak için q:").lower()
while True:
 while girdi=="1":
     bilesik()
     quit()
 while girdi =="2":
     vadelihes()
     quit()

 while girdi=="3":
     #tek fonksiyon halinde tek girdi ile aradaki farkı hesaplayacak fonsiyon yz,ayrı olsun -4- olarak girdinin içine ata
     print(str(int(bilesik1())-int(vadelihes1())))
     quit()
 while girdi == "4":
     tek()
     quit()
 while girdi =="q":
     quit()
