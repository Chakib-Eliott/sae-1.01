"""
MODULE DIAMANTS

AUTHORS : Eliott & Chakib
"""

from random import sample

CARTES = [1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 13, 14, 15, 17, 'Araignée', 'Araignée', 'Araignée', 'Serpent', 'Serpent', 'Serpent', 'Larve', 'Larve', 'Larve', 'Boulet', 'Boulet', 'Boulet', 'Bélier', 'Bélier', 'Bélier']


class Diamant:
    def __init__(self, nbJoueurs:int, typeJeu:bool):
        self.joueursRestants = nbJoueurs
        self.cartes = list()
        self.typeJeu = typeJeu # 0 joueurs | 1 IA
        self.manchesRestants = 5
        self.joueurs = dict()
        self.tapis = dict()
        self.creationJoueurs(nbJoueurs)
    
    def creationJoueurs(self, nbJoueurs:int):
        """
        Crée le dictionnaire comprenant les caractéristiques de chaque joueur
        PARAMS : 
            - nbjoueurs: Nombre de joueur
        """
        for i in range(1, nbJoueurs+1):
            self.joueurs[i] = [0, 0] # [Trésor (nb diamants), nombre de reliques]
    def caracteristiquesJoueur(self, joueur:int):
        """
        Récupérer les caractéristiques d'un joueur en particulier
        PARAMS : 
            - joueur: Le joueur dont on veut récupérer les caractéristiques
             
        RETURN : 
            - Les caractéristiques du joueur
        """
        pass
    
    def verificationMonstre(self):
        """
        Vérifier si une carte monstre est déjà sortie

        RETURN :
            - Bool (la carte est déjà sortie ou non)
            - La carte en question
        """
        pass

    def melangeCarte(self):
        """
        Mélange le paquet de cartes
        """
        self.cartes = sample(CARTES)
    
    def repartitionTresor(self):
        """
        Répartit la dernière carte du tapis sortie entre les joueurs

        RETURN : 
            - Trésor/pers (int)
            - Trésor restant sur carte
        """
        pass

    def piocheCarte(self):
        """
        Pioche une carte du deck et la mets sur le tapis

        RETURN : 
            - La carte en question
        """
        pass

    def jouer(self, choix, joueur):
        """
        Applique l'action choisie par le joueur (rentrer ou rester)

        PARAMS : 
            - choix: Le choix en question
            - joueur: Le joueur en question
        """
        pass


Jeu = Diamant(5, 0)
print(Jeu.joueurs)