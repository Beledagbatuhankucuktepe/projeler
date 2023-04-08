import random
user_wins = 0
comp_wins = 0

options= ["taş","kağıt","makas"]
starting_screen= input("çıkmak için q yazın devam için d:").lower()

if starting_screen == "q":
    print("Görüşürüz")
    quit()

while True:
    user_input = input("Type taş,kağıt,makas, çıkmak için q : ").lower()
    if user_input == "q":
        break
    if user_input not in options :
        continue

    random_numb = random.randint(0,2)
    comp_pick = options[random_numb]
    print("bilgisayar", comp_pick,"seçti.")

    if user_input == "taş" and comp_pick == "makas":
        print("kazandın")
        user_wins+=1
    elif user_input == "makas" and comp_pick == "kağıt":
        print("kazandın")
        user_wins+=1
    elif user_input == "kağıt" and comp_pick == "taş":
        print("kazandın")
        user_wins+=1
    else :
        print("kaybettin")
        comp_wins+=1

if user_wins > comp_wins:
    print("kullanıcı kazandı", user_wins,"defa","bilgisayar kazandı", comp_wins,"defa")
elif comp_wins > user_wins :
    print("bilgisayar kazandı", comp_wins,"defa","sen kazandın", user_wins,"defa")
elif comp_wins == user_wins :
    print("berabere" ,"bilgisayar kazandı", comp_wins,"defa","sen kazandın", user_wins,"defa")
