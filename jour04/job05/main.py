L = list(range(1, 6))

def liste(list):
    return list
print (liste(L))

def liste(list):
    return list[1]
print (liste(L))

def liste(list):
    L[3]= L[2] + L[4]
    return list
print (liste(L))

def liste(list):
    L[3]= L[2] + L[4]
    return list[-1]
print (liste(L))