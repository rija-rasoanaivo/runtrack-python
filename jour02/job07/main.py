chaine = "abcdefghijklmnopqrstuvwxyz" * 10

i = 1

while i <= len(chaine):
    print(chaine[:i])
    i += 2
    if i > len(chaine):
        break