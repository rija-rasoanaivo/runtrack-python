L = [7, 11, 42, 39, 2]
def addition(liste):
    newlist=[i + 1 for i in liste]
    return newlist
print(addition(L))

#autre possibilité mais bof je trouve car ça affiche un "none"    
def list():
    for i in range(len(L)):
        L[i] += 1
    print(L)
print(list())