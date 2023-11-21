for i in range(1, 101):


    #Vérifie si le nombre est à la fois un multiple de 3 et de 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    #Vérifie si le nombre est un multiple de 3 mais pas de 5
    elif i % 3 == 0:
        print("Fizz")

    #Vérifie sur le nombre est un multiple de 5 mais pas de 3
    elif i % 5 == 0:
        print("Buzz")
    
    #Si aucune des conditions ci-dessus n'est satisfaite, affiche le nombre lui-même
    else:
        print (i)