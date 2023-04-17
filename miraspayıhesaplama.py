print("----Miras Hesaplama----\n*****")#curser kullanarak renk ver
girdi=input("Payı hesaplanacak durumu seçiniz:\n"
            "-1-Eş tek başına miraşçı ise:\n"
            "-2-Eş altsoy ile birlikte mirasçı ise:\n"
            "-3-Sadece altsoy miraşçıysa:\n"
            "-4-Eş anne-baba ile birlikte mirasçıysa:\n"
            "-5-Eş sadece anne ya da baba ile birlikte mirasçı ise:\n"
            "-6-Eş murisin anne-baba ve zümresi ile birlikte mirasçı ise:\n"
            "-7-Eş anne-baba'dan biri ile birlikte murisin anne-baba zümresinden( anne ya da baba ölmüş,amca vb.) kişilerle ortak şekilde mirasçı:\n"
            "-8-Eş murisin büyükanne-büyükbaba ve zümresi ile birlikte mirasçı:\n"
            "-9-Sadece murisin annesi ya da babası mirasçı:\n"
            "-10-Murisin anne-babası birlikte mirasçı:\n"
            "-11-Murisin büyükanne-büyükbaba ve zümresi mirasçı:\n"
            "-12-Çıkmak için q:").lower()

if girdi=="1":
    print("*****")
    miras=int(input("Miras tutarını giriniz:"))
    yasalmiras=str(miras)
    saklipay=str(miras*(3/4))
    print("Eşin Yasal miras:"+yasalmiras+"\n"+"Eşin Saklı pay:"+saklipay+"'dır")
    print("Görüşürüz\n*****")
    quit()
if girdi == "2":
    print("*****")
    miras = int(input("Miras tutarını giriniz:"))
    altsoy=int(input("Altsoy sayısını giriniz:"))
    esyslmrs = str(miras*(1/4))
    essklpy=esyslmrs
    altsoyyasalmrs=str(((3/4)*1/altsoy)*miras)
    altsoysaklipay=str(miras*3/8*(1/altsoy))
    print("Eşin yasal mirası:" + esyslmrs + "\n" + "Eşin saklı payı:" + essklpy + "'dır"+"\n"+"Altsoyun yasal mirası:"+altsoyyasalmrs+
          "\n"+"Altsoyun saklıpayı:"+altsoysaklipay+"'dır")
    print("Görüşürüz\n*****")
    quit()
if girdi == "3":
    print("*****")
    miras = int(input("Miras tutarını giriniz:"))
    altsoy = int(input("Altsoy sayısını giriniz:"))
    altsoyyasalmrs = str(miras*1/altsoy)
    altsoysaklipay = str(miras * 1/2 * (1 / altsoy))
    print(
        "Altsoyun yasal mirası:" + altsoyyasalmrs + "\n" + "Altsoyun saklıpayı:" + altsoysaklipay + "'dır")
    print("Görüşürüz\n*****")
    quit()
if girdi== "4":
    print("*****")
    miras = int(input("Miras tutarını giriniz:"))
    esyslmrs = str(miras * (1 / 2))
    essklpy = esyslmrs
    ustsoyyasalmrs = str(((1 / 4)) * miras)
    ustsoysaklipay = str(miras * 1 / 4 * (1 / 4))
    print(
        "Eşin yasal mirası:" + esyslmrs + "\n" + "Eşin saklı payı:" + essklpy + "'dır" + "\n" + "Annenin yasal mirası:"
        + ustsoyyasalmrs + "\n" + "Annenin saklıpayı:" + ustsoysaklipay + "'dır"+"\n"+"Babanın yasal mirası:"
        + ustsoyyasalmrs + "\n" + "Babanın saklıpayı:" + ustsoysaklipay + "'dır")
    print("Görüşürüz\n*****")
    quit()
if girdi == "5":
    print("*****")
    miras = int(input("Miras tutarını giriniz:"))
    esyslmrs = str(miras * (1 / 2))
    essklpy = esyslmrs
    ustsoyyasalmrs = str(((1 / 2)) * miras)
    ustsoysaklipay = str(miras * 1 / 4 * (1 / 2))
    print(
        "Eşin yasal mirası:" + esyslmrs + "\n" + "Eşin saklı payı:" + essklpy + "'dır" + "\n" + "Anne ya da babanın yasal mirası:"
        + ustsoyyasalmrs + "\n" + "Anne ya da babanın saklıpayı:" + ustsoysaklipay + "'dır" + "\n")
    print("Görüşürüz\n*****")
    quit()
if girdi == "6":
    print("*****")
    miras = int(input("Miras tutarını giriniz:"))
    zumre = int(input("Zümredeki kişi sayısını giriniz:"))
    esyslmrs = str(miras * (1 / 2))
    essklpy = esyslmrs
    ustsoyyasalmrs = str(((1 / 2)*1/zumre) * miras)
    ustsoysaklipay = str(0)
    print(
        "Eşin yasal mirası:" + esyslmrs + "\n" + "Eşin saklı payı:" + essklpy + "'dır" + "\n" + "Murisin Anne-Baba ve Zümresinin Kişi Başına Düşen Yasal Mirası:"
        + ustsoyyasalmrs + "\n" + "Murisin Anne-Baba ve Zümresinin Kişi Başına Düşen Saklıpayı:" + ustsoysaklipay + "'dır" + "\n")
    print("Görüşürüz\n*****")
    quit()
if girdi == "7":
    print("*****")
    miras = int(input("Miras tutarını giriniz:"))
    zumre = int(input("Zümredeki kişi sayısını giriniz:"))
    if zumre>2:
        print("2'den fazla olamaz!!!")
        quit()
    esyslmrs = str(miras * (1 / 2))
    essklpy = esyslmrs
    ustsoyyasalmrs = str(((1 / 4)) * miras)#anne ya da baba
    ustsoysaklipay=str(((1 /16) * miras))
    zumreyasalmiras=str(((1 /4) * miras))
    zumresaklipay = str(0)
    print(
        "Eşin yasal mirası:" + esyslmrs + "\n" + "Eşin saklı payı:" + essklpy + "'dır" + "\n"+ "Anne-baba yasal mirası:" + ustsoyyasalmrs + "\n" + "Anne-babanın saklı payı:" + ustsoysaklipay + "'dır" + "\n"+ "Murisin Anne-Baba ve Zümresinin Kişi Başına Düşen Yasal Mirası:"
        + zumreyasalmiras + "\n" + "Murisin Anne-Baba ve Zümresinin Kişi Başına Düşen Saklıpayı:" + zumresaklipay + "'dır" + "\n")
    print("Görüşürüz\n*****")
    quit()
if girdi == "8":
    print("*****")
    miras = int(input("Miras tutarını giriniz:"))
    zumre = int(input("Zümredeki kişi sayısını giriniz:"))
    esyslmrs = str(miras * (3 / 4))
    essklpy = str(miras*(9/16))
    ustsoyyasalmrs = str(((1 / 4)*1/zumre) * miras)
    ustsoysaklipay = str(0)
    print(
        "Eşin yasal mirası:" + esyslmrs + "\n" + "Eşin saklı payı:" + essklpy + "'dır" + "\n" + "Murisin Büyükanne-Büyükbaba ve Zümresinin Kişi Başına Düşen Yasal Mirası:"
        + ustsoyyasalmrs + "\n" + "Murisin Büyükanne-Büyükbaba ve Zümresinin Kişi Başına Düşen Saklı Payı :" + ustsoysaklipay + "'dır" + "\n")
    print("Görüşürüz\n*****")
    quit()
if girdi=="9":
    print("*****")
    miras=int(input("Miras tutarını giriniz:"))
    yasalmiras=str(miras)
    saklipay=str(miras*(1/4))
    print("Anne ya da Babanı Yasal mirası:"+yasalmiras+"\n"+"Anne ya da Babanın Saklı pay:"+saklipay+"'dır")
    print("Görüşürüz\n*****")
    quit()
if girdi=="10":
    print("*****")
    miras = int(input("Miras tutarını giriniz:"))
    altsoyyasalmrs = str(miras * 1 / 2)
    altsoysaklipay = str(miras *( 1 /8))
    print(
        "Anneni yasal mirası:" + altsoyyasalmrs + "\n" + "Annenin saklıpayı:" + altsoysaklipay +"\n"+ "'dır"+
"Babanın yasal mirası:" + altsoyyasalmrs + "\n" + "Babanın saklıpayı:" + altsoysaklipay + "'dır")
    print("Görüşürüz\n*****")
    quit()
if girdi == "11":
    print("*****")
    miras = int(input("Miras tutarını giriniz:"))
    altsoy = int(input("Zümre sayısını giriniz:"))
    altsoyyasalmrs = str(miras*1/altsoy)
    altsoysaklipay = str(0)
    print(
        "Murisin Büyükanne-Büyükbaba ve Zümresinin Kişi Başına Düşen Yasal Mirası :" + altsoyyasalmrs + "\n" + "Murisin Büyükanne-Büyükbaba ve Zümresinin Kişi Başına Düşen Saklı Payı:" + altsoysaklipay + "'dır")
    print("Görüşürüz\n*****")
    quit()
if girdi == "q":
    print("Görüşürüz \n*****")

