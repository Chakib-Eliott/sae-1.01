"""
VERSION GRAPHIQUE

AUTEURS : Eliott & Chakib
"""
import diamants # Les fonction qui permettent de faire fonctionner le jeu
from tkinter import *
import tkinter.font as TkFont

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




def accueil():
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

def Jouer():
    pass

def Vider():
    for widget in root.winfo_children():
        widget.destroy()

accueil()




root.mainloop()
