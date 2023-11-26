def distance_parcourue(nombre_marches, hauteur_marche):
    # Convertir la hauteur de chaque marche en mètres
    hauteur_marche_m = hauteur_marche / 100

    # Calculer la distance totale parcourue pour un aller-retour aux toilettes
    distance_aller_retour = 2 * nombre_marches * hauteur_marche_m

    # Calculer la distance totale parcourue par jour (5 fois aux toilettes)
    distance_par_jour = 5 * distance_aller_retour

    # Calculer la distance totale parcourue par semaine (7 jours)
    distance_par_semaine = 7 * distance_par_jour

    return distance_par_semaine

# Test de la fonction
nombre_marches = 100
hauteur_marche = 20  # en cm
distance = distance_parcourue(nombre_marches, hauteur_marche)
print(f"Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcourt {distance:.2f} m par semaine.")
