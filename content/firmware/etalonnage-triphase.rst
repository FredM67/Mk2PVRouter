.. _etalonnage-triphase:

=====================
Étalonnage — Triphasé
=====================

⏱️ **Temps estimé** : 1–2 heures

🔧 **Niveau de difficulté** : Avancé

⚠️ **Niveau de risque** : Élevé (manipulation 230 V sous tension)

.. admonition:: 📋 Prérequis

   Avant de commencer ce chapitre :

   | ☐ Chapitre :ref:`safety-overview` lu et compris
   | ☐ Tests électriques effectués (voir :ref:`tests-electriques`)
   | ☐ Firmware installé et fonctionnel (voir :ref:`logiciel-triphase`)
   | ☐ Routeur alimenté par le secteur
   | ☐ Un appareil de référence : wattmètre, pince wattmétrique ou affichage du Linky
   | ☐ Une forte charge résistive (bouilloire, radiateur, chauffe-eau), qui fonctionne sans passer par le routeur

.. important::
   L’étalonnage est **obligatoire** en triphasé. Le routeur calcule la somme algébrique des puissances instantanées des trois phases : une seule phase mal mesurée fausse la somme, donc le routage de l’énergie excédentaire.

   Les composants électroniques ne sont jamais parfaits : chacun a une tolérance, classiquement de 5 ou 10 %. Étalonner chaque ligne de mesure rend la somme finale la plus juste possible.

.. contents:: Sommaire
    :local:
    :depth: 2

Ce qu’il vous faut
------------------

.. danger::
   **ALERTE SÉCURITÉ**

   Installer les pinces et l’appareil de référence demande de modifier le câblage électrique. Avant toute manipulation, coupez l’alimentation au tableau et vérifiez l’absence effective de tension avec un testeur. Dans le doute, coupez le disjoncteur principal.

* **Une lecture de référence par phase**, prise en même temps que celle du routeur : un wattmètre enfichable ou une pince wattmétrique sur le câble de la phase.
* **L’affichage du Linky**, si vous n’avez rien d’autre : il donne la puissance **totale**, des trois phases, en puissance apparente (VA), avec un rafraîchissement lent ; VA et W ne sont égaux qu’avec une charge purement résistive. Il ne sert donc de référence qu’avec **une seule charge, sur une seule phase**, et toutes les autres consommations de la maison éteintes. Dès qu’il y a une autre consommation, prenez un appareil qui mesure une phase à la fois.
* **Une forte charge résistive** (bouilloire, radiateur, chauffe-eau) : au moins 300 W, car en dessous la correction est imprécise. Un appareil purement résistif, sans ventilateur ni électronique, simplifie grandement l’étalonnage. **Elle doit fonctionner sans passer par le routeur** : le mode étalonnage ne commute rien, donc une charge reliée à une sortie triac du routeur reste éteinte. Branchez une bouilloire ou un radiateur sur une prise, ou faites marcher le chauffe-eau par son propre contacteur, en position forcée.
* **Une consommation constante pendant l’étalonnage** : branchez la charge résistive et débranchez tout le reste, y compris votre ou vos systèmes de production d’électricité.
* **Les pinces installées sur la phase correspondante**, par rapport à l’alimentation du routeur : la pince de la phase **L1** sur la phase branchée au connecteur **L1** du routeur, et ainsi de suite.
* **Le** :ref:`configurateur <configurateur-triphase>`, qui fait le calcul pour vous et réécrit votre ``calibration.h``.
* Votre ``calibration.h`` (celui du dossier du firmware), si vous l’avez déjà modifié : le configurateur peut le charger.

Étalonner avec le configurateur
-------------------------------

Le routeur est étalonné en mode étalonnage : il mesure, sans rien commuter, et affiche ses mesures sur le moniteur série. Le configurateur règle ce mode, calcule les nouvelles valeurs à partir de vos relevés et réécrit ``calibration.h``.

Les valeurs, selon la carte
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le fichier ``calibration.h`` contient un jeu de valeurs par carte-mère, et le routeur utilise celui de ``PCB_VERSION`` (dans ``config.h``). Le configurateur ne montre et ne corrige que celles de la carte que vous avez choisie dans la page :

.. list-table::
   :header-rows: 1

   * - Carte
     - Puissance (pour le routage)
     - Tension (pour l’affichage)
   * - Ancienne carte triphasée (``PcbVersion::OLD``)
     - ``f_powerCalOldBoard``
     - ``f_voltageCalOldBoard``
   * - Carte universelle 3phaseDiverter (``PcbVersion::NEW``)
     - ``f_powerCalPerAmp``, multipliée par ``f_ctRating``
     - ``f_voltageCalNewBoard``

Seule la puissance compte pour le routage : la tension (``V1``, ``V2``, ``V3``) n’est qu’affichée.

**Carte universelle** : le facteur de puissance est donné par ampère de calibre de sonde, ``f_powerCal`` = ``f_powerCalPerAmp`` × ``f_ctRating``. Les valeurs par défaut découlent de la conception de la carte, corrigée par l’étalonnage d’une première carte : le routeur est en général précis à quelques pour cent avant étalonnage, ce qui ne dispense pas de le faire.

**Ancienne carte** : les valeurs se trouvent uniquement par étalonnage ; 0,05 est un bon départ pour ``f_powerCalOldBoard``.

Dans la suite de ce chapitre, ``f_powerCal`` désigne la valeur de puissance de votre carte : ``f_powerCalOldBoard`` ou ``f_powerCalPerAmp``.

Pas à pas
~~~~~~~~~

#. Ouvrez le :ref:`configurateur <configurateur-triphase>`, choisissez votre carte, puis cochez **« Mode étalonnage »**. La page ne montre plus que ce qui sert à l’étalonnage (vos autres réglages sont conservés).
#. Chargez votre ``calibration.h`` avec **« Charger mon calibration.h »**, ou saisissez les valeurs de puissance (et de tension) avec lesquelles tourne le routeur. Le fichier doit venir de la même version du firmware : un ``calibration.h`` plus ancien, avec un seul ``f_powerCal``, est refusé.
#. **Carte universelle seulement** : vérifiez le **calibre de la sonde** de chaque phase (``f_ctRating``), en ampères : 50 pour une sonde 50 A / 333 mV. Avec une sonde à sortie courant et une résistance de charge R, comme la YHDC SCT-013-000 (2000:1), le calibre vaut 666 / R, soit 30,3 avec 22 Ω. Un calibre se change dans ``calibration.h`` : voir le téléversement ci-dessous.
#. Dans le dossier du firmware, remplacez ``config.h`` par celui que génère le configurateur : il met le routeur en mode étalonnage, avec la sortie série lisible. Si vous avez changé un calibre, remplacez aussi ``calibration.h`` par le fichier du configurateur (après avoir chargé le vôtre), ou copiez la ligne ``f_ctRating`` qu’il donne dans le vôtre. Téléversez ensuite le firmware (le dossier du sketch) sur le routeur, avant les relevés.
#. Branchez la charge résistive sur une phase, par exemple **L1**, sans passer par le routeur, et ouvrez le moniteur série. Il affiche, toutes les 5 secondes, ``P1``, ``P2``, ``P3`` (la puissance de chaque phase) et ``P`` (le total) ; voir l’exemple plus bas, dans :ref:`Pour aller plus loin <etalonnage-triphase-aller-plus-loin>`.
#. Relevez **au même moment** la puissance du routeur (``P1`` pour la phase **L1**) et celle de l’appareil de référence, et saisissez les deux dans la ligne de cette phase. La tension (``V1``…) se corrige de la même façon, mais elle ne sert qu’à l’affichage.
#. Le configurateur calcule la nouvelle valeur (valeur actuelle × appareil / routeur) et signale ce qui est douteux : puissance négative (sonde à l’envers), charge trop faible, écart trop grand. Si l’un de ces signalements apparaît, corrigez la cause avant de continuer.
#. Copiez les lignes données, ou enregistrez les fichiers : votre ``calibration.h`` est réécrit avec les nouvelles valeurs, le reste du fichier intact. Remplacez-le dans le dossier du firmware et téléversez.
#. Cliquez sur **« Nouvelles valeurs téléversées : nouvelle mesure »** : les nouvelles valeurs deviennent les valeurs actuelles et les relevés sont effacés. Refaites une mesure pour vérifier (voir :ref:`la section suivante <etalonnage-triphase-verifier>`).
#. Recommencez avec la phase **L2**, puis **L3** : une phase à la fois, la charge sur la phase étalonnée.
#. Une fois les trois phases étalonnées, décochez **« Mode étalonnage »** dans le configurateur et téléversez à nouveau : le routeur reprend son fonctionnement normal.

.. attention::
   La phase doit correspondre. Si vous étalonnez la phase **L1**, la charge DOIT être branchée sur **L1** et la pince du routeur DOIT être celle qui correspond à la phase **L1**.

.. hint::
   Les numéros de phase sont purement arbitraires : la phase **L1** du routeur est celle branchée sur le connecteur **L1** du routeur, mais ce n’est pas forcément la phase branchée sur le bornier **L1** du compteur.

Une ligne de mesure comprend TOUS les composants, de la pince jusqu’au convertisseur analogique du microcontrôleur.

.. important::
   Chaque pince doit être marquée pour savoir à quelle ligne elle correspond, et ne jamais être intervertie après l’étalonnage.

.. _etalonnage-triphase-verifier:

Vérifier
--------

Après avoir téléversé les nouvelles valeurs, remettez la charge sur chaque phase tour à tour et comparez le routeur et la référence : ils doivent concorder à quelques pour cent près sur chaque phase (moins de 2 % est un bon résultat). Avec des charges sur plusieurs phases en même temps, la somme ``P`` du routeur doit correspondre à la puissance totale du compteur ou du Linky.

Un signe contraire signale un défaut de montage :

* **puissance négative** sur une phase alors qu’une charge y fonctionne : la pince de cette phase est montée à l’envers (retournez-la), ou elle n’est pas sur la phase de son entrée tension ;
* **valeur qui bouge sur une autre phase** quand vous allumez la charge : la pince est sur une autre phase que celle prévue ; revoyez le marquage des pinces.

.. admonition:: ✅ Point de Contrôle Final — Étalonnage Triphasé Complet

   Avant de passer à l'installation finale, vérifiez :

   | ☐ **f_powerCal validé pour L1, L2, L3**
   | ☐ Chaque phase mesure correctement (écart < 2 %)
   | ☐ **CTs marqués de manière PERMANENTE** (L1, L2, L3)
   | ☐ Test avec charge équilibrée : somme des phases = mesure compteur
   | ☐ « Mode étalonnage » décoché et ``config.h`` téléversé à nouveau
   | ☐ Documentation finale complète et conservée en lieu sûr

   ⚠️ **CRITIQUE : Ne JAMAIS intervertir les CTs après étalonnage** ⚠️

.. _etalonnage-triphase-aller-plus-loin:

Pour aller plus loin
--------------------

Le configurateur applique une formule simple, que vous pouvez appliquer à la main : sans lui, ou pour comprendre ce qu’il fait. Les méthodes ci-dessous donnent la référence autrement (compteur, appareil annexe) et se terminent par la recherche de la bonne valeur du premier coup.

La formule de correction
~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

   f_{powerCal} = f_{powerCal_{initial}} * \frac{P_{\text{référence}}}{P_{routeur}}

Où :math:`f_{powerCal_{initial}}` est la valeur actuelle (celle du sketch téléversé), :math:`P_{\text{référence}}` la puissance de l’appareil de référence et :math:`P_{routeur}` celle affichée par le routeur.

Le routeur pour cette méthode doit être en sortie lisible : ``SERIAL_OUTPUT_TYPE`` à ``SerialOutputType::HumanReadable`` dans ``config.h`` (le ``config.h`` fourni est en mode ``IoT``), et en mode étalonnage : ``CALIBRATION_MODE`` à ``true``, pour que le routeur ne commute plus aucune charge (remettez-le à ``false`` ensuite). Le mode étalonnage du :ref:`configurateur <configurateur-triphase>` le fait pour vous.

L'affichage dans le Moniteur Série se présente comme ceci : ::

    1797.67, P:-21, P1:368, P2:-113, P3:-276, V1:233.24, V2:233.82, V3:233.84, (minSampleSets/MC 32, #ofSampleSets 8014)
    1793.61, P:-18, P1:367, P2:-110, P3:-275, V1:233.46, V2:233.93, V3:233.99, (minSampleSets/MC 32, #ofSampleSets 8013)
    1780.56, P:-18, P1:374, P2:-116, P3:-276, V1:233.09, V2:233.53, V3:233.67, (minSampleSets/MC 32, #ofSampleSets 8014)
    1804.21, P:-24, P1:371, P2:-118, P3:-277, V1:233.04, V2:233.48, V3:233.55, (minSampleSets/MC 32, #ofSampleSets 8015)

``P1``, ``P2``, ``P3`` représentent les puissances moyennées sur 5 secondes sur chaque phase. ``P`` est la puissance totale moyennée sur 5 secondes.
Si vous étalonnez la phase **L1**, alors **P1** devra afficher la même valeur que celle affichée par la référence pour cette même phase.

Avec le compteur de distribution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette méthode ne nécessite aucun appareil de mesure, mais n'est pas la plus rapide à réaliser.

À l'aide des flash du compteur (1 flash = 1 Wh consommé)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La plupart des compteurs d'électricité génèrent un flux d'impulsions optiques pour indiquer le taux de consommation d'énergie. En installant un :term:`CT` autour de l'un des câbles d'alimentation entrants et en exécutant le logiciel approprié sur le routeur, un flux similaire d'impulsions optiques peut être généré.

Le débit du flux d'impulsions pour le routeur peut être ajusté en modifiant la valeur ``f_powerCal`` correspondante. Lorsque les deux flux d'impulsions sont synchronisés, un étalonnage correct a été réalisé.

Il faudra aller par tâtonnement. Si le flash du routeur est plus rapide que celui du compteur, il faut diminuer ``f_powerCal`` sinon l'augmenter.

À l'aide de l'affichage du compteur (plus simple et plus rapide)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il est possible également de relever la consommation affichée par le compteur sur la phase en cours d'étalonnage.
Il faudra alors faire correspondre la puissance affichée par le routeur dans le moniteur série avec celle affichée par le compteur.
D'où l'intérêt de ne pas avoir d'appareils qui vont se mettre en route sporadiquement (réfrigérateur…).

Comment trouver le bon ``f_powerCal`` du premier coup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Avant de téléverser le firmware, partez de valeurs connues dans ``calibration.h``.

Ancienne carte :

.. code-block:: cpp

   inline constexpr float f_powerCalOldBoard[NO_OF_PHASES]{ 0.05000F, 0.05000F, 0.05000F };

Carte universelle, avec les valeurs par défaut et le calibre de vos sondes :

.. code-block:: cpp

   inline constexpr float f_ctRating[NO_OF_PHASES]{ 50.0F, 50.0F, 50.0F };
   inline constexpr float f_powerCalPerAmp[NO_OF_PHASES]{ 0.00286405F, 0.00286405F, 0.00286405F };

L'exemple ci-dessous part de l'ancienne carte (0,05) ; avec la carte universelle, le calcul est le même à partir de ``f_powerCalPerAmp``.

| Supposons que le compteur affiche **2250**, et que le log du routeur affiche **2000**.
| On aura alors :

.. math::

   f_{powerCal} = 0.05000 * {2250 \over 2000} = 0.05625

.. note::
   La valeur ``0.05000`` dans la formule correspond à la valeur inscrite dans le sketch téléversé.
   Si le sketch contient une autre valeur, il conviendra alors d'adapter la formule en conséquence.

.. hint::
   Après avoir calculé le ``f_powerCal`` de la phase en cours d'étalonnage et saisi sa valeur dans le sketch, il peut être judicieux de téléverser à nouveau sur le routeur et de s'assurer que la valeur affichée dans le log correspond bien à celle du compteur.

En triphasé, il faudra répéter l'opération sur chacune des phases.

.. important::
   Chaque pince devra alors être marquée pour savoir à quelle ligne elle correspond.

.. admonition:: ✅ Point de Contrôle — Étalonnage Méthode Compteur

   Après avoir étalonné les 3 phases avec le compteur, vérifiez :

   | ☐ **f_powerCal trouvé pour CHAQUE phase** (L1, L2, L3)
   | ☐ Valeur de chaque phase synchronisée avec compteur
   | ☐ **Chaque CT marqué** avec son numéro de phase correspondant
   | ☐ Documentation complète : valeur de puissance de chaque phase (et, carte universelle, calibre de chaque sonde)
   | ☐ Test de vérification sur les 3 phases (somme = puissance totale compteur)

Avec un appareil de mesure annexe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette méthode nécessite un appareil de mesure, tel qu'un wattmètre, un compteur d'énergie portable, ou un autre dispositif de mesure de puissance.

Appareils de mesure possibles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Wattmètre portable** :

  - Affiche directement la puissance consommée en watts.
  - Idéal pour des mesures instantanées.

* **Compteur d'énergie portable** :

  - Permet de mesurer la consommation d'énergie sur une période donnée (kWh).
  - Utile pour des mesures prolongées.

* **Multimètre avec fonction wattmètre** :

  - Polyvalent, peut également mesurer la tension et le courant.
  - Peut nécessiter des calculs manuels pour obtenir la puissance (P = U × I).

* **Compteur d'énergie triphasé** :

  - Permet de mesurer directement les trois phases sans déplacer l'appareil.
  - Idéal pour des installations triphasées complexes.

Étapes pour l'étalonnage
^^^^^^^^^^^^^^^^^^^^^^^^

#. **Préparation** :

   - Coupez l'alimentation électrique au tableau pour garantir la sécurité.
   - Installez l'appareil de mesure sur la phase correspondante (par exemple, **L1**).
   - Connectez la pince ampèremétrique du routeur à la même phase.

#. **Mesure de la puissance** :

   - Rétablissez l'alimentation électrique.
   - Allumez un appareil purement résistif (par exemple, un radiateur ou une bouilloire).
   - Relevez la puissance affichée par l'appareil de mesure.

#. **Ajustement de** ``f_powerCal`` :

   - Comparez la puissance mesurée par l'appareil avec celle affichée dans le moniteur série.
   - Utilisez la formule de correction ci-dessus pour ajuster la valeur de ``f_powerCal``.

#. **Validation** :

   - Téléversez le sketch mis à jour sur le routeur.
   - Vérifiez que la puissance affichée par le routeur correspond à celle mesurée par l'appareil.
   - Répétez l'opération pour chaque phase (**L1**, **L2**, **L3**).

.. attention::
   La phase doit correspondre. Si vous étalonnez la phase **L1**, le chauffe-eau DOIT être branché sur **L1** et la pince du routeur DOIT être celle qui correspond à la phase **L1**.

Chauffe-eau triphasé
^^^^^^^^^^^^^^^^^^^^

Si vous utilisez un chauffe-eau triphasé comme appareil d'étalonnage, suivez ces étapes spécifiques :

* Branchez l'appareil de mesure sur une phase du chauffe-eau ainsi que la pince du routeur correspondante.
* Si l'appareil de mesure est triphasé, il n'est pas nécessaire de le déplacer de phase en phase. Sinon, déplacez-le sur chaque phase pour effectuer les mesures.
* Relevez les valeurs de puissance pour chaque phase et ajustez ``f_powerCal`` en conséquence.

| Exemple : supposons que le compteur/wattmètre affiche **2250**, et que le log du routeur affiche **2000**.
| On aura alors :

.. math::

   f_{powerCal} = 0.05000 * {2250 \over 2000} = 0.05625

| Répétez l'opération pour chaque phase. Une ligne de mesure comprend TOUS les composants en partant de la pince jusqu'au convertisseur analogique du microcontrôleur.

.. important::
   Chaque pince devra être marquée pour savoir à quelle ligne elle correspond.

.. |br| raw:: html

  <br/>
