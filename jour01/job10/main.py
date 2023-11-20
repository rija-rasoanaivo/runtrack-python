investissement_initial = 1000
rendement_annuel = 0.1
gain = investissement_initial * rendement_annuel
print (gain)

investissement_initial += gain
print (f' montant total :{investissement_initial} €')

augmentation = 5000
rendement_annuel_augmente = 0.02

investissement_initial += augmentation 
print (f' capital de linvestisseur :{investissement_initial} €')

rendement_annuel += rendement_annuel_augmente 
gain = investissement_initial *rendement_annuel
print (f' montant total après investissemnt :{gain} €')

investissement_initial += gain
print (f' total dans le compte en banque: {investissement_initial}')

retrait = 0.9

investissement_initial *= retrait
print (f'montant après le retrait de 10%: {investissement_initial} €')

rendement_annuel -= 0.01
gain = investissement_initial * rendement_annuel
print (f'gain après que le rendement diminue de 1%: {gain} €')



