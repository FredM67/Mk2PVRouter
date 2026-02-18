.. _test-logiciel:

===============
Tests logiciels
===============

| Une fois le processeur installé, il serait judicieux de vérifier que l'alimentation électrique fonctionne toujours correctement.
| Si c'est le cas, nous pouvons exécuter un croquis (programme) pour vérifier si le processeur fonctionne correctement.

| Nous allons maintenant tester le bon fonctionnement des autres parties matérielles de la carte-mère.
| Cela permettra à la fois de s'assurer que le processeur est opérationnel et de vérifier que les autres composants sont correctement installés et/ou assemblés.

| Pour cette prochaine étape, un dispositif de programmation approprié doit être mis en place.

.. contents:: Sommaire
    :local:
    :depth: 1

.. include:: ../common/test-logiciel-requirements.inc.rst

Choix du firmware
-----------------

Le firmware dépend de votre configuration :

.. list-table:: Firmware selon la configuration
   :header-rows: 1
   :widths: 30 40 30

   * - Configuration
     - Firmware
     - Dépôt
   * - Monophasé
     - Mk2_fasterControl_Full
     - `PVRouter-1-phase <https://github.com/FredM67/PVRouter-1-phase>`_
   * - Triphasé (avec ou sans neutre)
     - Mk2_3phase_RFdatalog_temp
     - `PVRouter-3-phase <https://github.com/FredM67/PVRouter-3-phase>`_

.. note::
   Le firmware monophasé et triphasé sont des projets distincts. Choisissez celui qui correspond à votre configuration électrique.

Installation du Firmware — Monophasé
-------------------------------------

**Étapes communes à toutes les versions** : :ref:`installation-logiciel`

.. include:: firmware-monophase.inc.rst

Installation du Firmware — Triphasé
------------------------------------

**Étapes communes à toutes les versions** : :ref:`installation-logiciel`

.. include:: firmware-triphase.inc.rst

Test de la partie *mesures* — Monophasé
-----------------------------------------

| Le transformateur a deux sorties : l'une pour l'alimentation CC, l'autre pour le capteur de tension CA qui devrait déjà fonctionner.
| Cela peut être vérifié en exécutant un programme (croquis) qui affiche les mesures analogiques prises par le processeur Atmel (**IC1**).

Le programme, qui se trouve également sur la page Téléchargements, est : *RawSamplesTool_2chan.ino*

| Après avoir téléchargé ce croquis sur le processeur via l'Arduino IDE, la fenêtre série (icône en forme de loupe) doit être ouverte.
| Après avoir terminé chaque exécution, le programme peut être redémarré à partir du clavier en saisissant le caractère "**g**", suivi de *Entrée*.

| Le programme *RawSamplesTool_2chan* affiche les échantillons de tension alternative et de courant pour un ou plusieurs cycles secteur complets.
| Si un courant important est mesuré ainsi que la tension, les résultats affichés sembleront plus intéressants.

| Voici quelques résultats capturés lors de la mesure du courant consommé par une charge de 3 kW avec le :term:`CT` branché sur **CT2**.
| Lorsque le :term:`CT` a été déplacé vers le port :term:`CT`\1, la sortie résultante semblait presque identique, mais avec les caractères "**1**" et "**2**" inversés.

RSResults_V_and_I2.txt

| Si aucun signal n'est disponible sur les ports **CT1** et **CT2**, les formes d'onde de ces canaux seront toutes deux des lignes droites.
| Seul le signal de tension affichera un aspect sinusoïdal.
| Pour vérifier le fonctionnement des ports **CT1** et **CT2** pendant que le :term:`PCB` est testé sur le banc, un câblage adapté sera nécessaire.

Test de la partie *mesures* — Triphasé
----------------------------------------

.. note::
   À partir de maintenant, une alimentation triphasée devra être fournie à la carte-mère.

Chaque transformateur a deux sorties : l'une pour l'alimentation CC, l'autre pour le capteur de tension CA qui devrait déjà fonctionner.
Cela peut être vérifié en exécutant un programme (croquis) qui affiche les mesures analogiques prises par le processeur Atmel (**IC1**).

Le programme, qui se trouve également sur la page Téléchargements, est : *RawSamplesTool_6chan.ino*

Après avoir téléchargé ce croquis sur le processeur via l'Arduino IDE, la fenêtre série (icône en forme de loupe) doit être ouverte.
Après avoir terminé chaque exécution, le programme peut être redémarré à partir du clavier en saisissant le caractère "**g**", suivi de *Entrée*.

Le programme *RawSamplesTool_6chan* affiche les échantillons des trois tensions alternatives et de courant pour un ou plusieurs cycles secteur complets.
Si un courant important est mesuré ainsi que la tension, les résultats affichés sembleront plus intéressants.

Voici quelques résultats capturés lors de la mesure du courant consommé par une charge de 3 kW avec le :term:`CT` branché sur **CT2**.
Lorsque le :term:`CT` a été déplacé vers le port **CT1**, la sortie résultante semblait presque identique, mais avec les caractères "**1**" et "**2**" inversés.

RSResults_V_and_I2.txt

Si aucun signal n'est disponible sur les ports **CT1-CT3**, les formes d'onde de ces canaux seront toutes deux des lignes droites.
Seuls les signaux de tension afficheront un aspect sinusoïdal.
Pour vérifier le fonctionnement des ports **CT1-CT3** pendant que le :term:`PCB` est testé sur le banc, un câblage adapté sera nécessaire.

.. |br| raw:: html

  <br/>
