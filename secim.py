def cb():
    aday=input("Aday ismini giriniz:").title()
    ister1,ister2=input("2018 ve 2014 seçim sonuçlarını giriniz:").split()
    g1=int(ister1)
    g2=int(ister2)

    ister3=input("Seçimin bölgesini belirtin(Genel ya da İl ismi):").title()
    degisim=int(g1-g2)

    if degisim < 0:
       dzl= degisim*(-1)
       sonuc1=g1/dzl/g1*100
       sonuc=str(sonuc1)
       print("Oyu azalmış")
       tahmin=str(g1-sonuc1)
       print("2023 seçiminde oyunun"+" "+tahmin+" "+"olması bekleniyor")

       with open("cb.txt", "a") as file:
           file.write(
               aday + "'in" + " " + ister3 + " " + "bolgesinde oyu" + " " + sonuc + " " + "kadar azalmistir.""\n")
           quit()

    if degisim == 0:
        g1a=str(g1)
        print("oy değişimi olmamış"+" " +g1a+" "+"oyu var")
        with open("cb.txt", "a") as file:
            file.write(
                aday + "'in" + " " + ister3 + " " + "bolgesinde oyu degismemistir \n")
            quit()

    if degisim >0:
        sonuc1 = g1 / degisim / g1 * 100
        sonuc = str(sonuc1)
        print("oyu artmış")
        tahmin = str(g1 + sonuc1)
        print("2023 seçiminde oyunun" + " " + tahmin + " " + "olması bekleniyor")
        with open("cb.txt", "a") as file:
            file.write(
                aday + "'in" + " " + ister3 + " " + "bolgesinde oyu" + " " + sonuc + " " + "kadar artmistir.""\n")
            quit()

def dhont():
    bolge = input("Seçim bölgesini giriniz:").title()
    prtsys= int(input("Seçim bölgesinde kaç parti seçime girdi:"))
    if prtsys > 0:
        mvsayi = int(input("Milletvekili sayısını giriniz:"))
        parties = []
        votes = []
        for i in range(prtsys):
            party, vote = input(f"Parti {i+1} adını ve oy sayısını giriniz: ").split()
            parties.append(party)
            votes.append(int(vote))

        seats = [0]*prtsys
        for i in range(mvsayi):
            quotients = [votes[j]/(seats[j]+1) for j in range(prtsys)]
            idx = quotients.index(max(quotients))
            seats[idx] += 1

        result = f"{bolge} seçim bölgesinde "
        for i in range(prtsys):
            result += f"{parties[i]} parti {seats[i]} milletvekili, "
        result = result.rstrip(", ")
        print(result)

        with open("sayı.txt", "a") as dosya:
            dosya.write(result + "\n")

        quit()

def itti(*args):
    itf = input("İttifakın adını giriniz:").__add__(" " + "ittifakının")
    args=input("İttifaktaki partilerin oy oranını giriniz:").split()
    if len(args) == 2 :
     oy=str(int(args[0])+int(args[1]))
     print(itf + " " + "oy oranı %" + " " + oy + " " + "kadardır.")
    if len(args)==3:
        oy = str(int(args[0]) + int(args[1])+ int(args[2]))
        print(itf + " " + "oy oranı %" + " " + oy + " " + "kadardır.")
    if len(args)==4:
        oy = str(int(args[0]) + int(args[1])+ int(args[2])+ int(args[3]))
        print(itf + " " + "oy oranı %" + " " + oy + " " + "kadardır.")
    if len(args)==5:
        oy = str(int(args[0]) + int(args[1])+ int(args[2])+ int(args[4])+ int(args[3]))
        print(itf + " " + "oy oranı %" + " " + oy + " " + "kadardır.")
    if len(args)==6:
        oy = str(int(args[0]) + int(args[1])+ int(args[2])+ int(args[4])+ int(args[3])+ int(args[5]))
        print(itf + " " + "oy oranı %" + " " + oy + " " + "kadardır.")
    if len(args)>6:
        print("maks 6 parti girilebilir")

def mvs(*args):
    args = input("İttifaktaki partilerin oy oranını giriniz:").split()
    if len(args) == 2:
        oy = int(int(args[0]) + int(args[1]))
        return oy


    if len(args) == 3:
        oy = int(int(args[0]) + int(args[1]) + int(args[2]))
        return oy


    if len(args) == 4:
        oy = int(int(args[0]) + int(args[1]) + int(args[2]) + int(args[3]))
        return oy

    if len(args) == 5:
        oy = int(int(args[0]) + int(args[1]) + int(args[2]) + int(args[4]) + int(args[3]))
        return oy

    if len(args) == 6:
        oy = int(int(args[0]) + int(args[1]) + int(args[2]) + int(args[4]) + int(args[3]) + int(args[5]))
        return oy

def mvs1(*args):
    args = input("İttifaktaki partilerin oy oranını giriniz:").split()
    if len(args) == 2:
        oy = int(int(args[0]) + int(args[1]))
        return oy

    if len(args) == 3:
        oy = int(int(args[0]) + int(args[1]) + int(args[2]))
        return oy

    if len(args) == 4:
        oy = int(int(args[0]) + int(args[1]) + int(args[2]) + int(args[3]))
        return oy

    if len(args) == 5:
        oy = int(int(args[0]) + int(args[1]) + int(args[2]) + int(args[4]) + int(args[3]))
        return oy

    if len(args) == 6:
        oy = int(int(args[0]) + int(args[1]) + int(args[2]) + int(args[4]) + int(args[3]) + int(args[5]))
        return oy

def mv():
    tercih=input("Yapmak istediğiniz işlemi seçiniz:\n -1-2015 seçimleri farkı ile  2018 seçim farkını hesaplama\n -2-2015 kasım ile 2018 farkını hesaplama\n-3-2015 Haziran ile 2018 seçim farklarını hesaplama\n-4-İttifakların oy oranlarını hesaplama\n-5-İttifakların oy oranlarını birbirnden çıkarma\n-6-Seçim bölgesine göre milletvekili sayısı hesaplama\n -7- Çıkış için q:").lower()
    if tercih == "1": #2015 hazrian-2018 seçimlerindeki oy değişimleri ile 2015 kasım-haziran oy değişimin kıyaslama
        sonuc1,sonuc2,sonuc3=input("2015 Haziran,2015 Kasım ve 2018 seçim sonuçlarını giriniz:").split()
        s1=int(sonuc1)
        s2=int(sonuc2)
        s3=int(sonuc3)
        ister = input("Seçimin bölgesini belirtin(Genel ya da İl ismi):").title()
        degisim = int(s2 - s1)

        if degisim<0:
            f=degisim*(-1)
            degisim=f




        if s3-s1<degisim:
            print("oyunuz daha az artmış\n")
        if s3-s1== degisim:
            print("oyunuz kaybettiğiniz kadar artmış\n")
        if s3-s1 > degisim:
            print("oyunuz daha çok artmış\n")

    if tercih == "2":
        sonuc1, sonuc2 = input("2015 Kasım ve 2018 seçim sonuçlarını giriniz:").split()
        s1 = int(sonuc1)
        s2 = int(sonuc2)

        ister = input("Seçimin bölgesini belirtin(Genel ya da İl ismi):").title()
        degisim = int(s2 - s1)

        if degisim < 0:
            f = degisim * (-1)
            degisim = f

        if s2 - s1 < degisim:
            print("oyunuz daha az artmış\n")
        if s2 - s1 == degisim:
            print("oyunuz kaybettiğiniz kadar artmış\n")
        if s2 - s1 > degisim:
            print("oyunuz daha çok artmış\n")

    if tercih == "3":
        sonuc1, sonuc2 = input("2015 haziran ve 2018 seçim sonuçlarını giriniz:").split()
        s1 = int(sonuc1)
        s2 = int(sonuc2)

        ister = input("Seçimin bölgesini belirtin(Genel ya da İl ismi):").title()
        degisim = int(s2 - s1)

        if degisim < 0:
            f = degisim * (-1)
            degisim = f

        if s2 - s1 < degisim:
            print("oyunuz daha az artmış\n")
        if s2 - s1 == degisim:
            print("oyunuz kaybettiğiniz kadar artmış\n")
        if s2 - s1 > degisim:
            print("oyunuz daha çok artmış\n")
    if tercih == "4":
        itti()
        print("\n")




    if tercih == "5":
        itf1 = input(" Birinci ittifakın adını giriniz:").__add__(" " + "ittifakı")
        itf2 = input("İkinci ittifakın adını giriniz:").__add__(" " + "ittifakı'nın")
        oy=str((mvs()-mvs1()))
        print(itf1+" "+"ile"+" "+itf2+" "+"oy farkı"+" "+"%"+oy+" "+"kadardır\n")

    if tercih == "6":
        dhont()
        quit()






    if tercih== "q":
        print("görüşürüz")
        quit()

girdi=input("Girmek istediğiniz seçim tipi hangisi: \n -1-Cumhurbaşkanlığı: \n -2-Milletvekilliği: \n -3- Milletvekili sayısı hesaplamak için: \n -4-Çıkmak için q:").lower()

while girdi == "1":
    cb()
while girdi == "2":
    mv()
while girdi == "3":
    dhont()
while girdi == "q":
    break