"""
MODULE DIAMANTS

AUTEURS : Eliott & Chakib

Ce jeu est développé dans le cadre d'une SAé (un projet) avec l'IUT de Vélizy.
"""

from random import sample

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
        joueurs : dictionnaire qui indique les caractéristiques des joueurs (nombre de diamants, nombre de reliques, en jeu ou non)
        tapis : dictionnaire qui montre le tapis de cartes ainsi que les diamants restants dessus (-1 = monstre)
    """

    def __init__(self, nbJoueurs: int, typeJeu: bool) -> None:
        assert nbJoueurs>=3 and nbJoueurs<=8, "Le jeu doit contenir au moins 3 joueurs et au maximum 8 joueurs."
        self.nbJoueurs = nbJoueurs  # nombre de joueur dans la partie (int)
        self.joueursRestants = nbJoueurs  # nombre de joueur restant dans la manche (int)
        self.cartes = list()  # paquet de carte (list)
        self.typeJeu = typeJeu  # 0 joueurs | 1 IA (int)
        self.manchesRestants = 5  # nombre manches restantes (int)
        self.joueurs = {}  # caractéristique des joueurs (dict) - joueur : nb de diamants, nb de relique, en jeu ou non
        # self.tapis = {}  # tapis des cartes sorties (dict) - carte : nombre de diamants restants (-1 si monstre)
        self.tapis = []
        self.creationJoueurs(nbJoueurs)  # appel de la fonction pour initialiser les caractéristiques (self.joueur)
    
    def creationJoueurs(self, nbJoueurs: int) -> None:
        """
        Crée le dictionnaire comprenant les caractéristiques de chaque joueur.

        Args:
            nbJoueurs (int): Nombre de joueur.
        """
        assert nbJoueurs>=3 and nbJoueurs<=8, "Le jeu doit contenir au moins 3 joueurs et au maximum 8 joueurs."
        for i in range(1, nbJoueurs+1):
            self.joueurs[i] = [0, 0, 0]  # [Trésor (nb diamants), nombre de reliques, etat (0 mine, 1 sortie)]

    def caracteristiquesJoueur(self, joueur: int):
        """
        Récupère les caractéristiques d'un joueur en particulier.

        Args:
            joueur (int): Le joueur dont on veut récupérer les caractéristiques.

        Returns:
            _type_: Les caractéristiques du joueur.
        """
        assert joueur>=0 and joueur<=7 and joueur in self.joueurs.keys(), "Le joueur doit exister."
        return self.joueurs[joueur]
    
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
        print(monstresSorties)
        for j in range(len(monstresSorties)):
            for k in range(len(monstresSorties)):
                if j!=k and monstresSorties[j]==monstresSorties[k]:
                    monstre = monstresSorties[j]
                    sortie = True
        return sortie, monstre

    def melangeCarte(self) -> None:
        """
        Mélange le paquet de cartes.
        """
        self.cartes = sample(CARTES, len(CARTES))
    
    def repartitionTresor(self) -> tuple:
        """
        Répartit la dernière carte du tapis sortie entre les joueurs et met le reste sur la carte.

        Returns:
            tuple[int, int]: Trésor par personnes, trésor restant sur la carte.
        """
        tresorPerPers = self.cartes[-1] // self.joueursRestants  # Défini le nb de diamants par personne
        self.tapis.append([self.cartes[-1], self.cartes[-1] % self.joueursRestants])   # Défini le reste des diamants et l'assigne à la carte sur le tapis
        self.tapis[-1][1] = self.cartes[-1] % self.joueursRestants  # Défini le reste des diamants et l'assigne à la carte sur le tapis
        for i in range(1,self.joueursRestants+1):
            self.joueurs[i][0] += tresorPerPers
        return tresorPerPers, self.tapis[-1][1]

    def piocheCarte(self) -> str:
        """
        Pioche une carte du deck et la mets sur le tapis.
        Si un monstre sort on vérifie qu'il ne soit pas déjà sortie une fois
        et si c'est la deuxième fois on retire le monstre des cartes et on défini la fin de manche.

        Returns:
            str: La carte en question.
        """
        if type(self.cartes[-1]) == int:
            self.repartitionTresor()
        else:
            print(self.cartes[-1])
            self.tapis.append([self.cartes[-1], -1])
            #self.tapis[self.cartes.index(self.cartes[-1])][1] = -1
            monstre = self.verificationMonstre()
            print(monstre)
            if monstre[0] == True:
                print(monstre[1])
                print(CARTES.index(monstre[1]))
                i = CARTES.index(monstre[1])
                CARTES.pop(i)
                return self.finManche(True)
        return str(self.cartes.pop(-1))

    def sortie(self, joueursSorties: list) -> None:
        """
        Est appelé lorsque tous les joueurs ont fait leurs choix, les joueurs sortis se répartissent le trésor sur le tapis.

        Args:
            joueursSorties (list): Liste des joueurs sortis.
        """
        assert len(joueursSorties) <= self.nbJoueurs, "Il ne peut pas avoir plus de joueur sorti que de joueurs en jeu"
        if len(joueursSorties) == 0:
            return
        # Calcule le nombre de diamants restants sur le tapis
        tresorParPers = 0
        for i in self.tapis:
            if i[1] > 0:
                tresorParPers += i[1]
                self.tapis[i[0]] = 0
        if len(joueursSorties) != 0:
            reste = tresorParPers%len(joueursSorties) 
            tresorParPers -= reste
            tresorParPers //= len(joueursSorties)
            # Remet le reste sur le tapis sur la première carte de valeur qu'on trouve
            for i in self.tapis:
                if i[1] != -1:
                    self.tapis[i[0]][1] = reste
                    break
            for k in joueursSorties:
                self.joueurs[k][0] += tresorParPers
            
        
    def jouer(self, choix: int, joueur: int) -> list:
        """
        Applique l'action choisie par le joueur (rentrer ou rester).

        Args:
            choix (int): Le choix en question.
            joueur (int): Le joueur en question.

        Returns:
            list: Classement des joueurs. (Voir documentation de la fonction 'finManche')
        """
        if self.joueursRestants == 0 :
            return self.finManche()
        if self.joueurs[joueur][2]==0 and choix==1: 
            self.joueursRestants -= 1
            self.joueurs[joueur][2] = 1
            # return joueur POURQUOI ON RETURN LE JOUEUR ??

    def finManche(self, monstre = False) -> list:
        """
        Applique tous les paramètres par défaut pour la création d'une nouvelle manche.
        Affiche le vainqueur et le classement en cas de fin de partie.

        Args:
            monstre (bool, optional): Indique si un monstre est sorti 2 fois. Par défaut sur False.

        Returns:
            list: Classement des joueurs. (Voir documentation de la fonction 'classement')
        """
        assert self.joueursRestants == 0 or monstre == True
        if self.manchesRestants != 0:
            for i in range(1, len(self.joueurs)+1):
                print("FIN MANCHE")
                self.joueurs[i][2] == 0  # On remet tous les joueurs en jeu
                self.joueursRestants = range(1, len(self.joueurs)+1)
        else:
            print("CLASSEMENT") 
            return self.classement()

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