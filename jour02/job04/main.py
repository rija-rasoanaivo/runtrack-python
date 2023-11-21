n = int(input("Entrez un entier supérieur à zéro (N)"))

if n <= 0:
    print("Veuillez respecter les conditions")
else:
    print(f"La table de multiplication de {n} est:")

    for i in range(1, 11):
        print(f"{i} x {n} = {i * n}")