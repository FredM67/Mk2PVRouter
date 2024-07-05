.. _carte-mere-mono-E:

Composants de la configuration E
================================

| Cette section décrit l'assemblage d'un routeur équipé d'un émetteur ou récepteur radiofréquence, permettant de contrôler une ou plusieurs charges à distance.
| 
| Ce montage peut inclure de 0 à 7 sorties triac et/ou relais. La tension d'alimentation du système doit être de **3,3 V**.

.. contents:: Sommaire
    :local:
    :depth: 1

Socles de sorties
-----------------

| Deux sorties sont natives sur les programmes standards du routeur MK2.
| Les emplacements **D3** et **D4** les représentent. Il faudra alors les utiliser en premier.
| 
| Soudez les socles **D3** et **D4** en fonction du nombre de sorties (triac et/ou relais) utilisées dans le kit.

.. include:: sorties.rst

.. warning::
   L'utilisation des autres emplacements de sortie nécessitera la modification des programmes standards.

Si vous avez besoin de plus de deux sorties triac et/ou relais, vous pouvez souder directement les socles **D5 à D9**.

.. include:: alim-3_3.rst

Ponts ou *jumpers*
------------------

Selon le mode de fonctionnement, des *jumpers* différents devront être soudés :
* mode **émetteur** : soudez les *jumpers* **J6 à J8**.
* mode **récepteur** : soudez le *jumper* **J15**.

.. warning::
   La résistance **R8** ne devra pas être mise en place.

Résistances
-----------

Aucune résistance n'est nécessaire.

.. include:: connecteur-nappe.rst

.. include:: module-rf.rst
