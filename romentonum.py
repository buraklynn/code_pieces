# Roma rakamlarını sayıya çevirme
def RomantoInt():
    romans = ("I", "V", "X", "L", "C", "D", "M")
    ints = (1, 5, 10, 50, 100, 500, 1000)

    thenum = input("Enter Roman Number: ").upper()
    a = list()
    for i in thenum:
        if i not in romans:
            print("Please enter romen.")
            break
        else:
            i = ints[romans.index(i)]
            a.append(i)
    c = 0
    if len(a) == 1:
        print(a[0])
    else:
        for t in a:
            if a.index(t)+1 != len(a):
                if t < a[a.index(t)+1]:
                    t *= -1
            c += t
        if c <= 3999:
            print(c)
        else:
            print("Romen nums can not be bigger than 3999.")

while True:
    RomantoInt()