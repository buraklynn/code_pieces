
# Find min
def minnum(listex):
    minx = listex[0]
    for i in range(len(listex)-1):
        if listex[i+1] < min:
            minx = listex[i+1]
    return minx


# Bubble sort
def bubble_sort(liste):
    liste_len = len(liste)
    for i in range(liste_len):
        for k in range(liste_len-(i+1)):
            if liste[k] > liste[k+1]:
                liste[k], liste[k+1] = liste[k+1], liste[k]
    return liste


# Sorting
def sortingx(liste):
    for k in range(len(liste)):
        for i in range(len(liste)-1):
            if liste[i] > liste[i+1]:
                liste[i], liste[i+1] = liste[i+1], liste[i]
    return liste


# Insertion sort
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

