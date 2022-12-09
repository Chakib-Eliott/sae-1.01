"""
MODULE DIAMANTS

AUTEURS : Eliott & Chakib

Ce jeu est développé dans le cadre d'une SAé (un projet) avec l'IUT de Vélizy.
"""

from random import sample  # Natif à Python

CARTES = [
    1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 13, 14, 15, 17,
    'Araignée', 'Araignée', 'Araignée', 'Serpent', 'Serpent', 'Serpent',
    'Larve', 'Larve', 'Larve', 'Boulet', 'Boulet', 'Boulet', 'Bélier', 'Bélier', 'Bélier'
    ]


class Diamant:
    """
    Classe du jeu Diamants.
    
    Attributes:
        nbJoueurs : entier qui défini le nombre de joueur de la partie
        typeJeu : booléen qui défini si le jeu est joué par une intelligence artificielle ou par un joueur
        cartes : liste qui représente le paquet de carte
        manchesRestants : entier défini à 5 par défaut qui indique le nombre de manches restantes
        joueurs : dictionnaire qui indique les caractéristiques des joueurs (nombre de diamants permanents, nombre de reliques, en jeu ou non, nombre de diamants)
        tapis : dictionnaire qui montre le tapis de cartes ainsi que les diamants restants dessus (-1 = monstre)
    """

    def __init__(self, nbJoueurs: int, typeJeu: bool) -> None:
        assert nbJoueurs>=3 and nbJoueurs<=8, "Le jeu doit contenir au moins 3 joueurs et au maximum 8 joueurs."
        self.nbJoueurs = nbJoueurs  # nombre de joueur dans la partie (int)
        self.joueursRestants = nbJoueurs  # nombre de joueur restant dans la manche (int)
        self.cartes = list()  # paquet de carte (list)
        self.typeJeu = typeJeu  # 0 joueurs | 1 IA (int)
        self.manchesRestants = 5  # nombre manches restantes (int)
        self.joueurs = {}  # caractéristique des joueurs (dict) - joueur : nb de diamants permanants, nb de relique, en jeu ou non, nb diamants temporaires
        self.tapis = [] # tapis des cartes sorties (list) - [carte, nombre de diamants restants (-1 si monstre)]
        self.creationJoueurs(nbJoueurs)  # appel de la fonction pour initialiser les caractéristiques (self.joueur)
    
    def melangeCarte(self) -> None:
        """
        Mélange le paquet de cartes.
        """
        self.cartes = sample(CARTES, len(CARTES))  # Utilise la méthode sample de random pour mélanger le paquet de carte.
    
    def creationJoueurs(self, nbJoueurs: int) -> None:
        """
        Crée le dictionnaire comprenant les caractéristiques de chaque joueur.

        Args:
            nbJoueurs (int): Nombre de joueur.
        """
        assert nbJoueurs>=3 and nbJoueurs<=8, "Le jeu doit contenir au moins 3 joueurs et au maximum 8 joueurs."
        for i in range(1, nbJoueurs+1):
            self.joueurs[i] = [0, 0, 0, 0]  # [Trésor (nb diamants), nombre de reliques, etat (0 mine, 1 sortie), Trésor courant]
    
    def piocheCarte(self) -> bool:
        """
        Pioche une carte du deck et la mets sur le tapis.
        Si un monstre sort on vérifie qu'il ne soit pas déjà sortie une fois
        et si c'est la deuxième fois on retire le monstre des cartes et on défini la fin de manche.
        
        Returns:
            bool: Fin de manche
        """
        carte = self.cartes.pop(-1)  # Retire du paquet de carte la carte
        if type(carte) == int:  # SI c'est une carte de diamants
            self.repartitionTresor(carte)  # On répartit le trésor
        else:  # Si c'est un monstre (ou une relique mais on verra plus tard)
            self.tapis.append([carte, -1])  # On ajoute la carte au tapis
            monstre = self.verificationMonstre()  # On vérifie si la dernière carte monstre est déjà sorti une fois
            if monstre[0] == True:  # Si c'est le cas
                CARTES.remove(monstre[1])  # On la retire du jeu jusqu'à la fin de la partie
                return self.finManche(True)  # on appel la fin de la manche

    def verificationMonstre(self) -> tuple:
        """
        Vérifie si une carte monstre est déjà sortie et indique du quel monstre s'agit-il.

        Returns:
            tuple[bool, str]: la carte est déjà sortie ou non, la carte(s) en question.
        """
        sortie = False
        monstresSorties = []
        monstre = None
        for i in self.tapis:
            if not type(i[0]) == int:
                monstresSorties.append(i[0])
        for j in range(len(monstresSorties)):
            for k in range(len(monstresSorties)):
                if j!=k and monstresSorties[j]==monstresSorties[k]:
                    monstre = monstresSorties[j]
                    sortie = True
        return sortie, monstre

    def repartitionTresor(self, carte: int) -> None:
        """
        Répartit la dernière carte du tapis sortie entre les joueurs et met le reste sur la carte.
        
        Args:
            carte (int): La carte sortie.
        """
        tresorPerPers = carte // self.joueursRestants  # Défini le nb de diamants par personne
        self.tapis.append([carte, carte % self.joueursRestants])  # Défini le reste des diamants et l'assigne à la carte sur le tapis
        for i in range(1, self.nbJoueurs+1):
            if self.joueurs[i][2] == 0:  # Si le joueur est encore dans la partie
                self.joueurs[i][3] += tresorPerPers  # On lui ajoute le trésor à son trésor courant

    def jouer(self, joueur: int, choix = 1) -> bool:
        """
        Applique l'action choisie par le joueur (rentrer ou rester).
        La fonction est appeler de base pour faire sortir le joueur.

        Args:
            joueur (int): Le joueur en question.
            choix (int): Le choix en question (1 = sortir, 0 = rester). Par défaut à 1.
            
        Returns:
            bool: Fin de manche
        """
        if self.joueursRestants == 0 :
            return self.finManche()
        if self.joueurs[joueur][2]==0 and choix==1:  # Si le joueur est encore en jeu et décide de sortir
            self.joueursRestants -= 1 
            self.joueurs[joueur][2] = 1  # On le sort de la mine
            self.joueurs[joueur][0] += self.joueurs[joueur][3]  # On lui met son trésor courant dans son coffre
            self.joueurs[joueur][3] = 0  # On vide le trésor courant

    def sortie(self, joueursSorties: list) -> None:
        """
        Est appelé lorsque tous les joueurs ont fait leurs choix,
        les joueurs sortis se répartissent le trésor sur le tapis.

        Args:
            joueursSorties (list): Liste des joueurs sortis.
        """
        assert len(joueursSorties) <= self.nbJoueurs, "Il ne peut pas avoir plus de joueur sorti que de joueurs en jeu"
        if len(joueursSorties) == 0:
            return
        # Calcule le nombre de diamants restants sur le tapis et le répartit entre les joueurs sortis
        if len(joueursSorties) != 0: 
            tresorParPers = 0
            for i in range(len(self.tapis)):
                if self.tapis[i][1] > 0:
                    tresorParPers += self.tapis[i][1]
                    self.tapis[i][1] = 0
            reste = tresorParPers%len(joueursSorties) 
            tresorParPers -= reste
            tresorParPers //= len(joueursSorties)
            # Remet le reste sur le tapis sur la première carte de valeur qu'on trouve
            for i in range(len(self.tapis)):
                if self.tapis[i][1] != -1:
                    self.tapis[i][1] = reste
                    break
            for k in joueursSorties:
                self.joueurs[k][3] += tresorParPers  # On met le trésor dans le coffre des joueurs sorti
            
    def finManche(self, monstre = False) -> bool:
        """
        Applique tous les paramètres par défaut pour la création d'une nouvelle manche.
        Affiche le vainqueur et le classement en cas de fin de partie.

        Args:
            monstre (bool, optional): Indique si un monstre est sorti 2 fois. Par défaut sur False.

        Returns:
            bool: Fin de la manche.
        """
        assert self.joueursRestants == 0 or monstre == True
        self.joueursRestants = 0
        if self.manchesRestants != 0:
            return True
        
    def changementManche(self) -> None:
        """
        Change la manche et réinitialise la partie.
        """
        for i in range(1, len(self.joueurs)+1):
            self.joueurs[i][2],self.joueurs[i][3] = 0,0  # Remet les joueurs en jeu, et supprime les coffres temporaires
            self.joueursRestants = self.nbJoueurs
        self.tapis = []
        self.manchesRestants -= 1

    def classement(self) -> list:
        """
        Affiche le classement final de la partie.

        Returns:
            list: Classement des joueurs
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

    def caracteristiquesJoueur(self, joueur: int) -> list:
        """
        Récupère les caractéristiques d'un joueur en particulier.

        Args:
            joueur (int): Le joueur dont on veut récupérer les caractéristiques.

        Returns:
            list: Les caractéristiques du joueur.
        """
        assert joueur in self.joueurs.keys(), "Le joueur doit exister."
        return self.joueurs[joueur]