(carte-mere-mono-A)=

# Composants de la configuration A

Cette section décrit l'assemblage d'un routeur pouvant comporter de 1 à 12 sorties triac et/ou relais.<br />
Les options d'afficheur à 7 segments et de radiofréquence ne sont pas prises en charge.

```{hint}
Pour avoir une option sortie relais avec un afficheur une seconde carte mère peut être installée.<br />
Veuillez remplir un formulaire sur notre site internet pour cette demande.
```

## Socles de sorties

Deux sorties sont natives sur les programmes standards du routeur MK2.<br />
Les emplacements **D3** et **D4** les représentent. Il faudra alors les utiliser en premier.

Soudez les socles **D3** et **D4** en fonction du nombre de sorties (triac et/ou relais) utilisées dans le kit.

```{eval-rst}
.. include:: sorties.md
   :parser: myst_parser.sphinx_
```

```{warning}
L'utilisation des autres emplacements de sortie nécessitera la modification des programmes standards.
```

Si vous avez besoin de plus de deux sorties triac et/ou relais, vous pouvez souder directement les socles **D5**, **D6**, **D7**, **D8** et **D9**.

```{eval-rst}
.. include:: jumpers-Dx.md
   :parser: myst_parser.sphinx_
```