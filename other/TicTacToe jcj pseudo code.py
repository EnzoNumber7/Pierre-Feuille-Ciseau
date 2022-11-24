#DEBUT
#On admet une fonction Random qui choisi un element aleatoire d'une liste

#Definir la fonction affichage_morpion qui permet d'afficher le jeux, qui prend en parametre le tableau de jeu
    #Afficher le numero des colone
        #Afficher le numero des lignes
        #Afficher le contenue de chaque case ainsi que les séparation

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

#Definir la fonction morpion_PVP, qui permet de faire une partie de morpion contre un autre joueur
    #Initialisation du tableau de morpion
    #Afficher le tableau grace à la fonction affichage_morpion

    #Initialiser la variable victoire à Faux

    #Initialiser la variable tours qui determine qui commence entre le joueur_⭘ et le joueur_✖ aleatoirement grace a la fonction random
    #Initialiser la variable nbTours qui compte les tours a 0
    
    #Tant que victoire est faut, donc que personne n'as gagner

        #Si c'est au tours du joueur_✖
            #Demande au joueur de choisir une ligne
            #Demande au joueur de choisir une colone
            #Si la ligne ou la colone ne sont pas presente dans le tableau
                #Afficher un  message d'erreur
            #Sinon, s'il y a déjà un symbole sur le couple ligne colone choisi
                #Afficher un message d'erreur
            #Sinon 
                #Rajouter le symbole au tableau, et on passe au tours du joueur suivant et on incremente nbTours de 1
            
            #On verifie si le joueur a gagner grâce à la fonction verification_victoire

            #S'il a gagner on arrete le jeu, donc si verification victoire est vrai
                #Afficher le tableau grace à la fonction affichage_morpion
                #Afficher un message de victoire
                #Retourner rien, pour arreter la fonction
            
            #Sinon, s'il y a eu 9 tours
                #Afficher le tableau grace à la fonction affichage_morpion
                #Afficher un message d'egalite, car au bout de 9 tours toute les case on ete remplis
                #Retourner rien, pour arreter la fonction

            #Sinon, afficher le tableau grace à la fonction affichage_morpion
        
        
        #Si c'est au tours du joueur_⭘
            #Demande au joueur de choisir une ligne

            #Demande au joueur de choisir une colone

            #Si la ligne ou la colone ne sont pas presente dans le tableau
                #Afficher un message d'erreur
            #S'il y a déjà un symbole sur le couple ligne colone choisi
                #Affciher un message d'erreur
            
            #Sinon, 
                #Rajouter le symbole au tableau, on passe au tours du joueur suivant et on incremente nbTours de 1
            
            #On verifie si le joueur a gagner grâce à la fonction verification_victoire
            
            #S'il a gagner on arrete le jeu
                #Afficher le tableau grace à la fonction affichage_morpion
                #Afficher un message de victoire
                #Retourner rien, pour arreter la fonction
            
            #Sinon, s'il y a eu 9 tours
                #Afficher le tableau grace à la fonction affichage_morpion
                #Afficher un message d'egalite, car au bout de 9 tours toute les case on ete remplis
                #Retourner rien, pour arreter la fonction

            #Sinon, afficher le tableau grace à la fonction affichage_morpion


#Initialiser la variable choix à ""

 #Tant que le choix est different de 2

    #On affiche les choix possible pour le joueur (1 pour jouer contre un joueur et 2 pour arreter de jouer)

    #Le joueur saisi sont choix dans la variable choix

    #Si le choix est 1
        #Alors lancer la fonction morpion_PVP

#Afficher le message à bientot

#FIN