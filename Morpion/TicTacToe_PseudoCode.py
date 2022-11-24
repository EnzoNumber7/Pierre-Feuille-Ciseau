#DEBUT
#On admet une fonction choice qui choisi un element aleatoire d'une liste
#On admet une fonction RockPaperScissor qui permet de lancer une partie de pierre feuille ciseau

#Definir la fonction affichage_morpion qui permet d'afficher le jeux, qui prend en parametre le tableau de jeu
    #Afficher le numero des colone
        #Afficher le numero des lignes
        #Afficher le contenue de chaque case ainsi que les séparation




#On crée une fonction ticTacToe
    #Initialisation de la variable symbol
    # Création du tableau de morpion

    #On crée la liste player qui prendra en compte les 2 joueurs du morpion
    #On affiche quel joueur commence
    #On demande le nom du joueur 1
    #On demande le nom du joueur 2
    #On affiche qui de quel joueur commençera

    #Initialisation des vartiable turn et who a 0

    #On appel la fonction player_choice qui va gérer le fonctionnement du jeu
    #On termine la fonction




#On crée la fonction player_choice qui prendra les valeurs player, who tab et turn

    #On appel la fonction print_game

    #On affiche le joueur dont c'est le tour
    #On associe le choix de ligne du joueur dans la fonction line
    #On associe le choix de colone du joueur dans la fonction column

    #On crée un tuple line,column associer a une variable case

    #Si le joueur repond "non" lorsqu'on lui demande de choisir une ligne ou une colone
                #Alors on quitte le programme

    #Tant que le choix du joueur est différent d'une des cases du morpion ou que la case est déjà pleine
        #On appel la fonction print_game
        #On affiche le joueur dont c'est le tour
        #On redemande au joueur son choix de ligne dans la variable line et de colone dans la variable column à l'aide de la fonction input avec un message d'erreur

    #On change la case correspondante au choix du joueur avec le symbole assigné à ce joueur
    #Incrémenter 1 à turn
    #Si la fonction didWin est vraie
        #Alors retourner la fonction

    #Sinon
        #Si le joueur est le joueur 1
            #Alors soustraire 1 à la variable who
        #Sinon
            #Alors ajouter 1 à la variable who

        #Appeler la fonction player_choice




#On crée la fonction didWin qui prend comme paramètres player, who, tab, symbol et turn
    
    #On crée le booléen a par défaut sur False

    #On vérifie les 3 lignes, si l'une d'entre elles possède le même symbole 3 fois
    #Alors mettre a sur True

    #On vérifie les 3 colonnes, si l'une d'entre elles possède le même symbole 3 fois
    #Alors mettre a sur True

    #On vérifie les 2 diagonales, si l'une d'entre elles possède le même symbole 3 fois
    #Alors mettre a sur True

    #Sinon si le tour est le neuvième
        #Alors mettre a sur True

    #Si a est Vrai et que le tour est le neuvième
        #Alors appeler la fonction print_game
        #Afficher le message d'égalité
        
        #Demander si le joueur veut un gagnant
        #Si oui
            #Lancer la fonction RockPaperScissor()
            #Retourner rien pour que la fonction s'arrete
        #Retourner Vrai

    #Sinon si a est Vrai
        #Alors appeler la fonction print_game
        #Afficher le gagnant de la partie
        #Retourner Vrai




#Definir la fonction verification_victoire qui permet de verifier les condition de victoire du morpion, c'est à dire, 3 fois le meme symbole sur la meme diagonal/ligne/colone, qui prend en parametre le tableau de jeu et le symbole du joueur 
    #Initialiser la variable nbSymbole et col à 0

    #Pour i allant de 0 à la longueur de tab
        #Pour j allant de 0 à la longeur de tab
            #S'il y a le symbole rechercher sur la case de coordonné i,j
                #Alors incrémenter la variable nbSymbole
        
        #S'il y a 3 fois le même symbole sur une ligne
            #Alors retourner Vrai

        #Sinon,
            #Remettre le compteur a 0 car on change de ligne
 

    #Pour i allant de 0 à la longueur de tab
        #Pour j allant de 0 à la longeur de tab
            #S'il y a le symbole rechercher sur la case de coordonné i,j
                #Alors incrémenter la variable nbSymbole
                
        #S'il y a 3 fois le symbole sur une colone
            #Alors retourner Vrai
        #Sinon,
            #Remettre le compteur a 0 car on change de colone

    #Pour i allant de 0 à la longueur de tab
        #S'il y a le symbole rechercher sur la case de coordonné i,j
            #Alors incrémenter la variable nbSymbole
    
    #S'il y a 3 fois le symbole sur la diagonal
        #Alors retourner Vrai
    #Sinon,
        #Remettre le compteur a 0 car on change de diagonal

    #Pour i allant de la longueur de tab jusqu'a -1 en allant de -1 en -1
        #S'il y a le symbole rechercher sur la case de coordonné i,col
            #Alors incrémenter la variable nbSymbole
        #Incrementer la variable col de 1

        #S'il y a 3 fois le symbole sur la diagonal
            #Alors retourner Vrai

    #Sinon, s'il n'y a aucune ligne/colone/diagonal, ou le joueur a 3 fois son symbole, alors renvoyer False




#Definir une fonction verification_CPU qui verifie toute les possibilité de jeux pour que l'ordi puisse réagir
    #Initialiser les variable nbSymbol,nbEmpty,EmptyLine,EmptyColumn et col a 0
    

    #Pour i allant de 0 à la longueur du tableau
        #Pour j allant de 0 à la longueur du tableau
            #Si la case de coordonné i,j est vide
                #Alors incrémenter la variable nbSymbole de 1
            #Sinon si la case de coordonné i,j est vide
                #Alors incrementer la variable nbEmpty de 1
                #Associer les variable EmptyLine,EmptyColumn au coordoner de la case vide (i et j)
        
        #Si nbSymbol = 2 et nbCaseVide = 1
            #Alors, renvoyer Vrai,EmptyLine et EmptyColumn
        #Sinon
            #Remettre les variable nbSymbol,nbEmpty,EmptyLine et EmptyColumn à 0
    
    #Pour i allant de 0 à la longueur du tableau
        #Pour j allant de 0 à la longueur du tableau
            #Si la case de coordonné j,i est egal a Symbol
                #Alors incrémenter la variable nbSymbole de 1
            #Sinon si la case de coordonné j,i est vide
                #Alors incrementer la variable nbEmpty de 1
                #Associer les variable EmptyLine,EmptyColumn au coordoner de la case vide (j et i)
                
        #Si nbSymbol = 2 et nbCaseVide = 1
            #Alors, renvoyer Vrai,EmptyLine et EmptyColumn
        #Sinon
            #Remettre les variable nbSymbol,nbEmpty,EmptyLine et EmptyColumn à 0

    
    #Pour i allant de 0 à la longueur du tableau
        #Si la case de coordonné i,i est egal a Symbol
            #Alors incrémenter la variable nbSymbole de 1
        #Sinon si la case de coordonné i,i est vide
            #Alors incrementer la variable nbEmpty de 1
            #Associer les variable EmptyLine,EmptyColumn au coordoner de la case vide (i et i)
    
        #Si nbSymbol = 2 et nbCaseVide = 1
            #Alors, renvoyer Vrai,EmptyLine et EmptyColumn
        #Sinon
            #Remettre les variable nbSymbol,nbEmpty,EmptyLine et EmptyColumn à 0
    
    #Pour i allant de la longueur du tableau -1 jusqu'a -1 en allant de -1 en -1
        #Si la case de coordonné i,col est egal a Symbol
            #Alors incrémenter la variable nbSymbole de 1
        #Sinon si la case de coordonné i,col est vide
            #Alors incrementer la variable nbEmpty de 1
            #Associer les variable ligneCaseVide et coloneCaseVide au coordoner de la case vide (i et j)
        #Incrementer col de 1

        #Si nbSymbol = 2 et nbCaseVide = 1
            #Alors, renvoyer Vrai,EmptyLine et EmptyColumn
        #Sinon
            #Remettre les variable nbSymbol,nbEmpty,EmptyLine et EmptyColumn à 0


    #S'il y a une ✖ dans la case de coordonnée 0,0 et  1,2
        #Alors si la case de coordonnée 0,2 est vide
            #Alors retourner vrai et les coordoner 0,2
    #Sinon s'il y a le symbole dans la case de coordonnée 0,0 et 2,1
        #Alors si la case de coordonnée 2,0 est vide
            #Alors retourner vrai et les coordoner 2,0
    
    #S'il y a une ✖ dans la case de coordonnée 2,2 et  0,1
        #Alors si la case de coordonnée 0,2 est vide
             #Alors retourner vrai et les coordonée 0,2
    #Sinon s'il y a une ✖ dans la case de coordonnée 2,2 et 1,0
        #Alors si la case de coordonnée 2,0 est vide
            #Alors retourner vrai et les coordonnés 2,0
    
    #S'il y a uen ✖ dans la case de coordonnée 2,0 et  0,2 ou 0,1
          #Alors si la case de coordonnée 0,0 est vide
            #Alors on retourne vrai et les coordonné 0,0
    #Sinon s'il y a une ✖ dans la case de coordonnée 2,0 et 1,2
         #Alors si la case de coordonnée 2,2 est vide
            #Alors on retourne vrai et les coordonnés 2,2
    
    #S'il y a une ✖ dans la case de coordonnée 0,2 et  2,0 ou 1,0
         #Alors si la case de coordonnée 0,0 est vide
            #Alors on retourne vrai et les coordonné 0,0
    #Sinon s'il y a une ✖ dans la case de coordonnée 0,2 et 2,1
         #Alors si la case de coordonnée 2,2 est vide
            #Alors on retourne vrai et les coordonnés 2,2 
    
    #Si la case 0,0 et 2,2 ou 2,0 et 0,2 sont des ✖
        #Alors si la cases 0,1 est vide
            #Alors retourner Vrai,0,1
        #Alors si la cases 1,2 est vide
            #Alors retourner Vrai,1,2
        #Alors si la cases 1,0 est vide
            #Alors retourner Vrai,1,0
        #Alors si la cases 2,1 est vide
            #Alors retourner Vrai,2,1

    #Si aucune des conditions est verifier alors retourner Faux, Vide et Vide




#Definir la fonction TicTacToe_PVC qui permet de faire une partie de morpion contre l'ordinateur
    # Création du tableau de morpion
    #Affichage du tableau grace à la fonction print_game


    #Initialiser la variable victory 

    #Choisir et associer a une variable turn qui commence grace à la fonction choice qui choisi entre "⭘" et "✖"
    #Initialiser la variable nbTurns a 0
    
    #Tant que personne n'as gagner
        #Si c'est au tours du joueur_✖
            #Demande au joueur de choisir une ligne qu'on associe à une variable line
            #Demande au joueur de choisir une colone qu'on associe à une variable column

            #Si le joueur repond "non" lorsqu'on lui demande de choisir une ligne ou une colone
                #Alors on quitte le programme

            
            #line est converti en nombre entier
            #Column est converti en nombre entier

            #Si la ligne ou la colone ne sont pas presente dans le tableau
                #Afficher un message d'erreur

            #S'il y a déjà un symbole sur le couple ligne colone choisi
                #Afficher un message d'erreur
            #Sinon
                #Remplacer la case de coordoner line column par ✖
                #Passer turn à ⭘
                #Ajouter 1 a nbTurn
            
            #Verifier si le joueur a gagner grace à la fonction victory_verification
            #S'il a gagner
                #Afficher le tableau grace a print_game
                #Afficher que le joueur à gagner
                #Retourner rien pour que la fonction s'arrete
            
            #Sinon on affiche le tableau grace a la fonction print_game

            
            
        #Si c'est au tours de l'ordinateur

            #Si le tours est 0, c'est le tout premier tour de la partie donc l'ordinateur commence
                #l'ordinateur joue en 0,0
                #Afficher le tableau
                #Ajouter 1 a nbTurn
                #Passer turn à ✖

            #Si c'est le premier tours du jeu, c'est à dire que le joueur a jouer en premier
                #Si la case central est vide
                    #l'ordinateur joue en 1,1
                    #Afficher le tableau grace a print_game
                    #Ajouter 1 a nbTurn
                    #Passer turn à ✖  
                
                #Sinon
                    #l'ordinateur joue en 2,2
                    #Afficher le tableau grace a print_game
                    #Ajouter 1 a nbTurn
                    #Passer turn à ✖  

            #Si c'est le 2ème ou le 4ème tours de jeux
                #Verifie si le joueur peut gagner grace à la fonction verification_CPU
                
                #Si le retour de la fonction est vrai
                    #Alors, on se place aux coordoné de la case vide renvoyer par cpu_verification
                
                #Sinon
                    #Si la case 2,2 est vide
                        #Placer un ⭘ sur cette case
                    #Si la case 0,2 est vide
                        #Placer un ⭘ sur cette case
                    #Si la case 2,0 est vide
                        #Placer un ⭘ sur cette case

                #Afficher le tableau
                #Ajouter 1 a nbTurn
                #Passer turn à ✖                   
                
            #Si c'est apres le 2éme tours et avant le 9ème et que l'on est pas au 8éme tours
                #Alors on verifie si l'ordinateur peut gagner grace à la fonction verification_CPU
                #S'il c'est faux, donc il ne peut pas gagner
                    #Alors on verifie pour le joueur

                #S'il y a deux ⭘ ou ✖ et une case vide dans la meme ligne/colone/diago
                    #Alors on remplace dans le tableau le couple ligne/colone (donc le couple verif[1]/verif[2])
                    #Afficher le tableau grace a print_game
                    #Ajouter 1 a nbTurn
                    #Passer turn à ✖
                
                #S'il n'y a pas deux ✖ ou deux ⭘ et une case vide dans une ligne/colone/diago
                    #Si la case de coordonner 0,0 est vide
                        #Alors on met un ⭘
                    #Si la case de coordonner 0,2 est vide
                        #Alors on met un ⭘
                    #Si la case de coordonner 2,0 est vide
                        #Alors on met un ⭘
                    #Si la case de coordonner 2,2 est vide
                        #Alors on met un ⭘
                    
                    #Sinon
                        #Pour i allant der 0 à la longueur du tableau
                            #Pour j allant der 0 à la longueur du tableau
                            #Si la case de coordonner i,j est "_", donc si elle est vide
                                    #Alors on place un ⭘
                                    #Retourner rien pour que la fonction s'arrete
                    #On change de tours, on passe au joueur et on affiche le jeu
            
            #Si on est au 8ème ou 9ème tours
                #Si le nombre de tours est egale à 8
                    #Pour i allant der 0 à la longueur du tableau
                        #Pour j allant der 0 à la longueur du tableau
                            #Si la case est vide
                            #on la remplace par un ⭘
                                    
                #Alors, toute les cases ont été remplis et donc personne n'as gagner

                #Demander si le joueur veut un gagnant
                #Si oui
                    #Lancer la fonction RockPaperScissor()
                    #Retourner rien pour que la fonction s'arrete

                        
                    
            #On verifie si l'ordinateur à gagner
            #S'il a gagner
                #Afficher la victoire et arreter le jeu





#Initialiser la variable gameChoixe

 #Tant que gameChoice est different de 3

    #On affiche les choix possible pour le joueur, 1 joueur contre joueur, 2 jouer contre ordinateur et 3 arreter de jouer
    #Le joueur saisi sont choix dans la variable choix

    #Si le choix est 1
        #Alors lancer la fonction TicTacToe_PVP()
    #Sino le choix est 2
        #Alors lancer la fonction TicTacToe_PVC()

#FIN