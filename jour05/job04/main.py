def dessin(hauteur):
    for i in range(hauteur + 2):
        if i == 0 or i == hauteur + 1:  # Pour la première et dernière ligne
            ligne = "+" + "-" * hauteur + "+"
        else:  # Pour les lignes intermédiaires
            nb_hashtags = hauteur - i + 1
            espaces = hauteur - nb_hashtags 
            ligne = "|" + "#" * nb_hashtags + " " * espaces + "|"
            if nb_hashtags == hauteur:  # Si la ligne contient '#' et est la dernière ligne de '#' (10 lignes)
                ligne = ligne[::-1].replace(" ", "#", 1)[::-1]
        print(ligne)

# Exemple d'utilisation avec une hauteur de 10
dessin(10)
