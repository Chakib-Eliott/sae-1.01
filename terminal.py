"""
VERSION TERMINAL

AUTEURS : Eliott & Chakib
"""

import diamants as D  # Les fonction qui permettent de faire fonctionner le jeu
import os
import time

print("INITIALISATION DE LA PARTIE ...")
print()

inputNombreJoueurs = 5
while inputNombreJoueurs < 2 or inputNombreJoueurs > 8:
    try:
        inputNombreJoueurs = int(input("Choisir le nombre de joueurs (2 à 8) : "))
    except ValueError:
        print("Entrez un entier !")


def clear():
    try: 
        os.system('clear')
    except:
        print()

clear()
print("BON JEU !")
print()

Jeu = D.Diamant(inputNombreJoueurs, 0) # Création de la partie
Jeu.melangeCarte()


def affichageCourant(instruction = ''):
    print("INSTRUCTION :", instruction)
    print()
    print("Manche :", 6-Jeu.manchesRestants)

    print()
    print('Contenu du tapis :')
    for i in Jeu.tapis.items():
        if i[1] <= 0:
            print(i[0])
        else:
            print(i[0], ':', i[1])
            
    print("\n"*2)

def pioche():
    carte = Jeu.piocheCarte()
        
for i in range(1):
    Jeu.piocheCarte()
    sortis = []
    for i in Jeu.joueurs.items():
        clear()
        affichageCourant("Choix des joueurs...")
        if i[1][2] == 0:
            print("Tour du joueur :", i[0])
            caras = Jeu.caracteristiquesJoueur(i[0])
            print("Diamants en votre possession :", caras[0])
            print("Relique(s) en votre possession :", caras[1])
            print('\n'*2)
            print("Joueur", i[0], ": que souhaitez vous faire ?")
            choix = str(input("rester, sortir"))
            while choix != 'rester' and choix != 'sortir':
                choix = str(input("rester, sortir"))
            if choix == 'sortir':
                Jeu.jouer(1, i[0])
                time.sleep(0.7)
                print()
                print("Vous avez choisi de quitter ce tour !")
                sortis.append(i[0])
            else:
                time.sleep(0.7)
                print()
                print("Vous avez choisi de rester dans le jeu !")
            time.sleep(0.5)
    print(sortis)
    Jeu.sortie(sortis)


"""
INSTRUCTION ex : Carte 15 sortie, chaque joueur recoit x diamants

MANCHE : 1
TAPIS : [25]  [3]  [Chauve-souris] 

JOUEURS : [1,"Explore"] [2,"Sort"] [3,"Est sortie"]

TOUR :

NB DIAMANTS PERSO :

RELIQUE(S) :

CHOIX :

"""

