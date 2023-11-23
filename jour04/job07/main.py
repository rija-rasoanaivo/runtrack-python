L = [8, 24,48,2,16]
#autre possibilité:
#count = len([multiples_de_3 for multiples_de_3  in L if (multiples_de_3  % 3 ==0)])
#print (count)

def multiple3(liste):
    compte = 0
    for i in liste:
        if i %3==0:
            compte += 1
    return compte
print("Nombre de multiple de 3 dans la lise:",multiple3(L))