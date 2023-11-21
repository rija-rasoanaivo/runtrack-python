for n in range(1, 1001):  # Boucle pour chaque nombre de 1 à 1000 inclus
    if n > 1:  # Vérifie si le nombre est supérieur à 1 (condition pour les nombres premiers)
        for i in range(2, n):  # Boucle pour tester la divisibilité de n par les nombres de 2 à n-1
            if (n % i) == 0:  # Vérifie si n est divisible par i
                break  # Si n est divisible par un nombre autre que 1 et lui-même, sort de la boucle
        else:  # Si la boucle s'est exécutée sans interruption (aucun diviseur trouvé)
            print(n)  # Affiche le nombre, car il est premier