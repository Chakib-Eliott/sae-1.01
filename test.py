"""
MODULE DE TEST

AUTEURS : Eliott & Chakib
"""
from diamants import Diamant

Jeu = Diamant(5, 0)
Jeu.melangeCarte()
Jeu.piocheCarte()
Jeu.joueurs[3][0] = 12
Jeu.manchesRestants = 0
Jeu.joueursRestants = 0
print(Jeu.jouer(1,1))