def dessin_triangle(hauteur):
    for i in range(hauteur):
        if i == 0:  # Pour la première ligne
            ligne = ' ' * (hauteur - i) + '/' + '\\'  # Construction de la première ligne
        elif i == hauteur - 1:  # Pour la dernière ligne
            ligne = ' /' + '_' * (2 * hauteur-2) + '\\'
        else:  # Pour les lignes intermédiaires
            espaces = ' ' * (hauteur - i)
            ligne = espaces + '/' + ' ' * (2 * i) + '\\' + espaces
        print(ligne)

dessin_triangle(5)
