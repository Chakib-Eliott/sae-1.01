"""
VERSION GRAPHIQUE

AUTEURS : Eliott & Chakib
"""
import tk # Tkinter pour l'affichage graphqiue du jeu
import diamants # Les fonction qui permettent de faire fonctionner le jeu

from tkinter import *
from PIL import Image, ImageTk

WIDTH="600"
HEIGHT="400"
BACKGROUND = '#DBC797'
root = Tk()
root.geometry(WIDTH+'x'+HEIGHT)  
root.resizable(width=False, height=False)
root.configure(bg=BACKGROUND)
root.grid_columnconfigure((0,1,2,3,4,5,6), minsize=30, weight=1)


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

bots = Checkbutton(root, text = "Bots", height = 2, width = 10, bg=BACKGROUND, activebackground=BACKGROUND)
bots.grid(row= 1, column= 3)






reduire = Button(root, text ="Réduire", command = minusplayer)
reduire.grid(row= 3, column= 2)

labelnbjoueurs = Label(root, text='Nombre de joueurs', bg=BACKGROUND)
labelnbjoueurs.grid(row=2, column=3)

cmd = root.register(lambda s: not s or (s.isdigit() and  int(s) >= 3 and int(s)< 9))
nbPlayers = Entry(root, validate="key", vcmd=(cmd, "%P"), width=5)
nbPlayers.grid(row= 3, column= 3)
nbPlayers.insert(0, "3")
nbPlayers.bind("<Return>")  


augmenter = Button(root, text ="Augmenter", command = plusplayer)
augmenter.grid(row= 3, column= 4)


jouer = Button(root, text ="JOUER!")
jouer.grid(row= 4, column= 3)

root.mainloop()
