.. _configurateur-monophase:

=======================================
Configurateur du firmware — Monophasé
=======================================

Le **configurateur** écrit pour vous les fichiers de configuration du firmware monophasé ``Mk2_1phase_RFdatalog_temp``, à partir d’une simple description de votre installation.

👉 **Ouvrir le configurateur :** `configurateur monophasé <../../configurateur-monophase/>`_

.. note::
   Le configurateur ne concerne que le firmware **monophasé** ``Mk2_1phase_RFdatalog_temp`` (`PVRouter-1-phase <https://github.com/FredM67/PVRouter-1-phase>`_). Pour le routeur triphasé, voir le :ref:`configurateur triphasé <configurateur-triphase>` ; en haut de chaque page, « Routeur : monophasé / triphasé » mène de l’un à l’autre. Il correspond toujours à la version du firmware décrite dans cette documentation.

.. contents:: Sommaire
    :local:
    :depth: 1

Ce qu’il fait
--------------

Vous décrivez votre installation :

- la **carte-mère** : la carte Mk2 d’origine avec afficheur 7 segments, la seconde ancienne carte avec écran OLED, ou la carte universelle ;
- l’**afficheur** : aucun, 7 segments (piloté par logiciel ou par circuit), ou OLED ;
- la sonde **CT2** (énergie routée) : présence, seuil anti-dérive, extinction de l’afficheur ;
- les **charges** (triacs), pilotées par le routeur ou par une unité distante par radio, et leurs priorités ;
- les **relais** ;
- les **entrées de commande** : arrêt du routage, arrêt du routeur, marche forcée, rotation des priorités ;
- le **double tarif**, les **sondes de température** ;
- les entrées du **module mk2Wifi** (carte universelle seulement) ;
- la **radio** (RFM69) et les **unités distantes**, plus rarement utilisées.

Il vérifie la cohérence de vos choix au fur et à mesure (broche utilisée deux fois, broche prise par l’afficheur ou la radio, valeur hors limites…), avec les mêmes règles que le compilateur.

Il produit ensuite :

- ``config.h``, ``config_system.h`` et ``config_rf.h`` pour le routeur ;
- ``config.h`` et ``config_rf.h`` pour chaque unité distante (firmware ``RemoteLoadReceiver``).

.. note::
   Le YAML ESPHome du module mk2Wifi n’est pas encore généré pour le routeur monophasé : il viendra dans une prochaine version.

Utilisation
-----------

#. Ouvrir le configurateur et décrire l’installation, section par section. Par défaut, il part de la carte universelle avec le module mk2Wifi (sortie série **IoT**) : avec une ancienne carte, la choisir en premier.
#. Consulter les **Vérifications** à droite : corriger les erreurs (en rouge), sans quoi les fichiers ne sont pas générés ; les avertissements (en orange) sont à vérifier, mais ne bloquent rien.
#. Avec Chrome ou Edge, cliquer sur **« Enregistrer dans le dossier du firmware… »** et choisir le dossier du firmware décompressé (celui qui contient ``Mk2_1phase_RFdatalog_temp`` et ``RemoteLoadReceiver``). Avant d’écrire, il sauvegarde ce qu’il remplace dans ``configurator-backup/<date_heure>``.

   Avec un autre navigateur, cliquer sur **« Tout télécharger (ZIP) »**, puis copier les fichiers du routeur dans le dossier ``Mk2_1phase_RFdatalog_temp``, à la place des fichiers du même nom.
#. **Garder votre** ``calibration.h`` : en dehors du mode étalonnage (voir ci-dessous), le configurateur ne le modifie jamais.
#. Compiler et téléverser comme d’habitude.

.. tip::
   Le bouton **« Enregistrer les choix »** sauvegarde votre configuration dans un fichier JSON, à recharger avec **« Charger des choix »** après une mise à jour du firmware. Une sauvegarde du configurateur triphasé est refusée, avec un lien vers celui-ci.

.. tip::
   Le configurateur fonctionne aussi hors ligne : ouvrir ``configurator/index.html`` depuis une copie du dépôt du firmware.

Étalonnage
----------

Cochez **« Mode étalonnage »** : le routeur mesure sans rien commuter, avec la sortie série lisible. La page ne montre plus que ce qui sert à l’étalonnage, les autres sections sont masquées et leurs réglages conservés. Le ``config.h`` généré met le routeur en mode étalonnage, et votre choix habituel revient en décochant le mode.

``calibration.h`` contient un jeu de valeurs par carte. Le configurateur ne montre et ne corrige que celles de la carte choisie dans la page :

- **anciennes cartes** : ``f_powerCalOldBoard`` (puissance réseau), ``f_powerCalDivertedOldBoard`` (puissance routée, CT2) et ``f_voltageCalOldBoard`` (tension) ;
- **carte universelle** : ``f_ctRating`` et ``f_ctRatingDiverted`` (calibres des sondes CT1 et CT2), ``f_powerCalPerAmp`` (puissance, par ampère de calibre) et ``f_voltageCalNewBoard`` (tension).

À l’écran :

- **« Charger mon calibration.h »** (facultatif) : la page réécrit votre fichier avec les nouvelles valeurs, le reste du fichier intact. Sans lui, saisissez les valeurs actuelles et copiez les lignes données. Le fichier doit venir de la même version du firmware : s’il manque des valeurs, il est refusé.
- **Calibre de CT1** (carte universelle seulement) : le courant nominal de CT1, en A. Le calibre de CT2 vient avec la puissance routée.
- **Puissance réseau** : la valeur actuelle, les relevés **Routeur (W)** et **Appareil (W)** (``P`` sur le moniteur série), et la **Nouvelle valeur** calculée (valeur actuelle × appareil / routeur).
- **Tension** (facultative, pour le journal seulement) : de même, avec ``V``.
- **Puissance routée** (avec CT2) : de même, avec ``diverted`` (la puissance en W, pas l’énergie en Wh). Sur la carte universelle, la valeur actuelle est le calibre de CT2 (``f_ctRatingDiverted``), en A, et la nouvelle valeur tient compte de la correction réseau que prend ``f_powerCalPerAmp``. Le mode étalonnage ne commute jamais de charge : ce relevé demande une charge résistive câblée à travers CT2 et mise en marche autrement.
- **Pour calibration.h** : les lignes à copier dans le fichier.
- **Fichiers pour le routeur** : le ``config.h`` (à téléverser en premier) et votre ``calibration.h`` avec les nouvelles valeurs.
- **« Nouvelles valeurs téléversées : nouvelle mesure »** : les nouvelles valeurs deviennent les valeurs actuelles et les relevés sont effacés, pour vérifier ou affiner.

Une valeur laissée vide garde sa valeur actuelle. Dans les **Vérifications**, la page signale, pour chaque relevé :

- une puissance négative sur le routeur : sa sonde est montée à l’envers ;
- des relevés qui ne sont pas positifs, une valeur actuelle manquante, un calibre de sonde qui n’est pas positif ;
- une puissance sous 300 W : la correction est imprécise ;
- une correction suspecte (inférieure à ×0,5 ou supérieure à ×2) : vérifiez le câblage, et que les deux relevés portent sur le même câble, au même moment.

La marche à suivre, pas à pas : :ref:`etalonnage-monophase`
