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

Pour utiliser les emplacements **D2**, **D10**, **D11**, **D12** et **D13**, il est nécessaire de souder non seulement les socles, mais aussi les ponts *Jumpers* associés.<br />
Pour ce faire, faites fondre de l'étain sur chaque partie du *jumper* et ajoutez-en suffisamment pour relier les deux parties ensemble.

Voici l'assignation de chaque *jumper* :
- pour **D2**, soudez **J16**.
- pour **D10**, soudez **J17**.
- pour **D11**, soudez **J18**.
- pour **D12**, soudez **J19**.
- pour **D13**, soudez **J20**.