from random import*
from pierreFeuilleCiseau import *
from TicTacToe_CPU import *

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

#On crée une fonction ticTacToe
def TicTacToe_PVP() :
    #Initialisation du tableau de morpion
    tab=[["_","_","_"],["_","_","_"],["_","_","_"]]
    print_game(tab)

    #Initialisation des vartiable turn et who a 0
    turn=0
    who=0

    #On crée la liste player qui prendra en compte les 2 joueurs du morpion
    player = []
    #On affiche quel joueur commence
    print("\nRemember that player 1 starts")
    #On demande le nom du joueur 1
    player.append (input("Who is player 1 ? "))
    #On demande le nom du joueur 2
    player.append (input("\nWho is player 2 ? "))
    print("\n")
    #On affiche qui de quel joueur commençera
    print("Now\033[1;31;40m", player[0], "\033[1;37;40mwill start and\033[1;31;40m", player[1], "\033[1;37;40mwill play second !")
    print("Good luck !\n\n\n\n\n")

    #On appel la fonction player_choice qui va gérer le fonctionnement du jeu
    player_choice(player, who, tab, turn)
    #On termine la fonction
    return

#On crée la fonction player_choice qui prend comme argument player, who et case
def player_choice(player, who, tab, turn):
    #Initialisation de la variable symbol
    symbol=["✖","⭘"]

    #On appel la fonction printer
    print_game(tab)

    #On affiche le joueur dont c'est le tour
    print("It's\033[1;31;40m", player[who], "\033[1;37;40m's turn !")
    #On demande au joueur son choix de case dans la variable choice à l'aide de la fonction input
    line = input("Chose a line: ")
    column = input("Chose a column: ")
    case = (line,column)

    #Si le joueur repond "non" lorsqu'on lui demande de choisir une ligne ou une colone
    if line.upper() == "NO" or column.upper() == "NO":
        #Alors on quitte le programme
        print("ok................................")
        exit()

    #Tant que le choix du joueur est différent d'une des cases du morpion ou que la case est déjà pleine
    while case != ("0","0") and case != ("0","1") and case != ("0","2") and case != ("1","0") and case != ("1","1") and case != ("1","2") and case != ("2","0") and case != ("2","1") and case != ("2","2") or (tab[int(line)][int(column)] == symbol[0] or tab[int(line)][int(column)] == symbol[1]):
        #On appel la fonction printer
        print_game(tab)
        #On affiche le joueur dont c'est le tour
        print("It's\033[1;31;40m", player[who], "\033[1;37;40m's turn !")
        #On redemande au joueur son choix de case dans la variable choice à l'aide de la fonction input avec un message d'erreur
        line = input("This does not correspond to any of the coordinates. Chose a line again : ")
        column = input("Chose a column again : ")
        case = (line,column)

    #On change la case correspondante au choix du joueur avec le symbole assigné à ce joueur
    tab[int(line)][int(column)] = symbol[who]
    #Incrémenter 1 à turn
    turn += 1
    #Si la fonction didWin est vraie
    if didWin(player, who, tab, symbol, turn) :
        #Alors retourner la fonction
        return

    #Sinon
    else :
        #Si le joueur est le joueur 1
        if who == 1 :
            #Alors soustraire 1 à la variable who
            who -= 1
        #Sinon
        else :
            #Alors ajouter 1 à la variable who
            who += 1

        #Appeler la fonction player_choice
        player_choice(player, who, tab, turn)

#On crée la fonction didWin qui prend comme paramètres player, who, case et symbol
def didWin(player, who, tab, symbol, turn) :
    
    #On crée le booléen a par défaut sur False
    a = False

    #On vérifie les 3 lignes, si l'une d'entre elles possède le même symbole 3 fois
    #Alors mettre a sur True
    if tab[0][0] == symbol[who] and tab[0][1] == symbol[who] and tab[0][2] == symbol[who] :
        a = True
    elif tab[1][0] == symbol[who] and tab[1][1] == symbol[who] and tab[1][2] == symbol[who] :
        a = True
    elif tab[2][0] == symbol[who] and tab[2][1] == symbol[who] and tab[2][2] == symbol[who] :
        a = True

    #On vérifie les 3 colonnes, si l'une d'entre elles possède le même symbole 3 fois
    #Alors mettre a sur True
    elif tab[0][0] == symbol[who] and tab[1][0] == symbol[who] and tab[2][0] == symbol[who] :
        a = True
    elif tab[0][1] == symbol[who] and tab[1][1] == symbol[who] and tab[2][1] == symbol[who] :
        a = True
    elif tab[0][2] == symbol[who] and tab[1][2] == symbol[who] and tab[2][2] == symbol[who] :
        a = True

    #On vérifie les 2 diagonales, si l'une d'entre elles possède le même symbole 3 fois
    #Alors mettre a sur True
    elif tab[0][0] == symbol[who] and tab[1][1] == symbol[who] and tab[2][2] == symbol[who] :
        a = True
    elif tab[0][2] == symbol[who] and tab[1][1] == symbol[who] and tab[2][0] == symbol[who] :
        a = True
    #Sinon si le tour est le neuvième
    #Alors mettre a sur True
    elif turn == 9 :
        a = True

    #Si a est sur True et que le tour est le neuvième
    if a and turn == 9:
        #Alors appeler la fonction printer
        print_game(tab)
        #Afficher le message d'égalité
        print("It's over ! It's a tie !")
        return True
    #Sinon si a est sur True
    elif a :
        #Alors appeler la fonction printer
        print_game(tab)
        #Afficher le gagnant de la partie
        print("It's over !\033[1;31;40m", player[who], "\033[1;37;40mwon the game !\n\n\n")
        return True


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