"""
VERSION GRAPHIQUE

AUTEURS : Eliott & Chakib

Ce jeu est développé dans le cadre d'une SAé (un projet) avec l'IUT de Vélizy.
"""
import diamants as D  # Les fonction qui permettent de faire fonctionner le jeu
from tkinter import *  # Natif à Python
import tkinter.font as TkFont  # Natif à Python

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

RESTERIMAGE = PhotoImage(file='./asset/diamant_rester.png')
SORTIRIMAGE = PhotoImage(file='./asset/diamant_sortir.png')


BOULETCARTE = PhotoImage(file='./asset/cartes/diamant-ball.png')
BELIERCARTE = PhotoImage(file='./asset/cartes/diamant-belier.png')
LAVECARTE = PhotoImage(file='./asset/cartes/diamant-lava.png')
RELIQUECARTE = PhotoImage(file='./asset/cartes/diamant-relique.png')
DIAMANTCARTE1 = PhotoImage(file='./asset/cartes/diamant-rubis-1.png')
DIAMANTCARTE2 = PhotoImage(file='./asset/cartes/diamant-rubis-2.png')
SERPANTCARTE = PhotoImage(file='./asset/cartes/diamant-snake.png')
ARAIGNEESCARTE = PhotoImage(file='./asset/cartes/diamant-spiders.png')


def accueil():
    Vider()
    def plusplayer():
        value = nbPlayers.get()
        if int(value) < 8:
            nbPlayers.delete(0,END)
            nbPlayers.insert(0,str(int(value)+1))

    def minusplayer():
        value = nbPlayers.get()
        if int(value) > 3:
            nbPlayers.delete(0,END)
            nbPlayers.insert(0,str(int(value)-1))
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
    jouer = Button(root, text ="JOUER!", font=jouer_text, activebackground='#89e37f', command=Vider)
    jouer.place(x=440, y= 300)

### EN CONSTRUCTION
def Jouer():
    print(len(Jeu.tapis))
    carte = Label(image=BOULETCARTE)
    carte.configure(bg=BACKGROUND)  # Met la couleur du fond en fond de l'image PNG
    if len(Jeu.tapis) < 7:
        carte.place(x=10+100*len(Jeu.tapis), y=100)
    elif len(Jeu.tapis) < 14:
        carte.place(x=10+100*(len(Jeu.tapis)-7), y=200)
    Jeu.piocheCarte()

def Vider():
    for widget in root.winfo_children():
        widget.destroy()

accueil()
Vider()

Jeu = D.Diamant(8, 0) # Création de la partie
Jeu.melangeCarte()



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
joueurcarte = [['affjoueur', 'affstatut', 'affdiamant', 'affrelique'] for i in range(Jeu.nbJoueurs)]
for i in range(len(joueurcarte)):
    joueurcarte[i][0] = Label(root, text='Joueur '+str(i+1)+': ', bg=BACKGROUND)
    joueurcarte[i][0].place(x=850,y=80+i*70)

    joueurcarte[i][1] = Label(root, text='Explore', bg=BACKGROUND, fg='#58bf4e')
    joueurcarte[i][1].place(x=910,y=80+i*70)

    joueurcarte[i][2] = Label(root, text='Diamants : '+str(Jeu.joueurs[i+1][3]), bg=BACKGROUND)
    joueurcarte[i][2].place(x=850,y=100+i*70)

    joueurcarte[i][3] = Label(root, text='Reliques : '+str(Jeu.joueurs[i+1][1]), bg=BACKGROUND)
    joueurcarte[i][3].place(x=850,y=120+i*70)


rester = Button(image=RESTERIMAGE, text='Rester', compound=TOP, activebackground='#a9f099')
rester.configure(bg=BACKGROUND)  # Met la couleur du fond en fond de l'image PNG
rester.place(x=320, y=450)

sortir = Button(image=SORTIRIMAGE, text='Sortir', compound=TOP, activebackground='#f09999', command=Jouer)
sortir.configure(bg=BACKGROUND)  # Met la couleur du fond en fond de l'image PNG
sortir.place(x=520, y=450)

root.mainloop()



# Max 25 cartes
# Pioche de cartes (récupérer cartes offi)
# Fond officiel du plateau
# Jeu fonctionnel enft 
# sleep entre les tours pour rendre + cohérent 