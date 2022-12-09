"""
VERSION TERMINAL

AUTEURS : Eliott & Chakib

Ce jeu est développé dans le cadre d'une SAé (un projet) avec l'IUT de Vélizy.
"""

import diamants as D  # Les fonction qui permettent de faire fonctionner le jeu
import os  # Natif à Python
import time  # Natif à Python

print("INITIALISATION DE LA PARTIE ...")
print()

# Initialisation du nombre de joueurs (Entre 3 et 8 joueurs).
inputNombreJoueurs = 3
while inputNombreJoueurs not in list(range(3,9)):  # Bloque le choix du joueur jusqu'à que le nombre rentré soit correct.
    try:
        print("RAPPEL : Le jeu se joue de 3 à 8 joueurs.")
        inputNombreJoueurs = int(input("Choisir le nombre de joueurs (3 à 8) : "))
    except ValueError:
        print("Entrez un entier !")


def clear() -> None:
    """
    Nettoie le terminal Windows avec la commande 'cls'
    ou le terminal Linux et MacOS avec la commande 'clear'.
    """
    try: 
        if os.name == 'nt': os.system('cls')
        else: os.system('clear')
    except:
        print()
    # print('##############################')


clear()
print("BON JEU !")
print()

Jeu = D.Diamant(inputNombreJoueurs, 0) # Création de la partie
Jeu.melangeCarte()


def affichageCourant(instruction = '') -> None:
    """
    Affichage du plateau de jeu.

    Args:
        instruction (str): Instruction du jeu.
    """
    print("INSTRUCTION :", instruction)
    print()
    print("Manche :", 6-Jeu.manchesRestants)
    print()
    print('Contenu du tapis :')
    for i in Jeu.tapis:
        if i[1] <= 0:  # Affichage juste du nom de monstre.
            print(i[0])
        else:  # Affichage de la carte trésor et de son reste de diamant.
            print(i[0], ':', i[1])
            
    print("\n"*2)


# Boucle du jeu
while Jeu.manchesRestants > 0:
    if Jeu.joueursRestants == 0:
        Jeu.changementManche()
    elif Jeu.piocheCarte() != True:  # Vérifie que ce n'est pas la fin de la manche.
        sortis = []  # Liste des joueurs sorties
        for i in Jeu.joueurs.items():
            clear()
            affichageCourant("Choix des joueurs...")
            if i[1][2] == 0:  # Si le joueur n'est pas sortie.
                print("Tour du joueur :", i[0])  # i[0] = joueur jouant
                caras = Jeu.caracteristiquesJoueur(i[0])
                print("Diamants en votre possession :", caras[3])  # Nombre de diamants pendant l'expédition
                print("Relique(s) en votre possession :", caras[1])
                print("Nombre de diamants dans votre coffre :", caras[0])  # Nombre de diamants dans le coffre
                print('\n'*2)
                print("Joueur", i[0], ": que souhaitez vous faire ?")
                choix = str(input("rester, sortir\n >> ")) 
                # Boucle sur le choix du joueur jusqu'à qu'il soit valide.
                while choix != 'rester' and choix != 'sortir' and choix != 's' and choix != 'r':
                    choix = str(input("rester, sortir\n >> "))
                if choix == 'sortir' or choix == 's':
                    Jeu.jouer(i[0],1)
                    time.sleep(0.1)
                    print()
                    print("Vous avez choisi de quitter ce tour !")
                    sortis.append(i[0])  # Ajout du joueur dans la liste des joueurs sorties.
                else:
                    # Aucune intéraction nécessaire, le jeu continue pour ces joueurs.
                    time.sleep(0.1)
                    print()
                    print("Vous avez choisi de rester dans le jeu !")
                time.sleep(0.1)
        Jeu.sortie(sortis)  # Vérifie que la manche n'est pas fini et réparti le trésor aux joueurs sorties.
        print(Jeu.tapis)
    else:
        print("VOUS ETES MORT", Jeu.tapis[-1][0])
        Jeu.changementManche()

clear()
print("Le classement est :")
for i in Jeu.classement():
    print('Joueur',i[0],'avec',i[1],'diamants')

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

