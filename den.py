

# print("Sorting Methods")


def find_min(liste):
    for i in range(len(liste)-1):
        mint = liste[i]
        for n in range(len(liste)):
            if mint < liste[n]:
                continue
            else:
                mint = liste[n]
                continue
    return mint


def minnum(listex):
    minx = listex[0]
    for i in range(len(listex)-1):
        if listex[i+1] < min:
            minx = listex[i+1]
    return minx


def bubble_sort(liste):
    liste_len = len(liste)
    for i in range(liste_len):
        for k in range(liste_len-(i+1)):
            if liste[k] > liste[k+1]:
                liste[k], liste[k+1] = liste[k+1], liste[k]
    return liste


def sortingx(liste):
    for k in range(len(liste)):
        for i in range(len(liste)-1):
            if liste[i] > liste[i+1]:
                liste[i], liste[i+1] = liste[i+1], liste[i]
    return liste


def insertion_sort(liste):
    nlist = list()
    for i in range(len(liste)):
        nlist.append(liste[i])
        for x in range(len(nlist)):
            for t in range(len(nlist)-1):
                if nlist[t] < nlist[t+1]:
                    continue
                else:
                    nlist[t], nlist[t+1] = nlist[t+1], nlist[t]
                    continue
        print(nlist)
    return nlist



# Roma rakamlarını sayıya çevirme
def RomantoInt():
    romans = ("I", "V", "X", "L", "C", "D", "M")
    ints = (1, 5, 10, 50, 100, 500, 1000)

    thenum = input("Enter Roman Number: ").upper()
    a = list()
    for i in thenum:
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
            print("Geçerli bir sayı girin.")


