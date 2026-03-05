.. _carte-indicateur:

====================
Carte indicateur LED
====================

⏱️ **Temps estimé** : 15–30 min par carte (débutant), 10–15 min (expérimenté)

🔧 **Niveau de difficulté** : Débutant

⚠️ **Niveau de risque** : Faible

.. admonition:: 📋 Prérequis

   Avant de commencer ce chapitre :

   | ☐ Chapitre :ref:`safety-overview` lu et compris
   | ☐ Fer à souder et fil de soudure à disposition
   | ☐ Carte de sortie correspondante assemblée — triac (voir :ref:`carte-sortie`) ou relais (voir :ref:`carte-sortie-relais`)

Vue d’ensemble
--------------

La carte indicateur est un petit :term:`PCB` dédié qui porte une LED témoin. Elle permet de visualiser l’état de chaque sortie, qu’il s’agisse d’une sortie :term:`triac` (voir :ref:`carte-sortie`) ou d’une sortie relais (voir :ref:`carte-sortie-relais`) :

- **LED allumée** : la sortie est active (courant passe)
- **LED éteinte** : la sortie est inactive (courant coupé)
- **LED clignotante** : régulation en cours (voir :ref:`principe-fonctionnement:Fonctionnement des LED`)

Il faut **une carte indicateur par étage de sortie** (triac ou relais). Chaque carte se connecte au signal de commande de l’étage de sortie correspondant via un câble Molex 2 broches.

Images de la carte
------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Face avant (assemblée)
     - Face arrière (assemblée)
   * - .. figure:: ../img/indicator-front.png
          :alt: Carte indicateur — face avant assemblée
          :class: clickable-img

     - .. figure:: ../img/indicator-back.png
          :alt: Carte indicateur — face arrière assemblée
          :class: clickable-img

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Circuit imprimé nu — face avant
     - Circuit imprimé nu — face arrière
   * - .. figure:: ../img/indicator-bare-front.png
          :alt: Carte indicateur — PCB nu face avant
          :class: clickable-img

     - .. figure:: ../img/indicator-bare-back.png
          :alt: Carte indicateur — PCB nu face arrière
          :class: clickable-img

Liste des composants
--------------------

La carte ne comporte que 3 composants :

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Composant
     - Description
   * - Résistance 1 kΩ
     - Limitation du courant dans la LED (marquée **R1** sur la sérigraphie avant)
   * - Connecteur Molex 2 broches
     - Signal de commande depuis l’étage de sortie ou la seconde rangée de connecteurs Molex de la carte-mère
   * - LED
     - Témoin visuel (couleur au choix)

Assemblage
----------

.. important::
   Cette carte est à **double face** : la résistance et le connecteur se soudent sur la face **avant**, tandis que la LED se soude sur la face **arrière**. Consultez les images du :term:`PCB` nu ci-dessus pour repérer les emplacements.

La sérigraphie de la face avant montre l’empreinte de la LED avec des **points** : il s’agit d’un simple rappel visuel. Les pastilles réelles de la LED, avec les marquages ``+`` et ``-``, se trouvent sur la sérigraphie de la face **arrière**.

Ordre de soudure
~~~~~~~~~~~~~~~~~

**Étape 1 : Face avant — Résistance**

#. Placer la carte face avant vers le haut
#. Insérer la résistance (1 kΩ) dans l’emplacement marqué **R1**
#. Souder et couper les pattes excédentaires

**Étape 2 : Face avant — Connecteur**

#. Insérer le connecteur Molex 2 broches dans son emplacement (à côté de la résistance)
#. Souder les 2 broches

**Étape 3 : Face arrière — LED**

#. Retourner la carte (face arrière vers le haut)
#. Insérer la LED en **respectant la polarité** : la patte longue (anode, ``+``) correspond au marquage ``+`` sur la sérigraphie
#. Souder et couper les pattes excédentaires

.. warning::
   Respectez la polarité de la LED. Si elle est montée à l’envers, elle ne s’allumera pas. En cas de doute, la patte la plus **longue** est l’anode (``+``).

Montage dans le boîtier
~~~~~~~~~~~~~~~~~~~~~~~~

La LED dépasse à travers un trou dans le couvercle du boîtier (perçage de 3 mm, voir :ref:`percages`). La carte est fixée sur la face intérieure du couvercle.

Connexion
~~~~~~~~~

Le connecteur Molex se raccorde au signal de commande, via un câble Molex 2 fils. Le signal peut provenir soit de l’étage de sortie, soit de la seconde rangée de connecteurs Molex sur la carte-mère. Consultez :ref:`confection-cables` pour les longueurs recommandées.

.. admonition:: ✅ Point de Contrôle — Carte Indicateur

   Avant de continuer, vérifiez pour chaque carte indicateur :

   | ☐ Résistance et connecteur soudés sur la face **avant**
   | ☐ LED soudée sur la face **arrière**, polarité respectée
   | ☐ Aucun pont de soudure entre les pastilles
   | ☐ La LED s’allume lorsque le signal de commande est actif (test optionnel avec la carte-mère)
