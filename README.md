# Diamants

**Auteurs :** Eliott, Chakib  
**Années :** 2022-2023
**GitHub :** [https://github.com/Chakib-Eliott/sae-1.01](https://github.com/Chakib-Eliott/sae-1.01)

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
Le troisième bug était qu'on **n'attribuait jamais les bonus de la relique**. Ce bug a rapidement été réglé après le rajout du bonus.

## Idées

Afin d'améliorer notre programme, nous avons décidé de **nettoyer (clear) le terminal à chaque interraction** différente afin d'avoir un terminal clair et cohérent avec l'action du jeu.<br>
Nous avons aussi **ajouté des couleurs à ce terminal** pour le rendre plus lisible.<br>
Au lancement du jeu vous **choisissez directement la version du jeu**, soit dans le terminal soit avec l'interface graphique, et vous pouvez même rentrer ce choix avec des **arguments** après la commande Python.<br>
Pour mieux implémenter le jeu dans le terminal et l'interface graphique, nous avons décidé de construire le module `diamants.py` avec une classe (**Class**).

## Captures d'écran

*à ajouter*

<br>

[*Lien vers le sujet.*](https://ecampus.paris-saclay.fr/pluginfile.php/1965841/mod_resource/content/0/sae01_diamants.pdf)

<br>
&copy; Eliott / Chakib