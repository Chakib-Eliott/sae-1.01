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

print("{r}INITIALISATION DE LA PARTIE ...".format(r=R))
print()

# Initialisation du nombre de joueurs (Entre 3 et 8 joueurs).
inputNombreJoueurs = 0
while inputNombreJoueurs not in list(range(3,9)):  # Bloque le choix du joueur jusqu'à que le nombre rentré soit correct.
    try:
        inputNombreJoueurs = int(input("{g}Choisir le nombre de joueurs (3 à 8) : ".format(g=G)))
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
print("{r}BON JEU !{n}".format(r=R,n=N))
time.sleep(1)

Jeu = D.Diamant(inputNombreJoueurs, 0) # Création de la partie
Jeu.melangeCarte()


def affichageCourant(instruction = '') -> None:
    """
    Affichage du plateau de jeu.

    Args:
        instruction (str): Instruction du jeu.
    """
    print("{r}INSTRUCTION : {y}{i}".format(r=R,y=Y,i=instruction))
    print()
    print("{r}Manche : {y}{m}/5".format(r=R,y=Y,m=6-Jeu.manchesRestants))
    print()
    print('{r}Contenu du tapis :{y}'.format(r=R,y=Y))
    for i in Jeu.tapis:
        if i[1] <= 0:  # Affichage juste du nom de piege.
            print(i[0])
        else:  # Affichage de la carte trésor et de son reste de diamant.
            print(i[0], ':', i[1])  
    print(N,"\n"*2)


# Boucle du jeu.
while Jeu.manchesRestants > 0:
    if Jeu.joueursRestants == 0:
        Jeu.changementManche()
    elif Jeu.piocheCarte() != True:  # Vérifie que ce n'est pas la fin de la manche.
        Jeu.joueurssortis = []  # Liste des joueurs sorties
        for i in Jeu.joueurs.items():
            clear()
            time.sleep(0.5)
            affichageCourant("Choix des joueurs...")
            if i[1][2]==0:  # Vérifie si le joueur est toujours en jeu.
                # Vérifie qu'on joue sans bot ou que c'est le joueur 1 soit nous.
                if choixJB==1 or i[0]==1:
                    print("{r}Tour du joueur :{y} {i}".format(r=R,y=Y,i=i[0]))  # i[0] = joueur jouant
                    caras = Jeu.caracteristiquesJoueur(i[0])
                    print("{r}Diamants en votre possession :{y} {c}".format(r=R,y=Y,c=caras[3]))  # Nombre de diamants pendant l'expédition
                    print("{r}Relique(s) en votre possession :{y} {c}".format(r=R,y=Y,c=caras[1]))
                    print("{r}Nombre de diamants dans votre coffre :{y} {c}".format(r=R,y=Y,c=caras[0]))  # Nombre de diamants dans le coffre
                    print('\n'*2)
                    print("{r}Joueur {i} :{y} que souhaitez vous faire ?{n}".format(r=R,i=i[0],y=Y,n=N))
                    choix = str(input("rester, sortir\n >> ")) 
                    # Boucle sur le choix du joueur jusqu'à qu'il soit valide.
                    while choix != 'rester' and choix != 'sortir' and choix != 's' and choix != 'r':
                        choix = str(input("rester, sortir\n >> "))
                    if choix == 'sortir' or choix == 's':
                        Jeu.jouer(i[0],1)
                        print()
                        print("{g}Vous avez choisi de quitter ce tour !{n}".format(g=G,n=N))
                        Jeu.joueurssortis.append(i[0])  # Ajout du joueur dans la liste des joueurs sorties.
                    else:
                        # Aucune intéraction nécessaire, le jeu continue pour ces joueurs.
                        print()
                        print("{g}Vous avez choisi de rester dans le jeu !{n}".format(g=G,n=N))
                    time.sleep(1)
                elif choixJB == 0:  # Vérifie si il faut faire jouer les bots.
                    print("{r}Tour du joueur :{y} {i}".format(r=R,y=Y,i=i[0]))  # i[0] = joueur jouant
                    caras1 = Jeu.caracteristiquesJoueur(i[0])  # Caractéristique du bot jouant
                    print("{r}Diamants en sa possession :{y} {c}".format(r=R,y=Y,c=caras1[3]))  # Nombre de diamants pendant l'expédition
                    print("{r}Relique en sa possession :{y} {c}".format(r=R,y=Y,c=caras1[1]))  # Nombre de relique pendant l'expédition
                    caras = Jeu.caracteristiquesJoueur(1)  # Caractéristique du joueur
                    print("{r}Diamants en votre possession :{y} {c}".format(r=R,y=Y,c=caras[3]))  # Nombre de diamants pendant l'expédition
                    print("{r}Relique(s) en votre possession :{y} {c}".format(r=R,y=Y,c=caras[1]))
                    print("{r}Nombre de diamants dans votre coffre :{y} {c}".format(r=R,y=Y,c=caras[0]))  # Nombre de diamants dans le coffre
                    print('\n'*2)
                    choix = randint(0,1)  # Choisi entre sortir et rester de façon aléatoire.
                    if choix == 1:
                        Jeu.jouer(i[0],1)
                        print()
                        print("{g}Le joueur {i} a décidé de quitter ce tour !{n}".format(g=G,i=i[0],n=N))
                        Jeu.joueurssortis.append(i[0])  # Ajout du joueur dans la liste des joueurs sorties.
                    else:
                        # Aucune intéraction nécessaire, le jeu continue pour ces joueurs.
                        print()
                        print("{g}Le joueur {i} a décidé de rester dans le jeu !{n}".format(g=G,i=i[0],n=N))
                    time.sleep(3)
        Jeu.sortie()  # Vérifie que la manche n'est pas fini et réparti le trésor aux joueurs sorties.
    else:
        print("{r}Un obstacle surgit ! Les joueurs restants dans la grotte fuit ! (L'obstacle était {t}){n}".format(r=R,t=Jeu.tapis[-1][0],n=N))
        time.sleep(5)
        Jeu.changementManche()

clear()
print("{r}Fin de la partie.\nLe classement est :{y}".format(r=R,y=Y))
for i in Jeu.classement():
    print('Joueur {i} avec {j} diamants'.format(i=i[0],j=i[1]))
print(N)