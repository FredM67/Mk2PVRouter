(carte-mere-mono-A)=

# Composants de la configuration A

L’assemblage décrit dans cette partie est pour un routeur comprenant 1 à 12 sorties triac et/ou relais. Les options afficheur 7 segments et radiofréquence ne pourront pas être prises en compte.


```{hint}
Pour avoir une option sortie relais avec un afficheur une seconde carte mère peut être installée.<br />
Veuillez remplir un formulaire sur notre site internet pour cette demande.
```

## Socles de sorties
Deux sorties sont natives sur les programmes standards du routeur MK2.<br />
Les emplacements **D3** et **D4** les représentent. Il faudra alors les utiliser en premier.

Soudez les socles **D3** et **D4** en fonction du nombre de sorties (triac et/ou relais) utilisées dans le kit.

Chaque sortie est dispose de deux emplacements :
- un emplacement à 3 positions. Les 3 positions correspondent à la **masse** (ou **-**), la sortie du microcontrôleur ainsi que le **+** (tension de fonctionnement du système).
- un emplacement à 2 positions. Les 2 positions correspondent à la **masse** et la sortie du microcontrôleur.

Pour une sortie triac, on pourra utiliser indifféremment l'un ou l'autre emplacement, en veillant à souder/câbler les 2 broches **-** et centrale.<br />
Le deuxième emplacement pourra recevoir le connecteur du témoin LED. Selon les préférences de chacun, ce témoin pourra aussi être câblé via la carte de sortie elle-même.

Pour une sortie relais, il est nécessaire d'utiliser l'emplacement à 3 positions.<br />
En effet, un relais nécessite pour fonctionnement une alimentation permanente, ainsi qu'un fil de commande.<br />
Cette alimentation sera fournie par les broches **+**  et **-**, la commande sera câblée via la broche centrale.<br />
Le deuxième emplacement recevra le connecteur du témoin LED.

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