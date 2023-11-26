def chiffrement_cesar(message, decalage):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message_chiffre = ''

    for lettre in message:
        if lettre.lower() in alphabet:  # Vérifie si la lettre est dans l'alphabet
            index = (alphabet.index(lettre.lower()) + decalage) % len(alphabet)
            if lettre.isupper():  # Vérifie si la lettre est en majuscule
                lettre_chiffree = alphabet[index].upper()
            else:
                lettre_chiffree = alphabet[index]
            message_chiffre += lettre_chiffree  # Ajoute la lettre décalée au message chiffré
        else:
            message_chiffre += lettre  # Ajoute les caractères spéciaux sans les modifier

    return message_chiffre

message = 'Bonjour ! Rija Rasoanaivo xYz'
decalage = 3
print(chiffrement_cesar(message, decalage))