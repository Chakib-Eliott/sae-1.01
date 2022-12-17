"""
MODULE DIAMANTS

AUTEURS : Eliott & Chakib

Ce jeu est développé dans le cadre d'une SAé (un projet) avec l'IUT de Vélizy.
"""

from random import sample  # Natif à Python

CARTES = [
    1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 13, 14, 15, 17,
    'Araignée', 'Araignée', 'Araignée', 'Serpent', 'Serpent', 'Serpent',
    'Lave', 'Lave', 'Lave', 'Boulet', 'Boulet', 'Boulet', 'Bélier', 'Bélier', 'Bélier',
    'Relique'
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
        tapis : dictionnaire qui montre le tapis de cartes ainsi que les diamants restants dessus (-1 = piege)
        relique : liste des joueurs ayant obtenu des reliques
        joueurssortie : liste des joueurs sorties pendant le tour
    """

    def __init__(self, nbJoueurs: int, typeJeu: bool) -> None:
        assert nbJoueurs>=3 and nbJoueurs<=8, "Le jeu doit contenir au moins 3 joueurs et au maximum 8 joueurs."
        self.nbJoueurs = nbJoueurs  # nombre de joueur dans la partie (int)
        self.joueursRestants = nbJoueurs  # nombre de joueur restant dans la manche (int)
        self.cartes = list()  # paquet de carte (list)
        self.typeJeu = typeJeu  # 0 joueurs | 1 IA (int)
        self.manchesRestants = 5  # nombre manches restantes (int)
        self.joueurs = {}  # caractéristique des joueurs (dict) - joueur : nb de diamants permanants, nb de relique, en jeu ou non, nb diamants temporaires
        self.tapis = [] # tapis des cartes sorties (list) - [carte, nombre de diamants restants (-1 si piege)]
        self.relique = []  # des joueurs ayant des reliques (list)
        self.creationJoueurs(nbJoueurs)  # appel de la fonction pour initialiser les caractéristiques (self.joueur)
        self.joueurssortis = []  # joueurs sorties pendant le tour (list)
    
    def melangeCarte(self) -> None:
        """
        Mélange le paquet de cartes.
        """
        self.cartes = sample(CARTES, len(CARTES))  # Utilise la méthode sample de random pour mélanger le paquet de carte.
        assert len(self.cartes) == len(CARTES), "La taille du pack mélangé doit correspondre à la taille du paquet original"
        
    def creationJoueurs(self, nbJoueurs: int) -> None:
        """
        Crée le dictionnaire comprenant les caractéristiques de chaque joueur.
        La clée du dictionnaire est le numéro du joueur.
        Le 1er argument est le nombre de diamants permanant du joueur.
        Le 2ème argument est le nombre de relique que possède le joueur.
        Le 3ème argument est l'état du joueur (0 si il explore, 1 si il est sortie).
        Le 4ème argument est le trésor que le joueur possède pendant l'expédition.

        Args:
            nbJoueurs (int): Nombre de joueur.
        """
        assert nbJoueurs>=3 and nbJoueurs<=8, "Le jeu doit contenir au moins 3 joueurs et au maximum 8 joueurs."
        for i in range(1, nbJoueurs+1):
            self.joueurs[i] = [0, 0, 0, 0]  # [Trésor (nb diamants), nombre de reliques, etat (0 mine, 1 sortie), Trésor courant]

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
    
    def piocheCarte(self) -> bool:
        """
        Pioche une carte du paquet de cartes et la mets sur le tapis.
        Si un piège sort on vérifie qu'il ne soit pas déjà sortie une fois
        et si c'est la deuxième fois on retire le piège des cartes et on défini la fin de manche.
        
        Returns:
            bool: Fin de manche
        """
        carte = self.cartes.pop(-1)  # Retire du paquet de carte la carte
        if type(carte) == int:  # SI c'est une carte de diamants
            self.repartitionTresor(carte)  # On répartit le trésor
        else:  # Si c'est un piège ou une relique
            if carte == 'Relique':  # Si c'est une carte diamant
                self.tapis.append([carte, -2])
            else:
                self.tapis.append([carte, -1])  # On ajoute la carte au tapis
                piege = self.verificationPiege()  # On vérifie si la dernière carte piège est déjà sorti une fois
                if piege[0] == True:  # Si c'est le cas
                    CARTES.remove(piege[1])  # On la retire du jeu jusqu'à la fin de la partie
                    return True  # on appel la fin de la manche

    def verificationPiege(self) -> tuple:
        """
        Vérifie si une carte piège est déjà sortie et indique du quel piège s'agit-il.

        Returns:
            tuple[bool, str]: la carte est déjà sortie ou non, la carte(s) en question.
        """
        sortie = False
        piegeSorties = []
        piege = None
        for i in self.tapis:
            if not type(i[0]) == int:
                piegeSorties.append(i[0])
        for j in range(len(piegeSorties)):
            for k in range(len(piegeSorties)):
                if j!=k and piegeSorties[j]==piegeSorties[k]:
                    piege = piegeSorties[j]
                    sortie = True
        return sortie, piege

    def repartitionTresor(self, carte: int) -> None:
        """
        Répartit la dernière carte du tapis sortie entre les joueurs et met le reste sur la carte.
        
        Args:
            carte (int): La carte sortie.
        """
        assert carte in CARTES, "La carte doit exister"
        tresorPerPers = carte // self.joueursRestants  # Défini le nb de diamants par personne
        self.tapis.append([carte, carte % self.joueursRestants])  # Défini le reste des diamants et l'assigne à la carte sur le tapis
        for i in range(1, self.nbJoueurs+1):
            if self.joueurs[i][2] == 0:  # Si le joueur est encore dans la partie
                self.joueurs[i][3] += tresorPerPers  # On lui ajoute le trésor à son trésor courant

    def jouer(self, joueur: int, choix = 1) -> bool:
        """
        Applique l'action choisie par le joueur (rentrer ou rester).
        La fonction est appeler de base pour faire sortir le joueur
        vu qu'aucune action n'est à faire si le joueur reste.

        Args:
            joueur (int): Le joueur en question.
            choix (int): Le choix en question (1 = sortir, 0 = rester). Par défaut à 1.
            
        Returns:
            bool: Si fin de manche.
        """
        assert choix in [0,1], "Le choix du joueur doit être 0 ou 1"
        assert joueur in list(range(1,self.nbJoueurs+1)), "Le joueur doit exister"
        if self.joueursRestants == 0 :
            return True
        if self.joueurs[joueur][2]==0 and choix==1:  # Si le joueur est encore en jeu et décide de sortir
            self.joueursRestants -= 1 
            self.joueurs[joueur][2] = 1  # On le sort de la mine
            self.joueurs[joueur][0] += self.joueurs[joueur][3]  # On lui met son trésor courant dans son coffre
            self.joueurs[joueur][3] = 0  # On vide le trésor courant
            # self.joueurssortis.append(joueur)

    def sortie(self) -> None:
        """
        Est appelé lorsque tous les joueurs ont fait leurs choix,
        les joueurs sortis se répartissent le trésor sur le tapis.
        """
        assert len(self.joueurssortis) <= self.nbJoueurs, "Il ne peut pas avoir plus de joueur sorti que de joueurs en jeu"
        if len(self.joueurssortis) == 0:
            return
        # Calcule le nombre de diamants restants sur le tapis et le répartit entre les joueurs sortis
        if len(self.joueurssortis) != 0:
            tresorParPers = 0
            for i in range(len(self.tapis)):
                if self.tapis[i][1] > 0:
                    tresorParPers += self.tapis[i][1]
                    self.tapis[i][1] = 0
            reste = tresorParPers%len(self.joueurssortis)
            tresorParPers //= len(self.joueurssortis)
            # Remet le reste sur le tapis sur la première carte de valeur qu'on trouve
            for i in range(len(self.tapis)):
                if type(self.tapis[i][0]) == int:
                    self.tapis[i][1] = reste
                    break
            for k in self.joueurssortis:
                self.joueurs[k][0] += tresorParPers  # On met le trésor dans le coffre des joueurs sorti
        # Vérifie si il y a qu'un joueur qui sort et une relique sur le tapis.
        if len(self.joueurssortis)==1 and ['Relique',-2] in self.tapis:
            # Boucle pour récupérer toutes les reliques du tapis
            while ['Relique',-2] in self.tapis:
                i = self.tapis.index(['Relique',-2])
                y = CARTES.index('Relique')
                CARTES.pop(y)  # Retire la relique du paquet de carte.
                self.tapis.pop(i)  # Retire la relique du tapis.
                self.joueurs[self.joueurssortis[0]][1] += 1  # Ajoute la relique au joueur.
                self.relique.append(self.joueurssortis[0])  # Ajoute le joueur à la liste des reliques
        
    def changementManche(self) -> None:
        """
        Change la manche et réinitialise la partie.
        """
        for i in range(1, len(self.joueurs)+1):
            self.joueurs[i][2],self.joueurs[i][3] = 0,0  # Remet les joueurs en jeu, et supprime les coffres temporaires
            self.joueursRestants = self.nbJoueurs
        self.tapis = []
        self.manchesRestants -= 1
        CARTES.append('Relique')  # Ajoute une relique au paquet

    def classement(self) -> list:
        """
        Affiche le classement final de la partie.

        Returns:
            list: Classement des joueurs
        """
        # Vérifie les reliques et donne les récompenses par rapport à quand ils les ont obtenu.
        for k in range(len(self.relique)):
            if k <= 3:
                self.joueurs[self.relique[k]][0] += 5
            else:
                self.joueurs[self.relique[k]][0] += 10
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
        assert len(classement) == self.nbJoueurs, "Le classement doit faire la taille des joueurs."
        return classement