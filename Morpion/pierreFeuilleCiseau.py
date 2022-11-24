#DEBUT
from random import *

#Definir une fonction pierreFeuilleCiseau
def pierreFeuilleCiseau():
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
        print("Mais ce n'est pas grave car vous savez, moi je ne crois pas qu’il y ait de bonne ou de mauvaise situation. Moi, si je devais résumer ma vie aujourd’hui avec vous, je dirais que c’est d’abord des rencontres, des gens qui m’ont tendu la main, peut-être à un moment où je ne pouvais pas, où j’étais seul chez moi. Et c’est assez curieux de se dire que les hasards, les rencontres forgent une destinée… Parce que quand on a le goût de la chose, quand on a le goût de la chose bien faite, le beau geste, parfois on ne trouve pas l’interlocuteur en face, je dirais, le miroir qui vous aide à avancer. Alors ce n’est pas mon cas, comme je le disais là, puisque moi au contraire, j’ai pu ; et je dis merci à la vie, je lui dis merci, je chante la vie, je danse la vie… Je ne suis qu’amour ! Et finalement, quand beaucoup de gens aujourd’hui me disent : « Mais comment fais-tu pour avoir cette humanité ? » Eh bien je leur réponds très simplement, je leur dis que c’est ce goût de l’amour, ce goût donc qui m’a poussé aujourd’hui à entreprendre une construction mécanique, mais demain, qui sait, peut-être simplement à me mettre au service de la communauté, à faire le don, le don de soi…")
        
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
