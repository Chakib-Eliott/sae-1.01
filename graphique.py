"""
VERSION GRAPHIQUE (attention aux yeux)

AUTEURS : Eliott & Chakib

Ce jeu est développé dans le cadre d'une SAé (un projet) avec l'IUT de Vélizy.
"""

import diamants as D  # Les fonction qui permettent de faire fonctionner le jeu
from tkinter import *  # Natif à Python
import tkinter.font as TkFont  # Natif à Python
from random import choice  # Natif à Python


# Initialisation de la fenêtre de jeu.
WIDTH="1000"
HEIGHT="700"
BACKGROUND = '#DBC797'
root = Tk()
root.title('Diamants by Eliott & Chakib')
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(width=False, height=False)
DIAMANTIMAGE = PhotoImage(file='./asset/diamants_logo.png')

root.iconphoto(False, DIAMANTIMAGE)
root.configure(bg=BACKGROUND)

# Initialisation des images des cartes 'sortir' et 'rester'.
RESTERIMAGE = PhotoImage(file='./asset/diamant_rester.png')
SORTIRIMAGE = PhotoImage(file='./asset/diamant_sortir.png')

# Initialisation des images des cartes.
BOULETCARTE = PhotoImage(file='./asset/cartes/diamant-ball.png')
BELIERCARTE = PhotoImage(file='./asset/cartes/diamant-belier.png')
LAVECARTE = PhotoImage(file='./asset/cartes/diamant-lava.png')
RELIQUECARTE = PhotoImage(file='./asset/cartes/diamant-relique.png')
DIAMANTCARTE1 = PhotoImage(file='./asset/cartes/diamant-rubis-1.png')
DIAMANTCARTE2 = PhotoImage(file='./asset/cartes/diamant-rubis-2.png')
SERPENTCARTE = PhotoImage(file='./asset/cartes/diamant-snake.png')
ARAIGNEESCARTE = PhotoImage(file='./asset/cartes/diamant-spiders.png')

CARTE_SPECIAL = {
    'Relique':RELIQUECARTE, 'Boulet':BOULETCARTE, 'Bélier':BELIERCARTE,
    'Lave':LAVECARTE, 'Serpent':SERPENTCARTE, 'Araignée':ARAIGNEESCARTE
}

CARTE_DIAMANT = [DIAMANTCARTE1,DIAMANTCARTE2]

STATUT = {0:["Explore", '#58bf4e'], 1:["Sorti", '#d94636']}

NOMBREJOUEURS = 3

def getPlayer() -> int:
    """
    Permet d'obtenir le nombre de joueurs.

    Returns :
        int: Nombre de joueurs
    """
    return NOMBREJOUEURS

def accueil() -> None:
    Vider()

    def plusplayer() -> None:
        global NOMBREJOUEURS
        value = nbPlayers.get()
        if int(value) < 8:
            nbPlayers.delete(0,END)
            nbPlayers.insert(0,str(int(value)+1))
            NOMBREJOUEURS = nbPlayers.get()

    def minusplayer() -> None:
        global NOMBREJOUEURS
        value = nbPlayers.get()
        if int(value) > 3:
            nbPlayers.delete(0,END)
            nbPlayers.insert(0,str(int(value)-1))
            NOMBREJOUEURS = nbPlayers.get()
            
    # Logo diamants
    diamant = Label(image=DIAMANTIMAGE)
    diamant.configure(bg=BACKGROUND)  # Met la couleur du fond en fond de l'image PNG
    diamant.place(x=0, y=0)

    # Choix bot ou non
    bots = Checkbutton(root, text = "Bots", height = 2, width = 10, bg=BACKGROUND, activebackground=BACKGROUND)
    bots.place(x=750, y=300)

    # Label nombre joueurs
    labelnbjoueurs = Label(root, text='Nombre de joueurs', bg=BACKGROUND)
    labelnbjoueurs.place(x=115, y=275)

    # Bouton pour diminuer le nombre de joueur
    reduire = Button(root, text ="-", command = minusplayer)
    reduire.place(x= 113, y= 300)

    # Input du nombre de joueur
    cmd = root.register(lambda s: not s or (s.isdigit() and  int(s) >= 3 and int(s)< 9))
    nbPlayers = Entry(root, validate="key", vcmd=(cmd, "%P"), width=5)
    nbPlayers.place(x= 150, y= 300)
    nbPlayers.insert(0, "3")
    nbPlayers.bind("<Return>")  

    # Bouton pour augmenter le nombre de joueur
    augmenter = Button(root, text ="+", command = plusplayer)
    augmenter.place(x=200, y= 300)

    jouer_text = TkFont.Font(size=18)
    jouer = Button(root, text ="JOUER!", font=jouer_text, activebackground='#89e37f', command=lancementpartieintermediaire)
    jouer.place(x=440, y= 300)


def Vider() -> None:
    """
    Supprime tous les éléments de l'écran.
    Examples : Les titres, les boutons, ...
    """
    for widget in root.winfo_children():
        widget.destroy()

joueurencours = 1

def prochainJoueur(joueuractuel: int) -> int:
    prochain = (joueuractuel)%(Jeu.nbJoueurs)+1
    if Jeu.joueurs[prochain][2] == 0:
        return prochain
    else:
        return prochainJoueur(prochain)

def finTour(joueuractuel: int) -> bool:
    listejoueursenjeu = []
    for k,v in Jeu.joueurs.items():
        if v[2] == 0:
            listejoueursenjeu.append(k)
    if joueuractuel == listejoueursenjeu[-1]:
        return True
    return False

def Jouer(choix: int): # Quand le joueur en cours à cliquer
    # 0 = rester
    # 1 = sortir
    global Jeu
    global joueurcarte
    global joueurencours
    
    print(Jeu.joueurs)
    # Vérifie si c'est la fin du tour
    if choix == 1:
        Jeu.joueurssortis.append(joueurencours)
        listejoueursenjeu = []
        for k,v in Jeu.joueurs.items():
            if v[2] == 0:
                listejoueursenjeu.append(k)
        if len(listejoueursenjeu) == 1 and choix==1:
            if listejoueursenjeu[0] == joueurencours:
                Jeu.changementManche()
                joueurencours = 1
                return inigame()
    if finTour(joueurencours):
        # METTRE CARTE SUR TAPIS
        carte_tapis = Jeu.cartes[-1]
        if type(carte_tapis) == int:
            carte = Label(image=choice(CARTE_DIAMANT))
        else:
            carte = Label(image=CARTE_SPECIAL[carte_tapis])
        carte.configure(bg=BACKGROUND)  # Met la couleur du fond en fond de l'image PNG
        if len(Jeu.tapis) < 7:
            carte.place(x=10+100*len(Jeu.tapis), y=100)
        elif len(Jeu.tapis) < 14:
            carte.place(x=10+100*(len(Jeu.tapis)-7), y=200)
        # Vérifie que la carte n'est pas un piège
        if not(Jeu.piocheCarte()): 
            # APPLIQUE CARTE (donc vérifier joueurs sortis etc.)
            Jeu.sortie(Jeu.joueurssortis)
        else:
            # MONSTRE (donc fin manche)
            print('PERDRE A CAUSE DuN PIEGE')
            Jeu.changementManche()
            joueurencours = 1
            return inigame()
        Jeu.joueurssortis = []
 



    # APPLIQUER LE CHOIX DU JOUEUR
    Jeu.jouer(joueurencours, choix)
    joueurcarte[joueurencours][1]["text"]=STATUT[Jeu.joueurs[joueurencours][2]][0]
    joueurcarte[joueurencours][1]["fg"]=STATUT[Jeu.joueurs[joueurencours][2]][1]
            
    
    # CHAGEMENT DE JOUEUR
    joueurencours = prochainJoueur(joueurencours)
    joueurcarte[joueurencours][1]["text"]='Joue...'
    joueurcarte[joueurencours][1]["fg"]='#de96ff'
    diamants['text'] = 'Diamants :'+str(Jeu.joueurs[joueurencours][3])
    coffre['text'] = 'Coffre :'+str(Jeu.joueurs[joueurencours][0])
    reliques['text'] = 'Reliques :'+str(Jeu.joueurs[joueurencours][1])
    for i in range(1,Jeu.nbJoueurs+1):
        joueurcarte[i][2]["text"] = 'Diamants : '+str(Jeu.joueurs[i][3])
        joueurcarte[i][3]["text"] = 'Reliques : '+str(Jeu.joueurs[i][1])
    
            
def lancementpartieintermediaire():
    global Jeu
    Jeu = D.Diamant(int(getPlayer()), 0) # Création de la partie
    inigame()

def classement():
    Vider()
    print(Jeu.classement())
    print("Fin de la partie.\nLe classement est :")
    for i in Jeu.classement():
        Label(root, text='Joueur {i} avec {j} diamants'.format(i=i[0],j=i[1]), background=BACKGROUND).place(x=300, y=300+(Jeu.classement().index(i)*30))

def inigame():
    Vider()
    global Jeu
    global joueurcarte
    global diamants
    global reliques
    global coffre
    Jeu.melangeCarte()
    Jeu.joueurssortis = []
    
    if Jeu.manchesRestants == 0:
        return classement()

    # En jeu
    # Manche actuelle
    manche_text = TkFont.Font(size=30)
    manche = Label(root, text='Manche : '+str(6-Jeu.manchesRestants), bg=BACKGROUND, font=manche_text)
    manche.place(x=375, y=25)

    # Bouton quitter
    quitter_text = TkFont.Font(size=18)
    quitter = Button(root, text ="X", font=quitter_text, activebackground='red', command=accueil)
    quitter.place(x=950, y=650)

    # Statistiques du joueurs jouants
    stats = Label(root, text='Statistiques', bg=BACKGROUND, font=TkFont.Font(size=18, underline=True))
    stats.place(x=100, y=550)

    diamants = Label(root, text='Diamants : '+str(Jeu.joueurs[1][3]), bg=BACKGROUND, font=TkFont.Font(size=10))
    diamants.place(x=50, y=600)

    reliques = Label(root, text='Reliques : '+str(Jeu.joueurs[1][1]), bg=BACKGROUND, font=TkFont.Font(size=10))
    reliques.place(x=50, y=630)

    coffre = Label(root, text='Coffre : '+str(Jeu.joueurs[1][0]), bg=BACKGROUND, font=TkFont.Font(size=10))
    coffre.place(x=50, y=660)

    # Affichage des joueurs ainsi que leurs caractéristiques
    joueurcarte = [['affjoueur', 'affstatut', 'affdiamant', 'affrelique'] for i in range(1,Jeu.nbJoueurs+1)]
    joueurcarte.insert(0, 'test') # A CORRIGER
    for i in range(1,len(joueurcarte)):
        joueurcarte[i][0] = Label(root, text='Joueur '+str(i)+': ', bg=BACKGROUND)
        joueurcarte[i][0].place(x=850,y=80+i*70)

        joueurcarte[i][1] = Label(root, text='Explore', bg=BACKGROUND, fg='#58bf4e')
        joueurcarte[i][1].place(x=910,y=80+i*70)

        joueurcarte[i][2] = Label(root, text='Diamants : '+str(Jeu.joueurs[i][3]), bg=BACKGROUND)
        joueurcarte[i][2].place(x=850,y=100+i*70)

        joueurcarte[i][3] = Label(root, text='Reliques : '+str(Jeu.joueurs[i][1]), bg=BACKGROUND)
        joueurcarte[i][3].place(x=850,y=120+i*70)


    rester = Button(image=RESTERIMAGE, text='Rester', compound=TOP, activebackground='#a9f099', command=lambda:Jouer(0))
    rester.configure(bg=BACKGROUND)  # Met la couleur du fond en fond de l'image PNG
    rester.place(x=320, y=450)

    sortir = Button(image=SORTIRIMAGE, text='Sortir', compound=TOP, activebackground='#f09999', command=lambda:Jouer(1))
    sortir.configure(bg=BACKGROUND)  # Met la couleur du fond en fond de l'image PNG
    sortir.place(x=520, y=450)



    joueurcarte[1][1]["text"]='Joue...'
    joueurcarte[1][1]["fg"]='#de96ff'

    carte_tapis = Jeu.cartes[-1]
    if type(carte_tapis) == int:
        carte = Label(image=choice(CARTE_DIAMANT))
    else:
        carte = Label(image=CARTE_SPECIAL[carte_tapis])
    carte.configure(bg=BACKGROUND)  # Met la couleur du fond en fond de l'image PNG
    if len(Jeu.tapis) < 6:
        carte.place(x=10+100*len(Jeu.tapis), y=100)
    elif len(Jeu.tapis) < 14:
        carte.place(x=10+100*(len(Jeu.tapis)-7), y=200)
    elif len(Jeu.tapis) < 21:
        carte.place(x=10+100*(len(Jeu.tapis)-7), y=300)
    if not(Jeu.piocheCarte()): 
            # APPLIQUE CARTE (donc vérifier joueurs sortis etc.)
            Jeu.sortie(Jeu.joueurssortis)   
    for i in range(1,Jeu.nbJoueurs+1):
        joueurcarte[i][2]["text"] = 'Diamants : '+str(Jeu.joueurs[i][3])
        joueurcarte[i][3]["text"] = 'Reliques : '+str(Jeu.joueurs[i][1])


accueil()

root.mainloop()


# Max 25 cartes
# Pioche de cartes (récupérer cartes offi)
# Fond officiel du plateau
# Jeu fonctionnel enft 
# sleep entre les tours pour rendre + cohérent 