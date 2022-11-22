from random import randint, choice


nicks = ['']

input("""
    Takma ad oluşturmak için [ENTER]'a basınız
    İstemediğiniz alanları boş bırakabilirsiniz.
    Kelimeleri boşluklar ile ayırınız.
    """)

while True:

    color = input("Bir renk girin: ")
    obj = input("Bir isim, nesne veya özel bir şey girin:  ")
    place = input("Bir mekan girin: ")

    if color == "" and obj == "" and place == "":
        print("Lütfen en az bir renk, isim veya mekan girin.")
        continue
    newcolor = color.split(" ")
    newwobj = obj.split(" ")
    newplace = place.split(" ")

    cholist = [newwobj, newplace]

    lets = ['','x','-','_']

    nickname = choice(newcolor)+choice(lets)+choice(choice(cholist))

    if nickname in nicks:
        print(f"{nickname} adı kullanılıyor.")
        nickname = nickname+randint(0,9)
    else:
        nicks.append(nickname)
        print(f"Yeni takma adın: {nickname}")
    
    repeat = input("Tekrar denemek için [ENTER], çıkmak için 'q' basınız: ")
    if repeat == "q":
        break

