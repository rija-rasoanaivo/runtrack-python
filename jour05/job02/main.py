def draw_rectangle(width, height): #la fonction prend deux paramètres en entrée: largeur("width") et hauteur("height") du rectangle à dessiner
    rectangle=""#inititalisation de la variable rectangle qui sera utiliser pour stocker progressivement les lignes du rectangles à dessiner

    for h in range(height):#boucle "for" pour la hateur, la première boucle "for h in range(height)" est utilisée pour itérer à travers chaque ligne du rectangle en fontion de la hauteur donnée
        line="|"#A chaque itération, une variable "line" est initialisé avec le caractère "|".Ensuite, des conditions sont utilisées pour déterminer la construction de la ligne en fonction de sa position dans le rectangle
        if h == 0 or h == height -1:#Si c'est la première ou la dernière ligne (if h == 0 or h == height - 1), la ligne est construite avec des '-' à l'exception des coins où se trouvent les '|'
            line +="-" * (width-2) + "|"
        else:#Sinon, pour les lignes internes, la ligne est construite avec des espaces pour remplir l'intérieur du rectangle, à l'exception des coins où se trouvent les '|'.
            line += " " * (width-2) + "|"
        rectangle += line +"\n"#Assemblage du rectangle : À chaque itération de la boucle, la ligne complète est ajoutée à la variable rectangle
    print(rectangle)#Affichage du rectangle : Une fois que toutes les lignes du rectangle ont été générées et assemblées dans la variable rectangle, celui-ci est affiché dans la console à l'aide de print(rectangle)

draw_rectangle(10, 3)#En ajustant les valeurs de width et height dans l'appel à la fonction draw_rectangle(), vous pouvez dessiner des rectangles de différentes tailles.