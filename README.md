# Diamants

![iut-velizy](http://eliott-b.tech/iut-velizy/IUT%20Velizy%20Villacoublay%20logo%202020%20ecran.png)

**Auteurs :** Eliott, Chakib  
**Années :** 2022-2023   
**GitHub :** [https://github.com/Chakib-Eliott/sae-1.01](https://github.com/Chakib-Eliott/sae-1.01)  
**IA liée au jeu :** [https://github.com/Chakib-Eliott/sae-1-02](https://github.com/Chakib-Eliott/sae-1-02)  

## Sommaire

- [Diamants](#diamants)
  - [Sommaire](#sommaire)
  - [Description](#description)
  - [Règle du jeu](#règle-du-jeu)
  - [Contenu du jeu](#contenu-du-jeu)
  - [Fonctionnement](#fonctionnement)
  - [Bugs rencontrés](#bugs-rencontrés)
  - [Idées](#idées)
  - [Illustration des cartes](#illustration-des-cartes)
  - [Captures d'écran](#captures-décran)

## Description

**Diamants** est un jeu de société. Il a été ici développé sur Python pour pouvoir y jouer sur ordinateur par Eliott et Chakib.<br>
Ce projet a été développé afin de réaliser une SAé à l'**IUT de Vélizy** pendant le 1er semestre du BUT 1.

## Règle du jeu

Les règles officiels du jeu sont disponibles [ici](https://iello.fr/wp-content/uploads/2022/07/DIAMANT_regles.pdf).<br>
Le but de ce jeu est de gagner le plus de diamants durant **5 expéditions** dans des mines.<br>
Pendant les expéditions, les joueurs choisissent entre **rester** dans la grotte ou y **sortir**. Les joueurs font ce choix par rapport aux cartes qui sortent à chaques tours. Les cartes qui peuvent sortir sont :
 - des **cartes diamants**
 - des **cartes pièges**
 - des **cartes reliques**

Les cartes diamants comportent un trésor qui sera **partagé entre tous les participants** de l'expédition et le reste du trésor sera redéposé sur la carte. Le reste des diamants peut être récupéré si vous sortez de la grotte, le trésor est donc partagé avec tous les joueurs sortant.<br>
Les **cartes pièges** peuvent vous faire **perdre tous vos diamants** récoltés pendant votre expédition si un piège sort 2 fois.<br>
Les reliques sont des cartes qui rapporte beaucoup de diamants à la fin de la partie mais pour la récupérer il faut être le seul joueur à sortir. Les diamants des reliques sont par rapport à quand est-ce que vous les avez obtenu :
- **1ère** relique : **5** diamants
- **2ème** relique : **5** diamants
- **3ème** relique : **5** diamants
- **4ème** relique : **10** diamants
- **5ème** relique : **10** diamants

## Contenu du jeu

- **15 cartes trésors** (1,2,3,4,5,5,7,7,9,11,11,13,14,15,17)
- **15 cartes pièges** (3 araignées, 3 serpents, 3 laves, 3 boulets, 3 béliers)
- **5 reliques**

## Fonctionnement

Pour lancer le jeu il vous suffit d'aller **dans le répertoire où est le programme Python** dans un terminal et taper la commande suivante :
```bash
python3 main.py [arg]
```
*Le 'Python3' peut parfait être simplement 'Python'.*<br>
Dans l'argument 'arg' il faut que vous mettre un argument qui va lancer le jeu dans le mode que vous voulez. Si vous ne mettez pas d'argument le jeu va vous le demander par la suite.<br>
Les arguments possibles :
 - **terminal**
 - **graphique**

## Bugs rencontrés

Lors de la réalisation du projet, nous avons fait face à plusieurs bugs.<br>
Le premier bug était un bug sur les **vérifications des monstres**. En effet nous vérifions si un monstre sortait et on retournait `True` si il était déjà sorti. Mais nous analysons jamais ce booléen et donc cela ne stoppait jamais la partie. Nous avons donc analysé ce booléen dans la fonction `piocheCarte`<br>
Le deuxième bug était un **problème de type**. Nous avions utilisé un dictionnaire pour représenter le tapis mais le dictionnaire n'était pas le type le plus adapté à ce problème vu que les cartes ne pouvaient donc pas sortir deux fois et on avait donc un problème de tour 'vide'. Nous avons donc remplacé la type du tapis par une liste à 2 dimensions.<br>
Le troisième bug était qu'on **n'attribuait jamais les bonus de la relique**. Ce bug a rapidement été réglé après le rajout du bonus.<br>
Le quatrième bug était qu'on ne pouvait pas utiliser les 'print format' de la manière suivante avec les machines de l'IUT :
```python
text = "Hello World!"
print(f"{text}")
```
Nous avons donc modifié nos 'print' afin de les rendre utilisable avec la méthode suivante :
```python
print("Hello {w}!".format(w="World"))
```
Le cinquième bug était un bug où le **dernier joueur sorti ne récupérait jamais son bultin**. Nous avons règler ce problème après de longs moments d'analyse du code en remarquant que ne finissions le tour avant de faire jouer le joueur.<br>
Le sixième bug est que lors qu'on joue avec des **bots dans l'interface graphique**, on ne **voit pas leurs actions** et les tours se téléportent. Ce problème n'a pas pu être réglé car nous n'avons pas trouvé la solution compatible avec le module 'Tkinter' qui n'est pas adapté au module 'sleep'.

## Idées

Afin d'améliorer notre programme, nous avons décidé de **nettoyer (clear) le terminal à chaque interraction** différente afin d'avoir un terminal clair et cohérent avec l'action du jeu.<br>
Nous avons aussi **ajouté des couleurs à ce terminal** pour le rendre plus lisible.<br>
Au lancement du jeu vous **choisissez directement la version du jeu**, soit dans le terminal soit avec l'interface graphique, et vous pouvez même rentrer ce choix avec des **arguments** après la commande Python.<br>
Pour mieux implémenter le jeu dans le terminal et l'interface graphique, nous avons décidé de construire le module `diamants.py` avec une classe (**Class**).

## Illustration des cartes

Voici à quoi ressemble les cartes en jeu :
| Nom de la carte |                  Illustration                  |
| :-------------: | :--------------------------------------------: |
|   Diamants 1    | ![diamants1](asset/cartes/diamant-rubis-1.png) |
|   Diamants 2    | ![diamants2](asset/cartes/diamant-rubis-2.png) |
|    Reliques     |  ![relique](asset/cartes/diamant-relique.png)  |
|    Araignées    | ![araignees](asset/cartes/diamant-spiders.png) |
|    Serpents     |  ![serpents](asset/cartes/diamant-snake.png)   |
|     Boulets     |   ![boulets](asset/cartes/diamant-ball.png)    |
|     Béliers     |  ![beliers](asset/cartes/diamant-belier.png)   |
|      Laves      |    ![laves](asset/cartes/diamant-lava.png)     |

## Captures d'écran

- *Au démarage du jeu*<br>
![demarage](asset/captures/main.png)<br>
- *Affichage dans le terminal*<br>
![affichage-terminal](asset/captures/affichage-t.png)<br>
- *Classement dans le terminal*<br>
![classement-terminal](asset/captures/classement-t.png)<br>
- *Page d'accueil de l'interface graphique*<br>
![accueil-graphique](asset/captures/accueil-g.png)<br>
- *Partie dans l'interface graphique*<br>
![partie-graphique](asset/captures/partie-g.png)<br>
- *Classement dans l'interface graphique*<br>
![classement-graphique](asset/captures/classement-g.png)

*(Les images ont été prise sur un Mac, les graphismes de la page sont donc pas ceux d'un ordinateur sur Linux ou Windows)*

<br>

[*Lien vers le sujet.*](http://eliott-b.tech/sae_1_01/sae01_diamants.pdf)

<br>
&copy; Eliott / Chakib
