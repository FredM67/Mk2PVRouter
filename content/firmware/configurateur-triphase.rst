.. _configurateur-triphase:

=====================================
Configurateur du firmware — Triphasé
=====================================

Le **configurateur** écrit pour vous les fichiers de configuration du firmware triphasé ``Mk2_3phase_RFdatalog_temp``, à partir d’une simple description de votre installation.

👉 **Ouvrir le configurateur :** `configurateur triphasé <../../configurateur/>`_

.. note::
   Le configurateur ne concerne que le firmware **triphasé** (`PVRouter-3-phase <https://github.com/FredM67/PVRouter-3-phase>`_). Pour le routeur monophasé, voir le :ref:`configurateur monophasé <configurateur-monophase>` ; en haut de chaque page, « Routeur : monophasé / triphasé » mène de l’un à l’autre. Il correspond toujours à la version du firmware décrite dans cette documentation.

.. contents:: Sommaire
    :local:
    :depth: 1

Ce qu’il fait
--------------

Vous décrivez votre installation :

- les **charges** (triacs), pilotées par le routeur ou par une unité distante par radio, et leurs priorités ;
- les **relais** ;
- les **entrées de commande** : arrêt du routage, arrêt du routeur, marche forcée, rotation des priorités ;
- la **LED de vie** ;
- le **double tarif**, les **sondes de température** ;
- le **module mk2Wifi** ;
- la **radio** (RFM69) et les **unités distantes**, plus rarement utilisées.

Il vérifie la cohérence de vos choix au fur et à mesure (broche utilisée deux fois, broche réservée à la radio, valeur hors limites…), avec les mêmes règles que le compilateur, et en plus ce que le compilateur ne peut pas voir, comme le câblage du module mk2Wifi.

Il produit ensuite :

- ``config.h``, ``config_system.h`` et ``config_rf.h`` pour le routeur ;
- ``config.h`` et ``config_rf.h`` pour chaque unité distante (firmware ``RemoteLoadReceiver``) ;
- avec le module mk2Wifi, le fichier **YAML ESPHome** correspondant, ainsi que la liste des ponts de soudure à fermer et la position du cavalier TEMP.

Utilisation
-----------

#. Ouvrir le configurateur et décrire l’installation, section par section. Par défaut, il part de la carte universelle 3phaseDiverter avec le module mk2Wifi (sortie série **IoT**) : avec l’ancienne carte triphasée, la choisir en premier.
#. Consulter les **Vérifications** à droite : corriger les erreurs (en rouge), sans quoi les fichiers ne sont pas générés ; les avertissements (en orange) sont à vérifier, mais ne bloquent rien.
#. Avec Chrome ou Edge, cliquer sur **« Enregistrer dans le dossier du firmware… »** et choisir le dossier du firmware décompressé (celui qui contient ``Mk2_3phase_RFdatalog_temp`` et ``RemoteLoadReceiver``). Après confirmation, le configurateur y écrit tous les fichiers, à la place de ceux du même nom ; chaque unité distante reçoit son dossier ``RemoteLoadReceiver-unitN``.

   Avant d’écrire, il sauvegarde ce qu’il remplace dans ``configurator-backup/<date_heure>``. Si vous passez à moins d’unités distantes, les dossiers des unités en trop y sont déplacés.

   Avec un autre navigateur, cliquer sur **« Tout télécharger (ZIP) »**, puis copier les fichiers du routeur dans le dossier ``Mk2_3phase_RFdatalog_temp``, à la place des fichiers du même nom.
#. **Garder votre** ``calibration.h`` : en dehors du mode étalonnage (voir ci-dessous), le configurateur ne le modifie jamais.
#. Compiler et téléverser comme d’habitude (voir :ref:`logiciel-triphase`).

.. tip::
   Le bouton **« Annuler le dernier enregistrement… »** (Chrome ou Edge) remet le dossier du firmware dans l’état où il était avant le dernier enregistrement du configurateur : les fichiers remplacés et les dossiers supprimés reviennent, ceux qu’il a créés sont effacés.

.. tip::
   Le bouton **« Enregistrer les choix »** sauvegarde votre configuration dans un fichier JSON. Après une mise à jour du firmware, rechargez-le avec **« Charger des choix »** pour régénérer des fichiers à jour.

.. tip::
   Le configurateur fonctionne aussi hors ligne : ouvrir ``configurator/index.html`` depuis une copie du dépôt du firmware.

Étalonnage
----------

Cochez **« Mode étalonnage »** : le routeur mesure sans rien commuter, avec la sortie série lisible. La page ne montre plus que ce qui sert à l’étalonnage, les autres sections sont masquées et leurs réglages conservés. Le ``config.h`` généré met le routeur en mode étalonnage, et votre choix habituel revient en décochant le mode.

``calibration.h`` contient un jeu de valeurs par carte-mère. Le configurateur ne montre et ne corrige que celles de la carte choisie dans la page :

- **ancienne carte triphasée** : ``f_powerCalOldBoard`` (puissance) et ``f_voltageCalOldBoard`` (tension) ;
- **carte universelle** : ``f_ctRating`` (calibre des sondes), ``f_powerCalPerAmp`` (puissance, par ampère de calibre) et ``f_voltageCalNewBoard`` (tension).

À l’écran :

- **« Charger mon calibration.h »** (facultatif) : la page réécrit votre fichier avec les nouvelles valeurs, le reste du fichier intact. Sans lui, saisissez les valeurs actuelles et copiez les lignes données. Le fichier doit venir de la même version du firmware : un ``calibration.h`` plus ancien, avec un seul ``f_powerCal``, est refusé.
- **Calibre des sondes** (carte universelle seulement) : le courant nominal de la sonde de chaque phase, en A, repris de votre fichier s’il est chargé.
- **Puissance** et **Tension** : pour chaque phase, la valeur actuelle, les relevés **Routeur (W)** et **Appareil (W)** (ou **(V)** pour la tension), et la **Nouvelle valeur** calculée (valeur actuelle × appareil / routeur). Une phase laissée vide garde sa valeur. La tension est facultative : elle ne sert qu’à l’affichage.
- **Pour calibration.h** : les lignes à copier dans le fichier.
- **Fichiers pour le routeur** : le ``config.h`` (à téléverser en premier) et votre ``calibration.h`` avec les nouvelles valeurs.
- **« Nouvelles valeurs téléversées : nouvelle mesure »** : les nouvelles valeurs deviennent les valeurs actuelles et les relevés sont effacés, pour vérifier ou affiner.

Dans les **Vérifications**, la page signale, phase par phase :

- une puissance négative sur le routeur : sa sonde est montée à l’envers, ou n’est pas sur la phase de son entrée tension ;
- des relevés qui ne sont pas positifs, une valeur actuelle manquante, un calibre de sonde qui n’est pas positif ;
- une charge sous 300 W : la correction est imprécise ;
- une correction suspecte (inférieure à ×0,5 ou supérieure à ×2) : vérifiez le câblage, et que les deux relevés portent sur la même phase, au même moment.

La marche à suivre, pas à pas : :ref:`etalonnage-triphase`

Module mk2Wifi
--------------

Avec le module mk2Wifi, le configurateur règle la sortie série du routeur en mode **IoT** et génère un YAML ESPHome complet, cohérent avec le ``config.h`` :

- un capteur pour chaque mesure réellement envoyée par le routeur (puissances, tensions, taux de routage de chaque charge, relais, températures, heures creuses…) ;
- une commande pour chaque entrée du routeur reliée au module (D5 à D9).

Le YAML utilise le composant ``mk2pvrouter`` intégré à ESPHome (version 2026.10.0 et suivantes).

.. note::
   Pour mettre à jour un YAML écrit pour une version plus ancienne, le plus simple est de le régénérer avec le configurateur. À la main : supprimer le bloc ``external_components``, écrire ``tag:`` au lieu de ``tag_name:`` dans les capteurs, et supprimer ``update_interval`` sous ``mk2pvrouter:``.

.. note::
   Au démarrage, le routeur affiche sa configuration à 9600 bauds 8N1, puis passe en 7E1 pour les données destinées à Home Assistant. Le module ignore tout ce qui précède la première trame : ces lignes ne le gênent pas.

.. important::
   Les commandes sont **sûres en cas de défaut** : le module ne tire une entrée du routeur à l’état bas que pour l’état non par défaut, et la relâche sinon. Un fil coupé, un pont de soudure ouvert ou un module qui redémarre laissent donc le routeur dans son état normal : routage actif, routeur en marche, pas de marche forcée. À chaque démarrage du module, toutes les commandes reviennent à cet état.

Seuls les ponts de soudure listés par le configurateur doivent être fermés : les autres broches D5 à D9 peuvent être utilisées par le routeur lui-même (charges, relais…).
