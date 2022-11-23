#DEBUT
from random import *

#Definir une fonction pierreFeuilleCiseau
def pierreFeuilleCiseau():
    #Afficher les choix possible 1(Pierre), 2(Feuille), 3(Ciseau)
    print("Choisissez un chiffre: 1 pour Pierre, 2 pour Feuille, 3 pour Ciseau")
    #Assigner a choixJoueur le choix du joueur grace à la fonction input
    choixJoueur = int(input(""))
    #Assigner a choixOrdi le retour de la fonction Random
    choixOrdi = randint(1,3)

    #Initialiser une variable nombreVictoire à 0
    nombreVictoire = 0
    #Initialiser une variable nombreDefaite à 0
    nombreDefaite = 0
    #Initialiser une variable nombreEgalite à 0
    nombreEgalite = 0
    #Initialiser une variable nombrePartie à 0
    nombrePartie = 0
    #Initialiser une variable continuerPartie à True
    continuerPartie = True

    #Tant que continuerPartie est True
    while continuerPartie:
       
        #Alors si choixJoueur est égal à choixOrdi
        if choixJoueur == choixOrdi:
            #Alors afficher "Egalité"
            print("\nIl y a Egalité")
            #Incrementer la variable nombreEgalite de 1
            nombreEgalite += 1
            #Incrementer la variable nombrePartie de 1
            nombrePartie += 1
        
        #Si choixJoueur est 1 et choixOrdi est 2
        elif choixJoueur == 1 and choixOrdi == 2:
            #Alors afficher choixJoueur et choixOrdi
            print("\nPierre Contre Feuille")
            #Afficher "Défaite du Joueur"
            print("Défaiter du joueur")
            #Incrementer la variable nombreDefaite de 1
            nombreDefaite += 1
            #Incrementer la variable nombrePartie de 1
            nombrePartie += 1

        #Sinon si choixJoueur est 1 et choixOrdi est 3
        elif choixJoueur == 1 and choixOrdi == 3:
            #Alors afficher choixJoueur et choixOrdi
            print("\nPierre Contre Ciseau")
            #Afficher "Victoire du Joueur"
            print("Victoire du Joueur")
            #Incrementer la variable nombreVictoire de 1
            nombreVictoire += 1
            #Incrementer la variable nombrePartie de 1
            nombrePartie += 1

        #Sinon si choixJoueur est 2 et choixOrdi est 1
        elif choixJoueur == 2 and choixOrdi == 1:
            #Alors afficher choixJoueur et choixOrdi
            print("\nFeuille Contre Pierre")
            #Afficher "Victoire du Joueur"
            print("Victoire Joueur")
            #Incrementer la variable nombreVictoire de 1
            nombreVictoire += 1
            #Incrementer la variable nombrePartie de 1
            nombrePartie += 1

        #Sinon si choixJoueur est 2 et choixOrdi est 3
        elif choixJoueur == 2 and choixOrdi ==3:
            #Alors afficher choixJoueur et choixOrdi
            print("\nFeuille Contre Ciseau")
            #Afficher "Défaite du Joueur"
            print("Défaite du joueur")
            #Incrementer la variable nombreDefaite de 1
            nombreDefaite += 1
            #Incrementer la variable nombrePartie de 1
            nombrePartie += 1
        
        #Sinon si choixJoueur est 3 et choixOrdi est 1
        elif choixJoueur == 3 and choixOrdi == 2:
            #Alors afficher choixJoueur et choixOrdi
            print("\nCiseau Contre Feuille")
            #Afficher "Victoire du Joueur"
            print("Victoire du joueur")
            #Incrementer la variable nombreVictoire de 1
            nombreVictoire += 1
            #Incrementer la variable nombrePartie de 1
            nombrePartie += 1

        #Sinon si choixJoueur est 3 et choixOrdi est 2
        elif choixJoueur == 3 and choixOrdi == 1:
            #Alors afficher choixJoueur et choixOrdi
            print("\nCiseau Contre Pierre")
            #Afficher "Défaite du Joueur"
            print("Défaite du joueur")
            #Incrementer la variable nombreDefaite de 1
            nombreDefaite += 1
            #Incrementer la variable nombrePartie de 1
            nombrePartie += 1

        else:
            print("Erreur, vous n'avez pas rentrez un choix valide")

        
        #Assigner a continuer le retour de l'execution de la fonction input
        print("\nVoulez-vous refaire une partie ?")
        continuer = input("")
        #Si la reponse est non
        if continuer.upper() == "NON":
            #Alors changer la variable continuerPartie à False
            continuerPartie =False
        #Sinon 
        else:
            #Afficher "Votre nombre de partie est:" nombrePartie
            print("\nVotre nombre de partie est:", nombrePartie)
            #Afficher "Votre nombre de victoire est:" nombreVictoire
            print("Votre nombre de victoire est:", nombreVictoire)
            #Afficher "Votre nombre de Defaite est:" nombreDefaite
            print("Votre nombre de Defaite est:", nombreDefaite)
            #Afficher "Votre nombre d'Egalité est:" nombreEgalite
            print("Votre nombre d'Egalité est:", nombreEgalite)
            #Afficher les choix possible 1(Pierre), 2(Feuille), 3(Ciseau)
            print("\nChoisissez un chiffre: 1 pour Pierre, 2 pour Feuille, 3 pour Ciseau")
            #Assigner a choixJoueur le choix du joueur grace à la fonction input
            choixJoueur = int(input(""))
            #Assigner a choixOrdi le retour de la fonction Random
            choixOrdi = randint(1,3)
            print(choixOrdi)

    
    #Afficher "Votre nombre de partie est:" nombrePartie
    print("Votre nombre de partie est:", nombrePartie)
    #Afficher "Votre nombre de victoire est:" nombreVictoire
    print("Votre nombre de victoire est:", nombreVictoire)
    #Afficher "Votre nombre de Defaite est:" nombreDefaite
    print("Votre nombre de Defaite est:", nombreDefaite)
    #Afficher "Votre nombre d'Egalité est:" nombreEgalite
    print("Votre nombre d'Egalité est:", nombreEgalite)

#FIN
