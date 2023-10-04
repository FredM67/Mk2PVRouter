# Introduction

Cette documentation couvre toutes les versions du Mk2PVRouter, monophasée, comme triphasée.  
L'essentiel des informations est valable pour les 2 versions.  
Chacune des versions dispose de son chapitre dédié.

---
## Contenu du kit

Dans le kit, vous trouverez :
- le circuit imprimé ({term}`PCB`) de la carte-mère
- un ou plusieurs circuits imprimés pour chaque sortie
- des composants électroniques (résistances, condensateurs, ...). Attention, certains sont sensibles à l'électricité statique, il faut donc les manipuler avec soin
- un boîtier
- des câbles

---
## Étapes d'assemblage

L'assemblage complet va nécessiter plusieurs étapes :
- soudure et tests de la carte-mère
- soudure et tests de la ou les cartes de sortie
- perçage du boîtier
- perçage du ou des dissipateurs thermiques
- montage des circuits soudés dans le boîtier
- confection des câbles
- câblage
- étalonnage
- programmation finale

---
## Conseils pour les étapes de soudure

Les composants nécessaires sont très variés. Certains composants sont passifs (résistances, ...), d'autres sont actifs (AtMega, ...).
D'une manière générale, il faut considérer que tous les composants sont sensibles à l'électricité statique.
Il faut donc les manipuler avec soin, dans la mesure du possible, le corps humain doit être relié à la terre.

Certains composants sont polarisés (diodes, certains condensateurs, ...), d'autres ne le sont pas (résistances, certains condensateurs). Faites très attention au sens AVANT de souder. Le sens est réparable directement sur la carte-mère.

Ces composants sont aussi de tailles très différentes. Des plus petits, avec quelques millimètres d'épaisseur/diamètre aux plus gros avec plus centimètres d'épaisseur (transformateurs).

Pour des raisons pratiques, il est conseillé de procéder strictement par ordre de taille.
Ainsi, on soudera dans cet ordre :
1. résistances et diodes, ponts le cas échéant
2. supports IC1 et IC2 (voire IC3, IC4 selon le kit) (ne pas insérer les circuits intégrés dans les supports)
3. condensateurs "orange" non polarisés, oscillateur
4. pont(s) de diodes
5. tous les connecteurs SIL noirs et le connecteur d'affichage, le cas échéant
6. condensateurs polarisés (noir ou bleu)
7. le socle pour l'antenne, le cas échéant
8. le(s) gros connecteur(s) "haute tension"
9. le(s) porte-fusible
10. le ou les régulateur(s) de tension
11. enfin le(s) transformateur(s)

Cet ordre précis permet de s'affranchir de tordre les pattes des composants, utiliser de l'adhésif, ...

---

## Matériels nécessaires

- fer à souder
- fil de soudure
- pince coupante
- pince à sertir les cosses ou pince multifonction
- tournevis cruciforme
- clés plates ou douilles de 5,5 et 10
- clé six pans de 2 et 2,5
- une perceuse à colonne si possible, sinon n'importe quelle perceuse.
- foret métal de **3 mm**
- foret métal de **4 mm**
- foret (bois ou métal) de **8 mm**
- foret (bois ou métal) ou fraise de **20 mm**
- fraise de **35 mm**
- colle thermofusible
- gaine thermorétractable
- multimètre (au minimum voltmètre et ohmmètre)

Certains matériels sont optionnels (frais de 35, colle, gaine). Cependant, ils faciliteront certaines étapes et permettront de faire du travail plus propre et bien fini.