# Diamants

## Description

**Diamants** est un jeu de société. Il a été ici développé sur Python pour pouvoir y jouer sur ordinateur par Eliott et Chakib.

## Règle du jeu

Les règles officiels du jeu sont disponibles [ici](https://iello.fr/wp-content/uploads/2022/07/DIAMANT_regles.pdf).<br>
Le but de ce jeu est de gagner le plus de diamants durant **5 expéditions** dans des mines.<br>
Pendant les expéditions, les joueurs choisissent entre **rester** dans la grotte ou y **sortir**. Les joueurs font ce choix par rapport aux cartes qui sortent à chaques tours. Les cartes qui peuvent sortir sont :
 - des cartes diamants
 - des cartes pièges
 - des cartes reliques

Les cartes diamants comportent un trésor qui sera partagé entre tous les participants de l'expédition et le reste du trésor sera redéposé sur la carte. Le reste des diamants peut être récupéré si vous sortez de la grotte, le trésor est donc partagé avec tous les joueurs sortant.
Les cartes pièges peuvent vous faire perdre tous vos diamants récoltés pendant votre expédition si un piège sort 2 fois.
Les reliques sont des cartes qui rapporte beaucoup de diamants à la fin de la partie mais pour la récupérer il faut être le seul joueur à sortir.

## Contenu du jeu

- 15 cartes trésors (1,2,3,4,5,5,7,7,9,11,11,13,14,15,17)
- 15 cartes pièges (3 araignées, 3 serpents, 3 laves, 3 boulets, 3 béliers)
- 5 reliques

## Fonctionnement

Pour lancer le jeu il vous suffit d'aller dans le répertoire où est le programme Python dans un terminal et taper la commande suivante :
```bash
python3 main.py [arg]
```
*Le 'Python3' peut parfait être simplement 'Python'.*<br>
Dans l'argument 'arg' il faut que vous mettre un argument qui va lancer le jeu dans le mode que vous voulez. Si vous ne mettez pas d'argument le jeu va vous le demander par la suite.<br>
Les arguments possibles :
 - terminal
 - graphique

<br>
&copy; Eliott / Chakib