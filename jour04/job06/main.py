def echange_valeur():
    valeur=list(range(1,6))
    return valeur
print(echange_valeur())

def echange_valeur():
    valeur=list(range(1,6))
    valeur[0], valeur[-1] = valeur[-1], valeur[0]
    return valeur
print(echange_valeur())