.. _configurateur-triphase:

=====================================
Configurateur du firmware — Triphasé
=====================================

Le **configurateur** écrit pour vous les fichiers de configuration du firmware triphasé ``Mk2_3phase_RFdatalog_temp``, à partir d’une simple description de votre installation.

👉 **Ouvrir le configurateur :** `https://fredm67.github.io/Mk2PVRouter/configurateur/ <https://fredm67.github.io/Mk2PVRouter/configurateur/>`_

.. note::
   Le configurateur ne concerne que le firmware **triphasé** (`PVRouter-3-phase <https://github.com/FredM67/PVRouter-3-phase>`_). Il correspond toujours à la version du firmware décrite dans cette documentation.

.. contents:: Sommaire
    :local:
    :depth: 1

Ce qu’il fait
--------------

Vous décrivez votre installation :

- les **charges** (triacs), pilotées par le routeur ou par une unité distante par radio, et leurs priorités ;
- les **relais** ;
- les **entrées de commande** : arrêt du routage, arrêt du routeur, marche forcée, rotation des priorités ;
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

#. Ouvrir le configurateur et décrire l’installation, section par section.
#. Consulter les **Vérifications** à droite : corriger les erreurs (en rouge), sans quoi les fichiers ne sont pas générés ; les avertissements (en orange) sont à vérifier, mais ne bloquent rien.
#. Avec Chrome ou Edge, cliquer sur **« Enregistrer dans le dossier du firmware… »** et choisir le dossier du firmware décompressé (celui qui contient ``Mk2_3phase_RFdatalog_temp`` et ``RemoteLoadReceiver``). Après confirmation, le configurateur y écrit tous les fichiers, à la place de ceux du même nom ; chaque unité distante reçoit son dossier ``RemoteLoadReceiver-unitN``.

   Avant d’écrire, il sauvegarde ce qu’il remplace dans ``configurator-backup/<date_heure>``. Si vous passez à moins d’unités distantes, les dossiers des unités en trop y sont déplacés.

   Avec un autre navigateur, cliquer sur **« Tout télécharger (ZIP) »**, puis copier les fichiers du routeur dans le dossier ``Mk2_3phase_RFdatalog_temp``, à la place des fichiers du même nom.
#. **Garder votre** ``calibration.h`` : le configurateur ne le modifie jamais.
#. Compiler et téléverser comme d’habitude (voir :ref:`logiciel-triphase`).

.. tip::
   Le bouton **« Annuler le dernier enregistrement… »** (Chrome ou Edge) remet le dossier du firmware dans l’état où il était avant le dernier enregistrement du configurateur : les fichiers remplacés et les dossiers supprimés reviennent, ceux qu’il a créés sont effacés.

.. tip::
   Le bouton **« Enregistrer les choix »** sauvegarde votre configuration dans un fichier JSON. Après une mise à jour du firmware, rechargez-le avec **« Charger des choix »** pour régénérer des fichiers à jour.

.. tip::
   Le configurateur fonctionne aussi hors ligne : ouvrir ``configurator/index.html`` depuis une copie du dépôt du firmware.

Étalonnage
----------

Cochez **« Mode étalonnage »** : le configurateur ne montre plus que ce qui sert à l’étalonnage (les autres réglages sont conservés), et le ``config.h`` généré met le routeur en mode étalonnage, où il mesure sans rien commuter, avec la sortie série lisible (votre choix habituel revient en quittant le mode).

#. Chargez votre ``calibration.h`` avec **« Charger mon calibration.h »**, ou saisissez les valeurs de ``f_powerCal`` (et de ``f_voltageCal``) avec lesquelles tourne le routeur.
#. Avec une forte charge résistive sur une phase, relevez au même moment la puissance affichée par le routeur (``P1``, ``P2``, ``P3``) et celle d’un appareil de référence pincé sur le même câble, et saisissez-les. La tension (``V1``…) se corrige de la même façon.
#. Le configurateur calcule la nouvelle valeur (valeur actuelle × appareil / routeur) et la signale si elle est douteuse : sonde à l’envers, charge trop faible, écart trop grand. Copiez les lignes données, ou enregistrez les fichiers : votre ``calibration.h`` est réécrit avec les nouvelles valeurs, le reste du fichier intact.
#. Téléversez, puis cliquez sur **« Nouvelles valeurs téléversées : nouvelle mesure »** pour vérifier ou affiner.
#. Une fois étalonné, décochez **« Mode étalonnage »** et téléversez à nouveau.

Module mk2Wifi
--------------

Avec le module mk2Wifi, le configurateur règle la sortie série du routeur en mode **IoT** et génère un YAML ESPHome complet, cohérent avec le ``config.h`` :

- un capteur pour chaque mesure réellement envoyée par le routeur (puissances, tensions, taux de routage de chaque charge, relais, températures, heures creuses…) ;
- une commande pour chaque entrée du routeur reliée au module (D5 à D9).

.. important::
   Les commandes sont **sûres en cas de défaut** : le module ne tire une entrée du routeur à l’état bas que pour l’état non par défaut, et la relâche sinon. Un fil coupé, un pont de soudure ouvert ou un module qui redémarre laissent donc le routeur dans son état normal : routage actif, routeur en marche, pas de marche forcée. À chaque démarrage du module, toutes les commandes reviennent à cet état.

Seuls les ponts de soudure listés par le configurateur doivent être fermés : les autres broches D5 à D9 peuvent être utilisées par le routeur lui-même (charges, relais…).
