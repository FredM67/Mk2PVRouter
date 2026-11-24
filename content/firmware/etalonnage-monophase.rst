.. _etalonnage-monophase:

======================
Étalonnage — Monophasé
======================

⏱️ **Temps estimé** : 30–45 minutes

🔧 **Niveau de difficulté** : Intermédiaire

⚠️ **Niveau de risque** : Élevé (manipulation 230 V sous tension)

.. tip::
   L’étalonnage est **recommandé** en monophasé, sans être obligatoire.

   * **Pour dévier l’énergie vers les triacs, il n’est pas nécessaire** : le routeur agit sur le signe de l’énergie échangée avec le réseau, et une erreur d’échelle ne le change pas.
   * **Pour des valeurs réalistes, il l’est** : ce que le routeur affiche et envoie (afficheur, moniteur série, Home Assistant via le module mk2Wifi), et tous les réglages en watts comparés à la puissance mesurée. Dès que des **relais** routent le surplus, leurs seuils (surplus, import) sont en watts : sans étalonnage, ils s’appliquent à des watts faux. Même chose pour la limite anti-fluage de CT2 et l’export requis.

.. admonition:: 📋 Prérequis

   Avant de commencer ce chapitre :

   | ☐ Chapitre :ref:`safety-overview` lu et compris
   | ☐ Tests électriques effectués (voir :ref:`tests-electriques`)
   | ☐ Firmware installé et fonctionnel (voir :ref:`logiciel-monophase`)
   | ☐ Routeur alimenté par le secteur
   | ☐ Un appareil de référence : pince wattmétrique, wattmètre ou affichage du Linky
   | ☐ Une forte charge résistive (bouilloire, radiateur, chauffe-eau), qui fonctionne sans passer par le routeur

.. contents:: Sommaire
    :local:
    :depth: 2

Ce qu’il vous faut
------------------

.. danger::
   **ALERTE SÉCURITÉ**

   Tout travail sur le câblage (passer le câble d’une charge à travers CT2, intervenir dans le tableau ou sur une installation fixe) se fait **disjoncteur coupé au tableau**, après avoir vérifié l’absence de tension avec un testeur. Dans le doute, coupez le disjoncteur principal.

* **Une lecture de référence au point de raccordement**, prise en même temps que celle du routeur : une pince wattmétrique autour du même câble que CT1, ou l’affichage du Linky (sa puissance instantanée). Le Linky affiche une puissance apparente (en VA), avec un rafraîchissement lent : avec une charge purement résistive, VA et W sont égaux, à condition d’éteindre toutes les autres consommations de la maison (il donne la puissance totale).
* **Une forte charge résistive** (bouilloire, radiateur, chauffe-eau) : au moins 300 W, car en dessous la correction est imprécise. Un appareil purement résistif, sans ventilateur ni électronique, simplifie grandement l’étalonnage. **Elle doit fonctionner sans passer par le routeur** : le mode étalonnage ne commute rien, donc une charge reliée à la sortie triac du routeur reste éteinte. Branchez une bouilloire ou un radiateur sur une prise, ou faites marcher le chauffe-eau par son propre contacteur, en position forcée.
* **Une consommation constante pendant l’étalonnage** : branchez la charge résistive et débranchez tout le reste, y compris votre ou vos systèmes de production d’électricité.
* **Le** :ref:`configurateur <configurateur-monophase>`, qui fait le calcul pour vous et réécrit votre ``calibration.h``.
* Votre ``calibration.h`` (celui du dossier du firmware), si vous l’avez déjà modifié : le configurateur peut le charger.
* **Si le routeur a une sonde CT2** (énergie routée) et que vous voulez l’étalonner : une charge résistive dont le câble passe **à travers CT2**, par exemple un séparateur de ligne (ou « diviseur de ligne », vendu pour les pinces ampèremétriques), prêt à l’emploi, ou à défaut un câble d’extension modifié entre une prise et la charge (un seul des conducteurs traverse la sonde ; à faire hors tension, en ouvrant seulement la gaine extérieure, sans abîmer l’isolant des conducteurs intérieurs ; un tel câble ne sert qu’à l’étalonnage : marquez-le et ne le laissez jamais en service). Le mode étalonnage ne commute jamais de charge : cette charge doit fonctionner par d’autres moyens, branchée directement ou mise en marche à la main.

Étalonner avec le configurateur
-------------------------------

Le routeur est étalonné en mode étalonnage : il mesure, sans rien commuter (ni triacs, ni relais, ni charges distantes, ni forçages), et affiche ses mesures sur le moniteur série. Le configurateur règle ce mode, calcule les nouvelles valeurs à partir de vos relevés et réécrit ``calibration.h``.

Les valeurs, selon la carte
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le fichier ``calibration.h`` contient un jeu de valeurs pour les anciennes cartes et un pour la carte universelle, et le routeur utilise celui de ``PCB_VERSION`` (dans ``config.h``). Le configurateur ne montre et ne corrige que celles de la carte que vous avez choisie dans la page :

.. list-table::
   :header-rows: 1

   * - Carte
     - CT1, réseau (le routage)
     - CT2, énergie routée
     - Tension (affichage)
   * - Anciennes cartes (``PcbVersion::OLD_SEG`` et ``PcbVersion::OLD_OLED``)
     - ``f_powerCalOldBoard``
     - ``f_powerCalDivertedOldBoard``
     - ``f_voltageCalOldBoard``
   * - Carte universelle, rév. 6.0 et suivantes (``PcbVersion::NEW``)
     - ``f_powerCalPerAmp``, multipliée par ``f_ctRating``
     - ``f_powerCalPerAmp``, multipliée par ``f_ctRatingDiverted``
     - ``f_voltageCalNewBoard``

Le facteur de puissance de CT1 est celui avec lequel le routeur régule. Celui de CT2 ne sert qu’à l’énergie routée qu’il affiche. La tension (``V``) n’est qu’affichée.

**Carte universelle** : le facteur de puissance est donné par ampère de calibre de sonde, ``f_powerCal`` = ``f_powerCalPerAmp`` × ``f_ctRating`` (``f_ctRatingDiverted`` pour CT2). Changer de sonde revient donc à entrer son calibre. Les valeurs par défaut conviennent aux sondes à sortie tension 333 mV et découlent de la conception de la carte, corrigée par l’étalonnage d’une première carte : le routeur est en général précis à quelques pour cent avant étalonnage, ce qui ne dispense pas de le faire.

**Anciennes cartes** : les valeurs se trouvent uniquement par étalonnage ; 0,05 est un bon départ pour ``f_powerCalOldBoard`` et ``f_powerCalDivertedOldBoard``.

Dans la suite de ce chapitre, ``f_powerCal`` désigne la valeur de puissance de votre carte.

Pas à pas
~~~~~~~~~

#. Ouvrez le :ref:`configurateur <configurateur-monophase>`, choisissez votre **carte-mère**, puis cochez **« Mode étalonnage »**. La page ne montre plus que ce qui sert à l’étalonnage (vos autres réglages sont conservés).
#. Chargez votre ``calibration.h`` avec **« Charger mon calibration.h »**, ou saisissez les valeurs avec lesquelles tourne le routeur. Le fichier doit venir de la même version du firmware : s’il manque des valeurs (``f_powerCalOldBoard``, ``f_powerCalDivertedOldBoard``, ``f_voltageCalOldBoard``, ``f_ctRating``, ``f_ctRatingDiverted``, ``f_powerCalPerAmp``, ``f_voltageCalNewBoard``), il est refusé.
#. **Carte universelle seulement** : vérifiez le **calibre de CT1** (``f_ctRating``), en ampères : 50 pour une sonde 50 A / 333 mV. Avec une sonde à sortie courant et une résistance de charge R, comme la YHDC SCT-013-000 (2000:1), le calibre vaut 666 / R, soit 30,3 avec 22 Ω. Le calibre de CT2 (``f_ctRatingDiverted``) vient avec la puissance routée, plus bas.
#. Dans le dossier du firmware, remplacez ``config.h`` par celui que génère le configurateur : il met le routeur en mode étalonnage, avec la sortie série lisible. Un calibre se change dans ``calibration.h`` : si vous avez changé celui de CT1, remplacez aussi ``calibration.h`` par le fichier du configurateur (après avoir chargé le vôtre), ou copiez la ligne ``f_ctRating`` qu’il donne dans le vôtre. Téléversez ensuite le firmware (le dossier du sketch) sur le routeur, avant les relevés.
#. Mettez la forte charge résistive en marche, sans passer par le routeur (une bouilloire ou un radiateur sur une prise, sans production solaire), et ouvrez le moniteur série à 9600 bauds. Toutes les 5 secondes (valeur par défaut de ``DATALOG_PERIOD_IN_SECONDS``, dans ``config_system.h``, 30 s au plus), le routeur y affiche :

   * ``P`` : la puissance au point de raccordement, en W, positive en import (le premier nombre après ``P:``) ;
   * ``V`` : la tension, en V (le nombre après ``V:``) ;
   * ``diverted`` (avec CT2 seulement) : la puissance routée en W, suivie de l’énergie en Wh (``diverted <W> W, <Wh> Wh``). C’est la puissance en W qui sert à l’étalonnage, pas l’énergie.

#. Relevez **au même moment** la puissance du routeur (``P``) et celle de l’appareil de référence (pince sur le même câble que CT1, ou affichage du Linky), et saisissez les deux dans **« Puissance réseau »** (colonnes **Routeur (W)** et **Appareil (W)**). La tension (``V``) se corrige de la même façon, mais elle ne sert qu’à l’affichage : son champ est facultatif.
#. **Avec CT2, si vous voulez l’étalonner** : arrêtez la charge, et faites passer son câble à travers CT2 (disjoncteur coupé : voir l’alerte plus haut). Remettez le courant et mettez la charge en marche par un autre moyen que le routeur. Pincez l’appareil de référence sur ce même câble, relevez **au même moment** ``diverted`` (la puissance en W) et la référence, et saisissez-les dans **« Puissance routée »**. Sur les anciennes cartes, cela corrige ``f_powerCalDivertedOldBoard`` ; sur la carte universelle, la valeur actuelle est le calibre de CT2 (``f_ctRatingDiverted``), en A, et la nouvelle valeur tient compte de la correction de CT1 que prend ``f_powerCalPerAmp``.
#. Le configurateur calcule les nouvelles valeurs (valeur actuelle × appareil / routeur) et signale ce qui est douteux : puissance négative (sonde à l’envers), charge sous 300 W, écart trop grand. Si l’un de ces signalements apparaît, corrigez la cause avant de continuer.
#. Copiez les lignes données (**« Pour calibration.h »**), ou enregistrez les fichiers : votre ``calibration.h`` est réécrit avec les nouvelles valeurs, le reste du fichier intact. Remplacez-le dans le dossier du firmware et téléversez.
#. Cliquez sur **« Nouvelles valeurs téléversées : nouvelle mesure »** : les nouvelles valeurs deviennent les valeurs actuelles et les relevés sont effacés. Refaites une mesure pour vérifier (voir :ref:`la section suivante <etalonnage-monophase-verifier>`).
#. Une fois étalonné, décochez **« Mode étalonnage »** dans le configurateur et téléversez à nouveau : le routeur reprend son fonctionnement normal.

.. important::
   Une ligne de mesure comprend TOUS les composants, de la pince jusqu’au convertisseur analogique du microcontrôleur. Marquez chaque pince (CT1 = réseau, CT2 = routage) et ne les intervertissez jamais après l’étalonnage.

.. _etalonnage-monophase-verifier:

Vérifier
--------

Après avoir téléversé les nouvelles valeurs, refaites un relevé et comparez le routeur et la référence : ils doivent concorder à quelques pour cent près (moins de 2 % est un bon résultat), pour ``P`` comme, avec CT2, pour ``diverted``.

Un signe contraire signale un défaut de montage :

* ``P`` **négative alors que vous importez** (une charge fonctionne) : CT1 est monté à l’envers. Retournez-le ;
* **Puissance routée négative** (``diverted``) alors que la charge de CT2 fonctionne : CT2 est monté à l’envers. Retournez-le.

.. admonition:: ✅ Point de Contrôle Final — Étalonnage Monophasé Complet

   Avant de passer à l’installation finale, vérifiez :

   | ☐ Valeurs de CT1 (et de CT2, si installée) mises à jour dans ``calibration.h``
   | ☐ Routeur et référence concordent (écart < 2 %)
   | ☐ **CTs marqués** (CT1 = réseau, CT2 = routage)
   | ☐ « Mode étalonnage » décoché et ``config.h`` téléversé à nouveau
   | ☐ ``calibration.h`` conservé en lieu sûr

.. _etalonnage-monophase-aller-plus-loin:

Pour aller plus loin
--------------------

Le configurateur n’est pas la seule voie : le mode étalonnage se règle aussi à la main dans ``config.h``, et la formule qu’il applique se calcule à la main. C’est utile sans le configurateur, ou pour comprendre ce qu’il fait.

Le mode étalonnage à la main
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

L’étalonnage se fait avec le programme du routeur lui-même : les valeurs sont ainsi mesurées avec exactement le traitement avec lequel elles seront utilisées.

#. Dans ``config.h``, mettez ``CALIBRATION_MODE`` à ``true`` et ``SERIAL_OUTPUT_TYPE`` à ``SerialOutputType::HumanReadable`` (le ``config.h`` fourni est en mode ``IoT``), puis téléversez. Le routeur mesure et affiche comme d’habitude, mais ne commute plus aucune charge (triacs, relais, charges distantes, forçages) : cela modifierait la puissance mesurée. Il l’annonce au démarrage.
#. Mesurez la puissance au point de raccordement avec l’appareil de référence (par exemple une pince wattmétrique autour du même câble que CT1), avec une forte charge résistive en marche.
#. Comparez-la à ``P`` et corrigez CT1 avec la formule ci-dessous, pour ``f_powerCalOldBoard`` ou, sur la carte universelle, ``f_powerCalPerAmp``.
#. Pour CT2, passez-y le câble d’une charge résistive (disjoncteur coupé), mesurez cette charge avec l’appareil de référence et comparez à la puissance routée (``diverted``), avec la même formule, pour ``f_powerCalDivertedOldBoard`` ou, sur la carte universelle, ``f_ctRatingDiverted``. Étalonnez CT1 d’abord et téléversez : CT2 est alors relevé avec la valeur corrigée de ``f_powerCalPerAmp``.
#. Téléversez à nouveau et vérifiez, puis remettez ``CALIBRATION_MODE`` à ``false`` et téléversez : le routeur route à nouveau.

La formule de correction
~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

   nouvelle\ valeur = ancienne\ valeur * \frac{P_{\text{référence}}}{P_{routeur}}

Où l’ancienne valeur est celle du ``calibration.h`` téléversé, :math:`P_{\text{référence}}` la puissance de l’appareil de référence et :math:`P_{routeur}` celle affichée par le routeur (``P`` ou ``diverted``).

| Exemple, ancienne carte : la référence affiche **2250** et le routeur **2000**.
| On aura alors :

.. math::

   f_{powerCalOldBoard} = 0.05000 * {2250 \over 2000} = 0.05625

Avec la carte universelle, le calcul est le même à partir de ``f_powerCalPerAmp`` (0,00286405 par défaut) pour CT1, ou de ``f_ctRatingDiverted`` (50 par défaut) pour CT2.

.. note::
   La valeur ``0.05000`` de l’exemple est celle du ``calibration.h`` fourni. Si le vôtre contient une autre valeur, partez de celle-là.

Le filtre de CT1 (anciennes cartes)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sur les anciennes cartes, un filtre passe-bas du courant de CT1 compense le comportement de la sonde, réglé par ``lpf_gainOldBoard`` et ``alphaOldBoard`` : laissez les valeurs fournies, qui sont provisoires.
