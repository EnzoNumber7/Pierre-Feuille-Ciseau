from random import*

#Fonction qui permet d'afficher le morpion a joueur
def affichage_morpion(tab):
    print("    0   1   2")
    for i in range(len(tab)):
        print(i,"׀ ",end="")
        for j in range(len(tab[i])):
            print(tab[i][j], end=" ׀ ")
        print("\n")


#Fonction qui permet de verifier les condition de victoire du morpion, c'est à dire, 3 fois le meme symbole sur la meme diagonal/ligne/colone
def verification_victoire(tab,symbole):
    nbSymbole = 0
    #Verification des lignes
    for i in range(len(tab)):
        for j in range(len(tab)):
            #Si il y a le symbole rechercher sur la case
            if tab[i][j] == symbole:
                nbSymbole += 1
        
        #On verifie s'il y a 3 fois le symbole sur une ligne
        if nbSymbole == 3:
            #Si oui on a gagner
            return True
        else:
            #Sinon, on remet le compteur a 0 car on change de ligne
            nbSymbole = 0
 
    #Verification des colones
    for i in range(len(tab)):
        for j in range(len(tab)):
            #Si il y a le symbole rechercher sur la case
            if tab[j][i] == symbole:
                nbSymbole += 1
                
        #On verifie s'il y a 3 fois le symbole sur une colone
        if nbSymbole == 3:
            #Si oui on a gagner
            return True
        else:
            #Sinon, on remet le compteur a 0 car on change de colone
            nbSymbole = 0

    #Verification diagonal Haut-Gauche vers Bas Droite
    for i in range(len(tab)):
        #Si il y a le symbole rechercher sur la case
        if tab[i][i] == symbole:
            nbSymbole += 1
    
    #On verifie s'il y a 3 fois le symbole sur la diagonal
    if nbSymbole == 3:
        #Si oui on a gagner
        return True
    else:
        #Sinon, on remet le compteur a 0 car on change de diagonal
        nbSymbole = 0

    #Verification diagonal Bas-Gauche vers Haut-Droite
    j=0
    for i in range(len(tab)-1,-1,-1):
        if tab[i][j] == symbole:
            nbSymbole += 1
        j += 1

        #On verifie s'il y a 3 fois le symbole sur la diagonal
        if nbSymbole == 3:
            #Si oui on a gagner
            return True

    #Si il n'y a aucune ligne/colone/diagonal, ou le joueur a 3 fois son symbole, alors on renvoie False
    return False

#Une fonction qui verifie s'il y a 2 symbole et une case vide sur la meme ligne/colone    
def verification_CPU(tab,symbole):
    nbSymbole,nbCaseVide,ligneCaseVide,coloneCaseVide= 0,0,0,0
    #Verification des lignes
    for i in range(len(tab)):
        for j in range(len(tab)):
            #Si il y a le symbole sur la ligne
            if tab[i][j] == symbole:
                nbSymbole += 1
            #Sinon s'il y a une case vide
            elif tab[i][j] == "_":
                nbCaseVide += 1
                ligneCaseVide,coloneCaseVide = i,j
        
        #On verifie s'il y a 2 symbole et une case vide sur la meme ligne
        if nbSymbole == 2 and nbCaseVide == 1:
            #Si oui on renvoi Vrai, la ligne et la colone de la case vide
            return True,ligneCaseVide,coloneCaseVide
        else:
            #Sinon, on remet le compteur a 0 car on change de ligne
            nbSymbole,nbCaseVide,ligneCaseVide,coloneCaseVide= 0,0,0,0
    
    #Verification des colones
    for i in range(len(tab)):
        for j in range(len(tab)):
            #Si il y a le symbole sur la colone
            if tab[j][i] == symbole:
                nbSymbole += 1
            #Sinon s'il y a une case vide, et on ajoute ses coordonné
            elif tab[j][i] == "_":
                nbCaseVide += 1
                ligneCaseVide,coloneCaseVide = j,i
                
        #On verifie s'il y a 2 fois le symbole et une case vide sur une colone
        if nbSymbole == 2 and nbCaseVide == 1:
            #Si oui on renvoi Vrai, la ligne et la colone de la case vide
            return True,ligneCaseVide,coloneCaseVide
        else:
            #Sinon, on remet le compteur a 0 car on change de colone
            nbSymbole,nbCaseVide,ligneCaseVide,coloneCaseVide= 0,0,0,0

    
    #Verification de la diagonal haut gauche vers bas droite
    for i in range(len(tab)):
        #Si il y a le symbole rechercher sur la case
        if tab[i][i] == symbole:
            nbSymbole += 1
        #Sinon s'il y a une case vide, et on ajoute ses coordonné
        elif tab[i][i] == "_":
            nbCaseVide += 1
            ligneCaseVide,coloneCaseVide = i,i
    
    #On verifie s'il y a 2 fois le symbole et une case vide sur la diagonal
    if nbSymbole == 2 and nbCaseVide == 1:
        #Si oui on renvoi Vrai, la ligne et la colone de la case vide
        return True,ligneCaseVide,coloneCaseVide
    else:
        #Sinon, on remet le compteur a 0 car on change de diagonal
        nbSymbole,nbCaseVide,ligneCaseVide,coloneCaseVide= 0,0,0,0
    
    #Verification diagonal Bas-Gauche vers Haut-Droite
    j=0
    for i in range(len(tab)-1,-1,-1):
        if tab[i][j] == symbole:
            nbSymbole += 1
        elif tab[i][j] == "_":
            nbCaseVide += 1
            ligneCaseVide,coloneCaseVide = i,j
        j += 1

        #On verifie s'il y a 2 fois le symbole et une case vide sur la diagonal
        if nbSymbole == 2 and nbCaseVide == 1:
            #Si oui on a gagner
            return True,ligneCaseVide,coloneCaseVide
        else:
            #Sinon, on remet le compteur a 0 car on change de diagonal
            nbSymbole,nbCaseVide,ligneCaseVide,coloneCaseVide= 0,0,0,0


    #S'il y a le symbole en haut a gauche et en bas a droite ou au milieu à droite
    if (tab[0][0] == symbole and (tab[2][2] == symbole or tab[1][2] == symbole ))  :
        #Alors si la case en haut au milieu est vide
        if tab[0][2] == "_":
            #Alors on retourne vrai et les coordoner de la case en haut au milieu
            return True,0,2
    #Sinon s'il y a le symbole dans la case en haut a gauche et la case en bas au milieu
    elif tab[0][0] == symbole and tab[2][1] == symbole :
        #Alors on retourne vrai et les coordoner de la case en haut au milieu
        return True,2,0
    
    #S'il y a le symbole en bas a droite et en haut au milieu ou en haut a gauche
    if tab[2][2] == symbole and tab[0][1] == symbole:
        #Si la case à droite au milieu est vide
        if tab[1][2] == "_":
             #Alors on retourne vrai et les coordonée de la case à droite au milieu
            return True,0,2
    #Sinon s'il y a le symbole dans la case en bas a droite et la case a gauche au milieu
    elif tab[2][2] == symbole and tab[1][0] == symbole:
        if tab[2][0] == "_":
            #Alors on retourne vrai et les coordonnés de la case en haut à gauche
            return True,2,0
    
    #S'il y a le symbole en bas à gauche et en haut à droite ou en haut au milieu
    if tab[2][0] == symbole and (tab[0][2] == symbole or tab[0][1] == symbole):
        if tab[0][0] == "_":
            #Alors on retourne vrai et les coordonné de la case au milieu à gauche
            return True,0,0
    #Sinon s'il y a le symbole dans la case en au milieu a droite
    elif tab[2][0] == symbole and tab[1][2] == symbole:
        if tab[2][2] == "_":
            #Alors on retourne vrai et les coordonnés de la case en bas au milieu
            return True,2,2
    
    #S'il y a le symbole en bas à gauche et en haut à droite ou en haut au milieu
    if tab[0][2] == symbole and (tab[2][0] == symbole or tab[1][0] == symbole):
        if tab[0][0] == "_":
            #Alors on retourne vrai et les coordonné de la case au milieu à gauche
            return True,0,0
    #Sinon s'il y a le symbole dans la case en au milieu a droite
    elif tab[0][2] == symbole and tab[2][1] == symbole:
        if tab[2][2] == "_":
            #Alors on retourne vrai et les coordonnés de la case en bas au milieu
            return True,2,2
    
    #on cherche une diagonal vide 
    if tab[0][0] == "_":
        return True,0,0
    elif tab[0][2] == "_":
        return True,0,2
    elif tab[2][0] == "_":
        return True,2,0
    elif tab[2][2] == "_":
        return True,2,2

    #On parcours le tableau pour trouver une case vide
    for i in range(len(tab)):
        for j in range(len(tab)):
            #Si la case est vide
            if tab[i][j] == "_":
                #Alors on retourne vrai et les coordonné de la case vide
                return True,i,j    

    else:
        return False,None,None

    

def morpion_PVP():
    # Création du tableau de morpion
    tableau=[["_","_","_"],["_","_","_"],["_","_","_"]]
    affichage_morpion(tableau)

    victoire = False

    #Determine qui commence entre le joueur_⭘ et le joueur_✖
    tours = choice( ["✖","⭘"])
    #On compte les tours
    nbTours = 0
    
    # Tant que personne n'as gagner
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
            #On verifie si le joueur a gagner
            victoire = verification_victoire(tableau,"✖")
            #S'il a gagner on arrete le jeu
            if victoire:
                affichage_morpion(tableau)
                print("\nVictoire Joueur_✖")
                break  
            #Si il y a eu 9 tours
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
            #On verifie si le joueur a gagner
            victoire = verification_victoire(tableau,"⭘")
            #S'il a gagner on arrete le jeu
            if victoire:
                affichage_morpion(tableau)
                print("Victoire Joueur_⭘")
                break
            #Si il y a eu 9 tours
            elif nbTours == 9:
                affichage_morpion(tableau)
                #Alors, toute les cases ont été remplis et donc personne n'as gagner
                print("Egalite, personne n'as gagner !")
                break
            #Sinon on affiche l'etat actuel du morpion
            affichage_morpion(tableau)
        



def morpion_PVC():
    # Création du tableau de morpion
    tableau=[["_","_","_"],["_","_","_"],["_","_","_"]]
    affichage_morpion(tableau)

    victoire = False

    #Determine qui commence entre le joueur_⭘ et le joueur_✖
    tours = choice( ["✖"])
    #Compte le nombre de tours de jeu
    nbTours = 0
    
    # Tant que personne n'as gagner
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
            #On verifie si le joueur a gagner
            victoire = verification_victoire(tableau,"✖")
            #S'il a gagner on arrete le jeu
            if victoire:
                affichage_morpion(tableau)
                print("\nVictoire Joueur_✖")
                break
            #Sinon on affiche l'etat actuel du morpion
            else:
                affichage_morpion(tableau)
            
            
        #Si c'est au tours du CPU
        if tours == "⭘":
            #Si c'est le premier tours du jeu, c'est à dire que le joueur a jouer en premier
            if nbTours == 1:
                #Si la case central est vide
                if tableau[1][1] == "_":
                    #Alors le CPU joue au milieu, on passe au tours suivant, celui du joueur
                    tableau[1][1] = "⭘"
                    tours = "✖"
                    nbTours += 1
                    affichage_morpion(tableau)
                #Sinon le joueur à jouer sur la case central
                else:
                    #Alors le CPU joue dans l'angle en bas à droite, on passe au tours suivant, celui du joueur
                    tableau[2][2] = "⭘"
                    tours = "✖"
                    nbTours += 1
                    affichage_morpion(tableau)
            #Si c'est apres le 2éme tours, donc le second tours du CPU
            if nbTours >= 3 and nbTours < 9:
                #Alors on verifie les ligne, les colones et les diagonales via la fonction verification_CPU, pour le ⭘
                verif = verification_CPU(tableau,"⭘")
                #S'il n'y a pas 2 cercle sur la meme ligne colone diago
                #S'il y a deux ⭘ et une case vide dans la meme ligne/colone/diago
                if False in verif:
                    #Alors on verifie pour les ✖
                    verif = verification_CPU(tableau,"✖")
                if True in verif:
                    #Alors on remplace dans le tableau le couple ligne/colone (donc le couple verif[1]/verif[2]) par un ⭘
                    tableau[verif[1]][verif[2]] = "⭘"
                    affichage_morpion(tableau)
                    tours = "✖"
                    nbTours += 1
            if nbTours == 9 :
                affichage_morpion(tableau)
                #Alors, toute les cases ont été remplis et donc personne n'as gagner
                print("Egalite, personne n'as gagner !")
                break

                        
                    
            #On verifie si le CPU à gagner
            victoire = verification_victoire(tableau,"⭘")
            #S'il a gagner on arrete le jeu
            if victoire:
                affichage_morpion(tableau)
                print("\nVictoire Joueur_✖")
                break




            

morpion_PVC()