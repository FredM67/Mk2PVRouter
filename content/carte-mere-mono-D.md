(carte-mere-mono-D)=

# Composants de la configuration D

Cette section décrit l'assemblage d'un routeur équipé d'un émetteur ou récepteur radiofréquence. Cette option permet de contrôler une ou plusieurs charges à distance.

Le montage peut inclure de 0 à 2 sorties triac et/ou relais locales, ainsi qu'un afficheur à 7 segments avec des modules d'économie de broches.<br />
La tension d'alimentation de la carte-mère doit être de **5 V**, un régulateur de tension approprié est fourni à cet effet.

Le module radiofréquence doit être alimenté en **3,3 V**.</br />
Pour cela, nous abaissons la tension pour la partie alimentation de la carte RF en ajoutant un régulateur de tension supplémentaire.

## Socles de sorties

Deux sorties sont natives sur les programmes standards du routeur MK2.<br />
Les emplacements **D3** et **D4** les représentent.

```{eval-rst}
.. include:: sorties.md
   :parser: myst_parser.sphinx_
```

```{warning}
Les emplacements **D2 et D5 à D13** ne sont pas utilisables, car ces pins sont utilisés par l'afficheur ainsi que le module RF !
```

```{eval-rst}
.. _alim-3_3:

Alimentation secondaire **3,3 V**
---------------------------------

.. include:: alim-3_3.md
   :parser: myst_parser.sphinx_
```

## Ponts ou *jumpers*

Dans le seul cas où la carte-mère est utilisée en **récepteur**, le *jumper* **J15** doit être soudé.

```{warning}
La résistance **R8** ne devra pas être mise en place.
```

## Résistances

Associez les résistances fournies dans le kit aux emplacements indiqués sur la couche sérigraphiée. Il n'y a pas de polarité à respecter.<br />
Les résistances à souder sont **R11 à R18**.

```{note}
Si le système dispose d'une alimentation secondaire en **3,3 V**, un jeu de 6 résistances, repérées **R21 à R26**, devra être soudé aux emplacements correspondants.
```

```{admonition} Rappel
Si la carte mère est utilisée en mode récepteur radiofréquence, alors la résistance **R8** ne doit pas être soudée !
```

## Socles **IC3** et **IC4**

Ils doivent être placés selon le repérage sur la couche sérigraphiée.

```{warning}
Circuits intégrés CD4543 et 74HC138<br />
Ne pas installer ces composants pour le moment !
```

## Connecteur pour nappe

Soudez le connecteur **CN1** pour l'afficheur.<br />
Assurez-vous de le positionner correctement en suivant les indications sur la couche sérigraphiée.

```{eval-rst}
.. _module-rf:

Module radiofréquence
---------------------

.. include:: module-rf.md
   :parser: myst_parser.sphinx_
```