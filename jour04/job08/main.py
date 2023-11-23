L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

def somme():
    count = sum([nombre_pair for nombre_pair  in L if (nombre_pair  % 2 ==0)])
    return count
print(somme())