.. _carte-mere-mono-C:

Composants de la configuration C
================================

| Cette section explique comment assembler un routeur avec 3 à 7 sorties triac et un afficheur à 7 segments.
| L’option radiofréquence n’est pas supportée.
| 
| L’installation des circuits intégrés **IC3** et **IC4** est indispensable.
| Comme ces circuits ne sont pas disponibles en **3,3 V**, il est nécessaire d’alimenter le routeur en **5 V**.
| Le régulateur de tension **VR1** doit être une version **5 V**.

.. contents:: Sommaire
   :local:
   :depth: 1

Socles de sorties
-----------------

| Deux sorties sont natives sur les programmes standards du routeur MK2.
| Les emplacements **D3** et **D4** les représentent. Il faudra alors les utiliser en premier.

.. include:: ../common/sorties.inc.rst

.. warning::
   L’utilisation des autres emplacements de sortie nécessitera la modification des programmes standards.


.. warning::
   Les emplacements **D5 à D9** ne sont pas utilisables, car ces pins sont utilisés par l’afficheur !

.. include:: jumpers-Dx.rst

.. note::
   Ne soudez aucun autre *jumper* !

Résistances
-----------

| Associez les résistances fournies dans le kit aux emplacements indiqués sur la couche sérigraphiée. Il n’y a pas de polarité à respecter.
| Les résistances à souder sont **R11 à R18**.

Ponts ou *jumpers*
------------------

| Les résistances doivent être connectées à l’aide de ponts en étamant chaque *jumper* correspondant.
| Pour ce faire, faites fondre de l’étain sur chaque partie du *jumper*, puis ajoutez-en suffisamment pour relier les deux parties ensemble.
| Vous devez connecter les *jumpers* **J1 à J14**.

.. include:: ic3-ic4.inc.rst

.. include:: connecteur-nappe.inc.rst