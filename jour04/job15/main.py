L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

def arrondi(liste):
    L_arrondie = [int(num + 0.5) for num in liste]
    return L_arrondie

def tri_bulles(liste):
    n = 1
    while True:
        swapped = False
        i = 0
        while True:
            try:
                if liste[i] > liste[i + 1]:
                    liste[i], liste[i + 1] = liste[i + 1], liste[i]
                    swapped = True
            except IndexError:
                break
            i += 1

        if not swapped:
            break
        n += 1

L_arrondie = arrondi(L)
tri_bulles(L_arrondie)

print(L_arrondie)
