"""
VERSION TERMINAL

AUTEURS : Eliott & Chakib

Ce jeu est développé dans le cadre d'une SAé (un projet) avec l'IUT de Vélizy.
"""

import diamants as D  # Les fonction qui permettent de faire fonctionner le jeu
import os  # Natif à Python
import time  # Natif à Python
from random import randint  # Natif à Python

# Configuration des couleurs de terminal
G = '\033[92m'  # vert
Y = '\033[93m'  # jaune
R = '\033[91m'  # rouge
N = '\033[0m'  # gris, couleur normale

print(f"{R}INITIALISATION DE LA PARTIE ...")
print()

# Initialisation du nombre de joueurs (Entre 3 et 8 joueurs).
inputNombreJoueurs = 0
while inputNombreJoueurs not in list(range(3,9)):  # Bloque le choix du joueur jusqu'à que le nombre rentré soit correct.
    try:
        inputNombreJoueurs = int(input(f"{G}Choisir le nombre de joueurs (3 à 8) : "))
    except ValueError:
        print("Entrez un entier !")

# Choix entre joueur et bot (0: bot, 1: joueur).
choixJB = -1
while choixJB not in list(range(2)):  # Bloque le choix du joueur jusqu'à que le nombre rentré soit correct.
    try:
        choixJB = int(input("Choisir le mode de jeu (0 = bot, 1 = joueur) : "))
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


clear()
print(f"{R}BON JEU !{N}")
time.sleep(1)

Jeu = D.Diamant(inputNombreJoueurs, 0) # Création de la partie
Jeu.melangeCarte()


def affichageCourant(instruction = '') -> None:
    """
    Affichage du plateau de jeu.

    Args:
        instruction (str): Instruction du jeu.
    """
    print(f"{R}INSTRUCTION : {Y}{instruction}")
    print()
    print(f"{R}Manche : {Y}{6-Jeu.manchesRestants}/5")
    print()
    print(f'{R}Contenu du tapis :{Y}')
    for i in Jeu.tapis:
        if i[1] <= 0:  # Affichage juste du nom de monstre.
            print(i[0])
        else:  # Affichage de la carte trésor et de son reste de diamant.
            print(i[0], ':', i[1])  
    print(f"{N}\n"*2)


# Boucle du jeu.
while Jeu.manchesRestants > 0:
    if Jeu.joueursRestants == 0:
        Jeu.changementManche()
    elif Jeu.piocheCarte() != True:  # Vérifie que ce n'est pas la fin de la manche.
        sortis = []  # Liste des joueurs sorties
        for i in Jeu.joueurs.items():
            clear()
            time.sleep(0.5)
            affichageCourant("Choix des joueurs...")
            if i[1][2]==0:  # Vérifie si le joueur est toujours en jeu.
                # Vérifie qu'on joue sans bot ou que c'est le joueur 1 soit nous.
                if choixJB==1 or i[0]==1:
                    print(f"{R}Tour du joueur :{Y} {i[0]}")  # i[0] = joueur jouant
                    caras = Jeu.caracteristiquesJoueur(i[0])
                    print(f"{R}Diamants en votre possession :{Y} {caras[3]}")  # Nombre de diamants pendant l'expédition
                    print(f"{R}Relique(s) en votre possession :{Y} {caras[1]}")
                    print(f"{R}Nombre de diamants dans votre coffre :{Y} {caras[0]}")  # Nombre de diamants dans le coffre
                    print('\n'*2)
                    print(f"{R}Joueur {i[0]} :{Y} que souhaitez vous faire ?{N}")
                    choix = str(input("rester, sortir\n >> ")) 
                    # Boucle sur le choix du joueur jusqu'à qu'il soit valide.
                    while choix != 'rester' and choix != 'sortir' and choix != 's' and choix != 'r':
                        choix = str(input("rester, sortir\n >> "))
                    if choix == 'sortir' or choix == 's':
                        Jeu.jouer(i[0],1)
                        print()
                        print(f"{G}Vous avez choisi de quitter ce tour !{N}")
                        sortis.append(i[0])  # Ajout du joueur dans la liste des joueurs sorties.
                    else:
                        # Aucune intéraction nécessaire, le jeu continue pour ces joueurs.
                        print()
                        print(f"{G}Vous avez choisi de rester dans le jeu !{N}")
                    time.sleep(1)
                elif choixJB == 0:  # Vérifie si il faut faire jouer les bots.
                    print(f"{R}Tour du joueur :{Y}", i[0])  # i[0] = joueur jouant
                    caras1 = Jeu.caracteristiquesJoueur(i[0])
                    print(f"{R}Diamants en sa possession :{Y} {caras1[3]}")  # Nombre de diamants pendant l'expédition
                    print(f"{R}Relique en sa possession :{Y} {caras1[1]}")  # Nombre de relique pendant l'expédition
                    caras = Jeu.caracteristiquesJoueur(1)
                    print(f"{R}Diamants en votre possession :{Y} {caras[3]}")  # Nombre de diamants pendant l'expédition
                    print(f"{R}Relique(s) en votre possession :{Y} {caras[1]}")
                    print(f"{R}Nombre de diamants dans votre coffre :{Y} {caras[0]}")  # Nombre de diamants dans le coffre
                    print('\n'*2)
                    choix = randint(0,1)  # Choisi entre sortir et rester de façon aléatoire.
                    if choix == 1:
                        Jeu.jouer(i[0],1)
                        print()
                        print(f"{G}Le joueur {i[0]} a décidé de quitter ce tour !{N}")
                        sortis.append(i[0])  # Ajout du joueur dans la liste des joueurs sorties.
                    else:
                        # Aucune intéraction nécessaire, le jeu continue pour ces joueurs.
                        print()
                        print(f"{G}Le joueur {i[0]} a décidé de rester dans le jeu !{N}")
                    time.sleep(3)
        Jeu.sortie(sortis)  # Vérifie que la manche n'est pas fini et réparti le trésor aux joueurs sorties.
    else:
        print(f"{R}Un obstacle surgit ! Les joueurs restants dans la grotte fuit ! (L'obstacle était {Jeu.tapis[-1][0]}){N}")
        time.sleep(5)
        Jeu.changementManche()

clear()
print(f"{R}Fin de la partie.\nLe classement est :{Y}")
for i in Jeu.classement():
    print('Joueur',i[0],'avec',i[1],'diamants')
