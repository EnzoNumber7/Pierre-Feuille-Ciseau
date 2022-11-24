from random import*
from pierreFeuilleCiseau import *
from TicTacToe import *

#Definir la fonction affichage_morpion qui permet d'afficher le jeux
def print_game(tab):
    #Afficher le numero des colone
    print("    0   1   2")
    for i in range(len(tab)):
        #Afficher le numero des lignes
        print(i,"׀ ",end="")
        #Afficher le contenue de chaque case ainsi que les séparation
        for j in range(len(tab[i])):
            print(tab[i][j], end=" ׀ ")
        print("\n")


#Definir la fonction victory qui permet de verifier les condition de victoire du morpion, c'est à dire, 3 fois le meme symbole sur la meme diagonal/ligne/colone
def victory_verification(tab,symbol):
    #Initialiser la variable nbSymbol et col à 0
    nbSymbol,col = 0,0
    #Verification des lignes
    for i in range(len(tab)):
        for j in range(len(tab)):
            #Si il y a le symbole rechercher sur la case
            if tab[i][j] == symbol:
                #Alors incrémenter la variable nbSymbole
                nbSymbol += 1
        
        #S'il y a 3 fois le même symbole sur une ligne
        if nbSymbol == 3:
            #Alors retourner Vrai
            return True
        else:
            #Sinon, on remet le compteur a 0 car on change de ligne
            nbSymbol = 0
 
    #Verification des colones
    for i in range(len(tab)):
        for j in range(len(tab)):
            #Si il y a le symbole rechercher sur la case
            if tab[j][i] == symbol:
                #Alors incrémenter la variable nbSymbole
                nbSymbol += 1
                
        #S'il y a 3 fois le symbole sur une colone
        if nbSymbol == 3:
            #Alors retourner Vrai
            return True
        else:
            #Sinon, remettre le compteur a 0 car on change de colone
            nbSymbol = 0

    #Verification diagonal Haut-Gauche vers Bas Droite
    for i in range(len(tab)):
        #Si il y a le symbole rechercher sur la case
        if tab[i][i] == symbol:
            #Alors incrémenter la variable nbSymbole
            nbSymbol += 1
    
    #S'il y a 3 fois le symbole sur la diagonal
    if nbSymbol == 3:
        #Alors retourner Vrai
        return True
    else:
        #Sinon, remettre le compteur a 0 car on change de diagonal
        nbSymbol = 0

    #Verification diagonal Bas-Gauche vers Haut-Droite
    col=0
    for i in range(len(tab)-1,-1,-1):
        #S'il y a le symbole rechercher sur la case
        if tab[i][col] == symbol:
            #Alors incrémenter la variable nbSymbole
            nbSymbol += 1
        col += 1

        #S'il y a 3 fois le symbole sur la diagonal
        if nbSymbol == 3:
            #Alors retourner Vrai
            return True

    #Sinon, s'il n'y a aucune ligne/colone/diagonal, ou le joueur a 3 fois son symbole, alors renvoyer False
    return False

#Definir une fonction verification_CPU qui verifie toute les possibilité de jeux pour que l'ordi puisse réagir
def CPU_verification(tab,symbol):
    #Initialiser les variable nbSymbol,nbEmpty,EmptyLine,EmptyColumn et col
    nbSymbol,nbEmpty,EmptyLine,EmptyColumn,col= 0,0,0,0,0
    
    #Verification des lignes
    for i in range(len(tab)):
        for j in range(len(tab)):
            #Si il y a le symbole sur la ligne
            if tab[i][j] == symbol:
                #Alors incrémenter la variable nbSymbole
                nbSymbol += 1
            #Sinon s'il y a une case vide
            elif tab[i][j] == "_":
                #Alors incrementer la variable nbEmpty
                nbEmpty += 1
                #Associer les variable EmptyLine,EmptyColumn au coordoner de la case vide (i et j)
                EmptyLine,EmptyColumn = i,j
        
        #S'il y a 2 symbole et une case vide sur la meme ligne
        if nbSymbol == 2 and nbEmpty == 1:
            #Renvoyer Vrai, la ligne et la colone de la case vide
            return True,EmptyLine,EmptyColumn
        else:
            #Sinon, remettre les compteur a 0 car on change de ligne
            nbSymbol,nbEmpty,EmptyLine,EmptyColumn= 0,0,0,0
    
    #Verification des colones
    for i in range(len(tab)):
        for j in range(len(tab)):
            #Si il y a le symbole sur la colone
            if tab[j][i] == symbol:
                #Alors incrémenter la variable nbSymbole
                nbSymbol += 1
            #Sinon s'il y a une case vide, et on ajoute ses coordonné
            elif tab[j][i] == "_":
                #Alors incrementer la variable nbEmpty
                nbEmpty += 1
                #Associer les variable EmptyLine,EmptyColumn au coordoner de la case vide (j et i)
                EmptyLine,EmptyColumn = j,i
                
        #S'il y a 2 fois le symbole et une case vide sur une colone
        if nbSymbol == 2 and nbEmpty == 1:
            #Alors, renvoyer Vrai, la ligne et la colone de la case vide
            return True,EmptyLine,EmptyColumn
        else:
            #Sinon, remettre les compteur a 0 car on change de colone
            nbSymbol,nbEmpty,EmptyLine,EmptyColumn= 0,0,0,0

    
    #Verification de la diagonal haut gauche vers bas droite
    for i in range(len(tab)):
        #S'il y a le symbole rechercher sur la case
        if tab[i][i] == symbol:
            #Alors incrémenter la variable nbSymbole
            nbSymbol += 1
        #Sinon s'il y a une case vide, et on ajoute ses coordonné
        elif tab[i][i] == "_":
            #Alors incrementer la variable nbEmpty
            nbEmpty += 1
            #Associer les variable EmptyLine,EmptyColumn au coordoner de la case vide (i et i)
            EmptyLine,EmptyColumn = i,i
    
    #S'il y a 2 fois le symbole et une case vide sur la diagonal
    if nbSymbol == 2 and nbEmpty == 1:
        #Alors, renvoyer Vrai, la ligne et la colone de la case vide
        return True,EmptyLine,EmptyColumn
    else:
        #Sinon, remettre les compteur a 0 car on change de diagonal
        nbSymbol,nbEmpty,EmptyLine,EmptyColumn= 0,0,0,0
    
    #Verification diagonal Bas-Gauche vers Haut-Droite
    for i in range(len(tab)-1,-1,-1):
        #S'il y a le symbole rechercher sur la case
        if tab[i][col] == symbol:
            #Alors incrémenter la variable nbSymbole
            nbSymbol += 1
        #Sinon s'il y a une case vide, et on ajoute ses coordonné
        elif tab[i][col] == "_":
            #Alors incrementer la variable nbEmpty
            nbEmpty += 1
            #Associer les variable ligneCaseVide et coloneCaseVide au coordoner de la case vide (i et j)
            EmptyLine,EmptyColumn = i,j
        col += 1

        #S'il y a 2 fois le symbole et une case vide sur la diagonal
        if nbSymbol == 2 and nbEmpty == 1:
            #Alors, renvoyer Vrai, la ligne et la colone de la case vide
            return True,EmptyLine,EmptyColumn
        else:
            #Sinon, remettre les compteur a 0 car on change de diagonal
            nbSymbol,nbEmpty,EmptyLine,EmptyColumn= 0,0,0,0


    #S'il y a une ✖ dans la case de coordonnée 0,0 et  1,2
    if tab[0][0] == "✖" and tab[1][2] == "✖"  :
        #Alors si la case de coordonnée 0,2 est vide
        if tab[0][2] == "_":
            #Alors retourner vrai et les coordoner 0,2
            return True,0,2
    #Sinon s'il y a le symbole dans la case de coordonnée 0,0 et 2,1
    elif tab[0][0] == "✖" and tab[2][1] == "✖" :
        #Alors si la case de coordonnée 2,0 est vide
        if tab[2][0] == "_":
            #Alors retourner vrai et les coordoner 2,0
            return True,2,0
    
    #S'il y a une ✖ dans la case de coordonnée 2,2 et  0,1
    if tab[2][2] == "✖" and tab[0][1] == "✖":
        #Alors si la case de coordonnée 0,2 est vide
        if tab[0][2] == "_":
             #Alors retourner vrai et les coordonée 0,2
            return True,0,2
    #Sinon s'il y a une ✖ dans la case de coordonnée 2,2 et 1,0
    elif tab[2][2] == "✖" and tab[1][0] == "✖":
        #Alors si la case de coordonnée 2,0 est vide
        if tab[2][0] == "_":
            #Alors retourner vrai et les coordonnés 2,0
            return True,2,0
    
    #S'il y a uen ✖ dans la case de coordonnée 2,0 et  0,2 ou 0,1
    if tab[2][0] == "✖" and (tab[0][2] == "✖" or tab[0][1] == "✖"):
          #Alors si la case de coordonnée 0,0 est vide
        if tab[0][0] == "_":
            #Alors on retourne vrai et les coordonné 0,0
            return True,0,0
    #Sinon s'il y a une ✖ dans la case de coordonnée 2,0 et 1,2
    elif tab[2][0] == "✖" and tab[1][2] == "✖":
         #Alors si la case de coordonnée 2,2 est vide
        if tab[2][2] == "_":
            #Alors on retourne vrai et les coordonnés 2,2
            return True,2,2
    
    #S'il y a une ✖ dans la case de coordonnée 0,2 et  2,0 ou 1,0
    if tab[0][2] == "✖" and (tab[2][0] == "✖" or tab[1][0] == "✖"):
         #Alors si la case de coordonnée 0,0 est vide
        if tab[0][0] == "_":
            #Alors on retourne vrai et les coordonné 0,0
            return True,0,0
    #Sinon s'il y a une ✖ dans la case de coordonnée 0,2 et 2,1
    elif tab[0][2] == "✖"  and tab[2][1] == "✖":
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
            return True,1,0
        elif tab[2][1] == "_":
            return True,2,1
    if tab[2][0] == "✖" and tab[0][2] == "✖":
        if tab[0][1] == "_":
            return True,0,1
        elif tab[1][2] == "_":
            return True,1,2
        elif tab[1][0] == "_":
            return True,1,0
        elif tab[2][1] == "_":
            return True,2,1
      
    #Si aucune des conditions est verifier alors retourner Faux, Vide et Vide
    return False,None,None


#Definir la fonction morpion_PVO qui permet de faire une partie de morpion contre l'ordinateur
def TicTacToe_PVC():
    # Création du tableau de morpion
    tab=[["_","_","_"],["_","_","_"],["_","_","_"]]
    print_game(tab)

    #Initialiser la variable tours qui determine qui commence entre le joueur_⭘ et le joueur_✖ aleatoirement
    victory = False

    #Determine qui commence entre le joueur_⭘ et le joueur_✖
    turn = choice(["⭘","✖"])
    #Initialiser la variable nbTurns qui compte les tours
    nbTurns = 0
    
    #Tant que personne n'as gagner
    while victory == False:
        #Si c'est au tours du joueur_✖
        if turn == "✖":
            #Demande au joueur de choisir une ligne
            print("Player_✖ chose a line: ")
            line = input("")
            #Demande au joueur de choisir une colone
            print("\nPlayer_✖ chose a column: ")
            column = input("")

            #Si le joueur repond "non" lorsqu'on lui demande de choisir une ligne ou une colone
            if line.upper() == "NO" or column.upper() == "NO":
                #Alors on quitte le programme
                print("ok................................")
                exit()
            
            # line et column deviennent des entier
            line = int(line)
            column = int(column)
            
            #Si la ligne ou la colone ne sont pas presente dans le tableau
            if line > 2 or line < 0 or column < 0 or column > 2:
                print("This does not correspond to any of the coordinates.")
            #S'il y a déjà un symbole sur le couple ligne colone choisi
            elif tab[line][column] == "⭘" or tab[line][column] == "✖":
                print("This coordinates are already taken")
            #Sinon on rajoute le symbole au tableau, et on passe au tours suivant, celui du CPU
            else:
                tab[line][column] = "✖"
                turn = "⭘"
                nbTurns += 1 
            
            #On verifie si le joueur a gagner grace à la fonction victory_verification
            victory = victory_verification(tab,"✖")
            #S'il a gagner on arrete le jeu
            if victory:
                print_game(tab)
                print("\nPlayer_✖ win !")
                return
            
            #Sinon on affiche l'etat actuel du morpion
            else:
                print_game(tab)
            
            
        #Si c'est au tours de l'ordinateur
        if turn == "⭘":

            #Si le tours est 0, c'est le tout premier tour de la partie donc l'ordinateur commence
            if nbTurns == 0:
                #Alors on se place dans la premiere case
                tab[0][0] = "⭘"
                #On change de tours, on passe au joueur et on affiche le jeu
                nbTurns += 1
                turn = "✖"
                print_game(tab)

            #Si c'est le premier tours du jeu, c'est à dire que le joueur a jouer en premier
            elif nbTurns == 1:
                #Si la case central est vide
                if tab[1][1] == "_":
                    #Alors l'ordinateur joue au milieu, on passe au tours suivant, celui du joueur
                    tab[1][1] = "⭘"
                    turn = "✖"
                    nbTurns += 1
                    print_game(tab)
                
                #Sinon le joueur à jouer sur la case central
                else:
                    #Alors l'ordinateur joue dans l'angle en bas à droite, on passe au tours suivant, celui du joueur
                    tab[2][2] = "⭘"
                    turn = "✖"
                    nbTurns += 1
                    print_game(tab)

            #Si c'est le 2ème ou le 4ème tours de jeux
            elif nbTurns == 2 or nbTurns == 4:
                #On  verifie si le joueur peut gagner grace à la fonction verification_CPU
                verif = CPU_verification(tab,"✖")
                
                #Si c'est vrai
                if verif[0] == True:
                    #Alors, on le bloque
                    tab[verif[1]][verif[2]] = "⭘"
                
                else:
                    #Sinon, si la case 2,2 est vide on se place a cet endroit sinon, on se place dans une autre diagonal
                    if tab[2][2] == "_":
                        tab[2][2] = "⭘"
                    elif tab[0][2] == "_":
                        tab[0][2] = "⭘"
                    elif tab[2][0] == "_":
                        tab[2][0] = "⭘"
                
                #On change de tours, on passe au joueur et on affiche le jeu
                nbTurns += 1
                turn = "✖"
                print_game(tab)
                
            #Si c'est apres le 2éme tours et avant le 9ème et que l'on est pas au 8éme tours
            elif nbTurns >= 3 and nbTurns < 9 and nbTurns != 8:
                #Alors on verifie si l'ordinateur peut gagner grace à la fonction verification_CPU
                verif = CPU_verification(tab,"⭘")
                #S'il c'est faux, donc il ne peut pas gagner
                if verif[0] == False:
                    #Alors on verifie pour le joueur
                    verif = CPU_verification(tab,"✖")
                #S'il y a deux ⭘ ou ✖ et une case vide dans la meme ligne/colone/diago
                if verif[0] == True:
                    #Alors on remplace dans le tableau le couple ligne/colone (donc le couple verif[1]/verif[2]) par un ⭘
                    tab[verif[1]][verif[2]] = "⭘"
                    print_game(tab)
                    turn = "✖"
                    nbTurns += 1
                
                #S'il n'y a pas 2 ✖ ou ⭘ et une case vide dans une ligne/colone/diago
                if verif[0] == False:
                    #On verifie s'il y a une diagonal vide
                    if tab[0][0] == "_":
                        tab[0][0] = "⭘"
                    elif tab[0][2] == "_":
                        tab[0][2] = "⭘"
                    elif tab[2][0] == "_":
                        tab[2][0] = "⭘"
                    elif tab[2][2] == "_":
                        tab[2][2] = "⭘"
                    
                    #Sinon on cherche une case vide pour jouer
                    else:
                        for i in range(len(tab)):
                            for j in range(len(tab)):
                                if tab[i][j] == "_":
                                    tab[i][j] = "⭘"
                                    return
                    #On change de tours, on passe au joueur et on affiche le jeu
                    print_game(tab)
                    turn = "✖"
                    nbTurns += 1
            
            #Si on est au 8ème ou 9ème tours
            elif nbTurns == 9 or nbTurns == 8 :
                #Si le nombre de tours est egale à 8
                if nbTurns == 8:
                    #Chercher la derniere case vide
                    for i in range(len(tab)):
                                for j in range(len(tab)):
                                    #Si la case est vide
                                    if tab[i][j] == "_":
                                        #on la remplace par un ⭘
                                        tab[i][j] = "⭘"
                                    
                print_game(tab)
                #Alors, toute les cases ont été remplis et donc personne n'as gagner
                print("It's a Tie, nobody win")

                # Easter egg pierre feuille ciseau
                print("Do you want a winner ?")
                c = input("")
                if c == "yes":
                    RockPaperScissor()
                return

                        
                    
            #On verifie si l'ordinateur à gagner
            victory = victory_verification(tab,"⭘")
            #S'il a gagner on arrete le jeu
            if victory:
                print_game(tab)
                print("\nCPU win !")
                return




#Initialiser la variable choix
gameChoice = ""

 #Tant que le choix est different de 3
while gameChoice != "3":

    #On affiche les choix possible pour le joueur
    print("Play TicTacToe")
    print("1: Play Player versus Player")
    print("2: Play Player versus CPU")
    print("3: Stop playing")
    #Le joueur saisi sont choix dans la variable choix
    gameChoice = input("")

    #Si le choix est 1
    if gameChoice == "1":
        #Alors lancer la fonction morpion_PVP()
        TicTacToe_PVP()

    elif gameChoice == "2":
        TicTacToe_PVC()

print("See you next time !")