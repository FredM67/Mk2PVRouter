(introduction)=

# Introduction

Cette documentation est applicable à toutes les versions du Mk2PVRouter, qu'elles soient monophasées ou triphasées.<br />
La majorité des informations sont pertinentes pour les deux versions.<br />
Chaque version a son propre chapitre.

---
## Contenu du kit

Dans le kit, vous trouverez :
- le circuit imprimé ({term}`PCB`) de la carte-mère
- un ou plusieurs circuits imprimés pour chaque sortie
- des composants électroniques (résistances, condensateurs, …).<br />
  Attention, certains sont sensibles à l'électricité statique, il faut donc les manipuler avec soin.
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
## Recommandations pour les étapes de soudure

Les composants nécessaires sont très variés. Certains sont passifs (comme les résistances), tandis que d'autres sont actifs (comme l'AtMega328P).<br />
Tous ces composants sont généralement sensibles à l'électricité statique.<br />
Il est donc important de les manipuler avec soin et, si possible, de se mettre à la terre pour éviter toute décharge électrostatique.

Certains composants sont polarisés (comme les diodes et certains condensateurs), tandis que d'autres ne le sont pas (comme les résistances et certains condensateurs). Il est donc crucial de faire attention à l'orientation des composants AVANT de les souder. L'orientation est généralement indiquée directement sur la carte mère.

Les composants varient également en taille, allant de quelques millimètres à plusieurs centimètres (dans le cas des transformateurs).

Pour des raisons pratiques, il est recommandé de procéder à la soudure en suivant un ordre précis basé sur la taille des composants.

Ainsi, l'ordre de soudure recommandé est le suivant :
1. Résistances et diodes, et éventuellement les ponts
2. Supports IC1 et IC2 (et éventuellement IC3, IC4 selon le kit) (ne pas insérer les circuits intégrés dans les supports à ce stade)
3. Condensateurs non polarisés "orange", oscillateur
4. Pont·s de diodes
5. Tous les connecteurs SIL noirs et le connecteur d'affichage, le cas échéant
6. Condensateurs polarisés (noirs ou bleus)
7. Le socle pour l'antenne, le cas échéant
8. Les gros connecteurs "haute tension"
9. Les porte-fusibles
10. Les régulateurs de tension
11. Enfin, les transformateurs

Suivre cette séquence précise permet d'éviter de tordre les pattes des composants ou d'avoir à utiliser de l'adhésif, entre autres.

---
## Matériels nécessaires

- fer à souder
- fil de soudure
- pince coupante
- pince à sertir les cosses ou pince multifonction
- tournevis cruciforme
- clé plate ou douille de **5,5**
- clé plate de **10**
- clé six pans de **2** et **2,5**
- une perceuse à colonne si possible, sinon n'importe quelle perceuse.
- foret métal de **3 mm**
- foret métal de **4 mm**
- foret (bois ou métal) de **8 mm**
- foret (bois ou métal) ou fraise de **20 mm**
- fraise de **35 mm**
- colle thermofusible
- gaine thermorétractable
- multimètre (au minimum voltmètre et ohmmètre)

Certains matériels sont optionnels (fraise de 35, colle, gaine). Cependant, ils faciliteront certaines étapes et permettront de réaliser un travail plus soigné et bien fini.