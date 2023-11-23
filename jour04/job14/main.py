def my_long_word(number, text):#la fonction prend deux paramètres "number(chiffre entier)" et text
    words = text.split()#découpe de la chaîne text en une liste de mots en utilisant l'expace comme séparateur et stocke ces mots ces mots dans la variable "words"
    result = ""#Initialisation d'une chaine vide "result" qui stockera les mots plus longs que "number"

    for word in words:#boucle qui parcourt chaque mot dans dans la liste "words"
        word_length = 0 #initialisation d'un compteur "word_length" à zéro
        for char in word: #boucle qui parcourt chaque caractère dans le mot actuel
            word_length += 1 #pour chaque caractère, elle incrémente le compteur "word_length" de 1
        
        if word_length > number:#après avoir parcouru tous les caractères du mot, elle vérifie si "word_length" est supérieur à "number"
            result += word + " "#si la longueur du mot est supérieure au choffre donnée, elle ajoute ce mot à la chaîne "result" suivie d'un espace à l'aide de guillemets " "

    return result#la fonction retourne la chaîne de caractères 

output = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")
print("Output:", output)
