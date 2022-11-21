"""
MODULE DIAMANTS

AUTEURS : Eliott & Chakib
"""

from random import sample

CARTES = [1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 13, 14, 15, 17, 'Araignée', 'Araignée', 'Araignée', 'Serpent', 'Serpent', 'Serpent', 'Larve', 'Larve', 'Larve', 'Boulet', 'Boulet', 'Boulet', 'Bélier', 'Bélier', 'Bélier']


class Diamant:
    def __init__(self, nbJoueurs:int, typeJeu:bool):
        self.joueursRestants = nbJoueurs # nombre de joueur restant dans la manche (int)
        self.cartes = list() # paquet de carte (list)
        self.typeJeu = typeJeu # 0 joueurs | 1 IA (int)
        self.manchesRestants = 5 # nombre manches restantes (int)
        self.joueurs = {} # caractéristique des joueurs (dict) - joueur : nb de diamants, nb de relique, en jeu ou non
        self.tapis = {} # tapis des cartes sorties (dict) - carte : nombre de diamants restants (-1 si monstre)
        self.creationJoueurs(nbJoueurs) # appel de la fonction pour initialiser les caractéristiques (self.joueur)
    
    def creationJoueurs(self, nbJoueurs:int)->None:
        """
        Crée le dictionnaire comprenant les caractéristiques de chaque joueur

        PARAMS : 
            - nbjoueurs: Nombre de joueur
        """
        for i in range(1, nbJoueurs+1):
            self.joueurs[i] = [0, 0, 0] # [Trésor (nb diamants), nombre de reliques, etat (0 mine, 1 sortie)]

    def caracteristiquesJoueur(self, joueur:int):
        """
        Récupère les caractéristiques d'un joueur en particulier

        PARAMS : 
            - joueur: Le joueur dont on veut récupérer les caractéristiques
             
        RETURN : 
            - Les caractéristiques du joueur
        """
        return self.joueurs[joueur]
    
    def verificationMonstre(self):
        """
        Vérifie si une carte monstre est déjà sortie

        RETURN :
            - Bool (la carte est déjà sortie ou non)
            - La/les carte(s) en question
        """
        monstresSorties = []
        for i in self.tapis.keys():
            if not type(i) == int:
                monstresSorties.append(i)
        return True, monstresSorties

    def melangeCarte(self):
        """
        Mélange le paquet de cartes
        """
        self.cartes = sample(CARTES, len(CARTES))
    
    def repartitionTresor(self):
        """
        Répartit la dernière carte du tapis sortie entre les joueurs et met le reste sur la carte.

        RETURN : 
            - Trésor/pers (int)
            - Trésor restant sur carte
        """
        tresorPerPers = self.cartes[-1] // self.joueursRestants # Défini le nb de diamants par personne
        self.tapis[self.cartes[-1]] = self.cartes[-1] % self.joueursRestants # Défini le reste des diamants et l'assigne à la carte sur le tapis
        for i in range(1,self.joueursRestants+1):
            self.joueurs[i][0] += tresorPerPers
        return tresorPerPers, self.tapis[self.cartes[-1]]

    def piocheCarte(self):
        """
        Pioche une carte du deck et la mets sur le tapis

        RETURN : 
            - La carte en question
        """
        if type(self.cartes[-1]) == int:
            self.repartitionTresor()
        else: 
            self.tapis[self.cartes[-1]] = -1 
        return self.cartes.pop(-1)

    def sortie(self, joueursSorties:list):
        """
        Est appelé lorsque tous les joueurs ont fait leurs choix, les joueurs sortis se répartissent le trésor sur le tapis
        
        PARAMS :
            - Liste des joueurs sortis (list)
        """
        # Calcule le nombre de diamants restants sur le tapis
        tresorParPers = 0
        for i,j in self.tapis.keys(), self.tapis.values():
            if j > 0:
                tresorParPers += j
                self.tapis[i] = 0
                
        reste = tresorParPers%len(joueursSorties) 
        tresorParPers -= reste
        tresorParPers //= len(joueursSorties)
        # Remet le reste sur le tapis sur la première carte de valeur qu'on trouve
        for i,j in self.tapis.keys(), self.tapis.values():
            if j != -1:
                self.tapis[i] = reste
                break
        for i in joueursSorties:
            self.joueurs[i] += tresorParPers
            
        
    def jouer(self, choix, joueur):
        """
        Applique l'action choisie par le joueur (rentrer ou rester)

        PARAMS : 
            - choix: Le choix en question
            - joueur: Le joueur en question
        """
        if self.joueursRestants == 0 :
            return self.finManche()
        if self.joueurs[joueur][2] == 0: 
            if choix == 1:
                self.joueursRestants -= 1
                self.joueurs[joueur][2] = 1
                return joueur

    def finManche(self):
        """
        Applique tous les paramètres par défaut pour la création d'une nouvelle manche.
        Affiche le vainqueur et le classement en cas de fin de partie.
        """
        assert self.joueursRestants == 0
        if self.manchesRestants != 0:
            for i in range(1, len(self.joueurs)+1):
                self.joueurs[i][2] == 0 # On remet tous les joueurs en jeu
                self.joueursRestants = range(1, len(self.joueurs)+1)
            
        else: 
            return self.classement()

    def classement(self)->list:
        """
        Affiche le classement final de la partie.

        RETURN :
            - classement (list)
        """
        classement = [[1,self.joueurs[1][0]]]
        for i in range(2,len(self.joueurs)+1):
            fin = False
            j = 0
            while not fin:
                if self.joueurs[i][0] >= self.joueurs[classement[j][0]][0]:
                    classement.insert(j,[i,self.joueurs[i][0]])
                    fin = True
                else:
                    j+=1
                if j == len(classement):
                    fin = True
                    classement.append([i,self.joueurs[i][0]])
        return classement