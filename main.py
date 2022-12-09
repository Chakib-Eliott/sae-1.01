"""
MAIN

AUTEURS : Eliott & Chakib
NOM DU JEU : DIAMANTS

Ce jeu est développé dans le cadre d'une SAé (un projet) avec l'IUT de Vélizy.
"""

import os  # Natif à Python
import sys  # Natif à Python

# Efface le terminal actuel pour avoir un terminal de jeu.
try: 
    if os.name == 'nt': os.system('cls') # si windows 
    else: os.system('clear')
except:
    print()

print("BIENVENUE SUR DIAMANTS ! \nCe jeu est un jeu codé par Eliott et Chakib et est une représentation du jeu `INCAN GOLD`.")
print()

# Gestion des arguments mit après l'appel du fichier
# Exemple : python3 main.py graphique
if len(sys.argv) > 1:
    if sys.argv[1].upper() == "GRAPHIQUE":
        from graphique import *
        print("L'interface graphique est lancé !")
    elif sys.argv[1].upper() == "TERMINAL":
        from terminal import *
        print()
    else:
        raise "L'argument entré est invalide ! (RAPPEL: les arguments disponibles sont `terminal` ou `graphique`)"
else:
    # Gestion du mode de jeu si aucun paramètre avait été rentré.
    mode = input("Entrez `T` pour lancer le jeu dans le terminal.\nEntrez `G` pour lancer le jeu dans l'interface graphique.\n")
    mode = mode.upper()
    assert mode == "G" or mode == "T", "Seulement les charactères `G` ou `T` sont autorisés !"
    if mode == "G":
        from graphique import *
        print("L'interface graphique est lancé !")
    elif mode == "T":
        from terminal import *
        print()
    else:
        raise "Erreur d'entrée !"
