from random import*

#Definir la fonction affichage_morpion qui permet d'afficher le jeux
def affichage_morpion(tab):
    #Afficher le numero des colone
    print("    0   1   2")
    for i in range(len(tab)):
        #Afficher le numero des lignes
        print(i,"׀ ",end="")
        #Afficher le contenue de chaque case ainsi que les séparation
        for j in range(len(tab[i])):
            print(tab[i][j], end=" ׀ ")
        print("\n")


#Definir la fonction verification_victoire qui permet de verifier les condition de victoire du morpion, c'est à dire, 3 fois le meme symbole sur la meme diagonal/ligne/colone
def verification_victoire(tab,symbole):
    #Initialiser la variable nbSymbole à 0
    nbSymbole = 0
    #Verification des lignes
    for i in range(len(tab)):
        for j in range(len(tab)):
            #Si il y a le symbole rechercher sur la case
            if tab[i][j] == symbole:
                #Alors incrémenter la variable nbSymbole
                nbSymbole += 1
        
        #S'il y a 3 fois le même symbole sur une ligne
        if nbSymbole == 3:
            #Alors retourner Vrai
            return True
        else:
            #Sinon, on remet le compteur a 0 car on change de ligne
            nbSymbole = 0
 
    #Verification des colones
    for i in range(len(tab)):
        for j in range(len(tab)):
            #Si il y a le symbole rechercher sur la case
            if tab[j][i] == symbole:
                #Alors incrémenter la variable nbSymbole
                nbSymbole += 1
                
        #S'il y a 3 fois le symbole sur une colone
        if nbSymbole == 3:
            #Alors retourner Vrai
            return True
        else:
            #Sinon, remettre le compteur a 0 car on change de colone
            nbSymbole = 0

    #Verification diagonal Haut-Gauche vers Bas Droite
    for i in range(len(tab)):
        #Si il y a le symbole rechercher sur la case
        if tab[i][i] == symbole:
            #Alors incrémenter la variable nbSymbole
            nbSymbole += 1
    
    #S'il y a 3 fois le symbole sur la diagonal
    if nbSymbole == 3:
        #Alors retourner Vrai
        return True
    else:
        #Sinon, remettre le compteur a 0 car on change de diagonal
        nbSymbole = 0

    #Verification diagonal Bas-Gauche vers Haut-Droite
    j=0
    for i in range(len(tab)-1,-1,-1):
        #S'il y a le symbole rechercher sur la case
        if tab[i][j] == symbole:
            #Alors incrémenter la variable nbSymbole
            nbSymbole += 1
        j += 1

        #S'il y a 3 fois le symbole sur la diagonal
        if nbSymbole == 3:
            #Alors retourner Vrai
            return True

    #Sinon, s'il n'y a aucune ligne/colone/diagonal, ou le joueur a 3 fois son symbole, alors renvoyer False
    return False

#Definir une fonction verification_CPU qui verifie toute les possibilité de jeux pour que l'ordi puisse réagir
def verification_CPU(tab,symbole):
    #Initialiser les variable nbSymbole, nbCaseVide, ligneCaseVide, coloneCaseVide et col
    nbSymbole,nbCaseVide,ligneCaseVide,coloneCaseVide,col= 0,0,0,0,0
    
    #Verification des lignes
    for i in range(len(tab)):
        for j in range(len(tab)):
            #Si il y a le symbole sur la ligne
            if tab[i][j] == symbole:
                #Alors incrémenter la variable nbSymbole
                nbSymbole += 1
            #Sinon s'il y a une case vide
            elif tab[i][j] == "_":
                #Alors incrementer la variable nbCaseVide
                nbCaseVide += 1
                #Associer les variable ligneCaseVide et coloneCaseVide au coordoner de la case vide (i et j)
                ligneCaseVide,coloneCaseVide = i,j
        
        #S'il y a 2 symbole et une case vide sur la meme ligne
        if nbSymbole == 2 and nbCaseVide == 1:
            #Renvoyer Vrai, la ligne et la colone de la case vide
            return True,ligneCaseVide,coloneCaseVide
        else:
            #Sinon, remettre les compteur a 0 car on change de ligne
            nbSymbole,nbCaseVide,ligneCaseVide,coloneCaseVide= 0,0,0,0
    
    #Verification des colones
    for i in range(len(tab)):
        for j in range(len(tab)):
            #Si il y a le symbole sur la colone
            if tab[j][i] == symbole:
                #Alors incrémenter la variable nbSymbole
                nbSymbole += 1
            #Sinon s'il y a une case vide, et on ajoute ses coordonné
            elif tab[j][i] == "_":
                #Alors incrementer la variable nbCaseVide
                nbCaseVide += 1
                #Associer les variable ligneCaseVide et coloneCaseVide au coordoner de la case vide (j et i)
                ligneCaseVide,coloneCaseVide = j,i
                
        #S'il y a 2 fois le symbole et une case vide sur une colone
        if nbSymbole == 2 and nbCaseVide == 1:
            #Alors, renvoyer Vrai, la ligne et la colone de la case vide
            return True,ligneCaseVide,coloneCaseVide
        else:
            #Sinon, remettre les compteur a 0 car on change de colone
            nbSymbole,nbCaseVide,ligneCaseVide,coloneCaseVide= 0,0,0,0

    
    #Verification de la diagonal haut gauche vers bas droite
    for i in range(len(tab)):
        #S'il y a le symbole rechercher sur la case
        if tab[i][i] == symbole:
            #Alors incrémenter la variable nbSymbole
            nbSymbole += 1
        #Sinon s'il y a une case vide, et on ajoute ses coordonné
        elif tab[i][i] == "_":
            #Alors incrementer la variable nbCaseVide
            nbCaseVide += 1
            #Associer les variable ligneCaseVide et coloneCaseVide au coordoner de la case vide (i et i)
            ligneCaseVide,coloneCaseVide = i,i
    
    #S'il y a 2 fois le symbole et une case vide sur la diagonal
    if nbSymbole == 2 and nbCaseVide == 1:
        #Alors, renvoyer Vrai, la ligne et la colone de la case vide
        return True,ligneCaseVide,coloneCaseVide
    else:
        #Sinon, remettre les compteur a 0 car on change de diagonal
        nbSymbole,nbCaseVide,ligneCaseVide,coloneCaseVide= 0,0,0,0
    
    #Verification diagonal Bas-Gauche vers Haut-Droite
    for i in range(len(tab)-1,-1,-1):
        #S'il y a le symbole rechercher sur la case
        if tab[i][j] == symbole:
            #Alors incrémenter la variable nbSymbole
            nbSymbole += 1
        #Sinon s'il y a une case vide, et on ajoute ses coordonné
        elif tab[i][j] == "_":
            #Alors incrementer la variable nbCaseVide
            nbCaseVide += 1
            #Associer les variable ligneCaseVide et coloneCaseVide au coordoner de la case vide (i et j)
            ligneCaseVide,coloneCaseVide = i,j
        col += 1

        #S'il y a 2 fois le symbole et une case vide sur la diagonal
        if nbSymbole == 2 and nbCaseVide == 1:
            #Alors, renvoyer Vrai, la ligne et la colone de la case vide
            return True,ligneCaseVide,coloneCaseVide
        else:
            #Sinon, remettre les compteur a 0 car on change de diagonal
            nbSymbole,nbCaseVide,ligneCaseVide,coloneCaseVide= 0,0,0,0


    #S'il y a le symbole dans la case de coordonnée 0,0 et  1,2
    if tab[0][0] == symbole and tab[1][2] == symbole  :
        #Alors si la case de coordonnée 0,2 est vide
        if tab[0][2] == "_":
            #Alors retourner vrai et les coordoner 0,2
            return True,0,2
    #Sinon s'il y a le symbole dans la case de coordonnée 0,0 et 2,1
    elif tab[0][0] == symbole and tab[2][1] == symbole :
        #Alors retourner vrai et les coordoner 2,0
        return True,2,0
    
    #S'il y a le symbole dans la case de coordonnée 2,2 et  0,1
    if tab[2][2] == symbole and tab[0][1] == symbole:
        #Alors si la case de coordonnée 0,2 est vide
        if tab[0][2] == "_":
             #Alors retourner vrai et les coordonée 0,2
            return True,0,2
    #Sinon s'il y a le symbole dans la case de coordonnée 2,2 et 1,0
    elif tab[2][2] == symbole and tab[1][0] == symbole:
        #Alors si la case de coordonnée 2,0 est vide
        if tab[2][0] == "_":
            #Alors retourner vrai et les coordonnés 2,0
            return True,2,0
    
    #S'il y a le symbole dans la case de coordonnée 2,0 et  0,2 ou 0,1
    if tab[2][0] == symbole and (tab[0][2] == symbole or tab[0][1] == symbole):
          #Alors si la case de coordonnée 0,0 est vide
        if tab[0][0] == "_":
            #Alors on retourne vrai et les coordonné 0,0
            return True,0,0
    #Sinon s'il y a le symbole dans la case de coordonnée 2,0 et 1,2
    elif tab[2][0] == symbole and tab[1][2] == symbole:
         #Alors si la case de coordonnée 2,2 est vide
        if tab[2][2] == "_":
            #Alors on retourne vrai et les coordonnés 2,2
            return True,2,2
    
    #S'il y a le symbole dans la case de coordonnée 0,2 et  2,0 ou 1,0
    if tab[0][2] == symbole and (tab[2][0] == symbole or tab[1][0] == symbole):
         #Alors si la case de coordonnée 0,0 est vide
        if tab[0][0] == "_":
            #Alors on retourne vrai et les coordonné 0,0
            return True,0,0
    #Sinon s'il y a le symbole dans la case de coordonnée 0,2 et 2,1
    elif tab[0][2] == symbole and tab[2][1] == symbole:
         #Alors si la case de coordonnée 2,2 est vide
        if tab[2][2] == "_":
            #Alors on retourne vrai et les coordonnés 2,2
            return True,2,2  
    
    #Si les angles opposer sont des ✖
    if tab[0][0] == "✖" and tab[2][2] == "✖":
        #Alors si les cases au milieu de chaque coté sont vides
        if tab[0][1] == "_":
            return True,0,1
        elif tab[1][2] == "_":
            return True,1,2
        elif tab[1][0] == "_":
            return True,2,0
        elif tab[2][1] == "_":
            return True,2,1
    if tab[2][0] == "✖" and tab[0][2] == "✖":
        if tab[0][1] == "_":
            return True,0,1
        elif tab[1][2] == "_":
            return True,1,2
        elif tab[1][0] == "_":
            return True,2,0
        elif tab[2][1] == "_":
            return True,2,1
      
    #Si aucune des conditions est verifier alors retourner Faux, Vide et Vide
    return False,None,None

    
#Definir la fonction morpion_PVP, qui permet de faire une partie de morpion contre un autre joueur
def morpion_PVP():
    #Initialisation du tableau de morpion
    tableau=[["_","_","_"],["_","_","_"],["_","_","_"]]
    affichage_morpion(tableau)

    #Initialiser la variable victoire à Faux
    victoire = False

    #Initialiser la variable tours qui determine qui commence entre le joueur_⭘ et le joueur_✖ aleatoirement
    tours = choice( ["✖","⭘"])
    #Initialiser la variable nbTours qui compte les tours
    nbTours = 0
    
    #Tant que personne n'as gagner
    while victoire == False:

        #Si c'est au tours du joueur_✖
        if tours == "✖":
            #Demande au joueur de choisir une ligne
            print("Joueur_✖ choisissez le numéro d'une ligne ")
            ligne = int(input(""))
            #Demande au joueur de choisir une colone
            print("\nJoueur_✖ choisissez le numéro d'une colone ")
            colone = int(input(""))
            #Si la ligne ou la colone ne sont pas presente dans le tableau
            if ligne > 2 or ligne < 0 or colone < 0 or colone > 2:
                print("Erreur dans la saisi de la ligne ou de la colone")
            #S'il y a déjà un symbole sur le couple ligne colone choisi
            if tableau[ligne][colone] == "⭘" or tableau[ligne][colone] == "✖":
                print("Erreur, la case à déjà été sélectionner")
            #Sinon on rajoute le symbole au tableau, et on passe au tours du joueur suivant
            else:
                tableau[ligne][colone] = "✖"
                tours = "⭘"
                nbTours += 1
            #On verifie si le joueur a gagner grâce à la fonction verification_victoire
            victoire = verification_victoire(tableau,"✖")

            #S'il a gagner on arrete le jeu
            if victoire:
                affichage_morpion(tableau)
                print("\nVictoire Joueur_✖")
                break  
            #Sino, s'il y a eu 9 tours
            elif nbTours == 9:
                affichage_morpion(tableau)
                #Alors, toute les cases ont été remplis et donc personne n'as gagner
                print("Egalite, personne n'as gagner !")
                break

            #Sinon on affiche l'etat actuel du morpion
            affichage_morpion(tableau)
        
        
        #Si c'est au tours du joueur_⭘
        if tours == "⭘":
            #Demande au joueur de choisir une ligne
            print("Joueur_⭘ choisissez le numéro d'une ligne ")
            ligne = int(input(""))
            #Demande au joueur de choisir une colone
            print("\nJoueur_⭘ choisissez le numéro d'une colone ")
            colone = int(input(""))
            #Si la ligne ou la colone ne sont pas presente dans le tableau
            if ligne > 2 or ligne < 0 or colone < 0 or colone > 2:
                print("Erreur dans la saisi de la ligne ou de la colone")
            #S'il y a déjà un symbole sur le couple ligne colone choisi
            if tableau[ligne][colone] == "⭘" or tableau[ligne][colone] == "✖":
                print("Erreur, la case à déjà été sélectionner")
            #Sinon on rajoute le symbole au tableau, et on passe au tours du joueur suivant
            else:
                tableau[ligne][colone] = "⭘"
                tours = "✖"
                nbTours += 1
            
            #On verifie si le joueur a gagner grâce à la fonction verification_victoire
            victoire = verification_victoire(tableau,"⭘")
            #S'il a gagner on arrete le jeu
            if victoire:
                affichage_morpion(tableau)
                print("Victoire Joueur_⭘")
                break
            
            #Sinon, s'il y a eu 9 tours
            elif nbTours == 9:
                affichage_morpion(tableau)
                #Alors, toute les cases ont été remplis et donc personne n'as gagner
                print("Egalite, personne n'as gagner !")
                break
            
            #Sinon on affiche l'etat actuel du morpion
            affichage_morpion(tableau)
        


#Definir la fonction morpion_PVO qui permet de faire une partie de morpion contre l'ordinateur
def morpion_PVO():
    # Création du tableau de morpion
    tableau=[["_","_","_"],["_","_","_"],["_","_","_"]]
    affichage_morpion(tableau)

    #Initialiser la variable tours qui determine qui commence entre le joueur_⭘ et le joueur_✖ aleatoirement
    victoire = False

    #Determine qui commence entre le joueur_⭘ et le joueur_✖
    tours = choice( ["⭘","✖"])
    #Initialiser la variable nbTours qui compte les tours
    nbTours = 0
    
    #Tant que personne n'as gagner
    while victoire == False:
        #Si c'est au tours du joueur_✖
        if tours == "✖":
            #Demande au joueur de choisir une ligne
            print("Joueur_✖ choisissez le numéro d'une ligne ")
            ligne = int(input(""))
            #Demande au joueur de choisir une colone
            print("\nJoueur_✖ choisissez le numéro d'une colone ")
            colone = int(input(""))
            
            #Si la ligne ou la colone ne sont pas presente dans le tableau
            if ligne > 2 or ligne < 0 or colone < 0 or colone > 2:
                print("Erreur dans la saisi de la ligne ou de la colone")
            #S'il y a déjà un symbole sur le couple ligne colone choisi
            if tableau[ligne][colone] == "⭘" or tableau[ligne][colone] == "✖":
                print("Erreur, la case à déjà été sélectionner")
            #Sinon on rajoute le symbole au tableau, et on passe au tours suivant, celui du CPU
            else:
                tableau[ligne][colone] = "✖"
                tours = "⭘"
                nbTours += 1 
            
            #On verifie si le joueur a gagner grace à la fonction verification_victoire 
            victoire = verification_victoire(tableau,"✖")
            #S'il a gagner on arrete le jeu
            if victoire:
                affichage_morpion(tableau)
                print("\nVictoire Joueur_✖")
                break
            
            #Sinon on affiche l'etat actuel du morpion
            else:
                affichage_morpion(tableau)
            
            
        #Si c'est au tours de l'ordinateur
        if tours == "⭘":

            #Si le tours est 0, c'est le tout premier tour de la partie donc l'ordinateur commence
            if nbTours == 0:
                #Alors on se place dans la premiere case
                tableau[0][0] = "⭘"
                #On change de tours, on passe au joueur et on affiche le jeu
                nbTours += 1
                tours = "✖"
                affichage_morpion(tableau)

            #Si c'est le premier tours du jeu, c'est à dire que le joueur a jouer en premier
            elif nbTours == 1:
                #Si la case central est vide
                if tableau[1][1] == "_":
                    #Alors l'ordinateur joue au milieu, on passe au tours suivant, celui du joueur
                    tableau[1][1] = "⭘"
                    tours = "✖"
                    nbTours += 1
                    affichage_morpion(tableau)
                
                #Sinon le joueur à jouer sur la case central
                else:
                    #Alors l'ordinateur joue dans l'angle en bas à droite, on passe au tours suivant, celui du joueur
                    tableau[2][2] = "⭘"
                    tours = "✖"
                    nbTours += 1
                    affichage_morpion(tableau)

            #Si c'est le 2ème ou le 4ème tours de jeux
            elif nbTours == 2 or nbTours == 4:
                #On  verifie si le joueur peut gagner grace à la fonction verification_CPU
                verif = verification_CPU(tableau,"✖")
                
                #Si c'est vrai
                if verif[0] == True:
                    #Alors, on le bloque
                    tableau[verif[1]][verif[2]] = "⭘"
                
                else:
                    #Sinon, si la case 2,2 est vide on se place a cet endroit sinon, on se place dans une autre diagonal
                    if tableau[2][2] == "_":
                        tableau[2][2] = "⭘"
                    elif tableau[0][2] == "_":
                        tableau[0][2] = "⭘"
                    elif tableau[2][0] == "_":
                        tableau[2][0] = "⭘"
                
                #On change de tours, on passe au joueur et on affiche le jeu
                nbTours += 1
                tours = "✖"
                affichage_morpion(tableau)
                
            #Si c'est apres le 2éme tours et avant le 9ème et que l'on est pas au 8éme tours, donc le second tours de l'ordinateur
            elif nbTours >= 3 and nbTours < 9:
                #Alors on verifie si l'ordinateur peut gagner grace à la fonction verification_CPU
                verif = verification_CPU(tableau,"⭘")
                #S'il c'est faux, donc il ne peut pas gagner
                if verif[0] == False:
                    #Alors on verifie pour le joueur
                    verif = verification_CPU(tableau,"✖")
                
                #S'il y a deux ⭘ ou ✖ et une case vide dans la meme ligne/colone/diago
                if verif[0] == True:
                    #Alors on remplace dans le tableau le couple ligne/colone (donc le couple verif[1]/verif[2]) par un ⭘
                    tableau[verif[1]][verif[2]] = "⭘"
                    affichage_morpion(tableau)
                    tours = "✖"
                    nbTours += 1
                
                #S'il n'y a pas 2 ✖ ou ⭘ et une case vide dans une ligne/colone/diago
                if verif[0] == False:
                    #On verifie s'il y a une diagonal vide
                    if tableau[0][0] == "_":
                        tableau[0][0] = "⭘"
                    elif tableau[0][2] == "_":
                        tableau[0][2] == "⭘"
                    elif tableau[2][0] == "_":
                        tableau[2][0] = "⭘"
                    elif tableau[2][2] == "_":
                        tableau[2][2] = "⭘"
                    
                    #Sinon on cherche une case vide pour jouer
                    else:
                        for i in range(len(tableau)):
                            for j in range(len(tableau)):
                                if tableau[i][j] == "_":
                                    tableau[i][j] = "⭘"
                                    break
                    #On change de tours, on passe au joueur et on affiche le jeu
                    affichage_morpion(tableau)
                    tours = "✖"
                    nbTours += 1
            
            #Si on est au 8ème ou 9ème tours
            if nbTours == 9 or nbTours == 8 :
                #Si le nombre de tours est egale à 8
                if nbTours == 8:
                    #Chercher la derniere case vide
                    for i in range(len(tableau)):
                                for j in range(len(tableau)):
                                    #Si la case est vide
                                    if tableau[i][j] == "_":
                                        #on la remplace par un ⭘
                                        tableau[i][j] = "⭘"
                                    
                affichage_morpion(tableau)
                #Alors, toute les cases ont été remplis et donc personne n'as gagner
                print("Egalite, personne n'as gagner !")
                break

                        
                    
            #On verifie si l'ordinateur à gagner
            victoire = verification_victoire(tableau,"⭘")
            #S'il a gagner on arrete le jeu
            if victoire:
                affichage_morpion(tableau)
                print("\nVictoire Ordinateur")
                break




#Initialiser la variable choix
choix = ""

 #Tant que le choix est different de 3
while choix != "3":

    #On affiche les choix possible pour le joueur
    print("Jeux du morpion")
    print("1: Jouer contre un autre joueur")
    print("2: Jouer contre l'ordinateur")
    print("3: Arreter de jouer")
    #Le joueur saisi sont choix dans la variable choix
    choix = input("")

    #Si le choix est 1
    if choix == "1":
        #Alors lancer la fonction morpion_PVP()
        morpion_PVP()

    elif choix == "2":
        morpion_PVO()

print("A bientot")