valeur=list(range(1,6))

def echange_valeur(liste):
    return liste
print(echange_valeur(valeur))

def echange_valeur(liste):
    liste[0], liste[-1] = liste[-1], liste[0]
    return liste
print(echange_valeur(valeur))