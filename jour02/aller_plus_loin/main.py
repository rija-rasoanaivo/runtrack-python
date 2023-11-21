a = int(input("Entrez la longueur a :"))
b = int(input("Entrez la longueur b :"))
c = int(input("Entrez la longueur c :"))

if a == b == c :
    print("Vous avez un triangle équilatéral")
elif a == b or a == c or b == c:
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Vous avez un triangle isocèle rectangle")
    else :
        print("Vous avez un triangle isocèle")

elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("Vous avez un triangle rectangle")

else:
    print("Vous avez unt triangle quelconque")
