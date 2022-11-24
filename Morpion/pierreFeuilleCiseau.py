#DEBUT
from random import *

#Definir une fonction pierreFeuilleCiseau
def RockPaperScissor():
    #Afficher les choix possible 1(Pierre), 2(Feuille), 3(Ciseau)
    print("Chose a number, 1 for Rock, 2 for Scissor, 3 for Paper")
    #Assigner a choixJoueur le choix du joueur grace à la fonction input
    choixJoueur = int(input(""))
    #Assigner a choixOrdi le retour de la fonction Random
    choixOrdi = randint(1,3)

    if choixJoueur == choixOrdi:
        #Alors afficher "Egalité"
        print("\nIt's a tie... Again\n")
        print("¯\_(ツ)_/\n")
       
    #Si choixJoueur est 1 et choixOrdi est 2
    elif choixJoueur == 1 and choixOrdi == 2:
        #Alors afficher choixJoueur et choixOrdi
        print("\nRock vs Paper")
        #Afficher "Défaite du Joueur"
        print("Player lose")

    #Sinon si choixJoueur est 1 et choixOrdi est 3
    elif choixJoueur == 1 and choixOrdi == 3:
        #Alors afficher choixJoueur et choixOrdi
        print("\nRock vs Scissor")
        #Afficher "Victoire du Joueur"
        print("Player win")

    #Sinon si choixJoueur est 2 et choixOrdi est 1
    elif choixJoueur == 2 and choixOrdi == 1:
        #Alors afficher choixJoueur et choixOrdi
        print("\nPaper vs Rock")
        #Afficher "Victoire du Joueur"
        print("Player win")

    #Sinon si choixJoueur est 2 et choixOrdi est 3
    elif choixJoueur == 2 and choixOrdi ==3:
        #Alors afficher choixJoueur et choixOrdi
        print("\nPaper vs Scissor")
        #Afficher "Défaite du Joueur"
        print("Player lose")
        
    #Sinon si choixJoueur est 3 et choixOrdi est 1
    elif choixJoueur == 3 and choixOrdi == 2:
        #Alors afficher choixJoueur et choixOrdi
        print("\nScissor vs Paper")
        #Afficher "Victoire du Joueur"
        print("Player win")


    #Sinon si choixJoueur est 3 et choixOrdi est 2
    elif choixJoueur == 3 and choixOrdi == 1:
        #Alors afficher choixJoueur et choixOrdi
        print("\nScissor vs Rock")
        #Afficher "Défaite du Joueur"
        print("Player lose")

    else:
        print("Wrong choice, chose the number 1,2 or 3")


#FIN
