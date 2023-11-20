nom = "lait"
prix_unitaire = 2
quantite_en_stock = 30

resultat= f'produit: {nom}, prix: {prix_unitaire} €, stock :{quantite_en_stock}'
print (resultat)

quantite_achete = int(input(f'combien de {nom} souhaitez vous acheter?'))

prix_unitaire *= 1.1
quantite_en_stock -= quantite_achete

resultat= f'produit: {nom}, prix: {prix_unitaire} €, stock :{quantite_en_stock}'
print (resultat)